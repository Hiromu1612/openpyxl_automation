import openpyxl

book=openpyxl.Workbook()
sheet=book.active

#A1,B1,C1に全て同じ値を指定
value=3.14159
sheet.append([value,value,value])

#小数点以下を省略
sheet["A1"].number_format="0"
#小数点以下2桁まで表示
sheet["B1"].number_format="0.00"
#小数点以下3桁まで表示
sheet["C1"].number_format="0.000"


#年/月/日の形式で表示
sheet["A2"]=2023614
sheet["A2"].number_format="yyyy/mm/dd"

book.save("chap2/excell_file/number_format_xl.xlsx")