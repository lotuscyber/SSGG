import os
import sys
import re
import subprocess
import time
import random

logo = ''' \033[1;31m \n
    ______   _____                  _                   
   / _____) (____ \                | |                  
  | /  ___   _   \ \   ___    ____ | |  _   ____   ____ 
  | | (__ ) | |   | | / _ \  / ___)| | / ) / _  ) / ___)
  | \____|| | |__/ / | |_| || |    | |< ( ( (/ / | |    
   \______/ |_____/   \___/ |_|    |_| \_) \____)|_|    
                                 \033[1m\033[37m Made with \033[91m<3\033[37m By 5HR3D\033[1;m\033[0m '''

print(logo)
print("\n\n")

try:
	from googlesearch import search
except:
	print("Installing Requirements")
	os.system("python3 -m pip install google")
	os.system("clear")
	print(logo)
	print("\n\n  Module Installed, Please Re-run the script.\n")
try:
	import requests
except:
	print("Installing Requirements")
	os.system("python3 -m pip install requests")
	os.system("clear")
	print(logo)
	print("\n\n  Module Installed, Please Re-run the script.\n")

os.system("clear")
print(logo)
print("\n\n")
print("  Choose: ")
print("")
print("  [01] Query Dorking")
print("  [02] Website Dorking")
print("  [03] About")

dtype = input("\n\033[1;33m   [#]:>\033[1;37m ")

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)


if dtype == "1" or dtype == "01":
	print("\n\n")
	slow_type("\n\033[1;33m   Starting...\n")
	time.sleep(2)
	os.system("clear")
	print(logo)
	print("\n\n")
	input("\033[1m   ENTER 'S' TO CONTINUE: ")
	os.system("clear")
	print(logo)
	print("\n\n")
	f = open('links.txt', 'w')
	usrquery = input(" \033[1;33m Enter your Query: \033[1;31m")
	numoflinks = input(" \033[1;33m Enter max number of links to scrape:\033[1;31m ")
	for url in search(usrquery, stop=int(numoflinks)):
		f.write(url + "\n")
		print(url)
	print("""

 ---------------------------------------------------------
   \033[1;33m       Contact Me:\033[1;31m https://linktr.ee/5HR3D
 ---------------------------------------------------------
 		       \033[1;37m./ThankYou
	
""")


elif dtype == "2" or dtype == "02":
	print("\n\n")
	slow_type("\n\033[1;33m   Starting...\n")
	time.sleep(2)
	os.system("clear")
	print(logo)
	print("\n\n")
	input("\033[1m   ENTER 'S' TO CONTINUE: ")
	os.system("clear")
	print(logo)
	print("\n\n")

	url = input("\033[1;33m  Website url:\033[1;31m ")
	print("\n\n")
	subprocess.call(["chmod", "777", url + ".html"])
	subprocess.call(["rm", url + ".html"])
	time.sleep(2)
	subprocess.call(["clear"])
	print(logo)
	print("\n\n")

	f = open(str(url) + ".html", "at")
	filekanaam = url + '.html' 
	f.write('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"> <title>Results from GDorker by 5HR3D</title> </head> <body><br>')
	
	
	def process_google():
		global f
		print("  Dorking via Google")
		print("\n")
		f.write("<h1>Results from Google</h1>")
		f.write("<br>")
		print ("  [#]Checking for Directory listing vulnerabilities")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+intitle:index.of&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>Possible Directory listing</h2>')
			f.write('<a href="' + requesturl + '">Click Here</a>')
			f.write("<br>")
		
		print ("  [#]Checking for Configuration files exposed")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>Possible Configuration files</h2>')
			f.write('<a href="' + requesturl + '">Click Here</a>')
			f.write("<br>")

		print ("  [#]Checking for Database files exposed")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:sql+|+ext:dbf+|+ext:mdb&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>Possible Database files</h2>')
			f.write('<a href="' + requesturl + '">Click Here</a>')
			f.write("<br>")
		
		print ("  [#]Checking for Log files exposed")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:log&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>Possible Log files</h2>')
			f.write('<a href="' + requesturl + '">Click Here</a>')
			f.write("<br>")
		
		print ("  [#]Checking for Backup and old files")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>Possible Backup and Old files</h2>')
			f.write('<a href="' + requesturl + '">Click Here</a>')
			f.write("<br>")

		print ("  [#]Checking for Login pages")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+inurl:login&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>Possible Login pages</h2>')
			f.write('<a href="' + requesturl + '">Click Here</a>')
			f.write("<br>")

		print ("  [#]Checking for SQL errors")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>Possible SQL Errors</h2>')
			f.write('<a href="' + requesturl + '">Click Here</a>')
			f.write("<br>")

		print("  [#]Checking for Publicly exposed documents ")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>Possible Publicly Exposed Documents</h2>')
			f.write('<a href="' + requesturl + '">Click Here</a>')
			f.write("<br>")

		print("  [#]Checking for phpinfo() ")
		requesturl = 'https://www.google.com/search?q=site:'+ url +'+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22&hl=en'
		response = requests.get(requesturl)
		notfound = re.search('\s-\sdid not match any documents.', response.text)
		captcha = re.search(',\ssolving the above CAPTCHA will let you continue\s', response.text)
		if notfound:
			print("  [-]No results found\n")
		elif captcha:
			print("  [-]Captcha triggered. Please try after some time.\n")
		else:
			print("  [+]Registering data into the file.\n")
			f.write('<h2>phpinfo()</h2>')
		f.write('<a href="' + requesturl + '">Click Here</a>')
		f.write("""<br><br><h1><a href="https://linktr.ee/5HR3D">CONTACT 5HR3D</a><br></h1>""")
		f.close()
		
		print("\n  Found data is registered in " + filekanaam + " :)")
		print("""
 ---------------------------------------------------------
   \033[1;33m       Contact Me:\033[1;31m https://linktr.ee/5HR3D
 ---------------------------------------------------------
 		       \033[1;37m./ThankYou
	
""")
	process_google()

elif dtype == "3" or dtype == "03":
	print("\n\n")
	slow_type("\n\033[1;33m   Loading...\n")
	time.sleep(1)
	os.system("clear")
	print(logo)
	print("\n\n")
	
	print("""

  \033[1;33m[\033[1;32m#\033[1;33m] ABOUT :>
  
  \033[1;37mGDorker \033[1;31mis a web scraper made purely with Python-3. It 
  has two main scraping options:
	-Query dorking
	-Website dorking
\033[1;31m
  Query dorking
	Scrapes URL's displayed in google for a specific 
	search query given by the user and saves it to a
	file  named 'links.txt'  and also prints the url 
	in the  terminal. It also  asks you how many top 
	url's to  scrape according  to your requirements.
\033[1;31m
  Website dorking
	Scrapes a website. After the URL of a website is 
	given it searches for indexed links of:
		     -Directory lisiting vulnerabilities
		     -Configuration files exposed
		     -Database files exposed
		     -Log files exposed
		     -Backup and old files
		     -Login pages
		     -SQL errors
		     -Publicly exposed documents
		     -PHPinfo() files

	then register's the  results in a html file with 
	the URL in its file name.
 ---------------------------------------------------------
   \033[1;33m       Contact Me:\033[1;31m https://linktr.ee/5HR3D
 ---------------------------------------------------------
 		       \033[1;37m./ThankYou
	""")  

else:
	print("\n \033[1;31m Encountered Error, Please Retry.\n")
	exit()




















