import csv
import os

# 入出力フォルダの指定
input_dir = 'removeCsvHeader'
output_dir = 'headerRemoved'

# 出力フォルダを作成（既にある場合は無視）
os.makedirs(output_dir, exist_ok=True)

# 入力フォルダ内のファイルを処理
for csv_filename in os.listdir(input_dir):
    if not csv_filename.endswith('.csv'):
        continue

    print(f'Removing header from {csv_filename}...')

    input_path = os.path.join(input_dir, csv_filename)
    output_path = os.path.join(output_dir, csv_filename)

    # ファイルを読み込み、1行目（ヘッダー）を飛ばす
    with open(input_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        next(reader, None)  # ヘッダー行をスキップ
        rows = list(reader)

    # ヘッダーを除いた内容を新しいファイルに書き込み
    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

