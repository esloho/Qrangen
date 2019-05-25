import argparse
from src.generator import Generator


def main(mode):
    qrangen = Generator(mode)
    print(qrangen.generate_number())


def get_help():
    return """Simulation mode: 0 for local | 1 for IBM server
                simulation | 2 for IBM server REAL experiment"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--mode',
        help=get_help(),
        default=0,
        type=int)
    args = parser.parse_args()
    mode = args.mode

    if mode not in range(2):
        print(f'Mode {mode} not allowed. {get_help()}')
    else:
        main(mode)
