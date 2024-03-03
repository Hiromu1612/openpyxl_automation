import openpyxl

book=openpyxl.Workbook()
sheet=book.active

#セル名から行/列番号を取得
cell=sheet["C2"]#セルを指定
(row,column)=(cell.row,cell.column)
print("C2=({},{})".format(row,column))

#行/列番号からセル名を取得
cell=sheet.cell(row=2,column=3)
print("(2,3)={}".format(cell.coordinate))