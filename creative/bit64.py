class ValueError(ValueError):
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message


class Bit64:
    bit_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-'
    number_int = 0
    number_64bit = ''
    number_binary = ''
    binary_length = 0

    def __init__(self, n, user_string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-'):
        self.bit_string = user_string
        if len(self.bit_string) != 64:
            raise ValueError(message='Insufficient literals in user_string')
        if isinstance(n, int) and n >= 0:
            self.number_int = n
            self.number_binary = bin(n).replace('0b', '')
            self.binary_length = len(self.number_binary)
            i = self.binary_length % 6
            pair6 = self.binary_length // 6
            num_set = list()
            var = self.number_binary[0:i]
            if var:
                num_set.append(var)
            while pair6:
                num_set.append(self.number_binary[i:i+6])
                i += 6
                pair6 -= 1
            for x in num_set:
                self.number_64bit += self.bit_string[int(x, 2)]
        else:
            raise ValueError(message='Unidentified datatype')

    def __str__(self):
        return self.number_64bit

    def to_int(self):
        return self.number_int

    def to_bin(self):
        return self.number_binary

    def __add__(self, other):
        return Bit64(self.to_int() + other.to_int())

    def __sub__(self, other):
        return Bit64(self.to_int() - other.to_int())

    def __mul__(self, other):
        return Bit64(self.to_int() * other.to_int())

    def __floordiv__(self, other):
        return Bit64(self.to_int() // other.to_int())

    def __mod__(self, other):
        return Bit64(self.to_int() % other.to_int())

    def __bool__(self):
        return bool(self.to_int())

    def __and__(self, other):
        return self.to_int() and other.to_int()

    def __or__(self, other):
        return self.to_int() and other.to_int()

    def __pow__(self, power, modulo=None):
        return Bit64(self.to_int() ** power)

    def __copy__(self):
        return Bit64(self.to_int())

    def __gt__(self, other):
        return self.to_int() > other.to_int()

    def __lt__(self, other):
        return self.to_int() < other.to_int()

    def __le__(self, other):
        return self.to_int() <= other.to_int()

    def __ge__(self, other):
        return self.to_int() >= other.to_int()

    def __eq__(self, other):
        return self.to_int() == other.to_int()

    def __int__(self):
        return self.to_int()

    def __ne__(self, other):
        return self.to_int() != other.to_int()

    def __xor__(self, other):
        return Bit64(self.to_int() ^ other.to_int())


def main():
    print(not Bit64(''))


if __name__ == '__main__':
    main()
