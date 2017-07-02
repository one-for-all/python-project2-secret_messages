import string
from ciphers import Cipher
from collections import OrderedDict


class KeywordCipher(Cipher):
    """Keyword cipher: https://en.wikipedia.org/wiki/Keyword_cipher"""
    mapping = {t: t for t in string.ascii_uppercase}
    reverse_mapping = mapping

    def set_keyword(self, keyword):
        """Set keyword for cipher
        Note: keyword should be composed only of alphabetical letters
        """
        if not keyword.isalpha():
            return False
        keyword = keyword.upper()
        keyword = ''.join(OrderedDict.fromkeys(keyword))
        keys = string.ascii_uppercase
        values = keyword+keys
        values = ''.join(OrderedDict.fromkeys(values))
        self.mapping = {k: v for k, v in zip(keys, values)}
        self.reverse_mapping = {v: k for k, v in self.mapping.items()}
        return True

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
        result = ''
        for t in text.upper():
            encr = self.reverse_mapping.get(t)
            if encr:
                result += encr
            else:
                result += t
        return result
