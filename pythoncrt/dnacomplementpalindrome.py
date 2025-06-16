dna = input("Enter the dna sequence:").upper()

# Create full mapping manually
complement = ""
for base in dna:
    if base == 'A':
        complement += 'T'
    elif base == 'T':
        complement += 'A'
    elif base == 'G':
        complement += 'C'
    elif base == 'C':
        complement += 'G'
    else:
        complement += base  # or raise error for invalid base

print("Complement:", complement)
v=complement[::-1]
print("Reverse complement:",v)
# Check if the complement is a palindrome
if dna ==v:
    print("True")
else:
    print("False")


