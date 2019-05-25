import argparse
from src.generator import Generator


def main():
    qrangen = Generator(mode)
    print(qrangen.generate_number())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', help='Simulation mode: 0 for local | 1 for IBM server simulation | 2 for IBM server REAL experiment', default=0, type=int)
    args = parser.parse_args()
    mode = args.mode

    if mode not in range(2):
        print(f'Mode {mode} not allowed. Use 0 (local), 1 (remote simulation), or 2 (remote execution)')
    else:
        main(mode)
