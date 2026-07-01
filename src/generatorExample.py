#regular prime number finder return a list
def get_primes_list(start, end):
    primes = []
    for num in range(start, end+1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
                primes.append(num)

    return primes

#print(get_primes_list(50, 60))


#generate one at a time
# use less memory since it spits one at a time
def gen_primes(start, end):
     for num in range(start, end + 1):
          if num < 2:
               continue
          is_prime = True
          for i in range(2, num):
               if num % i == 0:
                is_prime = False
                break
          if is_prime:
            yield num

oneVar = gen_primes(50, 60)
# print(next(oneVar))
# print(next(oneVar))

for value in gen_primes(50, 60):
    if value % 10 == 7:
        print (value)
        break