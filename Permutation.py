import itertools


class Permutation:

    def __init__(self):
        self.length = input("please import the length: ")

        self.chars = input("please import the numbers or letters: ")

        self.iterate()

    def iterate(self):
        letters = []
        chars = self.chars
        length = int(self.length)
        for c in chars:
            letters.append(c)
        s = list(itertools.permutations(letters, length))

        f = open('iter {} of {}.txt'.format(
            length, chars), 'w', encoding='utf-8')
        f.write("your words: \n")
        for word in s:
            fw = ''
            for n in range(length):
                fw += word[n]
            f.write(fw + '\n')
        f.close()


Permutation()
