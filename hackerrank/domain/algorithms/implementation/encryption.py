import math

class Encryption(object):
    """
    Problem Statement
        An English text needs to be encrypted using the following encryption
        scheme. First, the spaces are removed from the text. Let L be the
        length of this text. Then, characters are written into a grid, whose
        rows and columns have the following constraints:

        ?L?????rows?column??L????, where ?x? is floor function and ?x? is ceil
        function
        For example, the sentence 'if man was meant to stay on the ground god
        would have given us roots' after removing spaces is 54 characters long,
        so it is written in the form of a grid with 7 rows and 8 columns.

        ifmanwas
        meanttos
        tayonthe
        groundgo
        dwouldha
        vegivenu
        sroots

        Ensure that rows×columns?L
        If multiple grids satisfy the above conditions, choose the one with the
        minimum area, i.e. rows×columns. The encoded message is obtained by
        displaying the characters in a column, inserting a space, and then
        displaying the next column and inserting a space, and so on. For
        example, the encoded message for the above rectangle is:

        imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

        You will be given a message in English with no spaces between the
        words. The maximum message length can be 81 characters. Print the
        encoded message.

    Sample Input:
        haveaniceday

    Sample Output:
        hae and via ecy
    """
    def get_input(self):
        self.text = raw_input()

    def encrypt(self):
        text_len = len(self.text)
        square_root = math.sqrt(text_len)
        row = int(math.floor(square_root))
        col = int(math.ceil(square_root))
        while row * col < text_len:
            row += 1
        l = [['' for x in range(col)] for x in range(row)]
        index = 0
        for i in range(row):
            for j in range(col):
                if index >= text_len:
                    break
                l[i][j] = self.text[index]
                index += 1
        encrypted_text = ''
        for i in range(col):
            col_l = [row[i] for row in l]
            for j in col_l:
                if j != '':
                    encrypted_text += j
            encrypted_text += ' '
        return encrypted_text

encryption = Encryption()
encryption.get_input()
print encryption.encrypt()


