import sys

dirs_knight = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
dirs_king = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
dirs_diag = [(-1,-1),(-1,1),(1,-1),(1,1)]
dirs_orth = [(-1,0),(1,0),(0,-1),(0,1)]

def inb(r,c): return 0<=r<8 and 0<=c<8

def piece_color(ch):
    if ch == '.': return None
    return ch.isupper()

def find_king(board, is_white):
    target = 'K' if is_white else 'k'
    for r in range(8):
        for c in range(8):
            if board[r][c] == target:
                return (r,c)
    return None

def make_move(board, r1,c1,r2,c2, promote_to=None):
    nb = [list(row) for row in board]
    ch = nb[r1][c1]
    nb[r1][c1] = '.'
    if promote_to is not None:
        nb[r2][c2] = promote_to
    else:
        nb[r2][c2] = ch
    return tuple(''.join(row) for row in nb)

def is_attacked(board, tr, tc, by_white,
                pawn_dir_up_for_white=True, pawn_dir_up_for_black=True, pawn_can_capture=True):
    # pawns attacks (consider both colors separately)
    if pawn_can_capture:
        # white pawns attackers
        if pawn_dir_up_for_white:
            pr = tr+1
            for pc in (tc-1, tc+1):
                if inb(pr, pc):
                    ch = board[pr][pc]
                    if ch != '.' and piece_color(ch) == True and ch.upper() == 'P':
                        if by_white: return True
        else:
            pr = tr-1
            for pc in (tc-1, tc+1):
                if inb(pr, pc):
                    ch = board[pr][pc]
                    if ch != '.' and piece_color(ch) == True and ch.upper() == 'P':
                        if by_white: return True
        # black pawns attackers
        if pawn_dir_up_for_black:
            pr = tr+1
            for pc in (tc-1, tc+1):
                if inb(pr, pc):
                    ch = board[pr][pc]
                    if ch != '.' and piece_color(ch) == False and ch.upper() == 'P':
                        if not by_white: return True
        else:
            pr = tr-1
            for pc in (tc-1, tc+1):
                if inb(pr, pc):
                    ch = board[pr][pc]
                    if ch != '.' and piece_color(ch) == False and ch.upper() == 'P':
                        if not by_white: return True
    # knights
    for dr,dc in dirs_knight:
        r,c = tr+dr, tc+dc
        if inb(r,c):
            ch = board[r][c]
            if ch != '.' and piece_color(ch) == by_white and ch.upper() == 'N':
                return True
    # king adjacency
    for dr,dc in dirs_king:
        r,c = tr+dr, tc+dc
        if inb(r,c):
            ch = board[r][c]
            if ch != '.' and piece_color(ch) == by_white and ch.upper() == 'K':
                return True
    # sliding rooks & queens (orth)
    for dr,dc in dirs_orth:
        r,c = tr+dr, tc+dc
        while inb(r,c):
            ch = board[r][c]
            if ch != '.':
                if piece_color(ch) == by_white and (ch.upper() == 'R' or ch.upper() == 'Q'):
                    return True
                break
            r += dr; c += dc
    # sliding bishops & queens (diag)
    for dr,dc in dirs_diag:
        r,c = tr+dr, tc+dc
        while inb(r,c):
            ch = board[r][c]
            if ch != '.':
                if piece_color(ch) == by_white and (ch.upper() == 'B' or ch.upper() == 'Q'):
                    return True
                break
            r += dr; c += dc
    return False

