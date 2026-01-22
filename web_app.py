#!/usr/bin/env python3
"""
Medical Study Prompt Generator - Web Application
Beautiful web interface with real-time progress updates
"""

import os
import sys
from pathlib import Path
from flask import Flask, render_template, request, jsonify, Response, send_file
from flask_cors import CORS
from dotenv import load_dotenv, set_key
import json
import time
from generate_study_prompts import MedicalPromptGenerator
import threading
import queue

# Load environment
load_dotenv()

app = Flask(__name__)
CORS(app)

# Global variables for progress tracking
progress_queue = queue.Queue()
generation_status = {
    'is_running': False,
    'current_question': 0,
    'total_questions': 0,
    'current_message': '',
    'error': None,
    'output_file': None
}


def log_progress(message):
    """Add message to progress queue"""
    progress_queue.put({
        'message': message,
        'timestamp': time.time()
    })
    generation_status['current_message'] = message


def run_generation(input_pdf, firstaid_pdf, output_csv, input_nature, num_questions):
    """Run the generation process in background"""
    global generation_status
    
    try:
        generation_status['is_running'] = True
        generation_status['error'] = None
        generation_status['current_question'] = 0
        
        log_progress("=" * 60)
        log_progress("🚀 Starting Medical Study Prompt Generator")
        log_progress("=" * 60)
        log_progress("")
        
        # Initialize generator
        log_progress(f"📚 Loading First Aid reference from: {Path(firstaid_pdf).name}")
        generator = MedicalPromptGenerator(firstaid_pdf)
        log_progress(f"✓ Loaded {len(generator.firstaid_content):,} characters from First Aid")
        log_progress("")
        
        # Extract questions
        log_progress(f"📄 Extracting questions from: {Path(input_pdf).name}")
        questions = generator.extract_questions_from_pdf(input_pdf)
        generation_status['total_questions'] = len(questions)
        log_progress(f"✓ Extracted {len(questions)} questions")
        log_progress("")
        
        # Process each question
        results = []
        for i, q in enumerate(questions, 1):
            generation_status['current_question'] = i
            log_progress(f"[{i}/{len(questions)}] Processing Question {q['number']}...")
            
            # Identify concepts
            log_progress(f"  → 🔍 Identifying key concepts...")
            concepts = generator.identify_key_concepts(q['content'])
            log_progress(f"  → 💡 Concepts: {concepts[:80]}...")
            
            # Generate prompt
            log_progress(f"  → ✨ Generating enriched prompt...")
            prompt = generator.generate_enriched_prompt(q['number'], q['content'], concepts)
            
            results.append({
                'question_number': q['number'],
                'prompt': prompt
            })
            
            log_progress(f"  ✓ Complete!")
            log_progress("")
        
        # Sort and save
        results.sort(key=lambda x: x['question_number'])
        
        import csv
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Question Number', 'Prompt'])
            for result in results:
                writer.writerow([result['question_number'], result['prompt']])
        
        generation_status['output_file'] = output_csv
        
        log_progress("=" * 60)
        log_progress(f"🎉 Successfully generated {len(results)} study prompts!")
        log_progress(f"💾 Output saved to: {Path(output_csv).name}")
        log_progress("=" * 60)
        log_progress("")
        log_progress("✅ COMPLETE! You can now download your CSV file.")
        
    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        log_progress(error_msg)
        generation_status['error'] = str(e)
        import traceback
        log_progress(traceback.format_exc())
    
    finally:
        generation_status['is_running'] = False


