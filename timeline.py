#
#
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
import tweet_module
from clean_all_tweets import policy_words, filtered_tweets, personality_words
from lists import topics_time

colorlist = ['red','blue','green','orange','purple','brown','lime','pink','aqua','black','olive','orangered','yellow','mediumvioletred','steelblue','gray','palegoldenrod','khaki','rosybrown','lightskyblue']

labels = []
for tup in topics_time:
	labels.append(tup[0])

fig, ax = plt.subplots()

plt.suptitle('Timeline of Most Used Policy Keywords')
plt.xlabel('Days Since Candidacy Announced',labelpad=10)
plt.ylabel('Keywords',labelpad=20)
plt.axis([0,1223,0,20])
plt.yticks(range(1,22),labels)

colortick = 0
for label in labels:
	ax.get_yticklabels()[colortick].set_color(colorlist[colortick]) # Labelling ticks as keywords and coordinating colors with points
	colortick += 1

count = 0
colorcount = -1
for tup in topics_time: # Plotting points and coordinating colors with keyword labels
	count += 1
	colorcount += 1
	for date in tup[1]:
		plt.plot(date,count,color=colorlist[colorcount],marker='o')

ax.set_xticks(range(0,1223,30),minor=True)# Setting grid lines
plt.grid(True,which='minor',axis='x')
plt.show()