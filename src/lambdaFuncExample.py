#keyword lambda parameter body
#all in one line
lambda num: num ** 2

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def transform_list(num_list, transform_itemFumc):
    a = transform_itemFumc(num_list[0])
    b = transform_itemFumc(num_list[1])
    return [a, b]

my_list = [2, 3]
ans = transform_list(my_list, square)
#print(ans)

#same as
transform_list(my_list, lambda num: num ** 2)
#print(ans)

#map is a higher order function
ans = list(map(lambda num:num**3, my_list))
#print(ans)

#filtering out odd number
ans = list(filter(lambda num: num % 2 == 0, my_list))
print(ans)