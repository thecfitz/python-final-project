#
#
#import clean_all_tweets
import tweet_module
from clean_all_tweets import policy_words, filtered_tweets, personality_words
from clean_tweets_before_election import primary_listb
from clean_tweets_after_election import primary_lista
import csv

event_list = {}
events_dict = {}
events_frequency_dict = {}

with open('event_list.csv', 'r') as file:
    events = csv.reader(file)
    for row in events:
        event_list[row[0]] = int(row[1])

with open('event_list.csv', 'r') as file:
    events = csv.reader(file)
    for row in events:
        events_dict[row[0]] = int(row[1])
        events_frequency_dict[row[0]] = 0

events_list = list(events_dict.keys())

topics_time = tweet_module.topic_time_list(filtered_tweets, policy_words)
likes_word_time = tweet_module.likes_word_time_list(filtered_tweets)
pop_words = tweet_module.pop_words_list(policy_words, filtered_tweets)

policy_words = ['immigration','wall','iran','borders','tax','veterans','police','russia','michigan','leadership','jobs','trade','crime','military','china','isis','obamacare','economy','justice','mexico']
personality_words = ['crooked','wonderful','dishonest','love','fantastic','weak','smart','happy','strong','lightweight','radical','dumb','phony','heroes','liberal','nasty','disgrace','kind','disgusting','patriots']

# Separating words into before and after, as well as policy and personality.

policy_wordsb = []
personality_wordsb = []

policy_wordsa = []
personality_wordsa = []

for tweet in primary_listb:
	if tweet[0] in policy_words:
		policy_wordsb.append(tweet)
	elif tweet[0] in personality_words:
		personality_wordsb.append(tweet)

for tweet in primary_lista:
	if tweet[0] in policy_words:
		policy_wordsa.append(tweet)
	elif tweet[0] in personality_words:
		personality_wordsa.append(tweet)