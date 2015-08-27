def get_encrypted_char(k, ascii_val, ascii_list, limit):
    diff = k % 26
    rotate_val = ascii_val + diff
    encrypted_char = ''
    if rotate_val not in ascii_list:
        rotate_val -= limit
        encrypted_char += chr(ascii_list[rotate_val-1])
    else:
        encrypted_char += chr(rotate_val)
    return encrypted_char

def encrypt(s, k):
    """
    Problem Statement

    Julius Caesar protected his confidential information from his enemies by
    encrypting it. Caesar rotated every letter in the string by a fixed number
    K. This made the string unreadable by the enemy. You are given a string S
    and the number K. Encrypt the string and print the encrypted string.

    For example:
    If the string is middle-Outz and K=2, the encoded string is okffng-Qwvb.
    Note that only the letters are encrypted while symbols like - are
    untouched.

    'm' becomes 'o' when letters are rotated twice,
    'i' becomes 'k',
    '-' remains the same because only letters are encoded,
    'z' becomes 'b' when rotated twice.

    Input Format
        Input consists of an integer N equal to the length of the string,
        followed by the string S and an integer K.

    Constraints
        1?N?100
        0?K?100
        S is a valid ASCII string and doesn't contain any spaces.

    Output Format
        For each test case, print the encoded string.

    Sample Input
        11
        middle-Outz
        2
    Sample Output
        okffng-Qwvb

    a-z : 97-122
    A-Z : 65-90
    :param s: string to be encrypted
    :param k: Integer, by which each character is rotated
    :return: Encrypted string
    """
    lower_ascii_list = [i for i in range(97, 123)]
    upper_ascii_list = [i for i in range(65, 91)]
    encrypted_string = str()
    for c in s:
        ascii_val = ord(c)
        if ascii_val in lower_ascii_list or ascii_val in upper_ascii_list:
            limit = 122
            ascii_list = lower_ascii_list
            if ascii_val in upper_ascii_list:
                limit = 90
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