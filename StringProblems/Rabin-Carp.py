# Use of Rolling hash:

from collections import defaultdict


class RabinCarp:

    def __init__(self):
        self.prime_number = 3

    def findIndex(self, text, pattern):
        result_index = []
        k = len(pattern)
        pattern_hash = self.createHash(pattern)
        dict = defaultdict(int)
        dict[0] = self.createHash(text[:k])

        if dict[0] == pattern_hash and text[0: k] == pattern:
            result_index.append(0)

        for i in range(1, len(text) - k + 1):
            print("processing for text", text[i:i + k])
            dict[i] = self.recalculate_hash(dict[i - 1], text[i - 1], text[i + k - 1], k)
            if dict[i] == pattern_hash and text[i:i + k] == pattern:
                result_index.append(i)

        print(result_index)

    def createHash(self, text):
        hash_value = 0
        for i in range(len(text)):
            hash_value += self.getAscii(text[i]) * pow(self.prime_number, i)
        return hash_value

    def recalculate_hash(self, prev_hash, prev_char, new_char, k):
        prev_hash -= self.getAscii(prev_char)
        prev_hash /= self.prime_number
        prev_hash += self.getAscii(new_char) * pow(self.prime_number, k - 1)
        return int(prev_hash)

    def getAscii(self, ch):
        return ord(ch) - ord('a')


rc = RabinCarp()
rc.findIndex('abcdabcabcabcd', 'abcd')


class Plagirism:

    def __init__(self):
        self.prime_number = 3

    def findIndex(self, text, pattern):
        result_index = []
        k = len(pattern)
        pattern_hash = self.createHash(pattern)
        dict = defaultdict(int)
        dict[0] = self.createHash(text[:k])

        if dict[0] == pattern_hash and text[0: k] == pattern:
            result_index.append(0)

        for i in range(1, len(text) - k + 1):
            print("processing for text", text[i:i + k])
            dict[i] = self.recalculate_hash(dict[i - 1], text[i - 1], text[i + k - 1], k)
            if dict[i] == pattern_hash and text[i:i + k] == pattern:
                result_index.append(i)

        print(result_index)

    def createHash(self, text):
        hash_value = 0
        for i in range(len(text)):
            hash_value += self.getAscii(text[i]) * pow(self.prime_number, i)
        return hash_value

    def recalculate_hash(self, prev_hash, prev_char, new_char, k):
        prev_hash -= self.getAscii(prev_char)
        prev_hash /= self.prime_number
        prev_hash += self.getAscii(new_char) * pow(self.prime_number, k - 1)
        return int(prev_hash)

    def getAscii(self, ch):
        return ord(ch) - ord('a')


pg = Plagirism()
pg.findIndex('abcdabcabcabcd', ['abcd', 'cda'])
