import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import pdfkit

class HtmlToPdfToolInput(BaseModel):
    """Input schema for HtmlToPdfTool."""
    html_file_path: str = Field(..., description="HTML file to be converted to PDF.")

class HtmlToPdfTool(BaseTool):
    name: str = "html_to_pdf_tool"
    description: str = (
        "This tool is used to convert HTML to PDF."
    )
    args_schema: Type[BaseModel] = HtmlToPdfToolInput
    
    def _run(self, html_file_path: str) -> str:
        """Convert HTML to PDF"""
        try:
            output_pdf = "report.pdf"
            pdfkit.from_file(html_file_path, output_pdf)
            return f"PDF report created successfully at: {output_pdf}"
        except Exception as e:
            return f"Error creating PDF: {str(e)}"
