import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tweet_module
import operator
# download nltk stopwords and set to english
nltk.download('stopwords')
stopwords1 = set(stopwords.words('english'))

# create a stop word list
stop_words = []

# for add stopwords from nltk to stop word list
for word in stopwords1:
    stop_words.append(word)

# append stop_word list with new stop words
stop_words.append('@')
stop_words.append('!')
stop_words.append('-')
stop_words.append((','))
stop_words.append('?')
stop_words.append('.')
stop_words.append('...')
stop_words.append('#')
stop_words.append(':')
stop_words.append(';')
stop_words.append('&')
stop_words.append('--')
stop_words.append('$')
stop_words.append("''")
stop_words.append('(')
stop_words.append(')')
stop_words.append('..')
stop_words.append("'")
stop_words.append("''")
stop_words.append('``')
stop_words.append('http')
stop_words.append('https')
stop_words.append('/')
stop_words.append('amp')
stop_words.append('get')
stop_words.append("n't")




# create lists for tokenized tweets and filtered_tweets
filtered_tweets = []
tokenized_tweets = []

# read tweets from csv

with open('All_tweets_matter.csv', 'r', encoding="ISO-8859-1") as csv_file:
    tweet_reader = csv.reader(csv_file)
    # tokenize tweets and add to list

    for tweet in tweet_reader:
        for word in tweet:
            tokenized_tweets.append(word_tokenize(word))


     # clean unnecessary tweet elements
    for tweet in tokenized_tweets:
        tweet[-1] = tweet[-1].split(',')
        tweet[-1].pop(0)
        tweet[-1] = ''.join(tweet[-1])

    for tweet in tokenized_tweets:
        tweet[-2] = tweet[-2].split(',')
        tweet[-2].pop(0)
        tweet[-2] = ''.join(tweet[-2])




# lowercase all tweets
for row in range(len(tokenized_tweets)):
    tweet_lower = [tokenized_tweets[row][index].lower() for index in range(len(tokenized_tweets[row]))]
    tokenized_tweets[row] = tweet_lower





# clean tweets of stopwords and add to the filtered_tweets list
for tweet in tokenized_tweets:
    useful_tweets = []
    for word in tweet:
        if word not in stop_words:
            useful_tweets.append(word)
    filtered_tweets.append(useful_tweets)

# define a function for counting days since announcing candidacy
    def count_day_function():
        day_count = -1
        for i in range(len(filtered_tweets)):
            day = filtered_tweets[i][-2]
            if day != filtered_tweets[i - 1][-2]:
                day_count += 1
            filtered_tweets[i].insert(-2, day_count)
        for tweet in filtered_tweets:
            tweet.pop(-2)

# run count day function
count_day_function()


policy_words = ['immigration','wall','iran','borders','tax','veterans','police','russia','michigan','leadership','jobs','trade','crime','military','china','isis','obamacare','economy','justice','mexico']
personality_words = ['crooked','wonderful','dishonest','love','fantastic','weak','smart','happy','strong','lightweight','radical','dumb','phony','heroes','liberal','nasty','disgrace','kind','disgusting','patriots']

dict = {}

primary_list = []

filtered_tweets = tweet_module.updated_tweet_list(filtered_tweets)
filtered_tweets[0][2] = '0'
filtered_tweets[8765][2] = '0'

dict = tweet_module.common_keywords(filtered_tweets, dict)

primary_list = tweet_module.word_frequency_list(dict)

topics_time = tweet_module.topic_time_list(filtered_tweets, policy_words)

likes_word_time = tweet_module.likes_word_time_list(filtered_tweets)

pop_words = tweet_module.pop_words_list(policy_words, filtered_tweets)

for row in likes_word_time:
    print(row)










