fruits = ['apple', 'banana', 'apple', 'mango', 'banana', 'apple']
dic = {}

for fruit in fruits:
    if fruit in dic:
        dic[fruit] += 1
    else:
        dic[fruit] = 1
        
print(dic)
