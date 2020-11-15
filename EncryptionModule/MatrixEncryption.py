from .Encryption import EncryptionInterface
import binascii


class MatrixEncryption(EncryptionInterface):
    """
    Class inherits from Encryption class and implements the matrix encryption algorithm
    """

    def __init__(self, encryption_matrix):
        """
        Constructor of MatrixEncryption class
        :param encryption_matrix: a 16x16 matrix to be used at encrypting characters
        """
        super().__init__()
        self.name = 'Matrix Encryption'  # name of current algorithm to be used in cmd tool
        self.encryption_matrix = encryption_matrix

    def encrypt(self, string_to_be_encrypted):
        """
            applies the shift encryption algorithm for the given string and returns the encrypted string
            :param string_to_be_encrypted: the input string to apply the shift encryption method on it
            :return: the result of encryption as an array of size length_of(string_to_be_encrypted)*16
            """
        encrypted_res = []
        for character in string_to_be_encrypted:
            bin_vec = self.__charToBinary_16(character)
            encrypted_res.append(self.__binMultiplication(bin_vec))
        return encrypted_res

    def __charToBinary_16(self, character):
        """
        convert the given character to a binary representation(of 16 bits) of its ASCII code,
        each character will be represented by max 8 bits but we add a padding of zeros to keep the length of 16
        :param character: character to be converted to binary code
        :return: a vector of length 16 represents the binary encoding of the given character
        """
        bin_str = bin(int(binascii.hexlify(character.encode()), 16)) \
            .replace('b', '')
        bin_vec = [0.0] * (16 - len(bin_str)) + [float(c) for c in bin_str]
        return bin_vec

    def __binMultiplication(self, bin_vec):
        """
        Multiply the given vector of binary representation by the encryption matrix.
        for the given implementation we add a padding of 8 zeros at the binary vector to keep its length at 16 so
        we skip the first 8 elements of the bin_vec
        :param bin_vec: a vector of length 16 represents the binary encoding of a character
        :return: a vector of length 16 represents the result of the multiplication
        """
        res = [0.0] * len(bin_vec)
        for j in range(len(self.encryption_matrix[0])):
            for k in range(8, len(
                    bin_vec)):  # because of padding of at least 8 zeros, we will skip first 8 elements because they
                # won't add a value
                res[j] += bin_vec[k] * self.encryption_matrix[k][j]
        return res
