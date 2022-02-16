from PIL import Image
import os

for file in os.listdir(".") :
	if file.endswith(".jpg"):
		image_file = Image.open(file) # image_file 是物件
		image_file = image_file.convert("L")
		image_file.save(file[:-4] + "_gray.png")
		print(file)

