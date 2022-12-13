import zipfile
import os
from pathlib import Path
import csv
import io
from PyPDF2 import PdfReader
from openpyxl import load_workbook


def file_data_from_zip_to_list(file_dir: str, zip_file_name: str, file_name: str):
    file_format = file_name.split(".")[1]
    main_path = os.path.dirname(__file__)
    file_path = os.path.join((Path(main_path).parents[0]), f'{file_dir}{os.path.sep}{zip_file_name}.zip')
    file_text_in_list = []
    if file_format == 'csv':
        with zipfile.ZipFile(file_path) as zipf:
            with zipf.open(f'{file_name}', 'r') as f:
                reader = csv.reader(
                    io.TextIOWrapper(f, newline='')
                )
                for row in reader:
                    for item in row:
                        file_text_in_list.append([item])
        return file_text_in_list
    if file_format == 'pdf':
        with zipfile.ZipFile(file_path) as zipf:
            with zipf.open(f'{file_name}', 'r') as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    text = page.extract_text().split("\n")
                    file_text_in_list.append(text)
        return [item for sublist in file_text_in_list for item in sublist]
    if file_format == 'xlsx':
        with zipfile.ZipFile(file_path) as zipf:
            with zipf.open('Xlsx_file.xlsx', 'r') as f:
                workbook = load_workbook(f)
                sheet = workbook.active
                for row in sheet:
                    for cell in row:
                        file_text_in_list.append([sheet[cell.coordinate].value])
        return file_text_in_list
    else:
        return print('sorry we not supported yor file format yet')


def test_my_csv():
    assert ['Тест_2'] in file_data_from_zip_to_list('resources', 'test', 'Csv_file.csv')


def test_my_pdf():
    assert 'четыре' and 'пять' in file_data_from_zip_to_list('resources', 'test', 'Pdf_file.pdf')


def test_my_xlsx():
    assert ['строка1_3'] and ['строка2_3'] in file_data_from_zip_to_list('resources', 'test', 'Xlsx_file.xlsx')