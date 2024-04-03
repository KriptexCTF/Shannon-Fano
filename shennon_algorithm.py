def test_B(B):
	summ = 0.0
	for i in B:
		summ += i * 10
	if(summ != 10):
		print(f"Error B array\nsumm == {summ/10}")
		exit()
def find_k(matrix):
	k = 0
	if(len(matrix) == 1):
		return 0
	for i in range(1, len(matrix[0])):
		summ1, summ2 = 0, 0
		for j in range(0, i):
			summ1 += matrix[1][j]*10
		for q in range(i, len(matrix[0])):
			summ2 += matrix[1][q]*10
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
print("Алгоритм Шенона для:")
#A = ['a', 'b', 'c', 'd', 'e'] #Алфавит А
#B = [0.3, 0.2, 0.2, 0.2, 0.1] #Вероятности появления символов
A = ['k','d','c','g','h','b','e','x','t','j']
B = [0.045,0.01,0.1,0.5,0.1,0.02,0.1,0.015,0.01,0.1]
#A = ['a','b','c']
#B = [0.5, 0.25, 0.25]
#---------------------------
test_B(B)
print(f"A - {A}\nB - {B}\n")
koding_arr = create_koding_arr(A)
matrix = [A, B]
k = find_k(matrix)
add_kodding(k, A)
new_arr = split_arr_k(A, k)
while(len(new_arr) != len(A)):
	new_arr = create_new(new_arr)
for i in koding_arr:
	print(i)
