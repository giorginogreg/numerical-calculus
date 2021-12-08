def invert_string(string_to_invert):
    str_len = len(string_to_invert)
    inverted_str = ""
    if(str_len > 0):
        for i in range(1, str_len + 1):
            inverted_str += string_to_invert[str_len - i]

    return inverted_str
