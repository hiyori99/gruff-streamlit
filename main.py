import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# タイトルの追加
st.title('Streamlit 超入門')
# テキストの追加
st.write('DataFrame')

df = pd.DataFrame({
  '1列目': [1, 2, 3, 4],
  '2列目': [10, 20, 30, 40]
})

# 表の表示
st.write(df) #writeの方には引数がない
# 動的なテーブル
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200) 
# 静的なテーブル
st.table(df.style.highlight_max(axis=0)) 


# マジックコマンド
# マークダウンを適用できる
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


# チャートを描く
df1 = pd.DataFrame(
  np.random.rand(20, 3), # 正規分布で乱数を生成
  columns=['a', 'b', 'c']
)
# 折れ線グラフ
st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

# 地図にマッピングする
df2 = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], # 正規分布で乱数を生成
  columns=['lat', 'lon'] # 緯度と経度
)
st.map(df2)


st.write('Display Image')
if st.checkbox('Show Image'): # チェック入れたら表示する
  img = Image.open('icon.jpeg')
  st.image(img, caption='icon', use_column_width=True)

option = st.selectbox(
  'あなたが好きな数字を教えてください',
  list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'


st.write('Interactive Widgets')

# サイドバー
text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:', text
'コンディション:', condition

# 2カラム
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('回答')

st.write('プログレスバーの表示')
'Start!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range (100):
  latest_interation.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done!!!'
