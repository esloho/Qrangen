import argparse
from src.generator import Generator


def main(args):
    mode = args.mode
    amount = args.amount
    exponent = args.bits

    if mode not in range(3):
        raise Exception('Mode ' + str(mode)  + ' not allowed.')

    if amount < 0:
        raise Exception('Amount ' +  str(amount) + ' not allowed.')

    if exponent < 0:
        raise Exception('Number of bits ' + str(exponent) + ' not allowed.')

    qrangen = Generator(mode, amount, exponent)
    print(qrangen.generate_number())


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
        '-b',
        '--bits',
        help="""Generates numbers of b bits""",
        default=1,
        type=int)

    parsed_args = parser.parse_args()

    main(parsed_args)
