import sys

from satella.files import read_in_file
from imgmanip.classes import Image


def print_help():
    print('''Usage:
    imgmanip <name of script> <name of file1> <name of file2> ...

    imgmanip --help displays this message
    imgmanip -h displays this message
''')


def command():
    if len(sys.argv) < 2 or '-h' in sys.argv or '--help' in sys.argv:
        return print_help()

    script = read_in_file(sys.argv[1], 'utf-8')

    for file in sys.argv[2:]:
        img = Image(file)
        exec(script)
        img.save()


if __name__ == '__main__':
    command()
