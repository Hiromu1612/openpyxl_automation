import requests
import time
def send_line():
    url = "https://notify-api.line.me/api/notify"
    token = "wObGfATYZIPGdlMtsQhRNXYjH93IZcXzdkej1ARVUUp"
    headers = {"Authorization": "Bearer " + token}
    message = "Pythonからメッセージを送信しています"
    payload = {"message": message}

    while True:
        r = requests.post(url, headers=headers, params=payload)
        time.sleep(60)  # Sleep for 60 seconds (1 minute)

if __name__=="__main__":
    send_line() #メイン処理を実行
    print("メッセージを送信しました")