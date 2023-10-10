number_one = int(input("Please enter numer one: "))
number_two = int(input("Please enter number two: "))
symbol = input("Please enter mathematical symbol: ")
if symbol == "+":
    print(number_one+number_two)
elif symbol == "-":
    print(number_one-number_two)
elif symbol == "*":
    print(number_one*number_two)
elif symbol == "/":
    print(number_one/number_two)
else:
    print(f"We do not support this symbol {symbol}")