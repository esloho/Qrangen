import argparse
from src.generator import Generator


def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)


def main(args):
    mode = args.mode
    exponent = args.exponent

    if mode not in range(2):
        print(f'Mode {mode} not allowed.')
        print_help()
        return

    if not is_power2(exponent):
        print(f'Exponent {exponent} not allowed.')
        return

    qrangen = Generator(mode)
    print(qrangen.generate_number())


def print_help():
    print("""-m --mode : Simulation mode: 0 for local | 1 for IBM server
                simulation | 2 for IBM server REAL experiment\n\n"""
          + """"-e --exponent : Generates a random number between 0 and 2**u-1. Needs to be a power of 2""")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--mode',
        help="""Simulation mode: 0 for local | 1 for IBM server
                simulation | 2 for IBM server REAL experiment""",
        default=0,
        type=int)
    parser.add_argument(
        '-e',
        '--exponent',
        help="""Generates a random number between 0 and 2**u-1. Needs to be a power of 2""",
        default=1,
        type=int)

    parsed_args = parser.parse_args()

    main(parsed_args)
