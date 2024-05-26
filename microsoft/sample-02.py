import openai
import streamlit as st

openai.api_key = '781cc10b4c4141c58a4059d1780b5d29'
openai.azure_endpoint = 'https://helloaiopenai-01.openai.azure.com/'  
openai.api_type = 'azure'
openai.api_version = '2023-05-15'

st.header('Welcome to ChatBot', divider='rainbow')
st.write('안녕하세요! 인공지능 시인입니다:)')

# query = st.text_input('궁금한 내용을 입력하세요~')
subject = st.text_input('시의 주제를 입력해주세요.')
st.write('주제는' + subject)
content = st.text_area('시의 내용에 대해서 말씀해주세요.')
# text_area는 더 많은 줄의 내용을 적을 수 있다.

button_click = st.button('답변')

if(button_click):
  with st.spinner('loading...'):
    result = openai.chat.completions.create(
    model = 'dev-gpt-35-turbo-01',
    temperature=1, # 1로 설정해주면 좀 더 창의적으로 답해준다.
    messages = [
      # 원하는 내용을 계속 추가해주면 해당하는 내용을 엮어 답을 내준다.
      { 'role' : 'system', 'content': 'You are a helpful assistant!' },
      # { 'role' : 'user', 'content': query + '가 뭐야?' }
      { 'role' : 'user', 'content': '시의 주제는?' + subject },
      { 'role' : 'user', 'content': '시의 내용은?' + content },
      { 'role' : 'user', 'content': '이 내용으로 시를 지어줘' },
    ]
  )
  st.success('done!')
  st.write(result.choices[0].message.content)
