# 2020 Q2
print('Enter P:')
P = int(input())
print('Enter N:')
N = int(input())
print('Enter R:')
R = int(input())

counter = 0
total = N
new_case = N
while total <= P:
    counter += 1
    new_case = new_case*R
    total += new_case
print("Day: ", counter)
print("Total: ", total)