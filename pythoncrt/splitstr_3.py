# read str as input from the user and split the string into 3 equal halfs
input_string = input("Enter a string: ")
string_length = len(input_string)
if string_length % 3 == 0:
  part_length = string_length // 3

  part1 = input_string[0:part_length]
  part2 = input_string[part_length:2*part_length]
  part3 = input_string[2*part_length:string_length]

  print("First part:", part1)
  print("Second part:", part2)
  print("Third part:", part3)

else:
  print("The string cannot be split into 3 equal halves.")
  print("String length:", string_length)