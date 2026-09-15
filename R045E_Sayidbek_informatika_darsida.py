def css(n):
    binary = bin(n)[2:]  
    octal = oct(n)[2:]   
    hexadecimal = hex(n)[2:]  
    base36 = b(n)  
    lst = [binary, octal, hexadecimal, base36]
    return lst

def b(n):
    if n < 0:
        return '-' + b(-n)
    if n == 0:
        return '0'
    
    digits = []
    while n:
        remainder = n % 36
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder - 10 + ord('a')))
        n //= 36
    
    return ''.join(digits[::-1])
for i in range(int(input())):
	nn = int(input())
	qyq = css(nn)
	print(*qyq)
