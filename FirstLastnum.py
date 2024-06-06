c = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

input_str = input('Donner Input \n')

first_num = None
last_num = None

for char in input_str:
    if char in c:
        first_num = char
        break

for char in reversed(input_str):
    if char in c:
        last_num = char
        break

if first_num is not None and last_num is not None:
    result = first_num + last_num
    print("Concatenated number:", result)
else:
    print("No numeric characters found in the input.")