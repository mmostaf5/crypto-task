# Encryption and Decryption algorithms
this repo has an implementation of 3 Encryption methdos and thier decryption methods:
  1-Shift Algorithm:
    works on letters and numbers, the idea of it is to shift each letter of the string by 3 characters or numbers.
    For Example: 'ABC123' would result in an encrypted string 'DEF456'
  2-Matrix Algorithm:
    works on the binary representation of each character of the given string, it works by multiply the binary representaion by a matrix so it should result in a sequence of float numbers.
  3-Reverse Algorithm:
	reverse the given string.
# Repo Structure:
DecryptModule: contains the implementation of required decryption algorithms.

	|_ Decrypt.py: contains the decryption interface class

	|_ MatrixDecryption.py: implementation for matrix decryption algorithm

	|_ ReverseDecryption.Py: implementation for revrese decryption algorithm

	|_ ShiftDecryption.py: implementation for shift decryption algorithm

EncryptionModule: contains the impplementation of required encryption algorithms.

	|_ Encrypt.py: contains the encryption interface class
	
	|_ MatrixEncryption.py: implementation for matrix encryption algorithm
	
	|_ ReverseEncryption.Py: implementation for revrese encryption algorithm
	
	|_ ShiftEncryption.py: implementation for shift encryption algorithm

UnitTesting: contains some unit tests for Shift and Matrix encryption algorithms.

# How to use:
download the code and run 'python3 main.py str_to_be_processed -M algorithm_name[Shift,Matrix,Reverse] [Encrypt/Decrypt]'.

for example to run shift algorithm on 'hello world!' -> 'python3 main.py hello world! -M Shift Encrypt'

and to decrypt the result 'python3 main.py khoor zruog! -M Shift Decrypt'.

# Important notes:
  the code runs with python 3.x.
  
  '-M' flag is very important for parsing the arguments.
  
  If any wrong argument is passed the system will stop and raise 'invalid input' error.
  
# Docker Image:
	Also there is a docker image available here https://hub.docker.com/repository/docker/mmostaf5/crypto-task, to use it run the command 'docker run --rm crypto-app str_to_be_processed -M [Shift/Matrix/Reverse] [Encrypt/Decrypt]

