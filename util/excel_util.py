import openpyxl

# https://stackoverflow.com/questions/33541692/how-to-find-the-last-row-in-a-column-using-openpyxl-normal-workbook
def get_last_row(ws: openpyxl.worksheet.worksheet.Worksheet) -> int:
    return ws.max_row

def get_cell(column_letter: str, row_number: int) -> str:
    return column_letter + str(row_number)