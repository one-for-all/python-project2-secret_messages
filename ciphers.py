class Cipher:
    """Template cipher class"""
    def encrypt(self, text):
        raise NotImplementedError()

    def decrypt(self, text):
        raise NotImplementedError()

    def get_output(self, for_message="", encrypt=True):
        if encrypt:
            return self.encrypt(for_message)
        else:
            return self.decrypt(for_message)