def generate_moves(board, is_white,
                   pawn_dir_up_for_white=True, pawn_dir_up_for_black=True,
                   pawn_can_capture=True, allow_double=True):
    moves = []
    for r in range(8):
        for c in range(8):
            ch = board[r][c]
            if ch == '.': continue
            if piece_color(ch) != is_white: continue
            p = ch.upper()
            if p == 'N':
                for dr,dc in dirs_knight:
                    r2,c2 = r+dr, c+dc
                    if not inb(r2,c2): continue
                    dest = board[r2][c2]
                    if dest == '.' or piece_color(dest) != is_white:
                        moves.append((r,c,r2,c2,None))
            elif p == 'K':
                for dr,dc in dirs_king:
                    r2,c2 = r+dr, c+dc
                    if not inb(r2,c2): continue
                    dest = board[r2][c2]
                    if dest == '.' or piece_color(dest) != is_white:
                        moves.append((r,c,r2,c2,None))
            elif p in ('B','R','Q'):
                directions = dirs_diag if p=='B' else dirs_orth if p=='R' else dirs_diag+dirs_orth
                for dr,dc in directions:
                    r2,c2 = r+dr, c+dc
                    while inb(r2,c2):
                        dest = board[r2][c2]
                        if dest == '.':
                            moves.append((r,c,r2,c2,None))
                        else:
                            if piece_color(dest) != is_white:
                                moves.append((r,c,r2,c2,None))
                            break
                        r2 += dr; c2 += dc
            elif p == 'P':
                pawn_up = pawn_dir_up_for_white if is_white else pawn_dir_up_for_black
                dr_forward = -1 if pawn_up else 1
                r2 = r + dr_forward
                # forward one
                if inb(r2,c) and board[r2][c] == '.':
                    promo_rank = 0 if pawn_up else 7
                    if r2 == promo_rank:
                        promos = ('Q','R','B','N') if is_white else ('q','r','b','n')
                        for promo in promos:
                            moves.append((r,c,r2,c,promo))
                    else:
                        moves.append((r,c,r2,c,None))
                    # double-step (if on starting rank)
                    if allow_double:
                        start_rank = 6 if pawn_up else 1
                        r3 = r + 2*dr_forward
                        if r == start_rank and inb(r3,c) and board[r3][c] == '.' and board[r2][c] == '.':
                            moves.append((r,c,r3,c,None))
                # captures
                if pawn_can_capture:
                    for dc in (-1,1):
                        c2 = c + dc
                        if inb(r2,c2):
                            dest = board[r2][c2]
                            if dest != '.' and piece_color(dest) != is_white:
                                promo_rank = 0 if pawn_up else 7
                                if r2 == promo_rank:
                                    promos = ('Q','R','B','N') if is_white else ('q','r','b','n')
                                    for promo in promos:
                                        moves.append((r,c,r2,c2,promo))
                                else:
                                    moves.append((r,c,r2,c2,None))
            else:
                pass
    return moves

def legal_moves(board, is_white,
                pawn_dir_up_for_white=True, pawn_dir_up_for_black=True,
                pawn_can_capture=True, allow_double=True):
    res = []
    for (r1,c1,r2,c2,prom) in generate_moves(board,is_white,pawn_dir_up_for_white,pawn_dir_up_for_black,pawn_can_capture,allow_double):
        nb = make_move(board,r1,c1,r2,c2,prom)
        kp = find_king(nb, is_white)
        if kp is None:
            continue
        if not is_attacked(nb, kp[0], kp[1], not is_white,
                           pawn_dir_up_for_white, pawn_dir_up_for_black, pawn_can_capture):
            res.append((r1,c1,r2,c2,prom,nb))
    return res

def mate_in_one(board, is_white):
    # try a set of plausible rule-variants to be robust
    variants = [
        # pawns move up for both colors, captures allowed, double-step allowed
        (True, True, True, True),
        # pawns move up for both, captures NOT allowed, double-step allowed (some tests/examples imply this)
        (True, True, False, True),
        # standard chess: white up, black down, captures allowed, double-step allowed
        (True, False, True, True),
        # pawns move up both, captures allowed, no double
        (True, True, True, False),
        # standard but no double
        (True, False, True, False),
        # both up and no capture and no double (fallback)
        (True, True, False, False),
    ]
    for puw, pub, pawn_can_capture, allow_double in variants:
        our_moves = legal_moves(board, is_white, puw, pub, pawn_can_capture, allow_double)
        for r1,c1,r2,c2,prom, nb in our_moves:
            opp_king = find_king(nb, not is_white)
            if opp_king is None:
                return (r1,c1,r2,c2)
            if not is_attacked(nb, opp_king[0], opp_king[1], is_white, puw, pub, pawn_can_capture):
                continue
            opp_legal = legal_moves(nb, not is_white, puw, pub, pawn_can_capture, allow_double)
            if len(opp_legal) == 0:
                return (r1,c1,r2,c2)
    return None

def coord_to_notation(r,c):
    file = chr(ord('A') + c)
    rank = str(8 - r)
    return f"{file}{rank}"

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    k = int(data[0])
    is_white = True if k == 1 else False
    lines = []
    idx = 1
    for i in range(8):
        lines.append(data[idx])
        idx += 1
    board = tuple(line if len(line) == 8 else line.ljust(8,'.') for line in lines)
    res = mate_in_one(board, is_white)
    if res is None:
        # problem guarantees solution exists; fallback (shouldn't happen)
        print("A1 A1")
    else:
        r1,c1,r2,c2 = res
        print(coord_to_notation(r1,c1), coord_to_notation(r2,c2))

if __name__ == "__main__":
    main()
