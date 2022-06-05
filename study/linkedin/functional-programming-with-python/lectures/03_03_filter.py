numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = []
for x in numbers_list:
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)


# deepcode ignore useCompehensions: <please specify a reason of ignoring this>
even_numbers_functional = list(filter(lambda x: x % 2 == 0, numbers_list))
print(even_numbers_functional)
