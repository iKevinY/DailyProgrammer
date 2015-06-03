import sys

def next_num(n, base):
    return sum(int(x) ** base for x in str(n))

try:
    base, start = int(sys.argv[1]), int(sys.argv[2])
except IndexError:
    print("Usage: {} <base> <start>".format(sys.argv[0]))
    sys.exit(2)

cycle = [start]

# Compute values until a cycle has been formed
while next_num(cycle[-1], base) not in cycle:
    cycle.append(next_num(cycle[-1], base))

start = cycle.index(next_num(cycle[-1], base))
sad_cycle = cycle[start:]

print(', '.join(str(n) for n in sad_cycle))
