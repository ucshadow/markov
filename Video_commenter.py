__author__ = 'SHADOW'
import praw
import requests
from bs4 import BeautifulSoup
from random import randint
from termcolor import cprint
import logging
import time

logger = logging.getLogger()


def get_qt(qurl):
    with requests.Session() as b:
        response = b.get(qurl)
        return response.text


def id_check(id_):
    xx = open("IDs", "r")
    w = xx.read().split()
    xx.close()
    if id_ not in w:
        yy = open("IDs", "a")
        yy.write(id_)
        yy.write("\n")
        yy.close()
        return True
    xx.close()
    return False


def url_former(temp):
    if "http://youtu.be" in temp or "https://youtu.be" in temp:
        res = temp.split(".be/")[1][0:11]
        return "https://www.youtube.com/all_comments?v=" + res
    if "www.youtube.com" in temp:
        res = temp.split("v=")[1][0:11]
        return "https://www.youtube.com/all_comments?v=" + res
    else:
        cprint("no go on url" + temp, "grey")
        return "no go"


r = praw.Reddit(user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0')

while True:

    print("__STARTING__")
    t = r.get_subreddit('BOTTEST').get_rising(limit=10)
    for i in t:
        try:
            if id_check(i.id):
                url = url_former(i.url)
                if url != "no go":
                    print(i, " -- " + url)
                    result = get_qt(url)
                    a = (result.encode("utf-8"))
                    soup = BeautifulSoup(a, 'html.parser')
                    result = soup.findAll('div', {'class': 'comment-text-content'})
                    if len(result) > 2:
                        cprint("commenting to ", "yellow")
                        print(i)
                        cprint(result[0].text, "magenta")
                        print("\n")
                        r.login("--", "--", disable_warning=True)
                        i.add_comment(result[0].text)
                        cprint("----- done -----", "green")
                        sleep_time = randint(4 * 60, 12 * 60)
                        print('sleeping for', sleep_time)
                        time.sleep(sleep_time)
                    else:
                        continue
        except BaseException as e:
            print(i)
            logger.error('error: ' + str(e))
            continue
    time.sleep(1200)





