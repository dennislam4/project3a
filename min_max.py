# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 6/26/2022
# Description: Asks user to input how many integers they would like and then after all numbers have been entered,
#              the program prints out the min and max values

value = int(input("How many integers would you like to enter?"))
print("Please enter", value, "integers.")
minimum = int(input())
maximum = minimum
for i in range(1, value):
    num = int(input())
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("min:", minimum)
print("max:", maximum)
