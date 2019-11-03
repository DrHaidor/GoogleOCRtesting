from jiwer import wer
import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]
with open(filename1,'r') as f:
    data1 = f.read().replace('\n',' ').replace('\\',' ')#.split()
with open(filename2,'r') as f:
    data2 = f.read().replace('\n',' ').replace('\\',' ')#.split()

#
#  error = wer(ground_truth, hypothesis)
#
print('\nError rate (WER) for documents "{}" VS "{}":'.format(filename1, filename2))
print(round(wer(data1, data2),3))
