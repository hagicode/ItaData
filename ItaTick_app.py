import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import numpy as np
import glob
import pathlib
import os

#@st.cache_data
#def load_dataframe(f_):
#    df = pd.read_parquet(f_)
#    return df

#github
st.set_page_config(layout="wide")

l2 = sorted(glob.glob('files/*.parquet', recursive=True))
st.write(l2)
# code = st.text_input("銘柄コード","1301")
# l_in = [s for s in l2 if code in s][0]

# p = pathlib.Path(l_in)
# df = pd.read_parquet(p)
# st.dataframe

#update_date = os.path.split(p)[1].replace("_df_dayIta_all.parquet","")
#st.write("データ更新日：" + update_date)
#st.write(p)
#df = pd.read_parquet("files/" + "240522_df_day.parquet")
# df = pd.read_parquet(p)
# #df_Ita = df.loc["1301"].loc["2024-05-22 09:50:00"]

# col1,col2,col3,col4,col5,col6 = st.columns(6)
# col1.dataframe(df.loc["2024-05-22 09:00:00"])
# col2.dataframe(df.loc["2024-05-22 09:05:00"])
# col3.dataframe(df.loc["2024-05-22 09:10:00"])
# col4.dataframe(df.loc["2024-05-22 09:15:00"])
# col5.dataframe(df.loc["2024-05-22 09:20:00"])
# col6.dataframe(df.loc["2024-05-22 09:25:00"])

