import sys

from EncryptionModule.ShiftEncryption import ShiftEncryption
from EncryptionModule.MatrixEncryption import MatrixEncryption
from EncryptionModule import Config
from DecryptModule.ShiftDecryption import ShiftDecryption
from DecryptModule.MatrixDecryption import MatrixDecryption


def convert_matrix_to_string(mat):
    res = ''
    for row in mat:
        res += ','.join([str(elm) for elm in row])
        res += ','
    return res[:-1]


def convert_string_to_matrix(string):
    res = []
    elms = string.split(',')
    for i in range(len(elms)):
        if i % 16 == 0:
            res.append([])
        res[-1].append(float(elms[i]))
    return res  # [[float(elm) for elm in string.split(',')[i*16 :(i +1)* 16]] for i in range(len(string) // 16)]


def main():
    shift_encryption_obj = ShiftEncryption(shift_cnt=Config.ShiftEncryptionConfig["shift_cnt"])
    matrix_encryption_obj = MatrixEncryption(encryption_matrix=Config.MatrixEncyrptionConfig["encryption_matrix"])
    # Dictionary mapping each module with its name for ease of accessing modules
    encryption_modules = {
        shift_encryption_obj.name: shift_encryption_obj,
        matrix_encryption_obj.name: matrix_encryption_obj}

    shift_decryption_obj = ShiftDecryption(shift_cnt=Config.ShiftEncryptionConfig["shift_cnt"])
    matrix_decryption_obj = MatrixDecryption(decryption_matrix=Config.MatrixDecryptionConfig["decryption_matrix"])
    # Dictionary mapping each module with its name for ease of accessing modules
    decryption_modules = {
        shift_decryption_obj.name: shift_decryption_obj,
        matrix_decryption_obj.name: matrix_decryption_obj
    }
    args = sys.argv[1:]
    try:
        end_str_idx = len(args) - args[::-1].index('-M') - 1  # get the last occurrence of -M flag
        str_to_be_processed = ' '.join(args[:end_str_idx])
        algorithm_name = args[end_str_idx + 1]
        method = args[end_str_idx + 2]
        if method.lower().strip() == 'encrypt':
            res = encryption_modules[algorithm_name].encrypt(str_to_be_processed)
            if algorithm_name.lower().strip() == matrix_encryption_obj.name.lower().strip():
                res = convert_matrix_to_string(res)
        elif method.lower().strip() == 'decrypt':
            if algorithm_name.lower().strip() == matrix_decryption_obj.name.lower().strip():
                matrix_to_be_decrypted = convert_string_to_matrix(str_to_be_processed)
                res = decryption_modules[algorithm_name].decrypt(matrix_to_be_decrypted)
            else:
                res = decryption_modules[algorithm_name].decrypt(str_to_be_processed)
        else:
            raise
        print(res)
    except:
        print('invalid input!')



main()
