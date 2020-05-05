import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tweet_module

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


# create lists for tokenized tweets and filtered_tweets
filtered_tweets_after = []
tokenized_tweets_after = []

# read tweets from csv

with open('Trump_tweets_after_election2.csv', 'r', encoding="ISO-8859-1") as csv_file:
    tweet_reader = csv.reader(csv_file)
    # tokenize tweets and add to list

    for tweet in tweet_reader:
        for word in tweet:
            tokenized_tweets_after.append(word_tokenize(word))


    # clean unnecessary tweet elements
    for tweet in tokenized_tweets_after:
        tweet[-1] = tweet[-1].split(',')
        tweet[-1].pop(0)
        tweet[-1] = ''.join(tweet[-1])

    for tweet in tokenized_tweets_after:
        tweet[-2] = tweet[-2].split(',')
        tweet[-2].pop(0)
        tweet[-2] = ''.join(tweet[-2])

# lowercase all tweets
for row in range(len(tokenized_tweets_after)):
    tweet_lower = [tokenized_tweets_after[row][index].lower() for index in range(len(tokenized_tweets_after[row]))]
    tokenized_tweets_after[row] = tweet_lower


# clean tweets of stopwords and add to the filtered_tweets list
for tweet in tokenized_tweets_after:
    useful_tweets = []
    for word in tweet:
        if word not in stop_words:
            useful_tweets.append(word)
    filtered_tweets_after.append(useful_tweets)

# define a function for counting days since announcing candidacy
    def count_day_function():
        day_count = -1
        for i in range(len(filtered_tweets_after)):
            day = filtered_tweets_after[i][-2]
            if day != filtered_tweets_after[i - 1][-2]:
                day_count += 1
            filtered_tweets_after[i].insert(-2, day_count)
        for tweet in filtered_tweets_after:
            tweet.pop(-2)

# run count day function
count_day_function()

policy_words = ['immigration','wall','iran','borders','tax','veterans','police','russia','michigan','leadership','jobs','trade','crime','military','china','isis','obamacare','economy','justice','mexico']
personality_words = ['crooked','wonderful','dishonest','love','fantastic','weak','smart','happy','strong','lightweight','radical','dumb','phony','heroes','liberal','nasty','disgrace','kind','disgusting','patriots']


dict = {}

primary_lista = []

filtered_tweets_after = tweet_module.updated_tweet_list(filtered_tweets_after)

dict = tweet_module.common_keywords(filtered_tweets_after,dict)

primary_lista = tweet_module.word_frequency_list(dict)

#pop_words = tweet_module.pop_words_list(policy_words, filtered_tweets_after)


