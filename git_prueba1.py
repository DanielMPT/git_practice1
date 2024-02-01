dic = [1,2,3,4,5,6,7,8,9]

squared = [i**2 for i in dic if i % 2 == 0]  # 


# Multiplication

one_to_ten = [x for x in range(1, 11)]

multiplication = [x * y for x, y in zip(squared, one_to_ten)]
print(multiplication)