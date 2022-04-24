import argparse

argparser = argparse.ArgumentParser(description='DNSnake')
argparser.add_argument('-d', '--domain', help='Domain to scan', required=True)

def main():
    args = argparser.parse_args()
    return args

if __name__ == '__main__':
    main()
