# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

fichier = "JDM.csv"

dateDebut = "2018-01-01"
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
	if journee.month < 10 :
		mois = "0{}".format(journee.month)
	else : 
		mois = journee.month

	if journee.day < 10 :
		jour = "0{}".format(journee.day)
	else : 
		jour = journee.day

	fichier = "findesession.csv"
	#section = ("actualite")
	sections = ("actualite","enquetes", "sports","spectacles", "argent", "monde", "lesacdechips", "auto", "jm", "porte-monnaie", "5-minutes", "voyages", "opinions", "blogues", "24heures")
	for section in sections :
	
		url = "https://www.journaldemontreal.com/{}/archives/{}/{}/{}.php".format(section,journee.year,mois,jour)
		print(url)

		contenu = requests.get(url, headers=entete)
		try :
			if contenu.status_code == 200 :

			
					page = BeautifulSoup(contenu.text, "html.parser")

					textes = page.find("div", class_="article-container").find_all("article", class_="archive")
					#print(textes)

					for texte in textes :
						href = texte.find("a")["href"]
						print(href)

						contenu2 = requests.get(href, headers=entete)

						page2 = BeautifulSoup(contenu2.text, "html.parser")
						print("<>"*40)

						#infos =  page2.find("script", "var")

						titre = page2.find("meta", attrs={"property":"og:title"})["content"]
						date = page2.find("meta", attrs={"name":"cXenseParse:recs:publishtime"})["content"]
						auteur = page2.find("meta", attrs={"name":"author"})["content"]
						section = page2.find("meta", attrs={"name":"cXenseParse:recs:que-sectionclassname"})["content"]
						tout = [auteur, titre, date, section]
						print(tout)
						f2 = open(fichier,"a")
						final = csv.writer(f2)
						final.writerow(tout)
		except :
			pass
		





				#"spectables", "argent", "monde", "lesacdechips", "auto", "jm", "porte-monnaie", "5-minutes", "voyages", "opinions", "blogues", "24heures"
