"""
Medical Question to Study Prompt Generator
Reads medical exam PDFs and generates enriched study prompts using AI + First Aid reference
"""

import os
import re
import csv
from pathlib import Path
from typing import List, Dict
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class MedicalPromptGenerator:
    def __init__(self, firstaid_pdf_path: str):
        """Initialize with First Aid PDF as knowledge base"""
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.firstaid_content = self._load_firstaid(firstaid_pdf_path)
        
    def _load_firstaid(self, pdf_path: str) -> str:
        """Load and extract text from First Aid PDF"""
        print(f"Loading First Aid reference from: {pdf_path}")
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            print(f"✓ Loaded {len(text)} characters from First Aid")
            return text
        except Exception as e:
            print(f"Warning: Could not load First Aid PDF: {e}")
            return ""
    
    def extract_questions_from_pdf(self, pdf_path: str) -> List[Dict]:
        """Extract individual questions from exam PDF"""
        print(f"\nExtracting questions from: {pdf_path}")
        
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            full_text = ""
            for page in reader.pages:
                full_text += page.extract_text() + "\n"
        
        # Try multiple extraction patterns
        questions = []
        
        # Pattern 1: NBME format "Exam Section X: Item Y of 50"
        pattern1 = r'Exam Section \d+[:\s]+Item\s+(\d+)\s+of\s+\d+'
        matches = list(re.finditer(pattern1, full_text, re.IGNORECASE))
        
        if len(matches) >= 40:
            print(f"  Using NBME format pattern (found {len(matches)} markers)")
            for i, match in enumerate(matches):
                q_num = int(match.group(1))
                start_pos = match.end()
                
                # Find the end (next question or end of text)
                if i < len(matches) - 1:
                    end_pos = matches[i + 1].start()
                else:
                    end_pos = len(full_text)
                
                content = full_text[start_pos:end_pos].strip()
                
                # Clean up content - remove extra markers
                content = re.sub(r'Previous\s+Next\s+Score Report.*?Pause', '', content, flags=re.IGNORECASE)
                content = re.sub(r'https://t\.me/\S+', '', content)
                
                questions.append({
                    'number': q_num,
                    'content': content[:5000]  # Limit length
                })
        
        # Pattern 2: Simple numbered format
        if len(questions) < 40:
            questions = self._extract_questions_alternative(full_text)
        
        # Sort by question number
        questions.sort(key=lambda x: x['number'])
        
        print(f"✓ Extracted {len(questions)} questions")
        return questions
    
    def _extract_questions_alternative(self, text: str) -> List[Dict]:
        """Alternative method to extract questions"""
        questions = []
        
        # Try to find sections that look like questions
        lines = text.split('\n')
        current_q = None
        current_content = []
        
        for line in lines:
            # Look for question numbers at start of line
            match = re.match(r'^(\d+)\.\s+(.+)', line)
            if match and 1 <= int(match.group(1)) <= 50:
                if current_q is not None:
                    questions.append({
                        'number': current_q,
                        'content': '\n'.join(current_content)
                    })
                current_q = int(match.group(1))
                current_content = [match.group(2)]
            elif current_q is not None:
                current_content.append(line)
        
        if current_q is not None:
            questions.append({
                'number': current_q,
                'content': '\n'.join(current_content)
            })
        
        return questions
    
    def identify_key_concepts(self, question_text: str) -> str:
        """Use AI to identify key medical concepts in the question"""
        
        prompt = f"""Analyze this medical exam question and identify the KEY MEDICAL CONCEPTS being tested.
List the main topics, diseases, mechanisms, or clinical findings that are central to this question.

Question:
{question_text[:3000]}

Return ONLY a concise list of key concepts (3-7 items), separated by semicolons."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a medical education expert analyzing USMLE-style questions."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=300
            )
            
            concepts = response.choices[0].message.content.strip()
            return concepts
        except Exception as e:
            print(f"Error identifying concepts: {e}")
            return "Unknown concepts"
    
    def generate_enriched_prompt(self, question_num: int, question_text: str, concepts: str) -> str:
        """Generate enriched study prompt using AI + First Aid"""
        
        # Find relevant First Aid sections
        firstaid_excerpt = self._find_relevant_firstaid_section(concepts)
        
        prompt = f"""You are creating a comprehensive study prompt for a medical student reviewing an NBME/USMLE practice question.

QUESTION NUMBER: {question_num}

QUESTION CONTENT:
{question_text[:4000]}

KEY CONCEPTS IDENTIFIED:
{concepts}

FIRST AID REFERENCE MATERIAL:
{firstaid_excerpt[:3000]}

