import argparse
from src.generator import Generator

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

def main(mode, upper_bound):
    if mode not in range(2):
        print(f'Mode {mode} not allowed. Use 0 (local), 1 (remote simulation), or 2 (remote execution)')
        return
    if not is_power2(upper_bound):
        print(f'Upper bound {upper_bound} not allowed. Needs to be a power of 2!!')
        return
    qrangen = Generator(mode)
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
        '-r',
        '--upper_bound',
        help="Generates a random number between 0 and 2**u-1. Needs to be a power of 2",
        default=1,
        type=int)

    args = parser.parse_args()
    mode = args.mode
    upper_bound = args.upper_bound
    main(mode, upper_bound)
