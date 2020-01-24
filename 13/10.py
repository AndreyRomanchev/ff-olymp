#!/usr/bin/env python3

n = int(input())
latin_dict = {}
for i in range(n):
    english, latin_string = input().split(' - ')
    latin_list = latin_string.split(', ')
    for latin_word in latin_list:
        if latin_word not in latin_dict:
            latin_dict[latin_word] = []
        latin_dict[latin_word].append(english)

print(len(latin_dict))
for latin_word, translations in sorted(latin_dict.items()):
    print(latin_word, '-', ', '.join(translations))
