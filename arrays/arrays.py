
numbers = [10,20,30,40,50]

# ramdom indexing --> O(1) get items if we know the index !!! 
print(numbers[0])
print(numbers[4])

numbers[1] = 200.3
numbers[2] = 'Adam'

print(numbers[1])

for num in numbers:
    print(num)
    
for i in range(len(numbers)):
    print(numbers[i])

print(numbers[0:2])
print(numbers[:-1])
print(numbers[:-2])

numbers2 = [10,20,30,40,50]

# O(n) search running time
maximum = numbers[0]

for num in numbers2:
    if num > maximum:
        maximum = num
        
print(maximum)