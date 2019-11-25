#run as
#python3 downloadscript.py <csv_filename>

import sys
import urllib
from urllib.request import urlretrieve
from csv import reader
import os.path

csv_filename = sys.argv[1]

with open(csv_filename+".csv".format(csv_filename), 'r') as csv_file:
	count = -1
	for line in reader(csv_file):
		count+=1
		if os.path.isfile("dankmemes_images/" + str(line)+ ".jpg"):
			print("Image skipped for %s" % str(line))
		else:
			try:
				urlretrieve(line[0], "dankmemes_images/"+str(count)+".jpg")
				print("Image saved for %s" % str(line))
			except (urllib.error.HTTPError, urllib.error.URLError):
				print("skipped bc httperror")

print("finished")
