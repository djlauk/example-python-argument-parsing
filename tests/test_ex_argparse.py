import pytest
import sys

from myapp.ex_argparse import parse_arguments


def test_default_values():
    args = parse_arguments([])
    assert not args.verbose
    assert args.file_in is sys.stdin
    assert args.file_out is sys.stdout


def test_quiet():
    args = parse_arguments(['-q'])
    assert not args.verbose
    args = parse_arguments(['--quiet'])
    assert not args.verbose


def test_verbose():
    args = parse_arguments(['-v'])
    assert args.verbose
    args = parse_arguments(['--verbose'])
    assert args.verbose


def test_file_in(tmp_path):
    # tmp_path is a pathlib.Path objected injected by pytest
    fpath = tmp_path / 'test-input.txt'
    assert not fpath.exists()
    fpath.write_text('Test data')
    assert fpath.exists()
    args = parse_arguments(['-i', str(fpath)])
    assert args.file_in.name == str(fpath)


def test_file_in_fails_nonexisting_file():
    with pytest.raises(SystemExit):
        args = parse_arguments(['-i', 'nosuchfile.txt'])

