import os

from caesar import Caesar
from atbash import Atbash
from polybius import Polybius
from keyword_cipher import KeywordCipher


class CipherController:
    def __init__(self):
        pass

    def run(self):
        self.print_welcome_message()
        while True:
            is_encrypt = self.get_encrypt_or_decrypt()
            encrypt_or_decrypt = 'encrypt' if is_encrypt is True else 'decrypt'

            cipher_class = self.get_cipher()
            cipher = cipher_class()
            if isinstance(cipher, KeywordCipher):
                while True:
                    keyword = input("What is your keyword for cipher? "
                                    "(Default is 'KRYPTOS') ")
                    valid_keyword = cipher.set_keyword(
                        keyword=(keyword if keyword else 'KRYPTOS'))
                    if valid_keyword:
                        break
                    else:
                        print('Keyword should be composed '
                              'only of alphabetical letters.')

            message = self.get_message()

            output = cipher.get_output(for_message=message, encrypt=is_encrypt)
            print('')
            print('The {}ed message is {}.'.format(encrypt_or_decrypt, output))

            print('')
            keep_going = input('Encrypt/Decrypt something again? Y/n ')
            if keep_going.lower() == 'n':
                break
            else:
                self.__clear_screen()

    def print_welcome_message(self):
        """print a welcome message"""
        print('')
        print('Welcome! This is a message encrypting and decrypting tool.')

    def get_encrypt_or_decrypt(self):
        """get input from user
        return True for encrypt and False for decrypt
        """
        print('')
        answer = input('Do you want to encrypt or decrypt? ')
        answer = answer.lower()
        if answer == 'encrypt':
            print('You choose to {}.'.format(answer))
            return True
        elif answer == 'decrypt':
            print('You choose to {}.'.format(answer))
            return False
        else:
            print('You must enter either encrypt or decrypt.')
            return self.get_encrypt_or_decrypt()

    def __clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_cipher(self):
        """prompt user to choose a cipher type
        return cipher class for the chosen type
        """
        print('')
        print('The currently available ciphers are:')
        print('')
        ciphers = {'caesar': Caesar, 'atbash': Atbash, 'polybius': Polybius,
                   'keyword': KeywordCipher}
        for name in ciphers.keys():
            print('-{}'.format(name.capitalize()))
        print('')
        cipher_chosen = input('Which cipher would you like to use? ').lower()
        cipher_class = ciphers.get(cipher_chosen)
        if cipher_class:
            return cipher_class
        else:
            print('You must choose from the available ciphers.')
            return self.get_cipher()

    def get_message(self):
        """prompt user and return message to be encrypted/decrypted"""
        print('')
        message = input("What's the message? ")
        print('')
        print('The message you provided is {}.'.format(message))
        return message


def main():
    cipher_controller = CipherController()
    cipher_controller.run()


if __name__ == '__main__':
    main()
