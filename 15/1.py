#!/usr/bin/env python3


def gcd(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)

print(gcd(77164189341682084692124351766096496451364840671846455244761, 46668734283684548617206823665104829826096872771679324943689))