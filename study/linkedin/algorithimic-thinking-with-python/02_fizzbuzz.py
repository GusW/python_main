for i in range(1, 101):
    exp = ""
    if i % 3 == 0:
        exp += "fizz"
    if i % 5 == 0:
        exp += "buzz"

    print(f"{i} => {exp}")
