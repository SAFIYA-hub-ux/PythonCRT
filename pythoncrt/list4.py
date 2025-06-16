b=int(input())
h=int(input())
area=0.5*b*h
print(f"{area:.2f}")


List = [1, None, "safi", None, "vasu"]
count = List.count(None)
print("Count of None values:", count)      #count the no of null values

list = ["safiya","vasu","honey","madhu","1234567"]
n = 5

for i in list:
    if len(i) == n:
        print(i)

l = ["sadsfds", 20, 30, 40, 34]

if len(l) >= 2:
    l[0], l[-1] = l[-1], l[0]

print(l)

numbers = [16,324,45,1,12]

if len(numbers) == 0:
    print("The list is empty. Cannot calculate average.")
else:
    total = sum(numbers)
    avg = total / len(numbers)
    print("Average:", avg)

nums = [-4, 3, -2, 8, 7, -1, 10, 11]
neg_sum = 0
pos_even_sum = 0
pos_odd_sum = 0

for num in nums:
    if num < 0:
        neg_sum +=num
    elif num > 0 and num % 2 == 0:
        pos_even_sum += num
    elif num > 0 and num % 2 != 0:
        pos_odd_sum += num

print("Sum of Negative Numbers:", neg_sum)
print("Sum of Positive Even Numbers:", pos_even_sum)
print("Sum of Positive Odd Numbers:", pos_odd_sum)

numbers = [100, 50, 25, 10]
divisor = 5

if divisor == 0:
    print("it goes to infinity")
else:
    result = []
    for num in numbers:
        result.append(num / divisor)
    print("Divided list:", result)
