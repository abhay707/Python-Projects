def generate_fibonacci(x):
    if x <= 1:
        return []

    fibonacci_series = [0, 1]

    while True:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        if next_number >= x:
            break
        fibonacci_series.append(next_number)

    return fibonacci_series


def calculate_sum_of_even_indexed_numbers(numbers):
    even_numbers = [number for index, number in enumerate(numbers) if index % 2 == 0]
    return sum(even_numbers)


# Input
x = int(input("Enter an integer (x): "))

if x < 2:
    print("Invalid input. Please enter a number greater than or equal to 2.")
else:
    fibonacci_series = generate_fibonacci(x)
    sum_of_even_numbers = calculate_sum_of_even_indexed_numbers(fibonacci_series)

    for i in range(fibonacci_series[]):
        print(i)
    print("Sum of even-indexed numbers:", sum_of_even_numbers)
