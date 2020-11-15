from .Decryption import DecryptionInterface
import requests


class ReverseDecryption(DecryptionInterface):
    def __init__(self, reverse_decode_post_url):
        super().__init__()
        self.name = 'Reverse'
        self.post_url = reverse_decode_post_url

    def decrypt(self, string_to_be_decrypted):
        res = requests.post(self.post_url, json={"string": string_to_be_decrypted})
        if res.status_code == 200:
            res = res.json()["string"]
        else:
            res = "Error while processing the string!"
        return res
