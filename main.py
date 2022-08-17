from select import select
import streamlit as st
import numpy as np
import pandas as pd
# from PIL import Image

st.title('これがタイトル')
# st.write('DataFrame')
# df = pd.DataFrame({
#   '1列目':[1,2,30,40],
#   '2列目':[40,30,2,1],
# })

# st.write(df)
# st.dataframe(df,width=100,height=100) # 引数が設定できる。
# st.dataframe(df.style.highlight_max(axis=0))
# st.dataframe(df.style.highlight_max(axis=1))
# st.table(df)

df99 = pd.DataFrame({
  'col1':['Tokyo','Tokyo','Aichi','Aichi','Tokyo','Tokyo','Aichi','Aichi','Tokyo','Tokyo','Aichi','Aichi','Tokyo','Tokyo','Aichi','Aichi','Tokyo','Tokyo','Aichi','Aichi','Tokyo','Tokyo','Aichi','Aichi'],
  'col2':['1<br>2','http://localhost','14','15','1<br>2','http://localhost','14','15','1<br>2','http://localhost','14','15','1<br>2','http://localhost','14','15','1<br>2','http://localhost','14','15','1<br>2','http://localhost','14','15'],
})

option = st.selectbox(
     'How would you like to be contacted?',
     ('Tokyo', 'Aichi'))

df98 = df99.query('col1 == @option')
st.write(df98.to_html(escape=False, index=False), unsafe_allow_html=True)
st.dataframe(df99) 
st.table(df99)



css = f"""
<style>
table {{
  border-collapse: collapse;
  width: 100%;
}}
th,
td {{
  padding: 1rem 2rem;
  text-align: center;
  border-bottom: 1px solid #ddd;
}}
th {{
  font-weight: normal;
  font-size: .875rem;
  color: #666;
  background: #eee;
  position: sticky;
  top: 0;
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# """
# # 1
# ## ｓ
# ```python
# aaa
# ```
# """

# df2 = pd.DataFrame(
#   np.random.rand(20,3),
#   columns=['a','b','c']
# )
# st.line_chart(df2)
# st.area_chart(df2)
# st.bar_chart(df2)


# locate_df = pd.DataFrame(
#   np.random.rand(100,2)/[50/50]+[34.956325, 137.1588248],
#   columns=['lat','lon']
# )

# st.map(locate_df)
# if st.checkbox('showimage'):
#   img = Image.open("sample.bmp")
#   st.image(img,caption="Discription",use_column_width=True)

# option= st.selectbox(
#   "inputnum",
#   options=list(range(1,1100))
# )

# '選択：',option,'です'

# text = st.text_input("what?")
# '選択：',text,'です'

# slider = st.slider("slider",0,100,50,step=10)

# '選択：',slider,'です'

# slider2 = st.sidebar.slider("slider",0,100,50) # サイドバーにしている。サイドバーでは使えないオプションとかもありそう

# '選択：',slider2,'です'

# left_column,right_column=st.columns(2)
# button = left_column.button("右カラムに文字を表示")
# if button:
#   right_column.write("みぎだよ")

# expander1 = st.expander("Q1")
# expander1.write("A1")


# expander2 = st.expander("Q2")
# expander2.write("A2")

# import time
# 'Start!'
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#   latest_iteration.text(f"ループ{i}")
#   bar.progress(i+1)
#   time.sleep(0.1)

# 'Done!'
