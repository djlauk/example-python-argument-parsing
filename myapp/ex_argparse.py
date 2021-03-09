import argparse
import os.path
import sys
from typing import List

__PROG__ = os.path.basename(sys.argv[0])


def main(arguments: List[str]) -> None:
    config = parse_arguments(arguments)
    print('Config from arguments:')
    print(config)


def parse_arguments(arguments: List[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--read-from', metavar='FILE', dest='file_in', help='Read from FILE (default STDIN)', default=sys.stdin, type=argparse.FileType('r'))
    parser.add_argument('-o', '--write-to', metavar='FILE', dest='file_out', help='Write to FILE (default STDOUT)', default=sys.stdout, type=argparse.FileType('w'))
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Print debug information')
    parser.add_argument('-q', '--quiet', dest='verbose', action='store_false', help='Suppress output')
    args = parser.parse_args(arguments)
    return args


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Exception as e:
        sys.stderr.write(f'{__PROG__}: {e}')
        sys.exit(1)
    sys.exit(0)