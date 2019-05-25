from src.generator import Generator
import sys


def main(mode=0):
    qrangen = Generator(mode)
    print(qrangen.generate_number())


if __name__ == '__main__':
    """ 0=local, 1=simulate, 2=ibm"""
    mode = sys.argv[1]

    if mode not in range(2):
        print(f'Mode {mode} not allowed. Use 0 (local), 1 (remote simulation), or 2 (remote execution)')
    else:
        main(mode)
