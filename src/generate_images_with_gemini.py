#!/usr/bin/env python3
"""
Generate images using Gemini API from CSV descriptions
Then automatically create PDF from generated images
"""

import os
import sys
import csv
import time
from pathlib import Path
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import argparse

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Try importing Gemini API
try:
    from google import genai
    from google.genai import types
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️  Warning: google-genai not installed. Install with: pip install google-genai")

# Import PDF generator
from generate_pdf_from_images import PDFGenerator

# Load environment
load_dotenv()


class GeminiImageGenerator:
    def __init__(self, api_key=None, model="gemini-2.5-flash-image"):
        """
        Initialize Gemini image generator
        
        Args:
            api_key: Gemini API key (or from GEMINI_API_KEY env var)
            model: Model to use (gemini-2.5-flash-image or gemini-3-pro-image-preview)
        """
        if not GEMINI_AVAILABLE:
            raise ImportError("google-genai package not installed. Run: pip install google-genai")
        
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key not found. Set GEMINI_API_KEY environment variable or pass api_key parameter.")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model = model
        print(f"✓ Initialized Gemini client with model: {model}")
    
    def generate_image(self, prompt, output_path, question_num=None):
        """
        Generate an image from a text prompt using Gemini API
        
        Args:
            prompt: Text description to generate image from
            output_path: Path to save the generated image
            question_num: Optional question number for progress tracking
        
        Returns:
            Path to saved image or None if failed
        """
        try:
            # Create a more detailed prompt for medical/educational content
            enhanced_prompt = self._create_image_prompt(prompt, question_num)
            
            if question_num:
                print(f"  [Q{question_num}] Generating image...")
            else:
                print(f"  Generating image...")
            
            # Generate image
            response = self.client.models.generate_content(
                model=self.model,
                contents=[enhanced_prompt],
            )
            
            # Extract image from response
            image_data = None
            for part in response.parts:
                if part.inline_data is not None:
                    image_data = part.inline_data.data
                    break
            
            if not image_data:
                # Try alternative response format
                if hasattr(response, 'candidates') and len(response.candidates) > 0:
                    for part in response.candidates[0].content.parts:
                        if part.inline_data is not None:
                            image_data = part.inline_data.data
                            break
            
            if not image_data:
                print(f"  ⚠️  Warning: No image data in response")
                return None
            
            # Save image
            image = Image.open(BytesIO(image_data))
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            image.save(output_path, format='PNG')
            
            if question_num:
                print(f"  ✓ Saved: {output_path.name}")
            else:
                print(f"  ✓ Saved: {output_path}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"  ❌ Error generating image: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _create_image_prompt(self, description, question_num=None):
        """
        Create an enhanced prompt for image generation from medical description
        
        Args:
            description: Original description from CSV
            question_num: Question number for context
        
        Returns:
            Enhanced prompt for Gemini with exhaustive detail
        """
        # Extract key concept from description (usually first part before colon)
        if ':' in description:
            concept = description.split(':')[0].strip()
            details = description.split(':', 1)[1].strip()
        else:
            concept = description[:100]
            details = description
        
        # Create an EXTREMELY DETAILED visual prompt that expands on every aspect
        prompt = f"""Create a comprehensive, detailed, professional medical illustration or diagram that visually represents and explains: {concept}

DETAILED CONTEXT AND REQUIREMENTS:
{details}

VISUAL REQUIREMENTS - Describe EVERY element in detail:

1. ANATOMICAL STRUCTURES: Show all relevant anatomical structures with precise detail. Include:
   - Exact shapes, sizes, and proportions of each structure
   - Spatial relationships and orientations between structures
   - Anatomical landmarks and reference points
   - Color coding for different tissue types (e.g., muscle in red/pink, bone in white/beige, nerves in yellow, blood vessels in red/blue)
   - Cross-sectional views if needed to show internal structures
   - Labels or clear visual indicators for key structures

2. CELLULAR AND MOLECULAR COMPONENTS: If applicable, show:
   - Cell types with distinct morphological features
   - Organelles and intracellular structures
   - Molecular structures, receptors, ligands, enzymes
   - Signaling pathways with arrows showing direction and interactions
   - Protein-protein interactions, binding sites, conformational changes
   - Membrane structures, channels, transporters

3. PATHOPHYSIOLOGICAL MECHANISMS: Illustrate:
   - Step-by-step processes with numbered or sequential visual elements
   - Cause-and-effect relationships with arrows and connecting lines
   - Temporal sequences showing progression over time
   - Normal vs abnormal states side-by-side if relevant
   - Feedback loops and regulatory mechanisms

4. CLINICAL FEATURES: If showing clinical presentation:
   - Visual representation of signs and symptoms
   - Physical exam findings
   - Diagnostic imaging appearances
   - Laboratory findings visualized (e.g., blood smear abnormalities, histology)
   - Disease progression stages

5. DIAGRAMMATIC ELEMENTS:
   - Flow charts for pathways and processes
   - Comparison tables or side-by-side illustrations
   - Hierarchical structures (e.g., immune system organization)
   - Network diagrams showing connections and interactions
   - Schematic representations of complex systems

6. VISUAL STYLE SPECIFICATIONS:
   - Professional medical illustration style, similar to First Aid or Netter's Atlas
   - Clean white or light background
   - High contrast for clarity
   - Consistent color scheme throughout
   - Clear, readable labels and annotations
   - Professional typography for any text elements
   - Appropriate level of detail - not too cluttered, but comprehensive

7. SPECIFIC DETAILS TO INCLUDE:
   - Every structure, mechanism, pathway, and concept mentioned in the description
   - All relationships and interactions between components
   - Visual differentiation between normal and abnormal states
   - Key distinguishing features that help with identification
   - Clinical correlations and practical applications

8. COMPOSITION AND LAYOUT:
   - Logical organization that guides the eye through the concept
   - Main focus in center or prominent position
   - Supporting details arranged around main concept
   - Use of visual hierarchy (size, color, position) to emphasize important elements
   - Adequate spacing to prevent visual clutter
   - Multiple panels or sections if needed to show different aspects

IMPORTANT: This illustration must be comprehensive enough that a medical student can study it and understand ALL aspects of the concept. Include EVERY detail mentioned in the description. Do not leave any concept, structure, mechanism, or relationship to interpretation - show it explicitly in the illustration.

The final image should be a complete, self-contained educational resource that visually explains every single aspect of the concept described above."""
        
        return prompt
    
    def generate_images_from_csv(self, csv_path, output_folder, delay=1.0):
        """
        Generate images for all questions in CSV file
        
        Args:
            csv_path: Path to CSV file with Question Number and Prompt columns
            output_folder: Folder to save generated images
            delay: Delay between API calls (seconds) to avoid rate limits
        
        Returns:
            List of generated image paths
        """
        print("=" * 60)
        print("🎨 Gemini Image Generator")
        print("=" * 60)
        print()
        
        # Load CSV
        csv_path = Path(csv_path)
        if not csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        
        questions = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                q_num = int(row['Question Number'])
                prompt = row['Prompt']
                questions.append((q_num, prompt))
        
        print(f"✓ Loaded {len(questions)} questions from CSV")
        print(f"📁 Output folder: {output_folder}")
        print()
        
        # Create output folder
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)
        
        # Generate images
        generated_images = []
        total = len(questions)
        
        for i, (q_num, prompt) in enumerate(questions, 1):
            print(f"[{i}/{total}] Processing Question {q_num}...")
            
            # Generate image filename
            image_path = output_folder / f"{q_num}.png"
            
            # Generate image
            result = self.generate_image(prompt, image_path, question_num=q_num)
            
            if result:
                generated_images.append(result)
            
            # Rate limiting - wait between requests
            if i < total:
                time.sleep(delay)
            
            print()
        
        print("=" * 60)
        print(f"✅ Generated {len(generated_images)}/{total} images")
        print(f"📁 Saved to: {output_folder}")
        print("=" * 60)
        
        return generated_images


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Generate images using Gemini API from CSV, then create PDF',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate images and PDF from CSV
  python3 generate_images_with_gemini.py armon.csv -o armon_images -t "Armon Missed Questions"
  
  # Use specific Gemini model
  python3 generate_images_with_gemini.py armon.csv -o armon_images -m gemini-3-pro-image-preview
  
  # Just generate images (skip PDF)
  python3 generate_images_with_gemini.py armon.csv -o armon_images --no-pdf
        """
    )
    
    parser.add_argument('csv_file', help='CSV file with Question Number and Prompt columns')
    parser.add_argument('-o', '--output-folder', default='generated_images', 
                        help='Folder to save generated images (default: generated_images)')
    parser.add_argument('-t', '--title', default='Study Questions', 
                        help='PDF title (default: Study Questions)')
    parser.add_argument('-a', '--additional-text', default='', 
                        help='Additional text for PDF title page')
    parser.add_argument('-m', '--model', default='gemini-2.5-flash-image',
                        choices=['gemini-2.5-flash-image', 'gemini-3-pro-image-preview'],
                        help='Gemini model to use (default: gemini-2.5-flash-image)')
    parser.add_argument('--api-key', default=None,
                        help='Gemini API key (or set GEMINI_API_KEY env var)')
    parser.add_argument('--delay', type=float, default=1.0,
                        help='Delay between API calls in seconds (default: 1.0)')
    parser.add_argument('--no-pdf', action='store_true',
                        help='Skip PDF generation, only generate images')
    parser.add_argument('--pdf-output', default=None,
                        help='PDF output filename (default: <title>_Enhanced.pdf)')
    
    args = parser.parse_args()
    
    # Check if Gemini is available
    if not GEMINI_AVAILABLE:
        print("❌ Error: google-genai package not installed")
        print("Install it with: pip install google-genai")
        sys.exit(1)
    
    try:
        # Initialize generator
        generator = GeminiImageGenerator(api_key=args.api_key, model=args.model)
        
        # Generate images
        generated_images = generator.generate_images_from_csv(
            csv_path=args.csv_file,
            output_folder=args.output_folder,
            delay=args.delay
        )
        
        if not generated_images:
            print("❌ No images were generated. Cannot create PDF.")
            sys.exit(1)
        
        # Generate PDF if requested
        if not args.no_pdf:
            print()
            print("=" * 60)
            print("📄 Generating PDF from images...")
            print("=" * 60)
            print()
            
            # Determine PDF output filename
            if args.pdf_output:
                pdf_output = args.pdf_output
            else:
                pdf_output = f"{args.title.replace(' ', '_')}_Enhanced.pdf"
            
            # Create PDF generator
            pdf_generator = PDFGenerator(
                title=args.title,
                additional_text=args.additional_text,
                csv_path=args.csv_file
            )
            
            # Generate PDF
            success = pdf_generator.create_pdf(args.output_folder, pdf_output)
            
            if success:
                print()
                print("=" * 60)
                print("🎉 Complete workflow finished!")
                print(f"📁 Images: {args.output_folder}")
                print(f"📄 PDF: {pdf_output}")
                print("=" * 60)
            else:
                print("⚠️  PDF generation had issues, but images were created.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
