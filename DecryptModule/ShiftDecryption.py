from .Decryption import DecryptionInterface


class ShiftDecryption(DecryptionInterface):
    """Class inherits from Decryption interface and implements the shift decryption algorithm"""
    
    def __init__(self, shift_cnt=3):
        """
        Constructor of ShiftDecryption algorithm.
        :param shift_cnt: the count of characters to be applied in the shift for decrypting the input string
        """
        self.name = 'Shift Decryption'
        self.shift_cnt = shift_cnt
        self.lower_chars = 'abcdefghijklmnopqrstuvwxyz'  # acts as a local array for lower case letters
        self.upper_chars = self.lower_chars.upper()  # acts as a local array for upper case letters

    def decrypt(self, string_to_be_decrypted):
        """
        applies the shift decryption algorithm for the given string by shift_cnt and returns the decrypted string
        :param string_to_be_decrypted: the input string to apply the shift decryption method on it
        :return: a decrypted string
        """
        decrypted_str = ''
        for character in string_to_be_decrypted:
            if character in self.lower_chars:
                decrypted_str += self.lower_chars[
                    (self.lower_chars.find(character) - self.shift_cnt) % len(self.lower_chars)]
            elif character in self.upper_chars:
                decrypted_str += self.upper_chars[
                    (self.upper_chars.find(character) - self.shift_cnt) % len(self.upper_chars)]
            else:
                decrypted_str += character
        return decrypted_str
