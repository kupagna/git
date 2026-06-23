def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for n in numbers[1:]:
        if n > largest:
            largest = n 

    return largest
