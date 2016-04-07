import math

class Encryption(object):
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


