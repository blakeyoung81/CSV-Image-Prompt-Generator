#!/usr/bin/env python3
"""
Medical Study Prompt Generator - GUI Application
User-friendly interface for generating enriched study prompts
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
import threading
from dotenv import load_dotenv, set_key
from generate_study_prompts import MedicalPromptGenerator


class StudyPromptGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Study Prompt Generator")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Load environment
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        
        # Variables
        self.input_pdf_path = tk.StringVar()
        self.firstaid_pdf_path = tk.StringVar()
        self.output_csv_path = tk.StringVar()
        self.input_nature = tk.StringVar(value="An NBME exam of 50 questions with some explanations that needs to be enriched by firstaid and made into prompts")
        self.num_questions = tk.StringVar(value="50")
        self.api_key_var = tk.StringVar(value=self.api_key if self.api_key else "")
        
        # Auto-detect PDFs
        self._auto_detect_pdfs()
        
        # Build UI
        self._build_ui()
        
        # Check API key on startup
        if not self.api_key:
            self._show_api_key_dialog()
    
    def _auto_detect_pdfs(self):
        """Auto-detect PDF files in current directory"""
        current_dir = Path.cwd()
        
        # Look for first aid PDF
        for name in ['first aid.pdf', 'firstaid.pdf', 'First Aid.pdf']:
            if (current_dir / name).exists():
                self.firstaid_pdf_path.set(str(current_dir / name))
                break
        
        # Look for input PDF
        for pdf in current_dir.glob('*.pdf'):
            if pdf.name.lower() not in ['first aid.pdf', 'firstaid.pdf']:
                if 'nbme' in pdf.name.lower() or 'input' in pdf.name.lower():
                    self.input_pdf_path.set(str(pdf))
                    # Auto-set output name
                    output_name = pdf.stem + "_study_prompts.csv"
                    self.output_csv_path.set(str(current_dir / output_name))
                    break
    
    def _build_ui(self):
        """Build the main user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="📚 Medical Study Prompt Generator",
            font=("Helvetica", 20, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Main container with padding
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # API Key Section
        api_frame = tk.LabelFrame(main_frame, text="🔑 OpenAI API Configuration", font=("Helvetica", 12, "bold"), padx=10, pady=10)
        api_frame.pack(fill=tk.X, pady=(0, 15))
        
        api_status = "✅ API Key Configured" if self.api_key else "⚠️ API Key Required"
        api_status_label = tk.Label(api_frame, text=api_status, font=("Helvetica", 10))
        api_status_label.pack(anchor=tk.W)
        
        if not self.api_key:
            change_key_btn = tk.Button(
                api_frame,
                text="Enter API Key",
                command=self._show_api_key_dialog,
                bg="#3498db",
                fg="white",
                font=("Helvetica", 10),
                cursor="hand2"
            )
            change_key_btn.pack(anchor=tk.W, pady=(5, 0))
        else:
            change_key_btn = tk.Button(
                api_frame,
                text="Change API Key",
                command=self._show_api_key_dialog,
                font=("Helvetica", 9),
                cursor="hand2"
            )
            change_key_btn.pack(anchor=tk.W, pady=(5, 0))
        
        # Input Nature Section
        nature_frame = tk.LabelFrame(main_frame, text="📝 Input Description", font=("Helvetica", 12, "bold"), padx=10, pady=10)
        nature_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(nature_frame, text="What is the nature of your input?", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(0, 5))
        
        nature_text = tk.Text(nature_frame, height=3, wrap=tk.WORD, font=("Helvetica", 10))
        nature_text.insert("1.0", self.input_nature.get())
        nature_text.pack(fill=tk.X, pady=(0, 5))
        
        # Update variable when text changes
        def update_nature(*args):
            self.input_nature.set(nature_text.get("1.0", tk.END).strip())
        nature_text.bind("<KeyRelease>", update_nature)
        
        # Number of Questions
        tk.Label(nature_frame, text="How many questions do you want to generate?", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(10, 5))
        
        num_frame = tk.Frame(nature_frame)
        num_frame.pack(fill=tk.X)
        
        num_entry = tk.Entry(num_frame, textvariable=self.num_questions, font=("Helvetica", 10), width=10)
        num_entry.pack(side=tk.LEFT)
        
        tk.Label(num_frame, text="(Set to 'auto' to detect automatically)", font=("Helvetica", 9), fg="gray").pack(side=tk.LEFT, padx=(10, 0))
        
        # File Selection Section
        files_frame = tk.LabelFrame(main_frame, text="📁 File Selection", font=("Helvetica", 12, "bold"), padx=10, pady=10)
        files_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Input PDF
        self._add_file_selector(files_frame, "Input Exam PDF:", self.input_pdf_path, "Select Input PDF")
        
        # First Aid PDF
        self._add_file_selector(files_frame, "First Aid PDF:", self.firstaid_pdf_path, "Select First Aid PDF")
        
        # Output CSV
        tk.Label(files_frame, text="Output CSV File:", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(10, 5))
        output_frame = tk.Frame(files_frame)
        output_frame.pack(fill=tk.X)
        
        output_entry = tk.Entry(output_frame, textvariable=self.output_csv_path, font=("Helvetica", 10))
        output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        output_btn = tk.Button(
            output_frame,
            text="Save As...",
            command=self._select_output_file,
            font=("Helvetica", 9)
        )
        output_btn.pack(side=tk.RIGHT)
        
        # Progress Section
        progress_frame = tk.LabelFrame(main_frame, text="📊 Progress", font=("Helvetica", 12, "bold"), padx=10, pady=10)
        progress_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        self.progress_bar = ttk.Progressbar(progress_frame, mode='indeterminate')
        self.progress_bar.pack(fill=tk.X, pady=(0, 10))
        
        self.status_text = scrolledtext.ScrolledText(
            progress_frame,
            height=8,
            font=("Courier", 9),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        self.status_text.pack(fill=tk.BOTH, expand=True)
        
        # Generate Button
        self.generate_btn = tk.Button(
            main_frame,
            text="🚀 Generate Study Prompts",
            command=self._start_generation,
            bg="#27ae60",
            fg="white",
            font=("Helvetica", 14, "bold"),
            height=2,
            cursor="hand2"
        )
        self.generate_btn.pack(fill=tk.X)
    
    def _add_file_selector(self, parent, label_text, var, button_text):
        """Add a file selector row"""
        tk.Label(parent, text=label_text, font=("Helvetica", 10)).pack(anchor=tk.W, pady=(5, 5))
        
        frame = tk.Frame(parent)
        frame.pack(fill=tk.X)
        
        entry = tk.Entry(frame, textvariable=var, font=("Helvetica", 10))
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        btn = tk.Button(
            frame,
            text=button_text,
            command=lambda: self._select_file(var),
            font=("Helvetica", 9)
        )
        btn.pack(side=tk.RIGHT)
    
    def _select_file(self, var):
        """Open file dialog to select a PDF"""
        filename = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if filename:
            var.set(filename)
            # Auto-set output if input PDF is selected
            if var == self.input_pdf_path and filename:
                output_name = Path(filename).stem + "_study_prompts.csv"
                self.output_csv_path.set(str(Path(filename).parent / output_name))
    
    def _select_output_file(self):
        """Open file dialog to select output CSV location"""
        filename = filedialog.asksaveasfilename(
            title="Save CSV As",
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            initialfile="study_prompts.csv"
        )
        if filename:
            self.output_csv_path.set(filename)
    
    def _show_api_key_dialog(self):
        """Show dialog to enter API key"""
        dialog = tk.Toplevel(self.root)
        dialog.title("OpenAI API Key")
        dialog.geometry("500x250")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        frame = tk.Frame(dialog, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            frame,
            text="🔑 Enter your OpenAI API Key",
            font=("Helvetica", 14, "bold")
        ).pack(pady=(0, 10))
        
        tk.Label(
            frame,
            text="Get your API key from: https://platform.openai.com/api-keys",
            font=("Helvetica", 9),
            fg="blue",
            cursor="hand2"
        ).pack(pady=(0, 15))
        
        tk.Label(frame, text="API Key:", font=("Helvetica", 10)).pack(anchor=tk.W)
        
        key_entry = tk.Entry(frame, font=("Helvetica", 10), show="*", width=50)
        key_entry.pack(fill=tk.X, pady=(5, 15))
        
        if self.api_key:
            key_entry.insert(0, self.api_key)
        
        def save_key():
            key = key_entry.get().strip()
            if not key:
                messagebox.showerror("Error", "Please enter an API key!")
                return
            
            if not key.startswith("sk-"):
                messagebox.showerror("Error", "Invalid API key format! Key should start with 'sk-'")
                return
            
            # Save to .env file
            env_path = Path.cwd() / '.env'
            if env_path.exists():
                set_key(env_path, 'OPENAI_API_KEY', key)
            else:
                with open(env_path, 'w') as f:
                    f.write(f'OPENAI_API_KEY={key}\n')
            
            self.api_key = key
            self.api_key_var.set(key)
            os.environ['OPENAI_API_KEY'] = key
            
            messagebox.showinfo("Success", "API key saved successfully!")
            dialog.destroy()
            self.root.destroy()
            
            # Restart the app to refresh UI
            python = sys.executable
            os.execl(python, python, *sys.argv)
        
        btn_frame = tk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        save_btn = tk.Button(
            btn_frame,
            text="Save",
            command=save_key,
            bg="#27ae60",
            fg="white",
            font=("Helvetica", 11, "bold"),
            width=15
        )
        save_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        cancel_btn = tk.Button(
            btn_frame,
            text="Cancel",
            command=dialog.destroy,
            font=("Helvetica", 11),
            width=15
        )
        cancel_btn.pack(side=tk.LEFT)
        
        key_entry.focus()
    
    def _log_status(self, message):
        """Add message to status text area"""
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.root.update_idletasks()
    
    def _validate_inputs(self):
        """Validate all inputs before generation"""
        if not self.api_key:
            messagebox.showerror("Error", "Please enter your OpenAI API key!")
            return False
        
        input_pdf = self.input_pdf_path.get()
        if not input_pdf or not Path(input_pdf).exists():
            messagebox.showerror("Error", "Please select a valid input PDF file!")
            return False
        
        firstaid_pdf = self.firstaid_pdf_path.get()
        if not firstaid_pdf or not Path(firstaid_pdf).exists():
            messagebox.showerror("Error", "Please select a valid First Aid PDF file!")
            return False
        
        output_csv = self.output_csv_path.get()
        if not output_csv:
            messagebox.showerror("Error", "Please specify an output CSV file!")
            return False
        
        return True
    
    def _start_generation(self):
        """Start the generation process in a background thread"""
        if not self._validate_inputs():
            return
        
        # Disable button
        self.generate_btn.config(state=tk.DISABLED, text="⏳ Generating...")
        self.progress_bar.start(10)
        self.status_text.delete(1.0, tk.END)
        
        # Run in background thread
        thread = threading.Thread(target=self._run_generation, daemon=True)
        thread.start()
    
    def _run_generation(self):
        """Run the actual generation process"""
        try:
            input_pdf = self.input_pdf_path.get()
            firstaid_pdf = self.firstaid_pdf_path.get()
            output_csv = self.output_csv_path.get()
            
            self._log_status("=" * 60)
            self._log_status("Medical Study Prompt Generator")
            self._log_status("=" * 60)
            self._log_status("")
            
            # Initialize generator
            self._log_status(f"Loading First Aid reference from: {Path(firstaid_pdf).name}")
            generator = MedicalPromptGenerator(firstaid_pdf)
            self._log_status(f"✓ Loaded {len(generator.firstaid_content)} characters from First Aid")
            self._log_status("")
            
            # Extract questions
            self._log_status(f"Extracting questions from: {Path(input_pdf).name}")
            questions = generator.extract_questions_from_pdf(input_pdf)
            self._log_status(f"✓ Extracted {len(questions)} questions")
            self._log_status("")
            
            # Process each question
            results = []
            for i, q in enumerate(questions, 1):
                self._log_status(f"[{i}/{len(questions)}] Processing Question {q['number']}...")
                
                # Identify concepts
                self._log_status(f"  → Identifying key concepts...")
                concepts = generator.identify_key_concepts(q['content'])
                self._log_status(f"  → Concepts: {concepts[:100]}...")
                
                # Generate prompt
                self._log_status(f"  → Generating enriched prompt...")
                prompt = generator.generate_enriched_prompt(q['number'], q['content'], concepts)
                
                results.append({
                    'question_number': q['number'],
                    'prompt': prompt
                })
                
                self._log_status(f"  ✓ Complete")
                self._log_status("")
            
            # Sort and save
            results.sort(key=lambda x: x['question_number'])
            
            import csv
            with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Question Number', 'Prompt'])
                for result in results:
                    writer.writerow([result['question_number'], result['prompt']])
            
            self._log_status("=" * 60)
            self._log_status(f"✓ Successfully generated {len(results)} study prompts!")
            self._log_status(f"✓ Output saved to: {output_csv}")
            self._log_status("=" * 60)
            
            # Show success dialog
            self.root.after(0, lambda: messagebox.showinfo(
                "Success!",
                f"Successfully generated {len(results)} study prompts!\n\nSaved to:\n{output_csv}"
            ))
            
        except Exception as e:
            self._log_status(f"\n❌ Error: {str(e)}")
            import traceback
            self._log_status(traceback.format_exc())
            self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred:\n{str(e)}"))
        
        finally:
            # Re-enable button
            self.root.after(0, lambda: self.progress_bar.stop())
            self.root.after(0, lambda: self.generate_btn.config(state=tk.NORMAL, text="🚀 Generate Study Prompts"))


def main():
    """Main entry point"""
    root = tk.Tk()
    app = StudyPromptGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
