dic = [1,2,3,4,5,6,7,8,9]

squared = [i**2 for i in dic if i % 2 == 0]  # 
 
print(squared)

sum = [x + 5 for x in squared]

print(sum)
