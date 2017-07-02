import string
from ciphers import Cipher


class Atbash(Cipher):
    """Atbash cipher: https://en.wikipedia.org/wiki/Atbash"""
    mapping = {a: b for a, b in zip(string.ascii_uppercase,
                                    string.ascii_uppercase[::-1])}

    def encrypt(self, text):
        result = ''
        for t in text.upper():
            encr = self.mapping.get(t)
            if encr:
                result += encr
            else:
                result += t
        return result

    def decrypt(self, text):
        return self.encrypt(text)
