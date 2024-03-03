#ダミーデータ
dummy_data = [
    ["伊藤",300],
    ["伊藤",600],
    ["伊藤",200],
    ["田中",300],
    ["田中",200]
]

# dummy_data={"伊藤":300,"伊藤":600,"伊藤":200,"田中":300,"田中":200}

#データを顧客名で辞書型に分割
users={}
for row in dummy_data:
    name,value=row #変数に分ける
    #顧客名が初めてなら新しいリストを作成
    if not name in users:
        users[name]=[]
    users[name].append(row)#nameをキーにしてリストに追加

#顧客ごとに集計
for name,value in users.items(): #items()でキーと値を取得
    print(value)#集計対象データを表示
    total=0
    for row in value:
        total=total+row[1]
    print(name+"さんの合計:"+str(total))

#合計を計算するだけなら簡単
total={"伊藤":0,"田中":0}
for name,value in dummy_data:
    total[name]=total[name]+value
print(total)