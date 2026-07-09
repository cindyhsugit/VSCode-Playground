# swap without a temp varialbe
a = "a"
b = "b"
a, b = b, a
print (a, b)

# List slicing
arr = ["apple", "banana", "cat"]
print(arr[1:3]) # elements at index 1,2
print(arr[::-1]) # reversed
print(arr[:3]) # first 3
print(arr[-1]) # last element
#arr[start:stop:step]

# Dictionary basics
d = {"1": "apple", "2": "banana"}
d["key"] = "value"
d.get("key", "default") 
# look for "key", return its value if found, otherwise return "default".

"key" in d #membership check

for key, value in d.items(): # iterate both
    print(key, value)

# List comprehension
# For each number from 0 through 9, multiply it by itself and put the result in a list.
squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numArray = [1, 2, 3, 4, 5]
evens = [x for x in numArray if x % 2 == 0]
print (evens)

# enumerate - get index + value together
for i, val in enumerate(numArray):
    print (i, val)

# String reversal
sampleStr = "abcdefghijklmnopqrstuvwxyz"
print(sampleStr[::-1])

# sets for fast lookup/dedup
# A set stores only unique items, no particular order
seen = set()
seen = {7, 3, 19}

#################
# “Given an array of integers and a target number, return the indices 
# of the two numbers that add up to the target.
# sampleInputArray = [5, 8, 12, 4]
# sampleTargetSum = 9

def find_two_sum(inputArray, targetSum):
    answerList = []
    # loop through the array with starting index at 1,
    # pair with index + 1 each time
    for i, val in enumerate(inputArray):
       print (f"loop {i} -----")
       print (val)
       for secondIndex, secondValue in enumerate(inputArray[i+1:]):
           print (f"-----loop {secondIndex} -----")
           print (secondValue)
           if checkTheSum(val, secondValue, targetSum):
            answerList.append(val)
            answerList.append(secondValue)
            print (f"found the pair {val} + {secondValue} = {targetSum}")
      
    return answerList

# helper function 
def checkTheSum(inputA, inputB, targetSum):
    flag = False
    if inputA + inputB == targetSum:
        flag = True
    return flag

sampleInputArray = [5, 8, 12, 4]
sampleTargetSum = 9
#print (find_two_sum(sampleInputArray, sampleTargetSum))

# range(10) = generate numbers.
# [:] = copy the whole list.

# dictionary O(n) way
def dic_check_two_sum(inputArray, targetSum):
    dictionary = {}
    for i, val in enumerate(inputArray):
        dictionary[i] = val
    print (dictionary)    
    # with every index in the array, find its leftover
    for ii, vall in enumerate(inputArray):
        for key, value in dictionary.items():
            if value == targetSum - vall:
                return [key, ii]
   
#print(dic_check_two_sum(sampleInputArray, sampleTargetSum))    


sampleInputArray = [5, 8, 12, 4]
sampleTargetSum = 9
def dic_check_two_sum_opt(inputArray, targetSum):
    seen = {}
    for i, val in enumerate(inputArray):
        leftover = targetSum - val
        print (f"leftover is: {leftover}")
        if leftover in seen:
            return [seen[leftover], i]
        seen[val] = i
        print (f"set is: {seen}")
    return None

#print(dic_check_two_sum_opt(sampleInputArray, sampleTargetSum))    


def dict_check_two_sum_version_two(inputArray, targetSum):
    onePass = {}
    answer = []
    for x, y in enumerate(inputArray):
        if targetSum-y in onePass :
            answer.append(x)
            answer.append(onePass[targetSum-y])
            return answer
        else:
            onePass[y] = x
    return answer    

#print(dict_check_two_sum_version_two(sampleInputArray, sampleTargetSum))    

def dict_check_two_sum_version_three(inputArray, sampleTargetSum):
    #create a swapped dict
    swappedDictionary = {}
   
    for a, b in enumerate(inputArray):
        if sampleTargetSum - b in swappedDictionary:
            return [swappedDictionary.get(inputArray - b), a]
        else:
            swappedDictionary[b] = a
    return []        

#print(dict_check_two_sum_version_three(sampleInputArray, sampleTargetSum))    

def dic_check_two_sum_version_four(inputArray, sampleTargetSum):
    answer = []
    partnerPool = {}
    for x, y in enumerate(inputArray):
        if sampleTargetSum - y in partnerPool:
            answer.append(x)
            answer.append(partnerPool.get(sampleTargetSum-y))
        else:
            partnerPool[y] = x
    return answer


#print(dic_check_two_sum_version_four(sampleInputArray, sampleTargetSum))    

