class MatrixRotation(object):
    """
    Problem Statement

        You are given a 2D matrix, a, of dimension MxN and a positive integer R.
        You have to rotate the matrix R times and print the resultant matrix.
        Rotation should be in anti-clockwise direction.

        Rotation of a 4x5 matrix is represented by the following figure.
        Note that in one rotation, you have to shift elements by one step only.

        It is guaranteed that the minimum of M and N will be even.

    Input
        First line contains three space separated integers, M, N and R, where M
        is the number of rows, N is number of columns in matrix, and R is the
        number of times the matrix has to be rotated.
        Then M lines follow, where each line contains N space separated
        positive integers. These M lines represent the matrix.

    Output
        Print the rotated matrix.

    Constraints
        2 <= M, N <= 300
        1 <= R <= 109
        min(M, N) % 2 == 0
        1 <= aij <= 108, where i ? [1..M] & j ? [1..N]

    Sample Input #00
        4 4 1
        1 2 3 4
        5 6 7 8
        9 10 11 12
        13 14 15 16

    Sample Output #00
        2 3 4 8
        1 7 11 12
        5 6 10 16
        9 13 14 15
    """
    def get_input(self):
        l = map(int, raw_input().split(' '))
        self.m, self.n, self.r = l[0], l[1], l[2]
        self.matrix = [[x for x in raw_input().split(' ')] for x in range(self.m)]

    def rotate(self):
        m_start = 0
        m_end = self.m - 1
        n_start = 0
        n_end = self.n - 1
        m_len = m_end - m_start
        n_len = n_end - n_start
        loop_decrement = 1

        while (m_len >= 1 and n_len >= 1):
            #loop_rotation = number of items in current loop
            loop_rotation = (self.n - loop_decrement) + \
                            (self.m - loop_decrement) + \
                            (self.n - loop_decrement) + \
                            (self.m - loop_decrement)
            print loop_rotation
            rot = self.r % loop_rotation
            for rotations in range(0, rot):
                loop_start = self.matrix[m_start][n_start]
                #top row
                m_curr = m_start
                n_curr = n_start
                for i in range(0, n_len):
                    self.matrix[m_curr][n_curr] = self.matrix[m_curr][n_curr + 1]
                    n_curr += 1
                #right col
                m_curr = m_start
                n_curr = n_end
                for i in range(0, m_len):
                    self.matrix[m_curr][n_curr] = self.matrix[m_curr + 1][n_curr]
                    m_curr += 1
                #bottom row
                m_curr = m_end
                n_curr = n_end
                for i in range(0, n_len):
                    self.matrix[m_curr][n_curr] = self.matrix[m_curr][n_curr - 1]
                    n_curr -= 1
                #left col
                m_curr = m_end
                n_curr = n_start
                for i in range(1, m_len+1):
                    if i < m_len:
                        self.matrix[m_curr][n_curr] = self.matrix[m_curr - 1][n_curr]
                        m_curr -= 1
                    else:
                        self.matrix[m_curr][n_curr] = loop_start
            m_start += 1
            m_end -= 1
            n_start += 1
            n_end -= 1

            m_len = m_end - m_start
            n_len = n_end - n_start

            loop_decrement += 2
        for i in range(self.m):
            print " ".join(self.matrix[i])

matrix_rotation = MatrixRotation()
matrix_rotation.get_input()
matrix_rotation.rotate()
