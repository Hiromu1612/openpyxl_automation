import csv,pprint

#csvモジュールを使わない方法
with open("chap3\items.csv",encoding='utf-8') as f:
    text=f.read().strip() #stripで改行を取り除く
    lines=text.split("\n") #改行で分割
    data=[line.split(",") for line in lines] #カンマで分割
    pprint.pprint(data) #pprintはリストや辞書を見やすく表示する

#csvモジュールを使う方法
with open("chap3\items.csv",encoding='utf-8') as f:
    reader=csv.reader(f)
    data=[row for row in reader]
    pprint.pprint(data)