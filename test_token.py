import requests

Token = 'eabc41ba4cc25711f4ae49d5ae293ba92accb621'

headers = {
    'Authorization':f'Token {Token}',
}

body = {
    "message":"수정 수정",
}

res = requests.patch('http://localhost:8000/ukstagram/posts/33/', headers=headers, data=body)
print(res.json())