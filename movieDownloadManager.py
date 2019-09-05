#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:02:34 2019

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

movieUrl = movieSelected.find("a")["href"]
moviePage = requests.get(movieUrl)

soup = BeautifulSoup(moviePage.content, "html5lib")
divBody = soup.find_all("div",{"class":"-body"})
title = soup.find_all("h4",{"class":"-dl-title"})
counter = 1
for item in title:
    print(str(counter) + "){}".format(item.text.strip()) + "\n")
    counter += 1

userChoose = int(input("enter number of your choose: ")) - 1
insideTitle = title[userChoose].text.strip()

userSelected = divBody[userChoose]

counter = 1
userSelectedDescription = userSelected.find_all("div",{"class":"Block_infos"})
userSelectedLinks = userSelected.find_all("div",{"class":"Block_links"})
for item in userSelectedDescription:
    print()
    quality = item.find("li").text
    print(str(counter) + "){} {}".format(insideTitle,quality))
    counter += 1
    
userQuality = int(input("Enter number of quality: ")) - 1

userSelectedLink = userSelectedLinks[userQuality]
urlDownload = userSelectedLink.find("a",{"class":"dublboxa"})["href"]
print("\n\n\n")

system("mkdir -p '{}' && cd '{}' && wget '{}'".format(nameMovie,nameMovie,urlDownload))
system("notify-send 'Starting Download ...' -a 'movie and serial downloader' ")


