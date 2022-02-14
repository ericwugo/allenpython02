#dictionary 字典的定義與應用 key:value
words = {"raman":'拉麵', "pasta":"義大利麵"}

words["tea"] = "茶" # 字典內容的新增
print(words)

p0 = {
	"name":"麥香奶茶",
	"price":10
}
p1 = {
	"name":"珍珠奶茶",
	"price":60
}

drinks = [p0, p1]
print(drinks)

print(drinks[0]["name"]) # 麥香奶茶
print(drinks[1]["price"]) #60