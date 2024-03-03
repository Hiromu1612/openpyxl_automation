import docx

#既存のwordファイルを読み込む
doc = docx.Document(r"C:\Users\1612h\Downloads\0src\samples\ch3\letter.docx")

for p in doc.paragraphs:
    print(p.text) #段落のテキストを出力