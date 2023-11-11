#GET SITELIST V 1 .0!!!
# -*- coding: utf-8 -*
#!/usr/bin/python
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
#Created Date = January - 15 - 2k21
# Updated Date = January - 12 - 2k22
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
############# [ Module ] #############
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import json				   		
import getpass
from socket import gethostbyname
from base64 import b64decode
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
############# [ Color ] #############
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
############# [ Banner ] #############
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
          \033[31m\   \033[31m/
   \033[34m----- (9\033[31m"-_-\033[34m)9  \033[37mVs  \033[34m6(\033[31mx_x"\033[34m6) -----
   
   \033[32m>--------------------------------<
   - Jamet Crew aka KNTL Megalodon - 
      - GET SITELIST V 1 .0 !!! - Jenderal92 -
   
   
   \033[41m\033[1;33m[Blog : https://www.blog-gan.org\033[0m
   \033[41m\033[1;33m[ICQ : https://icq.im/Shin403\033[0m
   \033[32m>----------------------------------<
   [-] 1. GET domain by azstats.org
   [-] 2. GET domain by pagesinventory.com
   [-] 3. GET domain by worldsitelink.com
   [-] 4. GET domain by themesinfo.com
   [-] 5. GET domain by topmillion.net
   [-] 6. GET domain by dubdomain.com
   [-] 7. GET domain by uidomains.com
   [-] 8. GET domain by greensiteinfo.com
   [-] 9. GET domain by websitebiography.com
   [-] 10. UPDATED !!!

   \033[32m>---------------------------------<  
   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

pilihmas = raw_input(':~# \033[34mChoose\033[32m Number : ')

########JANCOKSURAIMU####
def sitenlist1():
	try:
		DOMAIN = raw_input('DOMAIN Ex : com@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(1, 100):
			urle = "https://azstats.org/top/domain-zone/"+DOMAIN+"/"+str(page)
			cook = requests.get(urle, headers=headers, timeout=15).content
			if "Domain" in cook:
				asus = re.findall('style="margin-left: 0;">(.*?)</a>',cook)
				for xx in asus:
					print('Result : '+ ijo + xx)
					open('domain.txt','a').write(xx+'\n')
				else:
					print(abang + 'Sabar Su ')
			else:
				print(abang + 'DONE')
	except:
		pass
	pass	

def sitenlist2():
	try:
		DOMAIN = raw_input('DOMAIN Ex : com@ ~#: ')
		TOOD = raw_input('PUT A-Z ex : a@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		cook = requests.get("https://www.pagesinventory.com/tld/"+DOMAIN +"/"+TOOD+".html", headers=headers, timeout=15).text
		if 'domain' in cook:
			print(cook)
			asus = re.findall('<td><a href="\\/domain\\/(.*?).html">', cook)
			for x in asus:
				print(str(x)+ ijo + '[!] LAGI GRAB SLUR . . .')
				open('domain.txt', 'a').write('http://'+x+'\n')
	except:
		pass
	pass	

def sitenlist3():
	try:
		DOMAIN = raw_input('EXAMPLE .org/.com@ ~#: ')
		PAGEAWAL = raw_input('Frist Page@ ~#: ')
		PAGEAKHIR = raw_input('Last Page@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			urle = "https://bestwebsiterank.com/domains/."+DOMAIN+"/"+str(page)
			cook = requests.get(urle, headers=headers, timeout=15).content
			if "Domain" in cook:
				asus = re.findall('<a href="https://bestwebsiterank.com/(.*?)/"><img src="',cook)
				for xx in asus:
					kimak = xx.replace("https://bestwebsiterank.com/","")
					print('Result : '+ ijo + kimak)
					open('domain.txt','a').write('http://'+kimak+'\n')
				else:
					print(abang + 'Sabar Su ')
			else:
				print(abang + 'DONE')
	except:
		pass
	pass	


def sitenlist5():
	try:
		TOOD = raw_input('Theme Name@ ~#: ')
		PAGEAWAL = raw_input('Frist Page@ ~#: ')
		PAGEAKHIR = raw_input('Last Page@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			urle = 'https://themesinfo.com/'+TOOD+'/'+str(page)+'/'
			cook = requests.get(urle, headers=headers, timeout=15).content
			asus = re.findall('<h2 class="theme_web_h2">(.*?)</h2>', cook)
			for xx in asus:
				print(str(xx) + ijo + '[!] LAGI GRAB SLUR . . .')
				kimak = xx.replace("https://themesinfo.com","")
				open('domain.txt', 'a').write('http://'+kimak+'\n')
			else:
				print(abang + 'Sabar Su ')
		else:
			print(abang + 'DONE')
	except:
		pass
	pass	

def sitenlist7():
	try:
		AWAL = raw_input('Frist Page@ ~#: ')
		AKHIR = raw_input('Last Page@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(int(AWAL), int(AKHIR)):
			urle = "https://www.topmillion.net/pages/websites/page/"+str(page)+"/"
			cook = requests.get(urle, headers=headers, timeout=15).content
			if "All websites" in cook:
				asus = re.findall('https://(.*?)?w=400" alt="Thumbnail" />',cook)
				for xx in asus:
					cot = xx.replace('?','')
					print(kuning + '[Geting website list --> ]' + ijo + cot)
					open("domain.txt","a").write("http://"+cot+"\n")
				else:
					print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass
	pass	
	

def sitenlist11():
	try:
		PAGEAWAL = raw_input('Frist Page@ ~#: ')
		PAGEAKHIR = raw_input('Last Page@ ~#: ')
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			coks = requests.get("https://www.dubdomain.com/index.php?page="+str(page), headers=headers, timeout=15).text
			if 'Recently Analyzed' in coks:
				asus = re.findall('data-src="(.*?)"',coks)
				for xx in asus:
					AC = xx.replace('https://www.google.com/s2/favicons?domain_url=', '')
					print(kuning + '[Geting website list --> ]' + ijo + AC)
					open("domain.txt","a").write("http://"+AC+"\n")
				else:
					print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass

def sitenlist12():
	try:
		TBNH = raw_input(' Ex : 2023-11-09 : ' )
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		coks = requests.get("https://www.uidomains.com/browse-daily-domains-difference/0/"+TBNH, headers=headers, timeout=15).text
		if 'Domains' in coks:
			asus = re.findall('<li>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</li>',coks)
			for xx in asus:
				cot = xx.replace('<li>','').replace('</li>','')
				print(kuning + '[Geting website list --> ]' + ijo + cot)
				open("domain.txt","a").write("http://"+cot+"\n")
			else:
				print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass

def sitenlist13():
	try:
		DOMAIN = raw_input('EXAMPLE org/com@ ~#: ')
		PAGEAWAL = raw_input('Frist Page@ ~#: ')
		PAGEAKHIR = raw_input('Last Page@ ~#: ')
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			coks = requests.get("https://www.greensiteinfo.com/domains/."+DOMAIN+"/"+str(page)+"/", headers=headers, timeout=15).text
			if 'Domain' in coks:
				asus = re.findall('<a href = https://www.greensiteinfo.com/search/(.*?)/ >',coks)
				for xx in asus:
					print(kuning + '[Geting website list --> ]' + ijo + xx)
					open("domain.txt","a").write("http://"+xx+"\n")
				else:
					print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass

def sitenlist14():
	try:
		TNBNHR = raw_input('Ex : 2023-06-19 @ ~#: ')
		PAGEAWAL = raw_input('Frist Page@ ~#: ')
		PAGEAKHIR = raw_input('Last Page@ ~#: ')
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			coks = requests.get("https://websitebiography.com/new_domain_registrations/"+TNBNHR+"/"+str(page)+"/", headers=headers, timeout=15).text
			asus = re.findall("<a href='https://(.*?).websitebiography.com' title='More",coks)
			for xx in asus:
				print(kuning + '[Geting website list --> ]' + ijo + xx)
				open("domain.txt","a").write("http://"+xx+"\n")
			else:
				print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass

######MENGONTOL#####
def Main():
	try:
		if pilihmas =='1':
			sitenlist1()
		if pilihmas =='2':
			sitenlist2()
		if pilihmas =='3':
			sitenlist3()
		if pilihmas =='4':
			sitenlist5()
		if pilihmas =='5':
			sitenlist7()
		if pilihmas =='6':
			sitenlist11()
		if pilihmas =='7':
			sitenlist12()
		if pilihmas =='8':
			sitenlist13()
		if pilihmas =='9':
			sitenlist14()
		if pilihmas =='10':
			print(ijo + '\nCooming Soon !!!\n' + putih)
		
	except:
		pass

if __name__ == '__main__':
	Main()
