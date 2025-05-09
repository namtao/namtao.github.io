# from weasyprint import HTML

# html_file = "index.html"
# css_file = "style.css"
# output_pdf = "NguyenVanNam-CV.pdf"

# HTML(html_file).write_pdf(output_pdf, stylesheets=[css_file])
# print(f"PDF đã được tạo: {output_pdf}")


# html_file = "cv-vn.html"
# css_file = "style-cv.css"
# output_pdf = "CV_NguyenVanNam-VN.pdf"

# HTML(html_file).write_pdf(output_pdf, stylesheets=[css_file])
# print(f"PDF đã được tạo: {output_pdf}")

# html_file = "cv-en.html"
# css_file = "style-cv.css"
# output_pdf = "CV_NguyenVanNam-EN.pdf"

# HTML(html_file).write_pdf(output_pdf, stylesheets=[css_file])
# print(f"PDF đã được tạo: {output_pdf}")


import asyncio
from playwright.async_api import async_playwright
import os


async def html_to_pdf(input_html_path, output_pdf_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Đảm bảo đường dẫn file:// đầy đủ
        file_url = "file://" + os.path.abspath(input_html_path)
        await page.goto(file_url)

        # Tạo PDF với lề và in nền
        await page.pdf(
            path=output_pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"},
        )

        await browser.close()
        print(f"✅ PDF đã được tạo tại: {output_pdf_path}")


# Gọi hàm
asyncio.run(html_to_pdf("cv-vn.html", "CV_NguyenVanNam_VN.pdf"))
asyncio.run(html_to_pdf("cv-en.html", "CV_NguyenVanNam_EN.pdf"))
