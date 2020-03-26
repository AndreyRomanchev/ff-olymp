#!/usr/bin/env python3


text = "Sam is a multi-file text editor based on structural regular expressions It was originally designed in the early 1980s at Bell Labs by Rob Pike with the help of Ken Thompson and other Unix developers for the Blit windowing terminal running on Unix it was later ported to other systems Sam follows a classical modular Unix aesthetic It is internally simple its power leveraged by the composability of a small command language and extensibility through shell integration".split()
print(sorted(text)[len(text)//2])
