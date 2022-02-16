from PIL import Image
import os

for file in os.listdir("orig") : # 打開 相同路徑下的 orig 資料夾
	if file.endswith(".jpg"): # 用 os.path.join 將檔案與資料夾合併 !
		image_file = Image.open(os.path.join("orig/", file)) # image_file 是物件 開啟檔案時 要加路徑 "orig/"
		image_file = image_file.convert("L")
		image_file.save(os.path.join("result/" , file[:-4] + "_gray.png")) # 儲存檔案 也要加路徑 "result/"
		print(file)

