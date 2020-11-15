from .Decryption import DecryptionInterface


class MatrixDecryption(DecryptionInterface):
    """
    Class inherits from Decryption interface and implements the matrix decryption algorithm
    """

    def __init__(self, decryption_matrix):
        """
        Constructor of MatrixEncryption class
        :param decryption_matrix: a 16x16 matrix to be used at decrypting characters
        """
        super().__init__()
        self.name = 'Matrix Decryption'  # name of current algorithm to be used in cmd tool
        self.decryption_matrix = decryption_matrix

    def decrypt(self, matrix_to_be_decrypted):
        """
            applies the matrix decryption algorithm for the given matrix and returns the decrypted string.
            :param matrix_to_be_decrypted: a matrix of size num_of_chars*16 represents the encrypted phrase
            :return: the decrypted string of the given matrix
            """
        decrypted_str = ''
        for encoded_vec in matrix_to_be_decrypted:  # loop over each row of the matrix and get the original character
            decrypted_vec = self.__vecMatMultiplication(encoded_vec)
            decrypted_str += self.__binaryToChar_16(decrypted_vec)
        return decrypted_str

    def __binaryToChar_16(self, bin_vec):
        """
        convert the given binary representation(of 16 bits) of its ASCII code to its original character
        :param bin_vec: binary vector to be converted to a meaningful character
        :return: a character
        """
        char_code = int(''.join([str(bit) for bit in bin_vec]), 2)
        return chr(char_code)

    def __vecMatMultiplication(self, encrypted_vec):
        """
        Multiply the given vector of binary representation by the encryption matrix.
        for the given implementation we add a padding of 8 zeros at the binary vector to keep its length at 16 so
        we skip the first 8 elements of the bin_vec
        :param encrypted_vec: a vector of length 16 represents the binary encoding of a character
        :return: a vector of length 16 represents the result of the multiplication rounded to nearest 0 or 1
        """
        res = [0.0] * len(encrypted_vec)
        for j in range(len(self.decryption_matrix[0])):
            for k in range(len(
                    encrypted_vec)):
                res[j] += encrypted_vec[k] * self.decryption_matrix[k][j]
            res[j] = round(res[j])
        return res
