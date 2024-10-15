#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.
N = []
for i in range(10):
    N.append(i)

print(N)

for i in range(len(N)):
    N[i] = N[i] + 1
print(N)
