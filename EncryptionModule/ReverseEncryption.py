from .Encryption import EncryptionInterface
import requests


class ReverseEncryption(EncryptionInterface):
    def __init__(self, reverse_encode_post_url):
        super().__init__()
        self.name = 'Reverse'
        self.post_url = reverse_encode_post_url

    def encrypt(self, string_to_be_encrypted):
        res=requests.post(self.post_url, json={"string": string_to_be_encrypted})
        if res.status_code==200:
            res=res.json()["string"]
        else:
            res="Error while processing the string!"
        return res
