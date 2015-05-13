__author__ = 'zephyrYin'
class Evaluate:
    def __init__(self, pre, test):
        self.predictions = pre
        self.test = test
        self.evaluation = self.getEvaluation()

    def getEvaluation(self):
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        rightCnt = 0
        wholeCnt = len(self.predictions)
        for i in range(len(self.predictions)):
            if self.predictions[i].lower() == 'ham':
                if self.test[i].lower() == 'ham':
                    rightCnt += 1
                    TP = TP + 1
                else:
                    FP = FP + 1
            else:
                if self.test[i].lower() == 'ham':
                    FN = FN + 1
                else:
                    TN = TN + 1
                    rightCnt += 1
        print(TP,FP,TN,FN)
        if TP == 0:
            precision = 0
            recall = 0
        else:
            precision = float(TP)/(TP + FP)
            recall = float(TP)/(TP + FN)
        if precision == 0 and recall == 0:
            F1 = 0
        else:
            F1 = 2*recall*precision/(recall + precision)
        accuracy = rightCnt / wholeCnt
        return [accuracy, precision, recall, F1]