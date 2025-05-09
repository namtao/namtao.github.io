from weasyprint import HTML

# html_file = "index.html"
# css_file = "style.css"
# output_pdf = "NguyenVanNam-CV.pdf"

# HTML(html_file).write_pdf(output_pdf, stylesheets=[css_file])
# print(f"PDF đã được tạo: {output_pdf}")


html_file = "cv-vn.html"
css_file = "style-cv.css"
output_pdf = "CV_NguyenVanNam-VN.pdf"

HTML(html_file).write_pdf(output_pdf, stylesheets=[css_file])
print(f"PDF đã được tạo: {output_pdf}")

html_file = "cv-en.html"
css_file = "style-cv.css"
output_pdf = "CV_NguyenVanNam-EN.pdf"

HTML(html_file).write_pdf(output_pdf, stylesheets=[css_file])
print(f"PDF đã được tạo: {output_pdf}")
