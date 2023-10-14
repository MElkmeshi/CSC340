number = int(input("Enter number: "))
divisors = []
for i in range(2, number-1, 1):
    if number % i == 0:
        divisors.append(i)
print("The divisors are", str(divisors).replace("[", "").replace("]", ""))
