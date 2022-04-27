import requests

TOKEN = 'eabc41ba4cc25711f4ae49d5ae293ba92accb621'
JWT_TOKEN = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
             ".eyJ1c2VybmFtZSI6ImNobHRqZGRucjk2IiwiaWF0IjoxNjUxMDUwMjY5LCJleHAiOjE2ODI1ODYyNjksImp0aSI"
             "6IjZkY2I0MWI1LTFmNWItNDNkZS1hMTQ3LTA1ZTMwYzk4MzBhNyIsInVzZXJfaWQiOjIsIm9yaWdfaWF0IjoxNjUxMDUwMjY5fQ"
             ".9thva3yacEBSlCiBkMayiI-X81y2mJo0dWDognfTvfo")

headers = {
    # 'Authorization':f'Token {TOKEN}',  # Token 인증
    'Authorization':f'Bearer {JWT_TOKEN}', # JWT 인증
}

body = {
    "message":"수정했습니다444.(JWT)",
}

res = requests.patch('http://localhost:8000/ukstagram/posts/33/', headers=headers, data=body)
print()
print(res.json())