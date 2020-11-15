import abc


class EncryptionInterface(metaclass=abc.ABCMeta):
    """
    Encryption Interface class. All other encyption algorithms should be inherited from this interface
    and implement the encrypt method
    """

    def __init__(self):
        """
        Constructor of Encryption Interface.
        """
        self.name = ''  # name of current algorithm to be used in cmd tool

    @abc.abstractmethod
    def encrypt(self, string_to_be_encrypted):
        """
         applies the required encryption for the given string and returns the encrypted string
        :param string_to_be_encrypted: the input string to apply the shift encryption method on it
        :return: an encrypted string
        """
        pass


class ShiftEncryption(EncryptionInterface):
    """Class inherits from Encryption class and implements the shift encryption algorithm"""

    def __init__(self, shift_cnt=3):
        """Constructor of ShiftEncryption algorithm.
        It takes one argument:
        shift_cnt--> the count of characters to be applied in the shift for encrypting the coming string
        """
        super().__init__()
        self.name = 'Shift Algorithm'  # name of current algorithm to be used in cmd tool
        self.shift_cnt = shift_cnt
        self.lower_chars = 'abcdefghijklmnopqrstuvwxyz'  # acts as a local array for lower case letters
        self.upper_chars = self.lower_chars.upper()  # acts as a local array for upper case letters

    def encrypt(self, string_to_be_encrypted):
        """
        applies the shift encryption algorithm for the given string and returns the encrypted string
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
            else:
                encrypted_str += character
        return encrypted_str