Generate a SINGLE, comprehensive study prompt that:
1. Professionally condenses and explains ALL concepts tested in this question
2. Integrates relevant First Aid material to enrich the explanation
3. Covers pathophysiology, clinical presentation, diagnosis, and mechanisms as relevant
4. Is detailed enough for deep understanding but concise enough to be actionable
5. Starts with "Professionally condense and explain..."

Return ONLY the prompt text, no additional commentary."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a medical educator creating high-yield study materials."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=500
            )
            
            enriched_prompt = response.choices[0].message.content.strip()
            
            # Clean up the prompt
            enriched_prompt = enriched_prompt.replace('"', '').strip()
            if not enriched_prompt.startswith("Professionally"):
                enriched_prompt = "Professionally condense and explain " + enriched_prompt
            
            return enriched_prompt
        except Exception as e:
            print(f"Error generating prompt for Q{question_num}: {e}")
            return f"Professionally condense and explain the concepts in question {question_num}."
    
    def _find_relevant_firstaid_section(self, concepts: str) -> str:
        """Find relevant sections in First Aid based on concepts"""
        if not self.firstaid_content:
            return ""
        
        # Simple keyword matching - find paragraphs containing concept keywords
        keywords = [k.strip().lower() for k in concepts.split(';')]
        
        lines = self.firstaid_content.split('\n')
        relevant_sections = []
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in keywords if len(keyword) > 3):
                # Get context around the matching line
                start = max(0, i - 5)
                end = min(len(lines), i + 10)
                section = '\n'.join(lines[start:end])
                relevant_sections.append(section)
        
        return '\n\n'.join(relevant_sections[:5]) if relevant_sections else self.firstaid_content[:2000]
    
    def process_exam(self, exam_pdf_path: str, output_csv_path: str):
        """Main processing pipeline"""
        print("=" * 60)
        print("Medical Question to Study Prompt Generator")
        print("=" * 60)
        
        # Extract questions
        questions = self.extract_questions_from_pdf(exam_pdf_path)
        
        if not questions:
            print("❌ No questions found. Please check the PDF format.")
            return
        
        # Process each question
        results = []
        
        for i, q in enumerate(questions, 1):
            print(f"\n[{i}/{len(questions)}] Processing Question {q['number']}...")
            
            # Identify concepts
            print(f"  → Identifying key concepts...")
            concepts = self.identify_key_concepts(q['content'])
            print(f"  → Concepts: {concepts[:100]}...")
            
            # Generate enriched prompt
            print(f"  → Generating enriched prompt...")
            enriched_prompt = self.generate_enriched_prompt(
                q['number'], 
                q['content'], 
                concepts
            )
            
            results.append({
                'question_number': q['number'],
                'prompt': enriched_prompt
            })
            
            print(f"  ✓ Complete")
        
        # Sort by question number
        results.sort(key=lambda x: x['question_number'])
        
        # Write to CSV
        print(f"\n{'=' * 60}")
        print(f"Writing results to: {output_csv_path}")
        
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Question Number', 'Prompt'])
            
            for result in results:
                writer.writerow([result['question_number'], result['prompt']])
        
        print(f"✓ Successfully generated {len(results)} study prompts!")
        print(f"✓ Output saved to: {output_csv_path}")
        print("=" * 60)


def main():
    """Main entry point"""
    import sys
    
    # Check for required files (handle both naming conventions)
    if os.path.exists("first aid.pdf"):
        firstaid_path = "first aid.pdf"
    elif os.path.exists("firstaid.pdf"):
        firstaid_path = "firstaid.pdf"
    else:
        firstaid_path = "firstaid.pdf"  # Default for error message
    
    if not os.path.exists(firstaid_path):
        print(f"❌ Error: {firstaid_path} not found!")
        print("Please place the First Aid PDF in the same directory as this script.")
        return
    
    # Get input PDF path
    if len(sys.argv) < 2:
        print("Usage: python generate_study_prompts.py <exam_pdf_path> [output_csv_path]")
        print("\nExample:")
        print('  python generate_study_prompts.py "NBME 30 A Part 2-ocr.pdf"')
        print('  python generate_study_prompts.py "NBME 30 A Part 2-ocr.pdf" output.csv')
        return
    
    exam_pdf = sys.argv[1]
    
    if not os.path.exists(exam_pdf):
        print(f"❌ Error: {exam_pdf} not found!")
        return
    
    # Generate output filename
    if len(sys.argv) >= 3:
        output_csv = sys.argv[2]
    else:
        base_name = Path(exam_pdf).stem
        output_csv = f"{base_name}_study_prompts.csv"
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not found in environment!")
        print("Please create a .env file with your OpenAI API key:")
        print("  OPENAI_API_KEY=sk-your-key-here")
        return
    
    # Initialize and run
    generator = MedicalPromptGenerator(firstaid_path)
    generator.process_exam(exam_pdf, output_csv)


if __name__ == "__main__":
    main()
