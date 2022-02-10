# 二維 List 紀錄 商品名稱 與 價錢
products = []
while True :
	name = input("請輸入商品名稱 :")
	if name == "q" :
		break
	price = input("請輸入商品價格 :")
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

