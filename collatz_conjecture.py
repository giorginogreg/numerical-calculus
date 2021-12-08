def collatz_conj(x0, n):
    if(not isinstance(x0, int) or x0 < 0):
        print("Number inserted is not an integer | is less than zero")
        return

    result = []
    first_1_position = -1
    result.append(x0)
    for i in range(1, n):
        new_value = result[i - 1] / 2 if result[i -
                                                1] % 2 == 0 else 3 * result[i - 1] + 1
        result.append(new_value)
        if new_value == 1:
            first_1_position = i
    return result, first_1_position
