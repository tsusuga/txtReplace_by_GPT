import csv

# CSVファイルのパス
csv_file_path = 'source.csv'

# 置換前文字列と置換後文字列の辞書を作成する
replace_dict = {}
with open(csv_file_path, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        replace_dict[row[0]] = row[1]

# テキストファイルのパス
print(replace_dict)
text_file_path = '_shopdata.ejs'

# テキストファイルを読み込む
with open(text_file_path, 'r', encoding="utf-8") as f:
    text = f.read()

# 置換を実行する
for key, value in replace_dict.items():
    text = text.replace(key, value)

with open(text_file_path, 'w', encoding="utf-8") as f:
  f.write(text)

# 結果を出力する
# print(text)