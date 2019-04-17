# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

fichier = "laPresse.csv"

dateDebut = "2018-11-09"
dateFin = "2018-12-31"

debut = datetime.strptime(dateDebut, "%Y-%m-%d")
fin = datetime.strptime(dateFin, "%Y-%m-%d")

diff = fin - debut

for j in range(diff.days + 1):
	journee = debut + timedelta(days = j)

	entete = {
	"User-Agent": "Laurent Lavoie",
	"From":"laurent.lavoie96@gmail.com"
	}

	url = "https://www.lapresse.ca/archives/{}/{}/{}.php".format(journee.year,journee.month,journee.day)
	print(journee,url)


	contenu = requests.get(url, headers=entete)
	if contenu.status_code == 200 :

		page = BeautifulSoup(contenu.text, "html.parser")

		links = page.find("ul", class_="square square-spread").find_all("li")
		#print(links)


		# Aller chercher les URL de chacun des articles
		for link in links :
			href = link.find('a')['href']

			try:
					
				contenu2 = requests.get(href, headers=entete)

				page2 = BeautifulSoup(contenu2.text, "html.parser")
				print("<>"*40)
				#Extraction des informations qu'on cherche

				#Titre - FONCTIONNE RELATIVEMENT BIEN : le problème ici : les titres se print en quadruple pour une raison que j'ignore
				# titre = page2.find("div", id="maincontent").find_next("h1").text
				# print(titre)
				print(href)
				print()
				
				
				try :
					auteur = page2.find("div", class_="boxAuteur").text
				except : 
					title = page2.find(title).text.split()
					if len(title) == 2:
						auteur = "Externe inconnu"
					else :
						auteur = title[1].strip()
						if "La Presse canadienne":
							print(auteur)

				try :
					auteur = page2.find("div", class_="boxAuteur").text
				except : 
					title = page2.find(title).text.split()
					if len(title) == 2:
						auteur = "Externe inconnu"
					else :
						auteur = title[1].strip()
						if "Agence France-Presse":
							print(auteur)

				try :
					auteur = page2.find("div", class_="boxAuteur").text
				except : 
					title = page2.find(title).text.split()
					if len(title) == 2:
						auteur = "Externe inconnu"
					else :
						auteur = title[1].strip()
						if "Associated Press":
							print(auteur)

				try :
					auteur = page2.find("div", class_="boxAuteur").text
				except : 
					title = page2.find(title).text.split()
					if len(title) == 2:
						auteur = "Externe inconnu"
					else :
						auteur = title[1].strip()
						if "La Presse":
							print(auteur)

				try :
					auteur = page2.find("div", class_="boxAuteur").text
				except : 
					title = page2.find(title).text.split()
					if len(title) == 2:
						auteur = "Externe inconnu"
					else :
						auteur = title[1].strip()
						if "Agence Science-Presse":
							print(auteur)

				# try :
				# 	auteur = page2.find("div", class_="boxAuteur").find("div", class_="infosAuteur").text
				# except :
				# 	title = page2.find(title).text.split()
				# 	if (title) == 0:
				# 		auteur = "None"


				#("meta", attrs={"property":"og:title"})["content"]
				
				#Date - FONCTIONNE
				date = page2.find("meta", attrs={"property":"article:published_time"})["content"]
				print(date)

				# #Section -FONCTIONNE
				section = page2.find("meta", attrs={"property":"article:section"})["content"]
				print(section)
			except :
				pass

			# try :
			# 	title = page2.find("div", class_="article-page").find("h1").text
			# except : 
			# 	title = page2.find(title).split()
			# 	if len(title) == 0:
			# 		title = "Supprimé"
			# 	else : 
			# 		title = page2.find("meta", attrs={"name":"description"})[content]
			# 		if None :
			# 			print(title)


			#tout
			tout = [auteur, date, section]


			f2 = open(fichier,"a")
			final = csv.writer(f2)
			final.writerow(tout)

			
			##################################################################
			##Notes ------ ce contenu était à l'essaie

			
			
			#auteur = page2.find("div", id="maincontent").find_next("div", class_="infosAuteurs").text
			#print(auteur)
			#problème ici : AttributeError: 'NoneType' object has no attribute 'text', je ne comprends pas pourquoi


			#Section
			#print(page2.find("meta", attrs={"property":"article:section"})["content"])
			#print(section)

			# tout = [titre, date, auteur, section]
			
			# print(tout)


			#auteur = page.find("div", id="wrapper").find("div", class_="leftbar").text

			# fichier = "misession.csv"
# # URL de base pour aller chercher les archives selon les dates
# for mois in range(1,13) :
# 	for jour in range(1, 32) :
# 		url = "https://www.lapresse.ca/archives/2018/{mois}/{jour}.php".format(mois=mois, jour=jour)
		#print (url)
		#*******il bogue le 28 février puisque le 29-30-31 février n'existe pas... dois-je mettre un try ?