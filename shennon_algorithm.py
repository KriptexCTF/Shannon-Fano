#Kriptex
def test_B(B):
	summ = 0.0
	for i in B:
		summ = round(summ + i, 5)
	if(round(summ, 2) != 1):
		print(f"Error B array\nsumm == {summ/10}")
		exit()
def find_k(matrix1):
	help_B = []
	for i in matrix1:
		for j in sorted_pairs:
			if(i == j[0]):
				help_B.append(j[1])	
	k = 0
	if(len(matrix1) == 2):
		return 0
	for i in range(1, len(matrix1)):
		summ1, summ2 = 0, 0
		for j in range(0, i):
			summ1 += help_B[j]*10
		for q in range(i, len(matrix1)):
			summ2 += help_B[q]*10
		if(i == 1):
			minimum = abs(summ1 - summ2)
			k = 0
		if(minimum > abs(summ1 - summ2)):
			minimum = abs(summ1 - summ2)
			k = i-1
	return k
def create_koding_arr(A):
	arr = []
	for i in A:
		arr.append([i, ''])
	return arr
def split_arr_k(A, k):
	new_arr1 = []
	new_arr2 = []
	for i in range(k+1):
		new_arr1.append(A[i])
	for i in range(k+1, len(A)):
		new_arr2.append(A[i])
	return [new_arr1, new_arr2] 
def add_kodding(k, diapozon):
	for i in range(len(koding_arr)):
		if(koding_arr[i][0] == diapozon[0]):
			start = i
		if(koding_arr[i][0] == diapozon[len(diapozon)-1]):
			stop = i
	for i in range(start, stop+1):
		if(i <= k+start):
			koding_arr[i][1] += '0'
		else:
			koding_arr[i][1] += '1'
def create_new(last_arr):
	new_arr = []
	for i in last_arr:
		if(len(i) != 1):
			test_k = find_k(i)
			add_kodding(test_k, i)
			t = split_arr_k(i, test_k)
			for i in t:
				new_arr.append(i)
		else:
			new_arr.append(i)
	return(new_arr)
#---------------------------Kriptex
print("Алгоритм Шенона для:")
#A = ['a', 'b', 'c', 'd', 'e'] #Алфавит А
#B = [0.3, 0.2, 0.2, 0.2, 0.1] #Вероятности появления символов
A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']
B = [0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.035,0.09]
#A = ['a','b','c','d','e','f','g']
#B = [0.05,0.2,0.2,0.125,0.125,0.05,0.25]
#---------------------------Kriptex
if(len(A) != len(B)):
	print("len A != len B")
	exit()
test_B(B)
pairs = list(zip(A, B))
# Сортируем пары по значениям из массива B
sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
print(f"A - {A}\nB - {B}\n")
A = []
B = []
for i in sorted_pairs:
	A.append(i[0])
	B.append(i[1])
koding_arr = create_koding_arr(A)
k = find_k(A)
add_kodding(k, A)
new_arr = split_arr_k(A, k)
while(len(new_arr) != len(A)):
	new_arr = create_new(new_arr)
for i in koding_arr:
	print(i)
print("__ENCODE__")
string = input("=> ")
output = ""
for i in string:
	for j in koding_arr:
		if(i == j[0]):
			output += j[1]
print(output)
print("__DECODE__")
string = input("=> ")
decode_str = ""
while(string != ""):
	for i in koding_arr:
		len_kod = len(i[1])
		if(string[:len_kod] == i[1]):
			string = string[len_kod:]
			decode_str += i[0]
print(decode_str)
