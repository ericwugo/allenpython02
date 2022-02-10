# 沒有 參數的 function
def wash():
	print("加水")
	print("家洗衣精")
	print("選轉")

#有參數 與 參數預設值的 function
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
print("------------")
def add(x, y) :
	return x + y

result = add(3, 4)
print(result)
print("------------")

def average(numbers):
	# avg = sum(numbers) / len(numbers)
	# return avg
	return sum(numbers) / len(numbers)
a = average([1, 2, 3])
print("average list 的平均值是 :", a)
print("第一個 List avg :",average([20,30,40]), "\n", 
	"第二 List avg :", average([200,250,300]))




