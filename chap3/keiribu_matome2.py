import openpyxl,json #jsonファイルならpythonの辞書型・リスト型のデータもファイルに保存できる

#入出力ファイルを指定
input_file="chap3/excell_file/keiribu_matome(1).xlsx"
output_file="chap3/excell_file/keiribu_matome(2).json"

#メイン処理
def split_users():
    users=read_and_split(input_file)
    #データを顧客名で辞書型に分割
    result={}
    for name,value in users.items():
        result[name]=calc_user(value)
        print(name,result[name]["total"])
    #ファイルに保存
    with open(output_file,"wt") as f:#wtは書き込みモード
        json.dump(result,f)#dumpでファイルに書き込む

#入力ファイルを読み込んで顧客ごとに分割
def read_and_split(input_file):
    users={} #辞書型の変数を初期化
    sheet=openpyxl.load_workbook(input_file,data_only=True).active
    for row in sheet.iter_rows():
        values = [col.value for col in row]
        name = values[1] # ２列目の顧客名を取り出す
        if not name in users:
            users[name]=[]
        users[name].append(values)
    return users

#顧客一人分のデータを集計する
def calc_user(value):
    total=0
    items=[]
    #集計処理
    for row in value:
        date,_,item,count,price,_=row
        print(date)
        date_s=date.strftime('%yyyy%m/%d')
        items.append([date_s,item,count,price])
        total=total+count*price
    return {'items':items,'total':total}

if __name__=="__main__":
    split_users() #メイン処理を実行    