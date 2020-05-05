#
#
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from lists import event_list, likes_word_time
#from clean_tweets_before_election import primary_listb

#likes_word_time = [('Immigrants',[(20,2000),(30,1500),(45,1700)]),('Democrats',[(18,900),(31,1200),(40,1400)])]
colorlist = ['red','blue','green','orange','purple','brown','lime','pink','aqua','black','olive','orangered','yellow','mediumvioletred','steelblue','gray','palegoldenrod','khaki','rosybrown','lightskyblue']

fig, ax = plt.subplots()

labels = []
count = -1
for tup in likes_word_time:
	labels.append(tup[0])
	dates = []
	likes = []
	count += 1
	for pair in tup[1]:
		dates.append(pair[0])
		likes.append(pair[1])
	plt.plot(dates,likes,colorlist[count],linewidth=2.0) # Plotting the lines and cycling through colors using the list of colors.


plt.suptitle('Popularity of Keywords on Twitter Since Candidacy was Announced')
plt.xlabel('Days Since Candidacy Announced',labelpad=10)# labelpad: space between label and x-axis
plt.ylabel('Popularity (Likes, in tens)')

#events = {'Parkland Shooting':321,'Pulse Shooting':101}

#print(events.items())
#print(event_list.items())
spacing = 0
count = 0
for key,value in event_list.items():
	plt.plot(value,700 + spacing,'ro') # Event points and labels
	plt.text(value,1050 + spacing,key)
	spacing += 700
	if spacing == 4200 or spacing == 11200 or spacing == 18200:
		count += 1
		spacing = 0
	print(count)


plt.axis([0,1223,0,35000],'equal') # (xmin, xmax, ymin, ymax)
plt.legend(labels)
plt.grid(True,which='major',axis='y',color='black') # Setting grid lines
plt.grid(True,which='minor',axis='x')
ax.set_xticks(range(0,1223,30),minor=True)
ax.set_yticks(range(0,35000,200),minor=True)
plt.show()