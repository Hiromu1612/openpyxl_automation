import smtplib,ssl #smtplibはメール送信を行う sslは暗号化通信を行う
from email.mime.text import MIMEText #MIMETextはテキストメールを作成する MIMEは標準の電子メールデータの規格、英数字以外の文字や添付ファイルを扱うための規格

#Gmailの設定
account="1612hiromu@gmail.com"
password="rejt nkbj veki zmhd" #アプリパスワード 2段階認証を有効にしている場合は必要



#メイン処理
def send_test_gmail():
    message=make_mime_message(
        mail_to=account,
        subject="メールの送信テスト",
        body="Pythonからメールを送信しています"
    )
    send_gmail(message)

#メールデータ(MINEText)を作成
def  make_mime_message(mail_to,subject,body):
    message=MIMEText(body,"html") #本文 html形式  plainはテキスト形式
    message["Subject"]=subject #件名
    message["To"]=mail_to #宛先
    message["From"]=account #送信元
    return message

#Gmailに接続
def send_gmail(message):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl.create_default_context()) #SMTPサーバーに接続 465はポート番号 contextは暗号化通信を行う
    server.set_debuglevel(0) #デバッグ情報を出力 0は出力しない 1は出力する
    server.login(account,password) #ログイン
    server.send_message(message) #メールを送信

if __name__=="__main__":
    send_test_gmail() #メイン処理を実行
    print("メールを送信しました")