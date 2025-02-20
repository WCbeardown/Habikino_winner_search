import streamlit as st
import numpy as np 
import pandas as pd
import re
import requests
import datetime 
import csv

#csvファイルの読み込み方を忘れないように　Pandasのデータフレームで読み込まれます
winner_list = pd.read_csv("winner_list.csv", index_col=0)

#更新日
last = winner_list.iloc[0]["日付"]

st.write('レイティング　入賞者の検索')
st.write('注意）羽曳野レイティングのみで、かつ54回（2015年）以降')
st.write('   最終更新日：',last)
#検索条件入力
name = st.text_input("苗字入力")
name2 = st.text_input("名前入力")
team = st.text_input("チーム名入力")

# 検索ボタン
#if st.button('検索'):
#    timestamp = str(datetime.datetime.now())  # 現在のタイムスタンプを取得
#    try:
#        with open('input.csv', mode='a', newline='') as file:
#            writer = csv.writer(file)
#            writer.writerow([timestamp, name, name2, team])
#    except Exception as e:
#        st.error(f"ファイルへの書き込み中にエラーが発生しました: {e}")

#検索結果
#result = winner_list[winner_list['名前'].str.contains(name)]
result = winner_list[winner_list['名前'].str.contains(name, na=False)]

#result = winner_list[winner_list['名前'].str.contains(name) & winner_list['名前'].str.contains(name2) & winner_list['チーム名'].str.contains(team)]
result = winner_list[winner_list['名前'].str.contains(name, na=False) & 
                     winner_list['名前'].str.contains(name2, na=False) & 
                     winner_list['チーム名'].str.contains(team, na=False)]


total = len(result)
a_1_1 = result[(result['クラス'].str.contains('A')) & (result['部'] == 1) & (result['位'] == 1)]
a_1_2 = result[(result['クラス'].str.contains('A')) & (result['部'] == 1) & (result['位'] == 2)]
a_1_3 = result[(result['クラス'].str.contains('A')) & (result['部'] == 1) & (result['位'] == 3)]
a_2_1 = result[(result['クラス'].str.contains('A')) & (result['部'] == 2) & (result['位'] == 1)]
a_2_2 = result[(result['クラス'].str.contains('A')) & (result['部'] == 2) & (result['位'] == 2)]
a_2_3 = result[(result['クラス'].str.contains('A')) & (result['部'] == 2) & (result['位'] == 3)]
b_1_1 = result[(result['クラス'].str.contains('B')) & (result['部'] == 1) & (result['位'] == 1)]
b_1_2 = result[(result['クラス'].str.contains('B')) & (result['部'] == 1) & (result['位'] == 2)]
b_1_3 = result[(result['クラス'].str.contains('B')) & (result['部'] == 1) & (result['位'] == 3)]
b_2_1 = result[(result['クラス'].str.contains('B')) & (result['部'] == 2) & (result['位'] == 1)]
b_2_2 = result[(result['クラス'].str.contains('B')) & (result['部'] == 2) & (result['位'] == 2)]
b_2_3 = result[(result['クラス'].str.contains('B')) & (result['部'] == 2) & (result['位'] == 3)]
c_1_1 = result[(result['クラス'].str.contains('C')) & (result['部'] == 1) & (result['位'] == 1)]
c_1_2 = result[(result['クラス'].str.contains('C')) & (result['部'] == 1) & (result['位'] == 2)]
c_1_3 = result[(result['クラス'].str.contains('C')) & (result['部'] == 1) & (result['位'] == 3)]
c_2_1 = result[(result['クラス'].str.contains('C')) & (result['部'] == 2) & (result['位'] == 1)]
c_2_2 = result[(result['クラス'].str.contains('C')) & (result['部'] == 2) & (result['位'] == 2)]
c_2_3 = result[(result['クラス'].str.contains('C')) & (result['部'] == 2) & (result['位'] == 3)]
d_1_1 = result[(result['クラス'].str.contains(re.compile('d', re.IGNORECASE))) & (result['部'] == 1) & (result['位'] == 1)]
d_1_2 = result[(result['クラス'].str.contains(re.compile('d', re.IGNORECASE))) & (result['部'] == 1) & (result['位'] == 2)]
d_1_3 = result[(result['クラス'].str.contains(re.compile('d', re.IGNORECASE))) & (result['部'] == 1) & (result['位'] == 3)]
d_2_1 = result[(result['クラス'].str.contains(re.compile('d', re.IGNORECASE))) & (result['部'] == 2) & (result['位'] == 1)]
d_2_2 = result[(result['クラス'].str.contains(re.compile('d', re.IGNORECASE))) & (result['部'] == 2) & (result['位'] == 2)]
d_2_3 = result[(result['クラス'].str.contains(re.compile('d', re.IGNORECASE))) & (result['部'] == 2) & (result['位'] == 3)]


# 表示したいデータを定義する
data = {'クラス': ['1部優勝', '1部準優勝', '1部3位', '2部優勝', '2部準優勝', '2部3位'],
        'Aグループ': [len(a_1_1), len(a_1_2), len(a_1_3), len(a_2_1), len(a_2_2), len(a_2_3)],
        'Bグループ': [len(b_1_1), len(b_1_2), len(b_1_3), len(b_2_1), len(b_2_2), len(b_2_3)],
        'Cグループ': [len(c_1_1), len(c_1_2), len(c_1_3), len(c_2_1), len(c_2_2), len(c_2_3)],
        'Dグループ': [len(d_1_1), len(d_1_2), len(d_1_3), len(d_2_1), len(d_2_2), len(d_2_3)]}

data = {'クラス': ['Aグループ', 'Bグループ', 'Cグループ', 'Dグループ'],
        '1部優勝': [len(a_1_1), len(b_1_1), len(c_1_1), len(d_1_1)],
        '1部準優勝': [len(a_1_2), len(b_1_2), len(c_1_2), len(d_1_2)],
        '1部3位': [len(a_1_3), len(b_1_3), len(c_1_3), len(d_1_3)],
        '2部優勝': [len(a_2_1), len(b_2_1), len(c_2_1), len(d_2_1)],
        '2部準優勝': [len(a_2_2), len(b_2_2), len(c_2_2), len(d_2_2)],
        '2部3位': [len(a_2_3), len(b_2_3), len(c_2_3), len(d_2_3)]}    
# データフレームを作成する　
kekka = pd.DataFrame(data)


# 結果表示　
st.write('総表彰回数',total)
st.table(kekka)
st.write('詳細表示')
st.table(result)
