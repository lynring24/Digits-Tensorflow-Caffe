import json, heapq
from pprint import pprint
from sklearn.metrics import accuracy_score, precision_score, recall_score
from statistics import mean


files = ['lenet_base.json','lenet_100.json', 'lenet_1_adadelta.json']

with open("prediction.txt", 'w') as dest:
    for file in files:
        with open(file) as data_file:
            data_file = json.load(data_file)

        y_true = []
        y_pred = []
        for predict in data_file['classifications'].items():
            # predict[0].encode("utf-8")[14]
            # for i in range(0, 5):
            #     expected.append([int(cols[2 * i + 2].text), float(cols[2 * i + 3].text[:-1])])
            argmax = heapq.nlargest(1, predict[1], lambda s: s[1])[0][0]
            y_true.append(predict[0].encode("utf-8")[14])
            y_pred.append(argmax)

        dest.write("\n"+file+"\n")
        dest.write('accuracy: ' + str(accuracy_score(y_true, y_pred))+"\n")
        dest.write('precision: ' + str(mean(precision_score(y_true, y_pred, average=None)))+"\n")
        dest.write('recall: ' + str(mean(recall_score(y_true, y_pred, average=None)))+"\n")