import random
def shuffle_array_swapping(inputArray):
    for x, y in enumerate(inputArray):
        # generate swap number
        newSeat = random.randint(x, len(inputArray)-1)
        
        inputArray[x] = inputArray[newSeat]
        inputArray[newSeat] = y
        # inputArray[x], inputArray[newSeat] = inputArray[newSeat], inputArray[x]
    
    return inputArray

#print(shuffle_array_swapping(sampleInputArray))

# FIZZBUZZ
# return a list of strings from 1 to 
# 𝑛
# n, but replace certain numbers based on divisibility rules. 
# The rules are: use "FizzBuzz" for numbers divisible by both 3 and 5, 
# "Fizz" for divisible by 3, "Buzz" for divisible by 5, and the 
# number itself as a string otherwise.
def fizz_buzz_array(n:int):
    answerList=[]
    for x in range(n):
        if x % 3 == 0:
            #FIZZ word
            answerList.append("FIZZ")
        elif x % 5 == 0:
            #BUZZ word
            answerList.append("BUZZ")
        elif x % 3 == 0 and x % 5 == 0:
            #FIZBUZZ
            answerList.append("FIZZBUZZ")
        else:
            answerList.append(str(x))
        
    return answerList

#print(fizz_buzz_array(15))

# valid anagram
# check to see if 2 strings are anagram using
# a dict or counter
# true if they are same count and used same letters
# false otherwise
def check_two_strings_anagram(sampleStringA, sampleStringB):
    is_anagram = False
    #my psuedo code
    # put input string to a dict 
    # store each letter and its count/appearance
    # compare both
    # convert string into array
    
    dictA = {}
    dictB = {}
    for letter in sampleStringA:
        if letter in dictA:
            dictA[letter] = dictA.get(letter, 0) + 1
        else:
            dictA[letter] = 1

    for letter in sampleStringB:
        if letter in dictB:
            dictB[letter] = dictB.get(letter, 0) + 1
        else:
            dictB[letter] = 1

    if dictA == dictB:
        is_anagram = True
    return is_anagram

# print(check_two_strings_anagram("rat","art"))
# print(check_two_strings_anagram("rat","car"))

def check_for_duplicates(sampleInputArray):
    newSet = set()
    for x in sampleInputArray:
        if x in newSet:
            return True
        else:
            newSet.add(x)
    return False

# print(check_for_duplicates([1,2,3,4]))
# print(check_for_duplicates([1,2,3,1]))

def is_out_of_bound(arrayToCheck, position):
    if position >= len(arrayToCheck) or position < 0:
        return True
    return False

def merge_two_sorted_arrays(sortedArray1, sortedArray2):
    mergedArray = []
    pointerA = 0
    pointerB = 0
    mergedArraySize = len(sortedArray1)+len(sortedArray2)
    for x in range(mergedArraySize+1):
        if (is_out_of_bound(sortedArray1, pointerA) == False
            and
            is_out_of_bound(sortedArray2, pointerB) == False
            and
            sortedArray1[pointerA] < sortedArray2[pointerB] 
            ):
            mergedArray.append(sortedArray1[pointerA])
            pointerA+=1
        elif is_out_of_bound(sortedArray1, pointerA) == True:
            mergedArray.extend(sortedArray2[pointerB:])
            return mergedArray
        elif is_out_of_bound(sortedArray2, pointerB) == True:
            mergedArray.extend(sortedArray1[pointerA:])
            return mergedArray
        else:
            mergedArray.append(sortedArray2[pointerB])
            pointerB+=1


    return mergedArray
    
print(merge_two_sorted_arrays([1, 3, 5], [2, 4, 6]))
print(merge_two_sorted_arrays([1, 2, 7], [3, 4, 5, 6]))
print(merge_two_sorted_arrays([], [1, 2, 3]))
print(merge_two_sorted_arrays([1,2,3], [3]))


def merge_two_sorted_arrays_version2(sortedArray1, sortedArray2):
    mergedArray = []
    pointerA = 0
    pointerB = 0
    while (is_out_of_bound(sortedArray1, pointerA) == False 
    and 
    is_out_of_bound(sortedArray2, pointerB) == False):
        if sortedArray1[pointerA] < sortedArray2[pointerB]:
            mergedArray.append(sortedArray1[pointerA])
            pointerA+=1
        else:    
            mergedArray.append(sortedArray2[pointerB])
            pointerB+=1

    if is_out_of_bound(sortedArray1, pointerA) == True:
        mergedArray.extend(sortedArray2[pointerB:])
    if is_out_of_bound(sortedArray2, pointerB) == True:
        mergedArray.extend(sortedArray1[pointerA:])
        
    return mergedArray


















