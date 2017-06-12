#package lin567_p1

import argparse
import NaiveBayes
import io

def main():
    parser = argparse.ArgumentParser(description="Parse Values.")
    parser.add_argument('-arg1', 'trainPath', type= str, required=True)
    parser.add_argument('-arg2', 'testPath', type= str, required=True)
    parser.add_argument('-arg3', 'n', type= int, required=True)
    parser.add_argument('-arg4', 'lamda', type= float, required=True)
    args = parser.parse_args()

    trainPath = args.trainPath
    testPath = args.testPath
    n = args.n
    lamda = args.lamda

    nbModel = NaiveBayes()

    inout = io.IO()

    trainSet = inout.readDocuments(trainPath,n)
    testSet = inout.readDocuments(testPath,n)

    nbModel.train(trainSet)

    for doc in testSet:
        bestLanguage = nbModel.mostLikelyLanguage(doc.text,lamda)
        print( id + "|" + bestLanguage )




