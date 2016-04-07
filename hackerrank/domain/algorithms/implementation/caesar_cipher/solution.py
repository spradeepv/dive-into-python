def get_encrypted_char(k, ascii_val, ascii_list, limit):
    diff = k % 26
    rotate_val = ascii_val + diff
    encrypted_char = ''
    if rotate_val not in ascii_list:
        rotate_val -= limit
        for i in ascii_list:
            rotate_val -= 1
            if rotate_val == 0:
                encrypted_char += chr(i)
    else:
        encrypted_char += chr(rotate_val)
    return encrypted_char

def encrypt(s, k):
    """

    a-z : 97-122
    A-Z : 65-90
    :param s: string to be encrypted
    :param k: Integer, by which each character is rotated
    :return: Encrypted string
    """
    lower_ascii_list = [i for i in range(97, 123)]
    upper_ascii_list = [i for i in range(65, 91)]
    lower_case_limit = 122
    upper_case_limit = 90
    encrypted_string = str()
    for c in s:
        ascii_val = ord(c)
        if ascii_val in lower_ascii_list or ascii_val in upper_ascii_list:
            limit = lower_case_limit
            ascii_list = lower_ascii_list
            if ascii_val in upper_ascii_list:
                limit = upper_case_limit
                ascii_list = upper_ascii_list
            encrypted_string += get_encrypted_char(k, ascii_val, ascii_list,
                                                   limit)
        else:
            encrypted_string += c
    return encrypted_string


l = raw_input()
s = raw_input()
k = int(raw_input())
print encrypt(s, k)