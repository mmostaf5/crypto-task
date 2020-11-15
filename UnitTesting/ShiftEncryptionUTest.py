from EncryptionModule.ShiftEncryption import ShiftEncryption
import unittest


class TestShiftEncryption(unittest.TestCase):
    __shift_encryption_obj = ShiftEncryption()

    def test_single_char_lower(self):
        lower_chars = 'abcdefghijklmnopqrstuvwxyz'
        lower_chars_encrypted = 'defghijklmnopqrstuvwxyzabc'
        for idx, character in enumerate(lower_chars):
            self.assertEqual(self.__shift_encryption_obj.encrypt(character),
                             lower_chars_encrypted[idx],
                             msg='Failed in TestShiftEncryption.test_single_char_lower')

    def test_single_char_upper(self):
        upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        upper_chars_encrypted = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
        for idx, character in enumerate(upper_chars):
            self.assertEqual(self.__shift_encryption_obj.encrypt(character),
                             upper_chars_encrypted[idx],
                             msg='Failed in TestShiftEncryption.test_single_char_upper')

    def test_phrase(self):
        input_str = 'Hello World!'
        expected_str = 'Khoor Zruog!'
        self.assertEqual(self.__shift_encryption_obj.encrypt(input_str),
                         expected_str,
                         msg='Failed in TestShiftEncryption.test_phrase')


if __name__ == '__main__':
    unittest.main()
