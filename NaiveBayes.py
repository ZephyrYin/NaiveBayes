__author__ = 'zephyrYin'
from random import randint

class NaiveBayes:
    def __init__(self, trainPath):
        self.trainPath = trainPath
        self.hamModel, self.spamModel = self.loadFile(trainPath)
        self.threshold = 0.9999999

    def loadFile(self, path):
        file = open(path)
        lines = file.readlines()
        file.close()
        cntDict = {}
        hamDict = {}
        spamDict = {}
        hamModel = {}
        spamModel = {}
        hamCnt = 0
        wordCnt = 0
        for line in lines:
            items = line.strip('\n').split(' ')
            id = items[0]
            label = items[1]
            hamCnt += 1 if label == 'ham' else 0
            for i in range(2, len(items), 2):
                name = items[i]
                cnt = int(items[i+1])
                wordCnt += cnt
                self.record(name, cnt, cntDict)
                if label == 'ham':
                    self.record(name, cnt, hamDict)
                elif label == 'spam':
                    self.record(name, cnt, spamDict)
        spamcnt = len(lines) - hamCnt
        for word in cntDict:
            if word in hamDict:
                hamModel[word] = hamDict[word]/hamCnt
            else:
                hamModel[word] = 0.01
            if word in spamDict:
                spamModel[word] = spamDict[word]/spamcnt
            else:
                spamModel[word] = 0.01
        return hamModel, spamModel

    def record(self, name, cnt, dict):
        if name not in dict:
            dict[name] = cnt
        else:
            dict[name] += cnt

    def displayDict(self, dict):
        for d in dict:
            print(d, dict[d])
        print('.......................')

    def predict(self, testPath):
        file = open(testPath)
        lines = file.readlines()
        file.close()
        hamProbility = 1.0
        spamProbility = 1.0
        actualLabels = []
        predictLabels = []
        for line in lines:
            dict = {}
            items = line.strip('\n').split(' ')
            id = items[0]
            label = items[1]
            actualLabels.append(label)
            for i in range(2, len(items), 2):
                name = items[i]
                if name in self.hamModel:
                    dict[name] = self.spamModel[name]/(self.spamModel[name] + self.hamModel[name])
            wordRank = sorted(dict.items(), key=lambda d:d[1], reverse=True)
            pro = self.combineProbility(wordRank[:15])
            print(pro)
            if pro > self.threshold:
                predictLabels.append('spam')
            else:
                predictLabels.append('ham')

        return predictLabels, actualLabels

    def combineProbility(self, wordProb):
        a = 1
        b = 1
        for w in wordProb:
            a *= w[1]
            b *= (1 - w[1])
        return a/(a+b)