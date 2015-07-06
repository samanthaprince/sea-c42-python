import random


d = {}


def read_text(lines):
    for x in range(0, len(lines) - 1):
        words = lines[x].lower().split()
        for y in range(0, len(words) - 2):
            d[(words[y], words[y + 1])] = [words[y + 2]]
    generate_new_text(d)


def generate_new_text(d):
    new_text_story = ""
    for x in range(5):
        new_sentence = list(random.choice(list(d.keys())))
        new_sentence[0] = new_sentence[0].capitalize()
        for y in range(random.randint(5, 10)):
            words = random.choice(list(d.keys()))
            new_sentence.extend(words)
        new_sentence[-1] += ". "
        new_sentence = " ".join(new_sentence)
        new_text_story += new_sentence
    print(new_text_story)

if __name__ == '__main__':
    try:
        # can also use file sherlock_small.txt
        f = open('sherlock.txt', 'r')
        lines = f.readlines()
        f.close()
    except IOError as e:
        print(str(e))
    read_text(lines)
