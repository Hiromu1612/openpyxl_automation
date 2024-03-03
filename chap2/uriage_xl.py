import openpyxl

book=openpyxl.load_workbook(r"C:\Users\1612h\Downloads\0src\samples\ch2\uriage.xlsx")
sheet=book.active

#A3かF9のセルを取得
rows=sheet["A3:F9"]
for row in rows:
    r=[]
    for cell in row:
        r.append(cell.value)
    print(r)#計算式が表示される

#A3かF9のセルを取得 計算結果を表示
book=openpyxl.load_workbook(r"C:\Users\1612h\Downloads\0src\samples\ch2\uriage.xlsx",data_only=True)#data_only=Trueで計算結果を取得
sheet=book.active
rows=sheet["A3:F9"]
for row in rows:
    r=[]
    for cell in row:
        r.append(cell.value)
    print(r)#計算結果が表示される