import sys

t = int(sys.stdin.readline())
pisano = [0, 1]
for i in range(2, 60):
    pisano.append((pisano[-1] + pisano[-2]) % 10)

out_lines = []
for _ in range(t):
    n = int(sys.stdin.readline())
    out_lines.append(str(pisano[n % 60]))

sys.stdout.write("\n".join(out_lines))
