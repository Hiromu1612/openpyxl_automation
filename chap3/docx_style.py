import docx,datetime

template_file=r"C:\Users\1612h\Downloads\0src\samples\ch3\letter.docx"
save_file="chap3\word_file\letter_style.docx"
now=datetime.datetime.now()

card={
    "2021年10月10日":now.strftime("%Y年%m月%d日"),
    "●●●御中":"まいなび出版御中",
    "■■■様":"山田様",
    "★★★の送付について":"契約書の送付について"
}

card_style={
    "★★★の送付について":True
}

doc=docx.Document(template_file)

for p in doc.paragraphs:
    for k,v in card.items():
        if p.text.find(k)>=0:
            p.text=p.text.replace(k,v)

            if k in card_style:
                font=p.runs[0].font #段落のフォントを取得 [0]は段落の先頭のフォントを取得
                font.bold=True
                font.underline=True
                font.size=docx.shared.Pt(14) #sharedモジュールのPt関数でフォントサイズを指定
            
doc.save(save_file)