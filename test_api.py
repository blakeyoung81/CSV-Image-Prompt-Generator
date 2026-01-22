#!/usr/bin/env python3
"""
Quick API test to verify OpenAI connection is working
"""

import os
from dotenv import load_dotenv
from openai import OpenAI


def test_api():
    """Test OpenAI API connection"""
    print("=" * 60)
    print("OpenAI API Connection Test")
    print("=" * 60)
    print()
    
    # Load environment
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env file")
        print()
        print("Create .env file with:")
        print("  OPENAI_API_KEY=sk-your-key-here")
        return False
    
    # Mask key for display
    masked_key = api_key[:7] + "..." + api_key[-4:] if len(api_key) > 11 else "***"
    print(f"✓ API Key found: {masked_key}")
    print()
    
    # Test connection
    print("Testing API connection...")
    try:
        client = OpenAI(api_key=api_key)
        
        # Make a simple test call
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'API test successful' in exactly those words."}
            ],
            max_tokens=10,
            temperature=0
        )
        
        result = response.choices[0].message.content.strip()
        
        print(f"✓ API Response: {result}")
        print()
        
        # Check usage
        usage = response.usage
        print(f"Token Usage:")
        print(f"  - Prompt: {usage.prompt_tokens}")
        print(f"  - Completion: {usage.completion_tokens}")
        print(f"  - Total: {usage.total_tokens}")
        print()
        
        print("=" * 60)
        print("✅ API connection successful!")
        print("=" * 60)
        print()
        print("Your setup is ready. You can now run:")
        print("  python3 run.py")
        print("  or")
        print("  python3 generate_study_prompts.py 'exam.pdf'")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ API Error: {e}")
        print()
        print("Common issues:")
        print("  1. Invalid API key")
        print("  2. No credits/billing not set up")
        print("  3. Rate limit exceeded")
        print("  4. Network connection issues")
        print()
        print("Check your API key at: https://platform.openai.com/api-keys")
        print("Check your usage at: https://platform.openai.com/usage")
        return False


def test_gpt35_fallback():
    """Test GPT-3.5 as cheaper alternative"""
    print()
    print("=" * 60)
    print("Testing GPT-3.5-turbo (cheaper alternative)...")
    print("=" * 60)
    print()
    
    try:
        load_dotenv()
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'GPT-3.5 works' in exactly those words."}
            ],
            max_tokens=10,
            temperature=0
        )
        
        result = response.choices[0].message.content.strip()
        print(f"✓ GPT-3.5 Response: {result}")
        print()
        print("💡 GPT-3.5 is ~10x cheaper than GPT-4")
        print("   Consider using it if cost is a concern (lower quality though)")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ GPT-3.5 Error: {e}")
        return False


if __name__ == "__main__":
    success = test_api()
    
    if success:
        # Also test GPT-3.5
        try:
            test_gpt35_fallback()
        except:
            pass
