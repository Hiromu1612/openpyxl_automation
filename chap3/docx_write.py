import docx,datetime

template_file=r"C:\Users\1612h\Downloads\0src\samples\ch3\letter.docx"
save_file="chap3\word_file\letter.docx"
now=datetime.datetime.now()

#書き換える内容を指定
card={
    "2021年10月10日":now.strftime("%Y年%m月%d日"),
    "●●●御中":"まいなび出版御中",
    "■■■様":"山田様",
    "★★の送付について":"契約書の送付について"
}

#wordファイルを読み込む
doc=docx.Document(template_file)
for p in doc.paragraphs:
    for k, v in card.items():
        p.text = p.text.replace(k, v)

#wordファイルを保存
doc.save(save_file)