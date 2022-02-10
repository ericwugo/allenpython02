import os
# 讀取檔案 並檢查 檔案是否存在 (os.path.isfile(檔名))
products = []
if os.path.isfile("products.csv") :
	print("yeah ! 找到檔案了")
	with open("products.csv", "r", encoding="utf-8") as f :
		for line in f:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name,price])
	print(products)

else :
	print("找不到檔案......")

# 二維 List 紀錄 商品名稱 與 價錢

#讓使用者輸入
while True :
	name = input("請輸入商品名稱 :")
	if name == "q" :
		break
	price = input("請輸入商品價格 :")
	price = int(price) # 把字串 轉型為 int
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price] # 用這一行 取代前三行
	products.append([name, price]) # 再度簡潔 用這行 取代前面程式
print(products)
print(products[0][0]) # 取出低一個商品的名稱

#印出所有購買資料
for p in products : # 印出 商品名稱與價錢
	print(p[0], "的價錢是 :", p[1])

#寫入檔案
with open("products.csv", "w", encoding="utf-8") as f : # 顯示正確中文的編碼 utf-8
	f.write("商品,價格\n")
	for p in products :
		f.write(p[0] + "," + str(p[1]) + "\n")

