from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
import re
import io

def generate(data):
    pdf_buffer = io.BytesIO()
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("cv_template.html")
    html_out = template.render(data)
    HTML(string=html_out).write_pdf(target=pdf_buffer, stylesheets=[CSS("static/style1.css")])
    pdf_buffer.seek(0)
    return pdf_buffer

def clear_filename(filename):
    # Usuwa niedozwolone znaki
    return re.sub(r'[\\/:*?"<>|]', '_', filename)