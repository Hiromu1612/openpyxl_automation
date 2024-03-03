import openpyxl

book=openpyxl.Workbook() #新規のワークブックを作成 ワークブックとはエクセルファイルのこと
sheet=book.active #アクティブ(最後に開いた)なワークシートを取得 ワークシートとはエクセルファイルのシートのこと 縦がrow(列)、横がcolumn(行)
sheet['A1']='Hello'
sheet['A2']='World!'
sheet['B1']='Hello'
sheet['B2']='World!'
#chap2フォルダにhello.xlsxとして保存
book.save('chap2/save.xlsx')