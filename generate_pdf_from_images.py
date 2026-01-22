#!/usr/bin/env python3
"""
Professional PDF Generator from Images
Creates a PDF with 2 images per page in a clean, professional layout
"""

import os
import sys
from pathlib import Path
from PIL import Image
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import argparse
from datetime import datetime


class PDFGenerator:
    def __init__(self, title="NBME 30", additional_text="", page_size=letter):
        self.title = title
        self.additional_text = additional_text
        self.page_size = page_size
        self.width, self.height = page_size
        self.margin = 0.75 * inch
        
    def create_pdf(self, image_folder, output_pdf):
        """Create PDF from images in folder"""
        print("=" * 60)
        print("📄 Professional PDF Generator")
        print("=" * 60)
        print()
        
        # Find all images
        images = self._find_images(image_folder)
        
        if not images:
            print("❌ No images found in folder!")
            return False
        
        print(f"✓ Found {len(images)} images")
        print(f"📝 Title: {self.title}")
        if self.additional_text:
            print(f"📝 Additional text: {self.additional_text}")
        print()
        
        # Create PDF
        c = canvas.Canvas(str(output_pdf), pagesize=self.page_size)
        
        # Add title page
        self._add_title_page(c)
        
        # Add images (2 per page)
        total_pages = (len(images) + 1) // 2  # Round up
        
        for i in range(0, len(images), 2):
            page_num = (i // 2) + 1
            print(f"[{page_num}/{total_pages}] Adding page {page_num}...")
            
            c.showPage()  # New page
            
            # Add header with title
            self._add_header(c, page_num, total_pages + 1)
            
            # Add first image (top)
            if i < len(images):
                self._add_image(c, images[i], position='top')
            
            # Add second image (bottom)
            if i + 1 < len(images):
                self._add_image(c, images[i + 1], position='bottom')
            
            # Add footer
            self._add_footer(c, page_num + 1, total_pages + 1)
        
        # Save PDF
        c.save()
        
        print()
        print("=" * 60)
        print(f"✅ PDF created successfully!")
        print(f"📄 Output: {output_pdf}")
        print(f"📊 Total pages: {total_pages + 1} (1 title + {total_pages} content)")
        print("=" * 60)
        
        return True
    
    def _find_images(self, folder):
        """Find and sort images by number"""
        folder = Path(folder)
        
        if not folder.exists():
            return []
        
        # Find all image files
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
        all_images = []
        
        for ext in extensions:
            all_images.extend(folder.glob(f'*{ext}'))
            all_images.extend(folder.glob(f'*{ext.upper()}'))
        
        # Sort by number in filename
        def get_number(path):
            # Extract number from filename
            import re
            numbers = re.findall(r'\d+', path.stem)
            return int(numbers[0]) if numbers else 0
        
        sorted_images = sorted(all_images, key=get_number)
        
        return sorted_images
    
    def _add_title_page(self, c):
        """Add professional title page"""
        # Background
        c.setFillColor(colors.HexColor('#667eea'))
        c.rect(0, 0, self.width, self.height, fill=True, stroke=False)
        
        # Title
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 48)
        title_y = self.height - 3 * inch
        c.drawCentredString(self.width / 2, title_y, self.title)
        
        # Subtitle/Additional text
        if self.additional_text:
            c.setFont("Helvetica", 18)
            c.drawCentredString(self.width / 2, title_y - 0.7 * inch, self.additional_text)
        
        # Date
        c.setFont("Helvetica", 14)
        date_str = datetime.now().strftime("%B %d, %Y")
        c.drawCentredString(self.width / 2, 2 * inch, date_str)
        
        # Footer line
        c.setStrokeColor(colors.white)
        c.setLineWidth(2)
        c.line(self.margin, 1.5 * inch, self.width - self.margin, 1.5 * inch)
        
        c.setFont("Helvetica", 12)
        c.drawCentredString(self.width / 2, 1.2 * inch, "Professional Study Material")
    
    def _add_header(self, c, page_num, total_pages):
        """Add header to page"""
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.HexColor('#667eea'))
        c.drawString(self.margin, self.height - 0.5 * inch, self.title)
        
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.grey)
        c.drawRightString(self.width - self.margin, self.height - 0.5 * inch, 
                         f"Page {page_num} of {total_pages}")
        
        # Header line
        c.setStrokeColor(colors.HexColor('#667eea'))
        c.setLineWidth(1)
        c.line(self.margin, self.height - 0.6 * inch, 
               self.width - self.margin, self.height - 0.6 * inch)
    
    def _add_footer(self, c, page_num, total_pages):
        """Add footer to page"""
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.grey)
        
        # Footer line
        c.setStrokeColor(colors.lightgrey)
        c.setLineWidth(0.5)
        c.line(self.margin, 0.6 * inch, self.width - self.margin, 0.6 * inch)
        
        # Page number
        c.drawCentredString(self.width / 2, 0.4 * inch, str(page_num))
    
    def _add_image(self, c, image_path, position='top'):
        """Add image to page"""
        try:
            # Open image to get dimensions
            img = Image.open(image_path)
            img_width, img_height = img.size
            
            # Calculate available space
            content_width = self.width - 2 * self.margin
            
            if position == 'top':
                content_height = (self.height - self.margin - 0.8 * inch - self.margin) / 2 - 0.2 * inch
                y_position = self.height - 0.9 * inch - content_height
            else:  # bottom
                content_height = (self.height - self.margin - 0.8 * inch - self.margin) / 2 - 0.2 * inch
                y_position = self.margin + 0.5 * inch
            
            # Calculate scaling to fit
            scale_w = content_width / img_width
            scale_h = content_height / img_height
            scale = min(scale_w, scale_h)
            
            new_width = img_width * scale * 0.95  # 95% to add padding
            new_height = img_height * scale * 0.95
            
            # Center the image
            x_position = (self.width - new_width) / 2
            
            # Add image
            c.drawImage(str(image_path), x_position, y_position - new_height, 
                       width=new_width, height=new_height, 
                       preserveAspectRatio=True, mask='auto')
            
            # Add image label
            c.setFont("Helvetica", 9)
            c.setFillColor(colors.grey)
            label = f"Question {image_path.stem}"
            c.drawCentredString(self.width / 2, y_position - new_height - 0.2 * inch, label)
            
        except Exception as e:
            print(f"⚠️  Warning: Could not add image {image_path.name}: {e}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Generate professional PDF from images')
    parser.add_argument('image_folder', help='Folder containing numbered images')
    parser.add_argument('-o', '--output', default='output.pdf', help='Output PDF filename')
    parser.add_argument('-t', '--title', default='NBME 30', help='PDF title (default: NBME 30)')
    parser.add_argument('-a', '--additional-text', default='', help='Additional text for title page')
    parser.add_argument('--letter', action='store_true', help='Use Letter size (default)')
    parser.add_argument('--a4', action='store_true', help='Use A4 size')
    
    args = parser.parse_args()
    
    # Determine page size
    page_size = A4 if args.a4 else letter
    
    # Create generator
    generator = PDFGenerator(
        title=args.title,
        additional_text=args.additional_text,
        page_size=page_size
    )
    
    # Generate PDF
    success = generator.create_pdf(args.image_folder, args.output)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
