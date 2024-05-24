from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.pdf import PageObject
from io import BytesIO

# Путь к шаблону PDF
template_path = 'base.pdf'
output_path = '4132300399.pdf'

# Открываем PDF-файлы
with open(template_path, 'rb') as template_file:
    template_pdf = PdfReader(template_file)
    output_pdf = PdfWriter()

    # Проходимся по каждой странице шаблона
    for page_num in range(len(template_pdf.pages)):
        page = template_pdf.pages[page_num]
        text = page.extract_text()

        # Создаем новую страницу с обновленным текстом
        new_page = PageObject.createBlankPage(width=page.mediaBox.getWidth(), height=page.mediaBox.getHeight())
        new_page.mergePage(page)
        new_page_content = new_page.getContents()
        if new_page_content:
            new_page_content += b"\n(Dopолнительный текст)"
        else:
            new_page_content = b"(Dopолнительный текст)"
        new_page.__setitem__(PageObject.CONTENTS, new_page_content)

        # Добавляем страницу в выходной PDF
        output_pdf.addPage(new_page)

    # Сохраняем измененный PDF
    with open(output_path, 'wb') as output_file:
        output_pdf.write(output_file)

print("Документ успешно сохранен.")
