import streamlit as st
import numpy as np 
import pandas as pd
import re
import requests
import datetime 
import csv

# CSVファイルの読み込み
winner_list = pd.read_csv("winner_list.csv", index_col=0)

# 更新日表示
last = winner_list.iloc[0]["日付"]
st.write('レイティング　入賞者の検索')
st.write('注意）羽曳野レイティングのみで、かつ54回（2015年）以降')
st.write('   最終更新日：', last)

# 検索条件入力
name = st.text_input("苗字入力")
name2 = st.text_input("名前入力")
team = st.text_input("チーム名入力")

# 検索ボタン
if st.button('検索'):
    if not name and not name2 and not team:
        st.error("少なくとも1つ以上の検索条件を入力してください。")
    else:
        # 条件に合致するデータを抽出
        result = winner_list[
            winner_list['名前'].str.contains(name, na=False) &
            winner_list['名前'].str.contains(name2, na=False) &
            winner_list['チーム名'].str.contains(team, na=False)
        ]

        total = len(result)

        # クラス・部・順位ごとの集計
        def count_result(group, part, rank):
            return result[
                (result['クラス'].str.contains(group, na=False, flags=re.IGNORECASE)) &
                (result['部'] == part) &
                (result['位'] == rank)
            ]

        a_1_1 = count_result('A', 1, 1)
        a_1_2 = count_result('A', 1, 2)
        a_1_3 = count_result('A', 1, 3)
        a_2_1 = count_result('A', 2, 1)
        a_2_2 = count_result('A', 2, 2)
        a_2_3 = count_result('A', 2, 3)

        b_1_1 = count_result('B', 1, 1)
        b_1_2 = count_result('B', 1, 2)
        b_1_3 = count_result('B', 1, 3)
        b_2_1 = count_result('B', 2, 1)
        b_2_2 = count_result('B', 2, 2)
        b_2_3 = count_result('B', 2, 3)

        c_1_1 = count_result('C', 1, 1)
        c_1_2 = count_result('C', 1, 2)
        c_1_3 = count_result('C', 1, 3)
        c_2_1 = count_result('C', 2, 1)
        c_2_2 = count_result('C', 2, 2)
        c_2_3 = count_result('C', 2, 3)

        d_1_1 = count_result('D', 1, 1)
        d_1_2 = count_result('D', 1, 2)
        d_1_3 = count_result('D', 1, 3)
        d_2_1 = count_result('D', 2, 1)
        d_2_2 = count_result('D', 2, 2)
        d_2_3 = count_result('D', 2, 3)

        # 集計結果をデータフレームにまとめる
        data = {
            'クラス': ['Aグループ', 'Bグループ', 'Cグループ', 'Dグループ'],
            '1部優勝': [len(a_1_1), len(b_1_1), len(c_1_1), len(d_1_1)],
            '1部準優勝': [len(a_1_2), len(b_1_2), len(c_1_2), len(d_1_2)],
            '1部3位': [len(a_1_3), len(b_1_3), len(c_1_3), len(d_1_3)],
            '2部優勝': [len(a_2_1), len(b_2_1), len(c_2_1), len(d_2_1)],
            '2部準優勝': [len(a_2_2), len(b_2_2), len(c_2_2), len(d_2_2)],
            '2部3位': [len(a_2_3), len(b_2_3), len(c_2_3), len(d_2_3)]
        }

        kekka = pd.DataFrame(data)

        # 結果表示
        st.write('総表彰回数', total)
        st.table(kekka)
        st.write('詳細表示')
        st.table(result)

