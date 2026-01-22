#!/usr/bin/env python3
"""
PDF Generator GUI - Create professional PDFs from images
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path
import threading
from generate_pdf_from_images import PDFGenerator


class PDFGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Generator - Images to Professional PDF")
        self.root.geometry("700x600")
        
        # Variables
        self.image_folder = tk.StringVar()
        self.output_pdf = tk.StringVar(value="output.pdf")
        self.title_var = tk.StringVar(value="NBME 30")
        self.additional_text = tk.StringVar()
        
        self._build_ui()
    
    def _build_ui(self):
        """Build the UI"""
        # Header
        header_frame = tk.Frame(self.root, bg="#667eea", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="📄 PDF Generator",
            font=("Helvetica", 20, "bold"),
            bg="#667eea",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Main container
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Settings
        settings_frame = tk.LabelFrame(main_frame, text="⚙️ PDF Settings", 
                                      font=("Helvetica", 12, "bold"), padx=10, pady=10)
        settings_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Title
        tk.Label(settings_frame, text="PDF Title:", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(0, 5))
        title_entry = tk.Entry(settings_frame, textvariable=self.title_var, font=("Helvetica", 10))
        title_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Additional text
        tk.Label(settings_frame, text="Additional Text (optional):", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(0, 5))
        text_entry = tk.Entry(settings_frame, textvariable=self.additional_text, font=("Helvetica", 10))
        text_entry.pack(fill=tk.X, pady=(0, 5))
        tk.Label(settings_frame, text="e.g., 'Practice Questions', 'Study Material', etc.", 
                font=("Helvetica", 9), fg="gray").pack(anchor=tk.W)
        
        # Files
        files_frame = tk.LabelFrame(main_frame, text="📁 Files", 
                                   font=("Helvetica", 12, "bold"), padx=10, pady=10)
        files_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Image folder
        tk.Label(files_frame, text="Image Folder:", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(0, 5))
        folder_frame = tk.Frame(files_frame)
        folder_frame.pack(fill=tk.X, pady=(0, 5))
        
        folder_entry = tk.Entry(folder_frame, textvariable=self.image_folder, font=("Helvetica", 10))
        folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        tk.Button(folder_frame, text="Browse...", command=self._select_folder, 
                 font=("Helvetica", 9)).pack(side=tk.RIGHT)
        
        tk.Label(files_frame, text="Folder containing numbered images (1.png, 2.jpg, etc.)", 
                font=("Helvetica", 9), fg="gray").pack(anchor=tk.W, pady=(0, 10))
        
        # Output PDF
        tk.Label(files_frame, text="Output PDF:", font=("Helvetica", 10)).pack(anchor=tk.W, pady=(0, 5))
        output_frame = tk.Frame(files_frame)
        output_frame.pack(fill=tk.X)
        
        output_entry = tk.Entry(output_frame, textvariable=self.output_pdf, font=("Helvetica", 10))
        output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        tk.Button(output_frame, text="Save As...", command=self._select_output, 
                 font=("Helvetica", 9)).pack(side=tk.RIGHT)
        
        # Progress
        progress_frame = tk.LabelFrame(main_frame, text="📊 Progress", 
                                      font=("Helvetica", 12, "bold"), padx=10, pady=10)
        progress_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        self.status_text = scrolledtext.ScrolledText(
            progress_frame,
            height=10,
            font=("Courier", 9),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        self.status_text.pack(fill=tk.BOTH, expand=True)
        
        # Generate button
        self.generate_btn = tk.Button(
            main_frame,
            text="📄 Generate PDF",
            command=self._start_generation,
            bg="#667eea",
            fg="white",
            font=("Helvetica", 14, "bold"),
            height=2,
            cursor="hand2"
        )
        self.generate_btn.pack(fill=tk.X)
    
    def _select_folder(self):
        """Select image folder"""
        folder = filedialog.askdirectory(title="Select Image Folder")
        if folder:
            self.image_folder.set(folder)
            
            # Auto-set output filename based on title
            title = self.title_var.get().replace(" ", "_")
            output = Path(folder).parent / f"{title}.pdf"
            self.output_pdf.set(str(output))
    
    def _select_output(self):
        """Select output PDF location"""
        filename = filedialog.asksaveasfilename(
            title="Save PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")],
            initialfile=self.output_pdf.get()
        )
        if filename:
            self.output_pdf.set(filename)
    
    def _log(self, message):
        """Add message to status log"""
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.root.update_idletasks()
    
    def _start_generation(self):
        """Start PDF generation"""
        # Validate
        if not self.image_folder.get():
            messagebox.showerror("Error", "Please select an image folder!")
            return
        
        if not Path(self.image_folder.get()).exists():
            messagebox.showerror("Error", "Image folder does not exist!")
            return
        
        if not self.output_pdf.get():
            messagebox.showerror("Error", "Please specify an output PDF file!")
            return
        
        # Disable button
        self.generate_btn.config(state=tk.DISABLED, text="⏳ Generating...")
        self.status_text.delete(1.0, tk.END)
        
        # Run in background
        thread = threading.Thread(target=self._run_generation, daemon=True)
        thread.start()
    
    def _run_generation(self):
        """Run the actual PDF generation"""
        try:
            # Create generator
            generator = PDFGenerator(
                title=self.title_var.get(),
                additional_text=self.additional_text.get()
            )
            
            # Redirect output
            import io
            import sys
            
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()
            
            # Generate PDF
            success = generator.create_pdf(
                self.image_folder.get(),
                self.output_pdf.get()
            )
            
            # Get output
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            # Display output
            for line in output.split('\n'):
                self.root.after(0, lambda l=line: self._log(l))
            
            if success:
                self.root.after(0, lambda: messagebox.showinfo(
                    "Success!",
                    f"PDF created successfully!\n\nSaved to:\n{self.output_pdf.get()}"
                ))
            
        except Exception as e:
            self.root.after(0, lambda: self._log(f"\n❌ Error: {str(e)}"))
            self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred:\n{str(e)}"))
        
        finally:
            self.root.after(0, lambda: self.generate_btn.config(
                state=tk.NORMAL, 
                text="📄 Generate PDF"
            ))


def main():
    """Main entry point"""
    root = tk.Tk()
    app = PDFGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
