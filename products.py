# 二維 List 紀錄 商品名稱 與 價錢
products = []
while True :
	name = input("請輸入商品名稱 :")
	if name == "q" :
		break
	price = input("請輸入商品價格 :")
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price] # 用這一行 取代前三行
	products.append([name, price]) # 再度簡潔 用這行 取代前面程式
print(products)
products[0][0] # 取出低一個商品的名稱


