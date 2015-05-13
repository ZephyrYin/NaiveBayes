__author__ = 'zephyrYin'
from NaiveBayes import NaiveBayes
from evaluation import  Evaluate

trainPath = 'train'
testPath = 'test'

nB = NaiveBayes(trainPath)
predictLabels, actualLabels = nB.predict(testPath)
print(predictLabels)
print(actualLabels)
e = Evaluate(predictLabels, actualLabels)
print(e.evaluation)