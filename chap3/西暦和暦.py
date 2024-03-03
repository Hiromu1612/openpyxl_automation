import openpyxl
import datetime

input_file=r"C:\Users\1612h\Downloads\0src\samples\ch3\date-sample.xlsx"
output_file="chap3/excell_file/wareki.xlsx"
cell_format='[$-ja-JP]gggg"年"m"月"d"日"'

#メイン処理
def date_wareki(input_file,output_file):
    book=openpyxl.load_workbook(input_file)
    #全シート
    for sheet in book.worksheets: #worksheetsはシートのリスト
        #全行
        for row in sheet.iter_rows():
            #全セル
            for cell in row:
                check_cell(cell)
    book.save(output_file)

def check_cell(cell):
    if type(cell.value) is datetime.datetime:
        cell.number_format=cell_format

if __name__=="__main__":
    date_wareki(input_file,output_file) #メイン処理を実行