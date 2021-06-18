data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')
print(data[0])

wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		print('感謝使用本查詢功能')
		break
	if word in wc:
		print(word,'出現的次數為',wc[word])
	else:
		print('這個字不在字典裡喔！！')




#um_len = 0
#for d in data:
	#len(d)
	#sum_len = sum_len + len(d)
#print(sum_len)
#print('留言的平均長度為', sum_len / len(data))

#new = []
#for d in data:
	#if len(d) < 100:
		#new.append(d)
#print('一共有', len(new), '筆資料小於100')

#good = []
#for d in data:
	#if 'good' in d:
		#good.append(d)
#good = [d +'123' for d in data if 'good' in d]
#print(good)




