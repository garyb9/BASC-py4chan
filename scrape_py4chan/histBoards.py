from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import csv4chan
from operator import itemgetter

dfBoards = csv4chan.processBoards(['pol'])

doNotInclude = ['href=', 'class=']

boardList  = [i.lower() for i in dfBoards['Subject'].values.tolist() if i is not None]    # subject column
boardList += [i.lower() for i in dfBoards['Comment'].values.tolist() if i is not None]    # comment column
histDict = {}
for text in boardList:
    words = text.split(' ')
    for word in words:
        if not any(s in word for s in doNotInclude):
            if word not in histDict:
                histDict[word] = 1
            else:
                histDict[word] += 1

listTuplesSorted = sorted(histDict.items(), key=itemgetter(1), reverse=True)

''' word_list = ['A', 'A', 'B', 'B', 'A', 'C', 'C', 'C', 'C'] '''
'''  
counts = Counter(word_list)

labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]
indexes = np.arange(len(labels))
print(indexes)
print(values)
print(labels)

bar_width = 0.35

plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.show()
'''
