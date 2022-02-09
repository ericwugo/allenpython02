data = []
count = 0
with open("reviews.txt", "r") as f :
	for line in f:
		data.append(line)
		count += 1
		if count % 200000 == 0 :
			print(len(data))
print("總共有", len(data), "筆資料")

sum_len = 0
for d in data :
	sum_len += len(d)

print("留言的平均長度為 :", sum_len/len(data))

new = []
for d in data :
	if len(d) < 100 :
		new.append(d)
print("一共有", len(new), "筆留言 長度小於 100")


good = []
for d in data :
	if "good" in d :
		good.append(d)
print("一共有", len(good), "筆留言 裡面有 Good ")
print(good[0])

good1 = [d for d in data if "good" in d]
print("List comprehensive 寫法 一共有", len(good1), "筆留言 裡面有 Good ")


bad = ["bad" in d for d in data]  # 如果留言裡面有 bad 就 出現 True, 沒有就出現 False
print("List comprehensive 寫法 一共有", len(bad), "筆留言 裡面有 True or False")
#print(bad)



