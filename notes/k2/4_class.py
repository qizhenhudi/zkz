class WordCount:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __repr__(self):
        return str(self.word) + ":" + str(self.count)


class ZKZ:
    def __init__(self):
        self.zc = list()

    def add(self, wc):
        return self.zc.append(wc)

    def __getitem__(self, index):
        return self.zc[index]

    def __repr__(self):
        return str(self.zc)


zkz = ZKZ()
zkz.add(WordCount("月", 12))
zkz.add(WordCount("日", 17))
zkz.add(WordCount("星", 8))
zkz.add(WordCount("期", 8))
print(zkz)

print(zkz[2])

print(zkz[1:3])
