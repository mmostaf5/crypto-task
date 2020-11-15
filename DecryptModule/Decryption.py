import abc


class DecryptionInterface(metaclass=abc.ABCMeta):
    """
    decryption Interface class. All other decryption algorithms should be inherited from this interface
    and implement the decrypt method
    """

    def __init__(self):
        """
        Constructor of decryption Interface.
        """
        self.name = ''  # name of current algorithm to be used in cmd tool

    @abc.abstractmethod
    def decrypt(self, string_to_be_decrypted):
        """
         applies the required decryption for the given string and returns the decrypted string
        :param string_to_be_decrypted: the input string to apply the decryption method on it
        :return: a decrypted string
        """
        pass
