import openpyxl

book=openpyxl.Workbook()
sheet=book.active

for i in range(1,21):
    for j in range(1,21):
        sheet.cell(row=i,column=j,value=i*j)
    
book.save('chap2/kuku2_xl.xlsx')