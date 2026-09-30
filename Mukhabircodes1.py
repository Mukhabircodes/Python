#lists 
names = ['John', 'Bob', 'Mosh', 'Sarah ', 'Mary']
names[0] = 'Jon'
print(names[2:])
print(names[2:-1])
print(names)

#A program to find the largest number in a list 
numbers = [3, 6, 2, 10, 9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number 
print(max)
      
      
