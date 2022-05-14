from stack import Stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
stack = Stack()

# Your solution here.

for char in string:
    stack.push(char)

while not stack.is_empty():
    reversed_string += stack.pop()

print(reversed_string)

string_to_list = list(string)
start_idx = 0
end_idx = len(string_to_list) - 1
while start_idx < end_idx:
    string_to_list[start_idx], string_to_list[end_idx] = string_to_list[end_idx], string_to_list[start_idx]
    start_idx += 1
    end_idx -= 1

print(''.join(string_to_list))
