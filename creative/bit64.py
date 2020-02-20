class Bit64:
    bit_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-'
    number_int = 0
    number_64bit = ''
    number_binary = ''

    class InvalidUserStringError(Exception):
        def __init__(self, message='Insufficient literals in user_string'):
            self.message = message

        def __str__(self):
            return self.message

    class NegativeNoError(Exception):
        def __init__(self, message='Negative Not Allowed'):
            self.message = message

        def __str__(self):
            return self.message

    class InvalidBit64Error(Exception):
        def __init__(self, message='Invalid 64bit No. '):
            self.message = message

        def __str__(self):
            return self.message

    def __init__(self, n, user_string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-'):
        self.bit_string = user_string
        if len(self.bit_string) != 64:
            raise self.InvalidUserStringError
        if isinstance(n, int):
            if n < 0:
                raise self.NegativeNoError
            self.number_int = n
            self.number_binary = bin(n).replace('0b', '')
            binary_length = len(self.number_binary)
            i = binary_length % 6
            pair6 = binary_length // 6
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
        elif isinstance(n, str):
            if not n:
                raise self.InvalidBit64Error
            for x in n:
                if x not in self.bit_string:
                    raise self.InvalidBit64Error
            self.number_64bit = n
            self.number_int = 0
            i = 0
            for x in reversed(self.number_64bit):
                self.number_int += self.bit_string.index(x) * (64**i)
                i += 1
            self.number_binary = bin(self.number_int)
        else:
            raise ValueError

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
    try:
        print(int(Bit64('ZmcBC9-wAXM')))
    except Bit64.InvalidBit64Error:
        print('Welcome')


if __name__ == '__main__':
    main()
