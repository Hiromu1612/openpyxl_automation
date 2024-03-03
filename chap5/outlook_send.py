import smtplib #smtplibはメール送信を行う
from email.mime.text import MIMEText #MIMETextはテキストメールを作成する MIMEは標準の電子メールデータの規格、英数字以外の文字や添付ファイルを扱うための規格

#Outlookの設定
account="hiromu1612@outlook.jp"
password="A49DR-J9QS9-NH5NU-9K54J-D8WCR"

#メイン処理
def send_test_outlook():
    message=make_mime_message(
        mail_to=account,
        subject="メールの送信テスト",
        body="Pythonからメールを送信しています"
    )
    send_outlook(message)

#メールデータ(MINEText)を作成
def make_mime_message(mail_to,subject,body):
    message=MIMEText(body,"plain") #本文 html形式  plainはテキスト形式
    message["Subject"]=subject #件名
    message["To"]=mail_to #宛先
    message["From"]=account #送信元
    return message

#Outlookのサーバーに接続
def send_outlook(message):
    server=smtplib.SMTP("smtp.office365.com",587) #SMTPサーバーに接続 465はポート番号 contextは暗号化通信を行う
    server.ehlo() #SMTPサーバーに挨拶
    server.starttls() #TLS暗号化通信を開始
    server.ehlo() #SMTPサーバーに挨拶
    server.login(account,password) #ログイン
    server.send_message(message) #メールを送信

if __name__=="__main__":
    send_test_outlook() #メイン処理を実行
    print("メールを送信しました")