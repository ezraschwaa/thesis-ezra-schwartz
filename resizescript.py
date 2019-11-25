#run
#python3 resizescript.py <data> <destination>

from PIL import Image
from PIL import ImageFile
import os,sys

ImageFile.LOAD_TRUNCATED_IMAGES = True

data_folder = sys.argv[1]
destination_folder = sys.argv[2]

path = "/Users/ezraschwartz/Documents/thesis/"+data_folder+"/"
new_path = "/Users/ezraschwartz/Documents/thesis/"+destination_folder+"/"
dirs = os.listdir(path)

def resize():
	count = 0
	for item in dirs:
		if item == ".DS_Store":
			continue
		if os.path.isfile(path+item):
			if not os.path.isfile(new_path+item):
				try:
					im = Image.open(path+item)
					f, e = os.path.splitext(item)
					imResize = im.resize((512,512), Image.ANTIALIAS)
					imResize.save(new_path + f + ".jpg", 'JPEG', quality = 90)
					print("Saved "+f+".jpg in resize folder")
				except(OSError):
					im = Image.open(path+item).convert('RGB').save(path+item)
					im = Image.open(path+item)
					f, e = os.path.splitext(item)
					imResize = im.resize((512,512), Image.ANTIALIAS)
					imResize.save(new_path + f + ".jpg", 'JPEG', quality = 90)
					print("Saved "+f+".jpg in resize folder")
			else:
				print("item already found in resized folder")
	print(str(count) + " IOErrors happened")
resize()
