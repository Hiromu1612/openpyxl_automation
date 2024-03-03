import requests

image="chap5/sky.jpg"

def send_line(message,image):
    url = "https://notify-api.line.me/api/notify"
    token = "wObGfATYZIPGdlMtsQhRNXYjH93IZcXzdkej1ARVUUp"
    headers = {"Authorization": "Bearer " + token}
    payload={"message":message}
    
    #画像を読み込む
    with open(image,"rb") as f:
        files={"imageFile":f}
        #画像を送信
        r=requests.post(url,headers=headers,params=payload,files=files)

if __name__=="__main__":
    send_line("Pythonから画像を送信しています",image) #メイン処理を実行
    print("画像を送信しました")