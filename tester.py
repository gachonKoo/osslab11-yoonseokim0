import geo.utils as utils
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        a, b = map(int, line.split())
        print(int(utils.pythagoras(a,b)))

