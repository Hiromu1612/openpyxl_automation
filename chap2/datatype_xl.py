import openpyxl
book=openpyxl.Workbook()
sheet=book.active

#数値を設定
cell=sheet["A1"]
cell.value=345
sheet["B1"]="data_type="+cell.data_type #data_typeでデータ型を取得

#文字列を設定
cell=sheet["A2"]
cell.value="abc"
sheet["B2"]="data_type="+cell.data_type

#日時を設定
cell=sheet["A3"]
from datetime import date
cell.value=date(2023,6,14)
sheet["B3"]="data_type="+cell.data_type

book.save("chap2/excell_file/data_type_xl.xlsx")

#nはnumber(数値)、sはstring(文字列)、dはdatetime(日時)を意味します。