import geo.utils as utils
import sys

for line in sys.stdin:
    line = line.strip()
    if line.startswith("pythagoras"):
        _, a, b = line.split()
        print(int(utils.pythagoras(int(a), int(b))))
    elif line.startswith("circle"):
        _, r = line.split()
        print(int(utils.circle(int(r))))

