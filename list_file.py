import csv
import tweet_module
from clean_all_tweets import policy_words, filtered_tweets, personality_words

events_dict = {}
events_frequency_dict = {}

with open('event_list.csv', 'r') as file:
    events = csv.reader(file)
    for row in events:
        events_dict[row[0]] = row[1]
        events_frequency_dict[row[0]] = 0


events_dict.pop('Event')



events_list = list(events_dict.keys())

print(events_list)



topics_time = tweet_module.topic_time_list(filtered_tweets, policy_words)
likes_word_time = tweet_module.likes_word_time_list(filtered_tweets)
pop_words = tweet_module.pop_words_list(policy_words, filtered_tweets)







