# 沒有 參數的 function
def wash():
	print("加水")
	print("家洗衣精")
	print("選轉")

#有參數的 function
def wash1(dry=False, water=8):
	if dry :
		print("烘衣")
	else :
		print("加水", water,"分滿")
		print("家洗衣精")
		print("選轉")
	

wash()
wash1()
wash1(True)

