#full path and name to your csv file
csv_filepathname="/Users/Nikaela/Desktop/Project/WordApp/zips/data/wordData.csv"
#full path to your Django project directory
your_djangoproject_home="/Users/Nikaela/Desktop/Project/WordApp/"

import sys, os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from .models import wordData

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    worddata = wordData()
    worddata.englishWord = row[0]
    worddata.maoriWord = row[1]
    worddata.save()