from PIL import Image
import os

for file in os.listdir("orig") : # 打開 相同路徑下的 orig 資料夾
	if file.endswith(".jpg"):
		image_file = Image.open("orig/" + file) # image_file 是物件 開啟檔案時 要加路徑 "orig/""
		image_file = image_file.convert("L")
		image_file.save("result/" + file[:-4] + "_gray.png") # 儲存檔案 也要加路徑 "result/"
		print(file)

