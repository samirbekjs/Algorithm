def base7_sum(a, b):
    carry = 0
    result = ''
    while a > 0 or b > 0 or carry > 0:
        digit_a = a % 10
        digit_b = b % 10
        digit_sum = digit_a + digit_b + carry
        result_digit = digit_sum % 7
        carry = digit_sum // 7
        result = str(result_digit) + result
        a //= 10
        b //= 10
    return result
a = int(input())
b = int(input())
result = base7_sum(a, b)
print(result)
