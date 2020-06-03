#!/usr/bin/env python3


def generate(n, prefix):
    if n == 0:
        print(" ".join(prefix))
    else:
        if len(prefix) < 2 or prefix[-2:] != "00":
            generate(n - 1, prefix + "0")
        if len(prefix) < 2 or prefix[-2:] != "11":
            generate(n - 1, prefix + "1")
generate(int(input()), "")