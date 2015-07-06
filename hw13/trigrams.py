import random


d = {}


def read_text(lines):
    for x in range(0, len(lines) - 1):
        words = lines[x].split()
        for y in range(0, len(words) - 2):
            d[(words[y], words[y + 1])] = [words[i + 2]]
    # output(d)


def generate_new_text(d):


if __name__ == '__main__':
    try:
        f = open('sherlock.txt', 'r')
        lines = f.readlines()
        f.close()
    except IOError as e:
        print(str(e))
    read_text(lines)
