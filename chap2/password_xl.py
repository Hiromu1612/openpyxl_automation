import msoffcrypto
import openpyxl

#パスワード付きのエクセルファイルを開く
fin=open("chap2/excell_file/wareki_list_xl.xlsx","rb") #rbは読み込み専用
file=msoffcrypto.OfficeFile(fin)
#パスワードを指定して開く
file.load_key(password="abcd")
#復号化したファイルを保存
file.decrypt(open("chap2/excell_file/wareki_list_xl_decrypt.xlsx","wb")) #wbは書き込み専用

book=openpyxl.load_workbook("chap2/excell_file/wareki_list_xl_decrypt.xlsx")
sheet=book.active
for row in sheet.iter_rows(min_row=2):
    r=[]
    for cell in row:
        r.append(cell.value)
    print(r)