import xlrd
from source_code import login_page

def read_locators():
    file_path = login_page.loc_file_path
    sheet_name = login_page.loc_sheet_name
    wb = xlrd.open_workbook(file_path)
    sh = wb.sheet_by_name(sheet_name)
    rows = sh.get_rows()
    header = next(rows)

    data = {}
    for row in rows:
        data[row[0].value] = (row[1].value, row[2].value)

    return data
