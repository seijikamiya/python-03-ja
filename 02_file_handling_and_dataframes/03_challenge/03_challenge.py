# 必要なライブラリをインポートする
import pandas as pd
from sklearn import datasets

# アイリスのデータセットを読み込み、DataFrameに変換する
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 品種の列を追加し、0～2の番号を記入する (各番号が異なる品種を表す)
iris_df['species'] = iris.target

print("##########データフレーム概要##########")
print(iris_df.head(5))

# データのクリーニングと検証
print("##########欠損値またはnull値の確認##########")
print(iris_df.isna().sum())

print("##########各列のデータ型の確認##########")
print(iris_df.dtypes)

# 基本的な分析と基本統計量
describe_df = iris_df.describe()
# 数値型の各特徴量について、基本統計量 (平均値、中央値、標準偏差) を計算します。
print("##########基本統計量 (平均値、中央値、標準偏差) の計算##########")
print(describe_df)

# DataFrameを新規作成します。各行が1つの特徴量を表し、各列に計算した統計情報を格納するようにします。これをCSV形式で出力します。
describe_df.to_csv("./iris_describe.csv")

# 特徴量エンジニアリング
# 新しい列 sepal_area (ガクの面積) を追加します。この値は、ガクの長さ×ガクの幅で算出します。
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']

# 別の列 petal_area (花弁の面積) も追加します。この値は、花弁の長さ×花弁の幅で算出します。
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# これらの新しい特徴量の基本統計量を算出し、統計情報のDataFrameに追加します。
describe_df = iris_df.describe()
print("##########新しい特徴量の基本統計量##########")
print(describe_df)

# データのフィルタリング
# 与えられた基準にもとづいてデータをフィルタリングする関数を書きます (例: ある列の値がしきい値を下回る行を除外する)。
def filter_sepal_length(df, threshold):
    return df[df['sepal_length'] > threshold]

# データのエクスポート
iris_df.to_csv("./iris_df.csv")