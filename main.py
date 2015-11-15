__author__ = 'SHADOW'

from collections import Counter
from random import randint
import praw


data = []


r = praw.Reddit(user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0')
print("logging in...")
#r.login("GeoffreyCharlot14", "sd6fbv8s", disable_warning=True)
print('login success!')
top1 = r.get_subreddit('all').get_hot(limit=1)
for i in top1:
    flat_comments = praw.helpers.flatten_tree(i.comments)
    for comment in flat_comments:
        try:
            data.append(comment.body)
        except:
            print("error")
            continue

# print("data is --------------", " ".join(data))


def starting_word():
    wordlist = " ".join(data).split()
    first_words = []
    for word in range(len(wordlist)):
        if "." in wordlist[word]:
            try:
                first_words.append(wordlist[word + 1])
            except IndexError:
                continue
    return first_words[randint(0, len(first_words) - 1)]


def chain():
    start = starting_word()
    res = [start]
    x = 0
    while x < 40:
        if "." in res[-1] and x >= 15:
            return " ".join(res)
        else:
            count = []
            wordlist = " ".join(data).split()
            for i in range(len(wordlist)):
                if res[-1] == wordlist[i]:
                    try:
                        count.append(wordlist[i + 1])
                    except IndexError:
                        continue
            res.append(count[randint(0, len(count) - 1)])
            # print(count)
            x += 1

    return " ".join(res)

print(chain())
