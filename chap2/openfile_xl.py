import openpyxl

book=openpyxl.load_workbook('chap2/save.xlsx') #保存したエクセルファイルを読み込む
sheet=book.worksheets[0] #ワークシートの1枚目を取得
cell=sheet['A1'] #A1のセルを取得
print(cell.value) #A1のセルの値を表示