#!/usr/bin/env python3
"""
Test script to validate installation and configuration
"""

import os
import sys


def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} (need 3.8+)")
        return False


def check_dependencies():
    """Check if required packages are installed"""
    packages = ['PyPDF2', 'openai', 'dotenv']
    all_good = True
    
    for package in packages:
        try:
            if package == 'dotenv':
                __import__('dotenv')
                module_name = 'python-dotenv'
            else:
                __import__(package)
                module_name = package
            print(f"✓ {module_name} installed")
        except ImportError:
            print(f"❌ {module_name} not installed")
            all_good = False
    
    return all_good


def check_api_key():
    """Check if OpenAI API key is configured"""
    from dotenv import load_dotenv
    load_dotenv()
    
    key = os.getenv('OPENAI_API_KEY')
    if key:
        masked_key = key[:7] + "..." + key[-4:] if len(key) > 11 else "***"
        print(f"✓ OpenAI API key configured ({masked_key})")
        return True
    else:
        print("❌ OpenAI API key not found")
        print("   Create .env file with: OPENAI_API_KEY=sk-your-key")
        return False


def check_firstaid():
    """Check if First Aid PDF exists"""
    if os.path.exists('first aid.pdf'):
        size_mb = os.path.getsize('first aid.pdf') / (1024 * 1024)
        print(f"✓ first aid.pdf found ({size_mb:.1f} MB)")
        return True
    elif os.path.exists('firstaid.pdf'):
        size_mb = os.path.getsize('firstaid.pdf') / (1024 * 1024)
        print(f"✓ firstaid.pdf found ({size_mb:.1f} MB)")
        return True
    else:
        print("❌ First Aid PDF not found")
        print("   Add First Aid PDF to this directory (firstaid.pdf or 'first aid.pdf')")
        return False


def check_exam_pdfs():
    """Check for exam PDFs"""
    from pathlib import Path
    pdfs = [p for p in Path('.').glob('*.pdf') if p.name != 'firstaid.pdf']
    
    if pdfs:
        print(f"✓ Found {len(pdfs)} exam PDF(s):")
        for pdf in pdfs:
            size_mb = pdf.stat().st_size / (1024 * 1024)
            print(f"   - {pdf.name} ({size_mb:.1f} MB)")
        return True
    else:
        print("⚠️  No exam PDFs found (optional for testing)")
        return True  # Not a blocker


def main():
    print("=" * 60)
    print("Medical Study Prompt Generator - Setup Validation")
    print("=" * 60)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("API Key", check_api_key),
        ("First Aid PDF", check_firstaid),
        ("Exam PDFs", check_exam_pdfs),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Error checking {name}: {e}")
            results.append(False)
        print()
    
    print("=" * 60)
    
    if all(results[:-1]):  # All except exam PDFs check
        print("✅ All checks passed! Ready to generate study prompts.")
        print()
        print("Next steps:")
        print("  1. Add exam PDF to this directory")
        print("  2. Run: python3 run.py")
        print("  3. Or: python3 generate_study_prompts.py 'exam.pdf'")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print()
        print("Quick fixes:")
        print("  - Install deps: pip3 install -r requirements.txt")
        print("  - Add API key: echo 'OPENAI_API_KEY=sk-...' > .env")
        print("  - Add firstaid.pdf to this directory")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
