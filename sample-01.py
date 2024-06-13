import openai

openai.api_key = '781cc10b4c4141c58a4059d1780b5d29'
openai.azure_endpoint = 'https://helloaiopenai-01.openai.azure.com/'  
openai.api_type = 'azure'
openai.api_version = '2023-05-15'

query = input('궁금한 것을 물어보세요!')

result = openai.chat.completions.create(
  model = 'dev-gpt-35-turbo-01',
  temperature=1, # 1로 설정해주면 좀 더 창의적으로 답해준다.
  messages = [
    { 'role' : 'system', 'content': 'You are a helpful assistant!' },
    { 'role' : 'user', 'content': query + '가 뭐야?' }
  ]
)

message = result.choices[0].message.content

print(message)