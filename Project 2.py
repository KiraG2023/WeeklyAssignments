fileName = input ("enter the filename:")
f = open (fileName, 'Project 1 median.py')
#input the text, convert it to number and
#add the numbers to a list
numbers = []
for line in f:
    words =line.split()
    for word in words : numbers.append(float(word))
    numbers.sort()
midpoint= len(numbers) // 2
print("the median is ", end = " ")
if len(numbers) % 2 ==1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint]+ numbers[midpoint - 1])/ 2)

