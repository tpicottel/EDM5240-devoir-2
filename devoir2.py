#coding: utf-8

import json
import csv
import requests

fichier = "banq.csv"

adresse = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

entete = {
	"User-Agent": "Thomas Picotte-Lavoie",
	"From": "514-746-7975"
}

l1 = range(1000,2001)
for numero in l1:
	
	url = adresse + str(numero)
	#print(url)
	req = requests.get(url,headers=entete)
	#print(req)
	if req.status_code == 200:
		infos = req.json()
		#print(infos)
		i = infos ["titre"]
		if infos["type"] == "audio":
			s = []
			s.append(infos["titre"][:(i.find("/"))])
			s.append(infos["createurs"][0])
			s.append(infos["dateCreation"])
			s.append(infos["descriptionMat"])
			print(infos["titre"][:(i.find("/"))])
			print(infos["createurs"][0])
			print(infos["dateCreation"])
			print(infos["descriptionMat"])
			#print(infos["url"])
			url1 = (infos["iris"]).replace("0000","/1/")
			#print(url0)
			url0 = (infos["url"].replace("ark:","bitstream"))
			#print(url1)
			url2 = ".m4a"
			url3 = url0 + url1 + url2
			#print(url3)
			print(url3)
			print("~"*80)
		

			f2 = open(fichier, "a")
			banq = csv.writer(f2)
			banq.writerow(s)
