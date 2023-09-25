workedHours = int(input("Enter the total worked hours:\n"))
rate = int(input("Enter the rate per hour:\n"))
salary = 0
if (workedHours > 40):
    salary = 40*rate
    workedHours -= 40
    rate = rate*1.5
    salary += rate*workedHours
else:
    salary = rate*workedHours
print("The gross pay is", int(salary))
