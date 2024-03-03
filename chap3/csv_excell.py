import csv,openpyxl

input_file=r"C:\Users\1612h\Downloads\0src\samples\ch3\meibo.csv"
template_file=r"C:\Users\1612h\Downloads\0src\samples\ch3\card-template.xlsx"
save_file="chap3\excell_file\csv_excell.xlsx"

#csvファイルを読み込む
def read_csv(filename):
    with open(filename,encoding="sjis") as f:
        reader=csv.reader(f)
        next(reader) #ヘッダ行を読み飛ばす
        return [row for row in reader]
    
#エクセルを読み込む
book=openpyxl.load_workbook(template_file)
sheet_template=book["Sheet"]#テンプレートのシートを取得
for i,customer in enumerate(read_csv(input_file)):
    name,post_code,address=customer
    idx=i%10 #10行ごとに新しいシートを作成 idxは0から9までの値を取る
    if idx==0:
        new_sheet=book.copy_worksheet(sheet_template)
        new_sheet.title="Page"+str(idx)

    row=4*(idx%5)+2 #5行ごとに新しい行を作成
    column=2*(idx//5)+2 #2列ごとに新しい列を作成

    new_sheet.cell(row=row+0,column=column,value=name)
    new_sheet.cell(row=row+1,column=column,value=post_code)
    new_sheet.cell(row=row+2,column=column,value=address)

book.remove(sheet_template) #テンプレートのシートを削除
book.save(save_file)