@app.route('/')
def index():
    """Main page"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    # Auto-detect PDFs
    current_dir = Path.cwd()
    
    # Find first aid PDF
    firstaid_pdf = None
    for name in ['first aid.pdf', 'firstaid.pdf', 'First Aid.pdf']:
        if (current_dir / name).exists():
            firstaid_pdf = name
            break
    
    # Find input PDFs
    input_pdfs = []
    for pdf in current_dir.glob('*.pdf'):
        if pdf.name.lower() not in ['first aid.pdf', 'firstaid.pdf']:
            input_pdfs.append(pdf.name)
    
    input_pdf = input_pdfs[0] if input_pdfs else None
    
    return render_template('index.html',
                         api_key_configured=bool(api_key),
                         firstaid_pdf=firstaid_pdf,
                         input_pdf=input_pdf,
                         input_pdfs=input_pdfs)


@app.route('/api/save_api_key', methods=['POST'])
def save_api_key():
    """Save API key to .env file"""
    data = request.json
    api_key = data.get('api_key', '').strip()
    
    if not api_key:
        return jsonify({'success': False, 'error': 'API key is required'})
    
    if not api_key.startswith('sk-'):
        return jsonify({'success': False, 'error': 'Invalid API key format'})
    
    # Save to .env
    env_path = Path.cwd() / '.env'
    if env_path.exists():
        set_key(env_path, 'OPENAI_API_KEY', api_key)
    else:
        with open(env_path, 'w') as f:
            f.write(f'OPENAI_API_KEY={api_key}\n')
    
    os.environ['OPENAI_API_KEY'] = api_key
    
    return jsonify({'success': True})


@app.route('/api/start_generation', methods=['POST'])
def start_generation():
    """Start the generation process"""
    global generation_status
    
    if generation_status['is_running']:
        return jsonify({'success': False, 'error': 'Generation already in progress'})
    
    data = request.json
    input_pdf = data.get('input_pdf')
    firstaid_pdf = data.get('firstaid_pdf')
    input_nature = data.get('input_nature')
    num_questions = data.get('num_questions')
    
    # Validate inputs
    if not input_pdf or not Path(input_pdf).exists():
        return jsonify({'success': False, 'error': 'Input PDF not found'})
    
    if not firstaid_pdf or not Path(firstaid_pdf).exists():
        return jsonify({'success': False, 'error': 'First Aid PDF not found'})
    
    # Generate output filename
    output_csv = Path(input_pdf).stem + '_study_prompts.csv'
    
    # Clear the queue
    while not progress_queue.empty():
        try:
            progress_queue.get_nowait()
        except:
            break
    
    # Reset status
    generation_status = {
        'is_running': True,
        'current_question': 0,
        'total_questions': 0,
        'current_message': '',
        'error': None,
        'output_file': None
    }
    
    # Start generation in background thread
    thread = threading.Thread(
        target=run_generation,
        args=(input_pdf, firstaid_pdf, output_csv, input_nature, num_questions),
        daemon=True
    )
    thread.start()
    
    return jsonify({'success': True})


@app.route('/api/progress')
def progress():
    """Server-sent events for real-time progress"""
    def generate():
        while True:
            try:
                # Get message from queue (with timeout)
                msg = progress_queue.get(timeout=1.0)
                yield f"data: {json.dumps(msg)}\n\n"
            except queue.Empty:
                # Send heartbeat
                yield f"data: {json.dumps({'heartbeat': True})}\n\n"
            
            # If generation is complete and queue is empty, close
            if not generation_status['is_running'] and progress_queue.empty():
                time.sleep(2)  # Give time for final messages
                break
    
    return Response(generate(), mimetype='text/event-stream')


@app.route('/api/status')
def status():
    """Get current status"""
    return jsonify(generation_status)


@app.route('/api/download')
def download():
    """Download the generated CSV"""
    output_file = generation_status.get('output_file')
    if output_file and Path(output_file).exists():
        return send_file(output_file, as_attachment=True)
    return jsonify({'error': 'File not found'}), 404


@app.route('/api/list_pdfs')
def list_pdfs():
    """List available PDF files"""
    current_dir = Path.cwd()
    
    # Find first aid PDF
    firstaid_pdf = None
    for name in ['first aid.pdf', 'firstaid.pdf', 'First Aid.pdf']:
        if (current_dir / name).exists():
            firstaid_pdf = name
            break
    
    # Find input PDFs
    input_pdfs = []
    for pdf in current_dir.glob('*.pdf'):
        if pdf.name.lower() not in ['first aid.pdf', 'firstaid.pdf']:
            input_pdfs.append(pdf.name)
    
    return jsonify({
        'firstaid_pdf': firstaid_pdf,
        'input_pdfs': input_pdfs
    })


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("🌐 Medical Study Prompt Generator - Web Interface")
    print("=" * 60)
    print()
    print("🚀 Starting server...")
    print()
    print("Open your browser and go to:")
    print()
    print("    👉 http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
