"""PDF manipulation tools using PyPDF2 and reportlab."""

from typing import Annotated
from semantic_kernel.functions import kernel_function

try:
    from PyPDF2 import PdfReader, PdfWriter, PdfMerger
    PYPDF2_AVAILABLE = True
except ImportError:
    PYPDF2_AVAILABLE = False

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


class PDFTools:
    """Tools for creating and manipulating PDF files."""

    def __init__(self):
        """Initialize PDFTools."""
        if not PYPDF2_AVAILABLE:
            print("Warning: PyPDF2 not installed. Install with: pip install PyPDF2")
        if not REPORTLAB_AVAILABLE:
            print("Warning: reportlab not installed. Install with: pip install reportlab")

    @kernel_function(
        name="create_pdf",
        description="Create a simple PDF document with text"
    )
    def create_pdf(
        self,
        file_path: Annotated[str, "Full path where the PDF will be created"],
        text: Annotated[str, "Text content to add to the PDF"]
    ) -> Annotated[str, "Success or error message"]:
        """Create a new PDF with text content."""
        if not REPORTLAB_AVAILABLE:
            return "Error: reportlab is not installed"
        
        try:
            c = canvas.Canvas(file_path, pagesize=letter)
            width, height = letter
            
            # Split text into lines and add to PDF
            y_position = height - 50
            lines = text.split('\n')
            
            for line in lines:
                if y_position < 50:
                    c.showPage()
                    y_position = height - 50
                c.drawString(50, y_position, line)
                y_position -= 15
            
            c.save()
            return f"PDF created successfully at: {file_path}"
        except Exception as err:
            return f"Error creating PDF: {str(err)}"

    @kernel_function(
        name="extract_pdf_text",
        description="Extract all text from a PDF file"
    )
    def extract_pdf_text(
        self,
        file_path: Annotated[str, "Path to the PDF file"]
    ) -> Annotated[str, "Extracted text or error message"]:
        """Extract all text content from a PDF."""
        if not PYPDF2_AVAILABLE:
            return "Error: PyPDF2 is not installed"
        
        try:
            reader = PdfReader(file_path)
            text_content = []
            
            for page in reader.pages:
                text_content.append(page.extract_text())
            
            return "\n\n".join(text_content)
        except Exception as err:
            return f"Error extracting text from PDF: {str(err)}"

    @kernel_function(
        name="merge_pdfs",
        description="Merge multiple PDF files into a single PDF"
    )
    def merge_pdfs(
        self,
        output_path: Annotated[str, "Path where the merged PDF will be saved"],
        input_paths: Annotated[str, "Comma-separated paths of PDFs to merge"]
    ) -> Annotated[str, "Success or error message"]:
        """Merge multiple PDF files into one."""
        if not PYPDF2_AVAILABLE:
            return "Error: PyPDF2 is not installed"
        
        try:
            merger = PdfMerger()
            paths = [p.strip() for p in input_paths.split(',')]
            
            for pdf_path in paths:
                merger.append(pdf_path)
            
            merger.write(output_path)
            merger.close()
            
            return f"Successfully merged {len(paths)} PDFs into: {output_path}"
        except Exception as err:
            return f"Error merging PDFs: {str(err)}"

    @kernel_function(
        name="split_pdf",
        description="Split a PDF into individual pages"
    )
    def split_pdf(
        self,
        file_path: Annotated[str, "Path to the PDF file to split"],
        output_dir: Annotated[str, "Directory where individual pages will be saved"]
    ) -> Annotated[str, "Success or error message"]:
        """Split a PDF into separate single-page PDFs."""
        if not PYPDF2_AVAILABLE:
            return "Error: PyPDF2 is not installed"
        
        try:
            import os
            reader = PdfReader(file_path)
            
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)
                
                output_filename = os.path.join(output_dir, f"page_{i+1}.pdf")
                with open(output_filename, 'wb') as output_file:
                    writer.write(output_file)
            
            return f"Successfully split PDF into {len(reader.pages)} pages in: {output_dir}"
        except Exception as err:
            return f"Error splitting PDF: {str(err)}"

    @kernel_function(
        name="get_pdf_info",
        description="Get information about a PDF file (page count, metadata)"
    )
    def get_pdf_info(
        self,
        file_path: Annotated[str, "Path to the PDF file"]
    ) -> Annotated[str, "PDF information or error message"]:
        """Get metadata and information about a PDF file."""
        if not PYPDF2_AVAILABLE:
            return "Error: PyPDF2 is not installed"
        
        try:
            reader = PdfReader(file_path)
            info = []
            
            info.append(f"Number of pages: {len(reader.pages)}")
            
            if reader.metadata:
                info.append("\nMetadata:")
                for key, value in reader.metadata.items():
                    info.append(f"  {key}: {value}")
            
            return "\n".join(info)
        except Exception as err:
            return f"Error reading PDF info: {str(err)}"

    @kernel_function(
        name="extract_pdf_page",
        description="Extract a specific page from a PDF"
    )
    def extract_pdf_page(
        self,
        file_path: Annotated[str, "Path to the PDF file"],
        page_number: Annotated[int, "Page number to extract (1-based)"],
        output_path: Annotated[str, "Path where the extracted page will be saved"]
    ) -> Annotated[str, "Success or error message"]:
        """Extract a specific page from a PDF to a new file."""
        if not PYPDF2_AVAILABLE:
            return "Error: PyPDF2 is not installed"
        
        try:
            reader = PdfReader(file_path)
            
            if page_number < 1 or page_number > len(reader.pages):
                return f"Error: Page number {page_number} out of range (1-{len(reader.pages)})"
            
            writer = PdfWriter()
            writer.add_page(reader.pages[page_number - 1])
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            return f"Page {page_number} extracted successfully to: {output_path}"
        except Exception as err:
            return f"Error extracting page: {str(err)}"

    @kernel_function(
        name="rotate_pdf_pages",
        description="Rotate all pages in a PDF by specified degrees"
    )
    def rotate_pdf_pages(
        self,
        file_path: Annotated[str, "Path to the PDF file"],
        output_path: Annotated[str, "Path where the rotated PDF will be saved"],
        degrees: Annotated[int, "Degrees to rotate (90, 180, 270)"]
    ) -> Annotated[str, "Success or error message"]:
        """Rotate all pages in a PDF."""
        if not PYPDF2_AVAILABLE:
            return "Error: PyPDF2 is not installed"
        
        try:
            if degrees not in [90, 180, 270]:
                return "Error: Degrees must be 90, 180, or 270"
            
            reader = PdfReader(file_path)
            writer = PdfWriter()
            
            for page in reader.pages:
                page.rotate(degrees)
                writer.add_page(page)
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            return f"PDF rotated {degrees} degrees and saved to: {output_path}"
        except Exception as err:
            return f"Error rotating PDF: {str(err)}"
