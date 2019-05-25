import argparse
from src.generator import Generator


def main(args):
    mode = args.mode
    amount = args.amount
    exponent = args.exponent

    if mode not in range(2):
        print(f'Mode {mode} not allowed.')
        print_help()
        return

    if amount < 0:
        print(f'Amount {amount} not allowed.')
        print_help()

    if exponent < 0:
        print(f'Exponent {exponent} not allowed.')
        print_help()
        return

    qrangen = Generator(mode, amount, exponent)
    print(qrangen.generate_number())


def print_help():
    print("""-m --mode : Simulation mode: 0 for local | 1 for IBM server
                simulation | 2 for IBM server REAL experiment\n\n"""
          + """-n --number_amount : Amount of numbers to generate. Must be greater than 0\n\n"""
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
        '-a',
        '--amount',
        help="""Amount of numbers to generate. Needs to be greater than 0""",
        default=1,
        type=int)
    parser.add_argument(
        '-e',
        '--exponent',
        help="""Generates a random number between 0 and 2**u-1. Needs to be a power of 2""",
        default=1,
        type=int)

    parsed_args = parser.parse_args()

    main(parsed_args)
