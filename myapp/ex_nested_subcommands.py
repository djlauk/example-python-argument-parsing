import argparse
import os.path
import sys
from typing import List

__PROG__ = os.path.basename(sys.argv[0])


def main(arguments: List[str]) -> None:
    parser = build_parser()
    args = parser.parse_args(arguments)
    args.func()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='sub-commands', required=True)

    p1 = subparsers.add_parser('foo', help='run foo commands')
    sp1 = p1.add_subparsers(title='foo commands', required=True)
    p11 = sp1.add_parser('command1', help='run command 1')
    p11.set_defaults(func=lambda: print('foo command1 called'))
    p12 = sp1.add_parser('command2', help='run command 2')
    p12.set_defaults(func=lambda: print('foo command2 called'))
    p13 = sp1.add_parser('command3', help='run command 3')
    p13.set_defaults(func=lambda: print('foo command3 called'))

    p2 = subparsers.add_parser('bar', help='run bar commands')
    sp2 = p2.add_subparsers(title='bar commands', required=True)
    p21 = sp2.add_parser('command1', help='run command 1')
    p21.set_defaults(func=lambda: print('bar command1 called'))
    p22 = sp2.add_parser('command2', help='run command 2')
    p22.set_defaults(func=lambda: print('bar command2 called'))
    
    return parser


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Exception as e:
        sys.stderr.write(f'{__PROG__}: {e}')
        sys.exit(1)
    sys.exit(0)
