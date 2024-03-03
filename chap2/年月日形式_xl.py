import openpyxl

book=openpyxl.Workbook()
sheet=book.active

import datetime
dt=datetime.datetime(year=2023,month=6,day=14,hour=12,minute=30,second=15)
sheet.append([dt,dt,dt,dt])

#年/月/日の形式で表示
sheet["A1"].number_format="yyyy/mm/dd" #number_format表示形式を指定
sheet["B1"].number_format="yyyy年mm月dd日"
sheet["C1"].number_format="hh:mm:ss"
sheet["D1"].number_format="yyyy/mm/dd hh:mm:ss"

book.save("chap2/excell_file/number_format3_xl.xlsx")#新規ブックを保存