import csv
import json
import os

def read_csv(file_path):
    """
    CSVファイルを読み取り、その内容を辞書のリストで返す

    :引数 file_path: 文字列 - CSVファイルへのパス
    :戻り値: リスト - CSVの列を表す辞書のリスト
    """
    with open(file_path, 'r') as f:
        csv_reader = csv.DictReader(f)
        csv_data = list(csv_reader)
    return csv_data


def csv_to_json(csv_data):
    """
    CSVデータ (辞書のリスト) を受け取り、それをJSON形式 (文字列) に変換する

    :引数 csv_data: リスト - 辞書のリストで表したCSVデータ
    :戻り値: 文字列 - JSON形式で表したデータ
    """
    return json.dumps(csv_data, sort_keys=True, indent=4)

def write_json(json_data, file_path):
    """
    JSONデータをファイルに書き込む

    :param json_data: 文字列 - 書き込むJSONデータ
    :param file_path: 文字列 - JSONファイルへのパス
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_data)

def read_json(file_path):
    """
    JSONファイルを読み取ってその内容を返す

    :引数 file_path: 文字列 - JSONファイルへのパス
    :戻り値: JSONファイルの内容
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def json_to_csv(json_data):
    """
    JSONデータを受け取り (通常は辞書のリスト)、それをCSV形式 (文字列) に変換する

    :引数 json_data: JSONデータ
    :戻り値: 文字列 - CSV形式で表したデータ
    """
    csv_data = ""
    for i , value in enumerate(json_data):
        if i == 0:
            csv_data += (",".join(value.keys()) + "\n")
        csv_data += (",".join([str(item) for item in value.values()]) + "\n")

    return csv_data

def write_csv(csv_data, file_path):
    """
    CSVデータをファイルに書き込む

    :引数 csv_data: 文字列 - 書き込むCSVデータ
    :引数 file_path: 文字列 - CSVファイルへのパス
    """
    # ここに実装してください
    with open(file_path, 'w', newline='') as f:
        f.write(csv_data)

def validate_data(data, data_type):
    """
    データの整合性を確認する (例: CSVの列数に一貫性があること)

    :引数 data: 検証対象のデータ
    :引数 data_type: 文字列 - データ型 ('CSV' または 'JSON')
    :戻り値: bool - データが有効な場合はTrue、無効な場合はFalse
    """
    if data_type == "CSV":
        for i, row in enumerate(data):
            if i == 0:
                keys = row.keys()
            else:
                if keys != row.keys():
                    return False
        return True
    
    elif data_type == "JSON":
        for i, row in enumerate(data):
            if i == 0:
                keys = row.keys()
            else:
                if keys != row.keys():
                    return False
        return True

    else:
        print("data_type is wrong")    

def process_directory(directory_path):
    """
    指定されたディレクトリにあるすべてのCSVまたはJSONファイルを確認し、適切に変換する

    :引数 directory_path: 文字列 - 処理対象のディレクトリへのパス
    """
    files = os.listdir(directory_path)
    csv_files = [i for i in files if i[-4:] == ".csv"]
    json_files = [i for i in files if i[-5:] == ".json"]

    for csv_file in csv_files:
        csv_data = read_csv(directory_path + csv_file)
        json_data = csv_to_json(csv_data)
        write_json(json_data, directory_path + csv_file[:-4] + "_converted.json")
    
    for json_file in json_files:
        json_data = read_json(directory_path + json_file)
        csv_data = json_to_csv(json_data)
        write_csv(csv_data, directory_path + json_file[:-5] + "_converted.csv")

# スクリプトを実行するmain関数
def main():
    # 使用例
    try:
        directory = "path_to_directory"
        process_directory(directory)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()