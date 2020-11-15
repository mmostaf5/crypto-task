import abc


class EncryptionInterface(metaclass=abc.ABCMeta):
    """
    Encryption Interface class. All other encryption algorithms should be inherited from this interface
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
        :param string_to_be_encrypted: the input string to apply the encryption method on it
        :return: an encrypted string
        """
        pass
