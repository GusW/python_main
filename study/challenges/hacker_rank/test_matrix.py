import re
from collections import deque


def _extract_multiple_inputs(multiple_inputs):
    rows = int(multiple_inputs[0])
    assert(isinstance(rows, int)), 'N should bean integer received {}'.type(rows)
    columns = int(multiple_inputs[1])
    assert(isinstance(columns, int)), 'M should bean integer received {}'.type(columns)
    return rows, columns


def _check_input_boundaries(rows, columns):
    assert(0 < rows < 100), 'N should be in between 0 and 100: got f{rows}'
    assert(0 < columns < 100), 'M should be in between 0 and 100: got f{columns}'


def _decode_matrix(received_input, columns):
    matrix = deque()
    for c in range(columns):
        matrix.append(received_input[c:][::columns])

    return list(matrix)


def _transform_decoded_input(decoded_input):
    replacement_list = re.findall('[0-9a-zA-Z]{1}[^0-9a-zA-Z]{2}[0-9a-zA-Z]{1}', decoded_input)
    for item in replacement_list:
        decoded_input = decoded_input.replace(item, item[0] + " " + item[-1])

    return(decoded_input)


def decode_matrix(received_matrix):
    received_matrix_as_str = ''.join(received_matrix)
    decoded_matrix = ''.join(_decode_matrix(received_matrix_as_str, columns))
    print(_transform_decoded_input(decoded_matrix))


rows, columns = _extract_multiple_inputs(input().rstrip().split())
_check_input_boundaries(rows, columns)
received_matrix = deque()
for _ in range(rows):
    received_matrix.append(input())

decode_matrix(list(received_matrix))
