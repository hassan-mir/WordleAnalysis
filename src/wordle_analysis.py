import numpy as np
from pprint import pprint
def printArray(arr):
    for row in arr:
        for item in row:
            print("{:8.3f}".format(item), end = " ")
        print("")


size = (26,5)
matrix = np.zeros(size)

tf = open("all_5_lettered_words.txt")
for word in tf:
    for slot in range(5):
        letter =  word[slot]
        matrix[[ord(letter) - ord('A')],[slot]]+=1

sum_of_each_slot = np.sum(matrix, axis=0)
print (sum_of_each_slot)

result = [[str(ele) for ele in sub] for sub in matrix]
print((result))
for i in range(26):
    for j in range(5):
        result[i][j] = "{0:.00%}".format(matrix[i][j] / sum_of_each_slot[j])

row_of_letters = [chr(65 + x) for x in range(26)]

for i in range(26):
    result[i].insert(0, row_of_letters[i])
    sum = 0
    for j in range(1,5):
        sum += float(result[i][j].replace('%','')) / 500
    result[i].append( "{0:.00%}".format(sum))

pprint(result)
