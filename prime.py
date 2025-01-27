import math


def is_prime(number):
    """ Função que verifica se o número 'n' é primo ou não. """
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def main():
    """ contém toda a lógica principal"""
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
