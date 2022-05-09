#GET SITELIST V 1 .0!!!
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
##############################
#####################################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
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
##########################################################################################
##########################################################################################
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
#####################################
##########################################################################################

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
   [-] 4. GET domain by moonsearch.com
   [-] 5. GET domain by themesinfo.com
   [-] 6. GET domain by thesiterank.com
   [-] 7. GET domain by list.topmillion.net
   [-] 8. GET domain by dnpedia.com
   [-] 9. GET domain by siterankdata.com
   [-] 10. GET domain by site-stats.org
   [-] 11. GET domain by dubdomain.com
   [-] 12. GET domain by uidomains.com
   [-] 13. GET domain by greensiteinfo.com
   [-] 14. GET domain by websitebiography.com
   [-] 15. UPDATED !!!

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
		DOMAIN = raw_input('DOMAIN@ ~#: ')
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
		DOMAINS = raw_input('DOMAIN@ ~#: ')
		SUU = raw_input('PUT A-Z@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		urle = "https://www.pagesinventory.com/tld/"+DOMAINS +"/"+SUU+".html"
		cook = requests.get(urle, headers=headers, timeout=15).content
		if 'domain' in cook:
			regx = reg('<td><a href="\\/domain\\/(.*?).html">', cook)
			for x in regx:
				print(str(x)+ ijo + '[!] LAGI GRAB SLUR . . .')
				open('domain.txt', 'a').write('http://'+x+'\n')
	except:
		pass
	pass	

def sitenlist3():
	try:
		DOMAIN = raw_input('EXAMPLE .org/.com@ ~#: ')
		PAGEAWAL = raw_input('Page Awal@ ~#: ')
		PAGEAKHIR = raw_input('Page Akhir@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			urle = "https://worldsitelink.com/domains/"+DOMAIN+"/"+str(page)
			cook = requests.get(urle, headers=headers, timeout=15).content
			if "Domain" in cook:
				asus = re.findall('<a href = https://worldsitelink.com/(.*?)/>',cook)
				for xx in asus:
					kimak = xx.replace("https://worldsitelink.com/","")
					print('Result : '+ ijo + kimak)
					open('domain.txt','a').write('http://'+kimak+'\n')
				else:
					print(abang + 'Sabar Su ')
			else:
				print(abang + 'DONE')
	except:
		pass
	pass	

def sitenlist4():
	try:
		PAGEAWAL = raw_input('DOMAIN@ ~#: ')
		PAGEAKHIR = raw_input('DOMAIN@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			urle = "http://moonsearch.com/report/?sort=newest&page="+str(page)
			cook = requests.get(urle, headers=headers, timeout=15).content
			if "Domains" in cook:
				asus = re.findall('<a class="domain f16 in-block v-align-t" href="/report/(.*?)/>"',cook)
				for xx in asus:
					kimak = xx.replace("/report/","").replace(".html", "")
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
		PAGEAWAL = raw_input('DOMAIN@ ~#: ')
		PAGEAKHIR = raw_input('DOMAIN@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			urle = 'https://themesinfo.com/'+TOOD+'/'+str(page)
			cook = requests.get(urle, headers=headers, timeout=15).content
			if "Domains" in cook:
				asus = reg('<h2 class="theme_web_h2">(.*?)</h2>', cook)
				for xx in asus:
					print(str(xx) + ijo + '[!] LAGI GRAB SLUR . . .')
					for site in xx:
						kimak = site.replace("https://themesinfo.com","")
						open('domain.txt', 'a').write('http://'+kimak+'\n')
				else:
					print(abang + 'Sabar Su ')
			else:
				print(abang + 'DONE')
	except:
		pass
	pass	

def sitenlist6():
	try:
		TAHUN = raw_input('TAHUN@ ~#: ')
		BULAN = raw_input('BULAN@ ~#: ')
		TANGGAL = raw_input('TANGGAL@ ~#: ')
		MMK = raw_input('Page Awal@ ~#: ')
		MMKK = raw_input('Page Akhir@ ~#: ')
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(int(MMK), int(MMKK)):
			response = requests.get("https://www.thesiterank.com/newly-registered-domain-names-by-date/"+TAHUN+"-"+BULAN+"-"+TANGGAL+"/"+str(page), headers=headers, timeout=15).content
			asu = re.findall('<div class=col-md-4 style=height:27px><a href="(.*?)">',response)
			for AB in asu:
				AC = AB.replace('https://www.thesiterank.com/stats/?domain=', '')
				print(kuning + '[Geting website list --> ]' + ijo + AC)
				open("domain.txt","a").write("http://"+AC+"\n")
			else:
				print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass
	pass

def sitenlist7():
	try:
		AWAL = raw_input('Page Awal@ ~#: ')
		AKHIR = raw_input('Page Akhir@ ~#: ')
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
		for page in range(int(AWAL), int(AKHIR)):
			urle = "http://www.list.topmillion.net/domain-list-"+str(page)
			cook = requests.get(urle, headers=headers, timeout=15).content
			if "Website URL" in cook:
				asus = re.findall("target='_blank'>(.*?)</a>",cook)
				for xx in asus:
					print(kuning + '[Geting website list --> ]' + ijo + xx)
					open("domain.txt","a").write("http://"+xx+"\n")
				else:
					print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass
	pass	
	
def sitenlist8():
	try:
		TNBNHR = raw_input('TAHUN-BULAN-TANGGAL@ ~#: ')
		DOMAINE = raw_input('Domaine@ ~#: ')
		MEM = raw_input('Page Awal@ ~#: ')
		MEK = raw_input('Page Akhir@ ~#: ')
		headers = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'X-Requested-With': 'XMLHttpRequest',
		'Connection': 'keep-alive',
		'Referer': 'https://dnpedia.com/tlds/daily.php',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		}
		for page in range(int(MEM), int(MEK)):
			response = requests.get('https://dnpedia.com/tlds/ajax.php?cmd=added&columns=id,name,length,idn,thedate,&ecf=zoneid,thedate&ecv=843,'+TNBNHR+'&zone='+DOMAINE+'&_search=false&nd=1639786229000&rows=2000&page='+str(page)+'&sidx=length&sord=asc', headers=headers, timeout=15).content
			asu = re.findall('"name":"(.*?)"',response)
			for kontol in asu:
				print(kuning + '[Geting website list --> ]' + ijo + kontol)
				open("domain.txt","a").write("http://"+kontol+"\n")
			else:
				print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass
	pass

def sitenlist9():
	try:
		TNBNHR = raw_input('TAHUN-BULAN-TANGGAL@ ~#: ')
		PAGEAWAL = raw_input('Page Awal@ ~#: ')
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(PAGEAWAL), 99999):
			coks = requests.get("https://siterankdata.com/show/detected/"+TNBNHR+"/"+str(page)+"-99999", headers=headers, timeout=15).text
			if 'Detected' in coks:
				asus = re.findall('<h4 class="m-b-xs"><a href="(.*?)">',coks)
				for xx in asus:
					AC = xx.replace('/', '').replace('.blogspot.com', '')
					print(kuning + '[Geting website list --> ]' + ijo + AC)
					open("domain.txt","a").write("http://"+AC+"\n")
				else:
					print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass

def sitenlist10():
	try:
		DOMAIN = raw_input('EXAMPLE org/com@ ~#: ')
		PAGEAWAL = raw_input('Page Awal@ ~#: ')
		PAGEAKHIR = raw_input('Page Akhir@ ~#: ')
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			coks = requests.get("https://site-stats.org/domains/."+DOMAIN+"/"+str(page)+"/", headers=headers, timeout=15).text
			if 'Domain' in coks:
				asus = re.findall('><strong>(.*?)</strong></a>',coks)
				for xx in asus:
					AC = xx.replace('First', '').replace('Email Address Search', '').replace('IP Address Blacklist Check', '').replace('Hosting Providers', '').replace('Domain Providers', '').replace('Website Error Checker', '')
					print(kuning + '[Geting website list --> ]' + ijo + AC)
					open("domain.txt","a").write("http://"+AC+"\n")
				else:
					print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass

def sitenlist11():
	try:
		PAGEAWAL = raw_input('Page Awal@ ~#: ')
		PAGEAKHIR = raw_input('Page Akhir@ ~#: ')
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
		PAGEAWAL = raw_input('Page Awal@ ~#: ')
		PAGEAKHIR = raw_input('Page Akhir@ ~#: ')
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			coks = requests.get("https://www.uidomains.com/available-domains/"+str(page), headers=headers, timeout=15).text
			if 'Recently Found Available Domains' in coks:
				asus = re.findall('<li>(.*?) - ',coks)
				for xx in asus:
					print(kuning + '[Geting website list --> ]' + ijo + xx)
					open("domain.txt","a").write("http://"+xx+"\n")
				else:
					print(kuning + '[CODED BY SHIN_CODE --> ]')
	except:
		pass

def sitenlist13():
	try:
		DOMAIN = raw_input('EXAMPLE org/com@ ~#: ')
		PAGEAWAL = raw_input('Page Awal@ ~#: ')
		PAGEAKHIR = raw_input('Page Akhir@ ~#: ')
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
		TNBNHR = raw_input('TAHUN-BULAN-TANGGAL@ ~#: ')
		PAGEAWAL = raw_input('Page Awal@ ~#: ')
		PAGEAKHIR = raw_input('Page Akhir@ ~#: ')
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(PAGEAWAL), int(PAGEAKHIR)):
			coks = requests.get("https://websitebiography.com/new_domain_registrations/"+TNBNHR+"/"+str(page)+"/", headers=headers, timeout=15).text
			if 'Domain' in coks:
				asus = re.findall("class='flexible_dv_30_50'> (.*?) </a>",coks)
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
			sitenlist4()
		if pilihmas =='5':
			sitenlist5()
		if pilihmas =='6':
			sitenlist6()
		if pilihmas =='7':
			sitenlist7()
		if pilihmas =='8':
			sitenlist8()
		if pilihmas =='9':
			sitenlist9()
		if pilihmas =='10':
			sitenlist10()
		if pilihmas =='11':
			sitenlist11()
		if pilihmas =='12':
			sitenlist12()
		if pilihmas =='13':
			sitenlist13()
		if pilihmas =='14':
			sitenlist14()
		if pilihmas =='15':
			print(ijo + '\nCooming Soon !!!\n' + putih)
		
	except:
		pass

if __name__ == '__main__':
	Main()