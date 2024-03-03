import openpyxl

book=openpyxl.load_workbook(r"C:\Users\1612h\Downloads\0src\samples\ch2\uriage.xlsx",data_only=True)#data_only=Trueで計算結果を取得
sheet=book.active

#A3からF999までの適当な範囲を取り出す
rows=sheet["A3:F999"]
for row in rows:
    r=[]
    for cell in row:
        r.append(cell.value)
    if r[0] is None:#空白のセルに到達したら終了
        break
    print(r)#計算結果が表示される