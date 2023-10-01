# Q1
def isPerfect(num:int):
    sum = 0
    for i in range(1,num):
        if(num%i == 0):
            sum+=i
    return sum == num 

print(isPerfect(6))
# Q2
def Q2():
    separator = input("Please enter the separator: ")
    sequence = input("Please enter the sequence: ")
    words = sequence.split(sep=separator)
    words.sort()
    print(words)
Q2()
# Q3
def Q3(arr:list):
    arr2 = []
    for num in arr:
        if num not in arr2:
            arr2.append(num)
    return arr2
print(Q3([1,2,3,4,2,4,3,3,5,7,3,2,1]))
# Q4
def Q4(list:list,sublist:list):
    for num in sublist:
        if num not in list:
            return False
    return True

print(Q4( [12,5,6,11,21,13], [1,5,6]))
def Q5(tuples:list):
    list = [0] * len(tuples[0])
    for i in range(len(list)):
        for j in range(len(tuples)):
            list[i] +=tuples[j][i]
    return tuple(list)

print(Q5([(1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1)]))
# Q6
def Q6(tuples:list):
    newlist = []
    for tuple in tuples:
        newlist.append(list(tuple))
    return newlist

print(Q6([(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]))

# Q7
def Q7(map:dict):
    print("Max key is",max(map))
    print("Min key is",min(map))
# Q7({"Name":"Mohamed Elkmeshi","ID":"2021/08926","Age":20})
# Q8
def Q8(map:dict):
    return dict(sorted(map.items()))
print(Q8({"Name":"Mohamed Elkmeshi","ID":"2021/08926","Age":20}))
# Q9
def Q9(dictt:dict):
    min_value = len(dictt[next(iter(dictt))])
    for value in dictt:
        if len(dictt[value]) < min_value:
            min_value = len(dictt[value])
    result =[]
    for k,v in dictt.items():
        if len(v) == (min_value):
            result.append(k)
    return result    


print(Q9( {
 'V': [10, 12],
 'VI': [10, 12],
 'VII': [10, 20, 30, 40],
 'VIII': [20,3],
 'IX': [10,30,50,70],
 'X': [80]
 }))