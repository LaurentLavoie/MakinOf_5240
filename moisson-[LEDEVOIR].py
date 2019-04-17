# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

entete = {
	"User-Agent": "Laurent Lavoie",
	"From":"laurent.lavoie96@gmail.com"
}

fichier = "LeDevoir2.csv"
#Première tentative de moissonnage
#for onglets in range(1, 1000000) :
	#for jour in range(1, 32) :
		#for mois in range(1,4) :
			#url = "https://www.ledevoir.com/recherche/{onglets}?tri=date_asc&section_id=&expression=&tri_widget=date_asc&tri_widget=date_asc&date=depuis_1998&format=tous&section=&date_debut=2019-{mois}-{jour}&date_fin=2019-{mois}-{jour}&section=&collaborateur_nom=".format(onglets=onglets, mois=mois, jour=jour)
			#print (len(url))


# Deuxième tentative de moissonnage, année 2018 - Les chiffres indiqués dans le range représentent le premier et dernier texte			
for numero in range(533296, 533480) :
	url = "http://m.ledevoir.com/article-{numero}".format(numero=numero)


	contenu = requests.get(url, headers=entete)
	if contenu.status_code == 200 :

		try :
			page = BeautifulSoup(contenu.text, "html.parser")

			print("<>"*40)

			info = page.find("div", class_="container")
			

			#Extraction des informations qu'on cherche
			print(url)

			titre = page.find("meta", attrs={"name":"title"})["content"].split("|")
			print(titre[0])
			
			#auteur = info.find("div", class_="col-xs-14").find_next("h1").text.strip()

			section = page.find("meta", attrs={"property":"og:url"})["content"].split("/")
			print(section[3])

			# #info.find("div", class_="headers-article-carousel hidden-xs").find("h3").find("a").text

			journaliste = page.find("aside", class_="author").find("h3").text.split("à")
			if "La Presse canadienne" :
				print(journaliste[0])

			tout = [url, titre[0], journaliste[0], section[3]]
			
			f2 = open(fichier,"a")
			final = csv.writer(f2)
			final.writerow(tout)
			
		except :
			pass
			
#533479
#############################################################################
	##Notes



# Ces formules étaient préalablements nécessaires pour aller chercher la section et la date mais, l'info sort complètement avec ce qui est au-dessus
	# section = info.find("div", class_="row").find("li").find("a").text.strip()
	
	# date = info.find("aside", class_="author").find("time").text.strip()
				

				#try :

			#section_li_articles = page.find("ul", class_="list-unstyled results").find_all("li")

			#except Exception as e:
				#raise e
			
			#for articles in section_li_articles :
				#href_article = articles.find("h2").find("a")["href"]
				
				#lien_article = "https://www.ledevoir.com" + href_article
				
				#contenu2 = requests.get(lien_article,headers=entete)

				#page_article = BeautifulSoup(contenu2.text, "html.parser")
				
				



				
								#titre = (texte.find("h2").text)
								#print(texte.find("a")["href"])
								#descriptif = (texte.find("p").text)
								#date = (texte.find("time").text)
								#auteur = (texte.find("span").find_next("").text) 
								#section = (texte.find("span").find_next(class_="section"))
								#infos =  [titre, date, auteur, section]
								#print(infos)
								#print("*"*30)
								#Agences = ["Agence France-Presse", "Associated Presse", "La Presse canadienne", "Reuters"]
									#for Agence in infos : 
										#print(Agence)

							#f2 = open(fichier,"a")
							#final = csv.writer(f2)
							#final.writerow(infos)

				#if not texte.find("span", "Rectificatif", class_="sans-datetime") :

				#n = 0

				#		for Agences in infos : 
				#			n += 1
				#			print(Agences)


				# Pour avoir les bons caractères : .encode("latin-1").decode("utf-8")

				# print()
				# print(len(page.find_all("article", class_="has-img"))) #une virgule signifie nouvel élément. Pour que class marche, il faut mettre une barre de soulignement
				# #pour avoir toute la liste, mettre "find_all"
				# print()

