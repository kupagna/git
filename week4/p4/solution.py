numbers = [5,7,2,5,9,6,0]
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Duplicates:",list(duplicates))
