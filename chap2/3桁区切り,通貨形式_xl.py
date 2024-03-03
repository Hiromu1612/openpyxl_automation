import openpyxl
book=openpyxl.Workbook()
sheet=book.active

#セルに値と書式を指定する関数を定義
def set_cell(cell_name,value,format):
    cell=sheet[cell_name]
    cell.value=value
    cell.number_format=format

#3桁ごとにカンマを表示
keta3_format="#,##0"
sheet["A1"]=keta3_format
set_cell("B1",12345,keta3_format) #set_cell()を使ってセルに値と書式を指定
set_cell("C1",123456789,keta3_format)

#通貨形式を指定
currency_format='"¥"#,##0;"¥"\\-#,##0'#正の場合;負の場合
sheet["A2"]=currency_format
set_cell("B2",12345,currency_format)
set_cell("C2",-12345,currency_format)

#数値のマイナス値を△で表し、赤色にする
minus_format='[Blue]"△"#,##0;[Red]"△"-#,##0'
sheet["A3"]=minus_format
set_cell("B3",12345,minus_format)
set_cell("C3",-12345,minus_format)

book.save("chap2/excell_file/number_format2_xl.xlsx")#新規ブックを保存