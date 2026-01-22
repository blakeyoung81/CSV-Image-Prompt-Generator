#!/usr/bin/env python3
"""
Interactive wrapper for Medical Study Prompt Generator
Provides a simple CLI interface
"""

import os
import sys
from pathlib import Path
from generate_study_prompts import MedicalPromptGenerator


def list_pdf_files():
    """List all PDF files in current directory"""
    pdfs = list(Path('.').glob('*.pdf'))
    return [p for p in pdfs if p.name != 'firstaid.pdf']


def main():
    print("=" * 70)
    print(" 📚 Medical Study Prompt Generator")
    print("=" * 70)
    print()
    
    # Check for First Aid (handle both naming conventions)
    if os.path.exists('first aid.pdf'):
        firstaid_path = 'first aid.pdf'
    elif os.path.exists('firstaid.pdf'):
        firstaid_path = 'firstaid.pdf'
    else:
        firstaid_path = None
    
    if not firstaid_path:
        print("❌ Error: firstaid.pdf not found!")
        print("   Please add the First Aid PDF to this directory.")
        print()
        return
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not set!")
        print()
        print("Quick fix:")
        print("  1. Get your API key from: https://platform.openai.com/api-keys")
        print("  2. Create .env file:")
        print("     echo 'OPENAI_API_KEY=sk-your-key-here' > .env")
        print()
        return
    
    print("✓ First Aid PDF found")
    print("✓ API key configured")
    print()
    
    # Find exam PDFs
    exam_pdfs = list_pdf_files()
    
    if not exam_pdfs:
        print("No exam PDFs found in current directory.")
        print()
        print("Usage:")
        print("  python run.py <path-to-exam.pdf>")
        print()
        print("Or place your exam PDF in this directory and run again.")
        return
    
    # If PDF provided as argument, use it
    if len(sys.argv) > 1:
        exam_pdf = sys.argv[1]
        if not os.path.exists(exam_pdf):
            print(f"❌ Error: {exam_pdf} not found!")
            return
    else:
        # Interactive selection
        print("Found exam PDFs:")
        for i, pdf in enumerate(exam_pdfs, 1):
            size_mb = pdf.stat().st_size / (1024 * 1024)
            print(f"  {i}. {pdf.name} ({size_mb:.1f} MB)")
        print()
        
        if len(exam_pdfs) == 1:
            choice = 1
            print(f"Using: {exam_pdfs[0].name}")
        else:
            try:
                choice = int(input("Select exam PDF (enter number): "))
                if choice < 1 or choice > len(exam_pdfs):
                    print("Invalid choice!")
                    return
            except (ValueError, KeyboardInterrupt):
                print("\nCancelled.")
                return
        
        exam_pdf = str(exam_pdfs[choice - 1])
    
    # Generate output filename
    base_name = Path(exam_pdf).stem
    output_csv = f"{base_name}_study_prompts.csv"
    
    print()
    print("=" * 70)
    print(f"Input:  {exam_pdf}")
    print(f"Output: {output_csv}")
    print("=" * 70)
    print()
    
    # Confirm
    if len(sys.argv) <= 1:
        confirm = input("Proceed? [Y/n]: ").strip().lower()
        if confirm and confirm != 'y':
            print("Cancelled.")
            return
    
    print()
    
    # Run generator
    try:
        generator = MedicalPromptGenerator(firstaid_path)
        generator.process_exam(exam_pdf, output_csv)
        
        print()
        print("🎉 Success! Your study prompts are ready.")
        print(f"📄 Open: {output_csv}")
        
    except KeyboardInterrupt:
        print("\n\n❌ Interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    main()
