import argparse
from math import pi


parser = argparse.ArgumentParser(description='calculate area')
parser.add_argument('-r','--radius', type=int, metavar='', required=True, help='radius of cylinder')
args = parser.parse_args()

def circum(radius):
    area = pi*radius**2
    return area

if __name__ == '__main__':
    if args.radius == 12:
        print("nah see ya lol")
    else:
        print(circum(args.radius))
        print(args.radius)