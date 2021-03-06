from .Encryption import EncryptionInterface


class ShiftEncryption(EncryptionInterface):
    """Class inherits from Encryption class and implements the shift encryption algorithm"""

    def __init__(self, shift_cnt=3):
        """
        Constructor of ShiftEncryption algorithm.
        :param shift_cnt: the count of characters to be applied in the shift for encrypting the input string
        """
        super().__init__()
        self.name = 'Shift'  # name of current algorithm to be used in cmd tool
        self.shift_cnt = shift_cnt
        self.lower_chars = 'abcdefghijklmnopqrstuvwxyz'  # acts as a local array for lower case letters
        self.upper_chars = self.lower_chars.upper()  # acts as a local array for upper case letters
        self.numbers='0123456789'

    def encrypt(self, string_to_be_encrypted):
        """
        applies the shift encryption algorithm for the given string by shift_cnt and returns the encrypted string
        :param string_to_be_encrypted: the input string to apply the shift encryption method on it
        :return: an encrypted string
        """
        encrypted_str = ''
        for character in string_to_be_encrypted:
            if character in self.lower_chars:
                encrypted_str += self.lower_chars[
                    (self.lower_chars.find(character) + self.shift_cnt) % len(self.lower_chars)]
            elif character in self.upper_chars:
                encrypted_str += self.upper_chars[
                    (self.upper_chars.find(character) + self.shift_cnt) % len(self.upper_chars)]
            elif character in self.numbers:
                encrypted_str += self.numbers[
                    (self.numbers.find(character) + self.shift_cnt) % len(self.numbers)]
            else:
                encrypted_str += character
        return encrypted_str
