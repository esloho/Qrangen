import argparse
from src.generator import Generator


def main(args):
    mode = args.mode
    amount = args.number_amount
    exponent = args.bits

    if mode not in range(3):
        raise Exception('Mode ' + str(mode)  + ' not allowed.')

    if amount < 0:
        raise Exception('Amount ' +  str(amount) + ' not allowed.')

    if exponent < 0:
        raise Exception('Number of bits ' + str(exponent) + ' not allowed.')

    qrangen = Generator(mode, amount, exponent)
    print(qrangen.generate_number())


def print_help():
    print("""-m --mode : Simulation mode: 0 for local | 1 for IBM server
                simulation | 2 for IBM server REAL experiment\n\n"""
          + """-n --number_amount : Amount of numbers to generate. Must be greater than 0\n\n"""
          + """"-e --exponent : Generates a random number between 0 and 2**u-1.
          Needs to be a power of 2""")


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
        '-n',
        '--number_amount',
        help="Amount of numbers to generate. Needs to be greater than 0",
        default=1,
        type=int)
    parser.add_argument(
        '-b',
        '--bits',
        help="""Generates numbers of b bits""",
        default=1,
        type=int)

    parsed_args = parser.parse_args()
    main(parsed_args)
