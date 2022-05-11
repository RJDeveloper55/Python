num = 1
sum = 0

print("Enter a Number. Please enter zero (0) to exit!")

while num != 0:
    num = float(input('Enter Number? '))
    sum += num
    print('sum =', sum)
else:
    print('Sum is ended')

i = 0
while i < 5:
    print('The value of i is:', i)
    i += 1
else:
    print("The while loop is ended")


A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
C = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
D = {'name':'safdar', 'age':35, 'gender':'male'}

for keys, values in D.items():
    print(keys, ':', values)

for i in range(2, 50, 4):
    print(i)
else:
    print('For loop Finished!0'
          '')


