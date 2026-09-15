import sys
from functools import lru_cache
from collections import defaultdict

def readints():
    return list(map(int, sys.stdin.read().strip().split()))

def main():
    data = readints()
    if not data:
        return
    it = iter(data)
    N = next(it); M = next(it)
    grid = [[next(it) for _ in range(M)] for __ in range(N)]

    FULL = (1 << M) - 1
    blocked = []
    for r in range(N):
        mask = 0
        for c in range(M):
            if grid[r][c] == 1:
                mask |= (1 << c)
        blocked.append(mask)
    # pad rows so blocked[r+2] is safe
    blocked += [FULL, FULL]

    # shapes defined inside a 2x2 box (no rotations allowed)
    shapes_cells = [
        [(0,0),(0,1)],                 # horizontal domino
        [(0,0),(1,0)],                 # vertical domino
        [(0,0),(1,1)],                 # diagonal TL-BR
        [(0,1),(1,0)],                 # diagonal TR-BL
        [(0,0),(0,1),(1,0),(1,1)],     # 2x2 square
        [(0,0),(0,1),(1,0)],           # L (missing br)
        [(0,0),(0,1),(1,1)],           # L (missing bl)
        [(0,0),(1,0),(1,1)],           # L (missing tr)
        [(0,1),(1,0),(1,1)],           # L (missing tl)
    ]
    shapes_masks = []
    for shape in shapes_cells:
        r0 = 0; r1 = 0; maxdc = 0
        for dr,dc in shape:
            if dr == 0:
                r0 |= (1 << dc)
            else:
                r1 |= (1 << dc)
            if dc > maxdc: maxdc = dc
        width = maxdc + 1
        shapes_masks.append((r0, r1, width))

    @lru_cache(maxsize=None)
    def dfs(a, b):
        if a == FULL:
            return {b: 1}
        inv = (~a) & FULL
        lsb = inv & -inv
        c0 = lsb.bit_length() - 1
        res = {}
        for r0mask, r1mask, width in shapes_masks:
            tb = r0mask
            while tb:
                bit = tb & -tb
                dc = bit.bit_length() - 1
                tb -= bit
                anchor = c0 - dc
                if anchor < 0 or anchor + width > M:
                    continue
                mask0 = r0mask << anchor
                mask1 = r1mask << anchor
                if (a & mask0) or (b & mask1):
                    continue
                na = a | mask0
                nb = b | mask1
                sub = dfs(na, nb)
                if sub:
                    for k,v in sub.items():
                        res[k] = res.get(k, 0) + v
        return res

    dp = defaultdict(int)
    start = (blocked[0] << M) | blocked[1]
    dp[start] = 1

    for r in range(N):
        dp_next = defaultdict(int)
        br2 = blocked[r+2]
        for key, ways in dp.items():
            a = key >> M
            b = key & ((1<<M)-1)
            trans = dfs(a, b)
            if not trans:
                continue
            for b_final, cnt in trans.items():
                nk = (b_final << M) | br2
                dp_next[nk] += ways * cnt
        dp = dp_next

    target = (FULL << M) | FULL
    print(dp.get(target, 0))

if __name__ == "__main__":
    main()
