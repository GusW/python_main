numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

doubled_list = []
for x in numbers_list:
    doubled_list.append(x * 2)

print(doubled_list)


# deepcode ignore useCompehensions: <please specify a reason of ignoring this>
doubled_list_functional = list(map(lambda x: x * 2, numbers_list))
print(doubled_list_functional)
