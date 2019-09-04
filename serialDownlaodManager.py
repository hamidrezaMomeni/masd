#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:49:00 2019

@author: hamidreza
"""
import requests
from bs4 import BeautifulSoup
from os import system

baseUrl = "http://mydiba.club"
userMovie = input("Enter name Movie (Example harry potter): ")
nameMovie = userMovie.replace(" ", "+")
searchUrl = baseUrl + "/?s="+str(nameMovie)
searchPage = requests.get(searchUrl)
soup = BeautifulSoup(searchPage.content, "html5lib")
div = soup.find_all("div",{"class":"search-results"})
print("we found {} movie: ".format(len(div)))
if len(div) == 0:
    exit(0)
print()
counter = 1
for item in div:
   print(str(counter) + "){}".format(item.text))
   counter += 1

userSelected = int(input("enter number of movie: ")) - 1
movieSelected = div[userSelected]
if "سریال" in movieSelected.text.strip():
    movieUrl = movieSelected.find("a")["href"]
    moviePage = requests.get(movieUrl)
    
    soup = BeautifulSoup(moviePage.content, "html5lib")
    divBody = soup.find_all("div",{"class":"-dl"})
    title = soup.find_all("h4",{"class":"-dl-title"})
    counter = 1
    for item in title:
        print(str(counter) + ") {}".format(item.text.strip()) + "\n")
        counter += 1
        
    userChoose = int(input("enter number of your coose: ")) - 1
    insideTitle = title[userChoose].text.strip() 
    userSelected = divBody[userChoose]
    blockLinks = userSelected.find("div",{"class":"Block_links"})
    movieLinks = blockLinks.find_all("a")
    counter = 1
    for item in movieLinks:
        print(str(counter) + ") " + item.text)
        print()
        counter += 1
    partSelected = int(input("Enter number of part movie: ")) - 1
    urlDownload = movieLinks[partSelected]["href"]
    
    system("mkdir -p '{}' && cd '{}' && wget '{}'".format(nameMovie,nameMovie,urlDownload))
    
    
    
    
    
    
    
