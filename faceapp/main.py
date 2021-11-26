import streamlit as st
import requests
from PIL import Image
from PIL import ImageDraw

SUBSCRIPTION_KEY = ''
assert  SUBSCRIPTION_KEY
face_api_url = 'https://~.azure.com/face/v1.0/detect'

st.title('顔認証アプリ')

uploaded_file = st.file_uploader("Choose an image...", type='jpg')

if uploaded_file is not None:
  img = Image.open(uploaded_file)
  st.image(img, caption='Upload Image.', use_column_width=True)

with open('サンプル.jpg', 'rb') as f:
  binary_img = f.read()

import io
with io.BytesI0() as output:
  img.save(output, format="JPEG")
  binary_img = output.getvalue() 

headers = {
  'Content-Type': 'application/octet-stream',
  '0cp-Apim-Subscription-Key': SUBSCRIPTION_KEY
}

params = {
  'returnFaceId': 'true',
  'returnFaceAttributes': 'age, blur, emotion, exposure, facialhair, gender, glasses, hair, headpose, makeup, noise, occlusion, smile'
}
response = requests.post(face_api_url, params=params,
headers=headers, data=binary_img)

results = response.json

# 画像の人数分をforループで回す
for result in results:
  rect = result[0]['faceRectangle'] 
  draw = ImageDraw(img)
  draw.rectangle [(rect ['left'], rect['top']), (rect['left']+rect ['width'], rect['top']+rect ['height'])], fill=None, outline='green', width=5