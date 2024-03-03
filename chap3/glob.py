import glob

#同じフォルダ内の全てのエクセルファイルを取得 *はワイルドカードで全てのファイルを取得
files=glob.glob("chap2\*")
print(files)