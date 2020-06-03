#!/usr/bin/env python3

n, k = map(int, input().split())


def generate(n, k, prefix):
    if n == 0:
        print(" ".join(prefix))
    else:
        generate(n - 1, k, prefix + "0")
        if k > 0:
            generate(n - 1, k-1, prefix + "1")


generate(n, k, "")
