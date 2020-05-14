#!/usr/bin/env python

import sys

def create_text(f):
    buffer = []
    lines = open(f).readlines()
    chapters = [
                "II.",
                "IV. The Boscombe Valley Mystery",
                "V. The Five Orange Pips",
                "VI. The Man with the Twisted Lip",
                "IX. The Adventure of the Engineer's Thumb",
                "X. The Adventure of the Noble Bachelor",
                "XI. The Adventure of the Beryl Coronet"]
    for line in lines[61:12630]:
        hit = 0
        for chapter in chapters:
            if chapter.lower() in line.lower():
                hit = 1
                break
        if not hit:
            buffer.append(line)
    return buffer

def count_chars(b):
    chars = 0
    for line in b:
        for c in line:
            if c.isalnum():
                chars += 1
    return chars

if __name__ == '__main__':
    buffer = create_text(sys.argv[1])
    print count_chars(buffer)
