import requests

def send_line(message,package_id,sticker_id):
    url = "https://notify-api.line.me/api/notify"
    token = "wObGfATYZIPGdlMtsQhRNXYjH93IZcXzdkej1ARVUUp"
    headers = {"Authorization": "Bearer " + token}
    payload={"message":message,"stickerPackageId":package_id,"stickerId":sticker_id}
    r=requests.post(url,headers=headers,params=payload)

if __name__=="__main__":
    send_line("Pythonからスタンプを送信しています",6370,11088016) #メイン処理を実行 2,144はスタンプのID
    print("スタンプを送信しました")