from weasyprint import HTML

html_file = "index.html"
css_file = "style.css"
output_pdf = "NguyenVanNam-CV.pdf"

HTML(html_file).write_pdf(output_pdf, stylesheets=[css_file])
print(f"PDF đã được tạo: {output_pdf}")
