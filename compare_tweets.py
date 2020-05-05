
import operator

from clean_all_tweets import filtered_tweets


# searches through all words and assigns a corresponding number value which increments whenever the word is found in a list. creates a dictionary of word/frequency
common_words = {}
def common_keywords(list_name, dict_name):
    for row in list_name:
        for position, element in enumerate(row[0]):
            if position == row[0].index(element):
                    if element in dict_name:
                        dict_name[element] += 1
                    else:
                        dict_name[element] = 1
    return dict_name




def word_frequency_list():
    # changes common_words into a list of tuples. sorts the the list with the module 'operator' in descending order. This is the primary list.
    primary_list = list(tuple(common_words.items()))
    primary_list.sort(key=operator.itemgetter(1), reverse=True)
    return primary_list




def topic_time_list(tweet_list):
    #this for-loop creates the outline of topics_time, which holds tuples containing a word and an empty set.
    topics_time = []
    for word in policy_words:
        topics_time.append((word, []))
    # this loop appends the tuples in topics_time with all the dates corresponding to each word.
    for num_row, row in enumerate(tweet_list):
        for num_set, set in enumerate(topics_time):
            if set[0] in row[0]:
                set[1].append(row[1])
    return topics_time

#puts the tweets strings contained in each row of the tweet list into it's own list of index 0.
def updated_tweet_list(tweet_list):
    for row_num, row in enumerate(tweet_list):
        row_list = []
        for element in row[:-2]:
            row_list.append(element)
        del tweet_list[row_num][:-2]
        tweet_list[row_num].insert(0, row_list)
    return tweet_list


def pop_words_list():
    pop_words = []
    for word in policy_words:
        like_count = 0
        for row in filtered_tweets:
            if row[0].count(word) == 1:
                like_count += int(row[2])
        pop_words.append((word, like_count))
    pop_words.sort(key=operator.itemgetter(1), reverse=True)
    return pop_words


updated_tweet_list(filtered_tweets)
common_keywords(filtered_tweets, common_words)



policy_words = ['immigration','wall','iran','borders','tax','veterans','police','russia','michigan','leadership','jobs','trade','crime','military','china','isis','obamacare','economy','justice','mexico']
personality_words = ['crooked','wonderful','dishonest','love','fantastic','weak','smart','happy','strong','lightweight','radical','dumb','phony','heroes','liberal','nasty','disgrace','kind','disgusting','patriots']

def likes_word_time_list(tweet_list):
    likes_word_time = []
    for word in policy_words:
        nested_list = []
        for row in tweet_list:
            if row[0].count(word) == 1:
                nested_list.append((row[1], row[2]))
        likes_word_time.append((word, nested_list))
    return likes_word_time


#print(pop_words_list())
for row in filtered_tweets:
    print(row[2])