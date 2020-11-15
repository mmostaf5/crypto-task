# Encryption and Decryption algorithms
this repo has an implementation of 3 Encryption methdos and thier decryption methods:
  1-Shift Algorithm:
    works on letters and numbers, the idea of it is to shift each letter of the string by 3 characters or numbers.
    For Example: 'ABC123' would result in an encrypted string 'DEF456'
  2-Matrix Algorithm:
    works on the binary representation of each character of the given string, it works by multiply the binary representaion by a matrix so it should result in a sequence of float numbers.
# How to use:
download the code and run 'python3 main.py str_to_be_processed -M algorithm_name[Shift,Matrix] Encrypt/Decrypt'.

for example to run shift algorithm on 'hello world!' -> 'python3 main.py hello world! -M Shift Encrypt'
and to decrypt the result 'python3 main.py khoor zruog! -M Shift Decrypt'.
# important note:
  the code runs with python 3.x.
  
  '-M' flag is very important for parsing the arguments.
  
  If any wrong argument is passed the system will stop and raise 'invalid input' error.

