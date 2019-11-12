from PIL import Image
import os,sys

path = "/Users/ezraschwartz/Documents/thesis/images/"
new_path = "/Users/ezraschwartz/Documents/thesis/resized_images/"
dirs = os.listdir(path)

def resize():
	count = 0
	for item in dirs:
		if os.path.isfile(path+item):
			if not os.path.isfile(new_path+item):
				try:
					im = Image.open(path+item)
					f, e = os.path.splitext(item)
					imResize = im.resize((128,128), Image.ANTIALIAS)
					try:
						imResize.save(new_path + f + ".jpg", 'JPEG', quality = 90)
						print("Saved "+f+".jpg in resize folder")
					except(IOError):
						count +=1
						print("IOError happened")
				except(OSError):
					print("OSError happened")
				
			else:
				print("item already found in resized folder")
	print(str(count) + " IOErrors happened")
resize()
