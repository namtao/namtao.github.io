from weasyprint import HTML

# Đường dẫn đến tệp HTML và CSS
html_file = "index.html"
css_file = "style.css"
output_pdf = "NguyenVanNam-CV.pdf"

# Tạo PDF từ tệp HTML
HTML(html_file).write_pdf(output_pdf, stylesheets=[css_file])

print(f"PDF đã được tạo: {output_pdf}")
