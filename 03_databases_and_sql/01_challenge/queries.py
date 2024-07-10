
# SQLとPython＋Chinookデータベース

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# アーティストの数
def number_of_artists(db):
    query = "SELECT count(*) FROM artists;"
    db.execute(query)
    results = db.fetchall()
    return results[0][0]

# アーティストのリスト
def list_of_artists(db):
    query = "SELECT Name FROM artists;"
    db.execute(query)
    results = db.fetchall()
    results = [artist[0] for artist in results]
    return results

# 「愛」をテーマにしたアルバムのリスト
def albums_about_love(db):
    query = "SELECT Title FROM albums WHERE Title LIKE '%love%' ORDER BY Title;"
    db.execute(query)
    results = db.fetchall()
    results = [artist[0] for artist in results]
    return results

# 指定された再生時間よりも長い楽曲数
def tracks_longer_than(db, duration):
    query = f"SELECT count(TrackID) FROM tracks WHERE Milliseconds > {duration};"
    db.execute(query)
    results = db.fetchall()
    return results[0][0]

# 最も楽曲数が多いジャンルのリスト
def genres_with_most_tracks(db):
    query = """
        SELECT genres.Name, count(Title) as TitleCount
        FROM tracks
        join genres on tracks.GenreId == genres.GenreId
        join albums on tracks.AlbumId == albums.AlbumId
        GROUP BY genres.Name
        ORDER BY TitleCount DESC;
    """
    db.execute(query)
    results = db.fetchall()
    return results

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()
