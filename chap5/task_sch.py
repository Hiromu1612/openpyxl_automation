import requests,os,platform

save_file="chap5/tennki.txt"

#クジラ気象情報APIから天気情報を取得
api_url="https://api.aoikujira.com/tenki/week.php?fmt=ini&city=319"
tenki=requests.get(api_url).text

#デスクトップに保存
with open(save_file,"wt",encoding="utf-8") as f:
    f.write(tenki)