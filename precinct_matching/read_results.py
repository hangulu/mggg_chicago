import collections
import pandas as pd
import pickle
import numpy as np

with open("chicago_rcv_race_3",'rb') as f:


	chic_impute = pickle.load(f)



totvots = collections.defaultdict(float)

for v in chic_impute.values():
	for k2,v2 in v.items():
		totvots[k2] += v2


print(len(totvots.keys()))

races = ['white','black','hispanic','asian','undetermined']
for r in races:
	sums = [0,0,0]
	for k,v in totvots.items():
		for i in range(1):
			if k[i] == r:
				sums[i] += v
	for i in range(1):
		print("{} Choice {}: {}".format(i+1,r,sums[i]))



for r in races:
	tot = 0
	for k,v in totvots.items():
		if r in k:
			tot+=v

	print("{} in top 3: {}".format(r,tot))