print("Number of symbols: ")
num = int(input())

appearances = []
symbol = []

for i in range(num):
    print("Repeated times: ")
    appearances.append(int(input()))
    print("Symbol: ")
    symbol.append(input())

for index in range(len(symbol)):
    print("OUTPUT:")
    print(appearances[index]*symbol[index])