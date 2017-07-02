from ciphers import Cipher


class Polybius(Cipher):
    """Polybius square cipher: https://en.wikipedia.org/wiki/Polybius_square"""
    mapping = {}
    reverse_mapping = {}
    cells = ()

    def __init__(self):
        super().__init__()
        self.cells = (
            ('A', 'B', 'C', 'D', 'E'),
            ('F', 'G', 'H', 'I', 'K'),
            ('L', 'M', 'N', 'O', 'P'),
            ('Q', 'R', 'S', 'T', 'U'),
            ('V', 'W', 'X', 'Y', 'Z'),
            ('J',)
        )
        for (i, row) in enumerate(self.cells, start=1):
            for (j, letter) in enumerate(row, start=1):
                self.mapping[letter] = str(i)+str(j)

        self.reverse_mapping = {v: k for k, v in self.mapping.items()}

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
        raw = text
        result = ''
        while raw:
            encr = raw[:2]
            decr = self.reverse_mapping.get(encr)
            if decr:
                result += decr
                raw = raw[2:]
            else:
                result += raw[:1]
                raw = raw[1:]
        return result
