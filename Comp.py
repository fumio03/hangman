
# Computer の振る舞い
import random

import Stages

ans_list = ["cat","dog","car","apple","orange","globe",
            "guiter","ball","music","hitachi"]
wrong = 0

def start():
    """
    ans select from ans_list randomly.
    :return: ans
    """
    ans = ans_list[random.randint(0,len(ans_list)-1)]
    return ans

def secret_ans(ans):
    """
    set seacret_ans list and haid ans character.
    :param ans:
    :return: secret_ans
    """
    secret_ans = ["_"] * len(ans)
    return secret_ans

def comparison(x,l):
    """
    comparion x in l
    :param x: string char
    :param l: string word
    :return:
    """
    if x in l:
        index_num = l.index(x)
        #print(index_num)
        return index_num
    else:
        print("It is not include.")
        return None

def rename_secret_ans(x,l,y):
    if x is not None:
        l[x] = y
        print(l)
        return l

def rename_ans(x,l,y):
    if x is not None:
        l[x] = y