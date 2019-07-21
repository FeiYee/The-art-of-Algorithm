'''
题目：
        1、斐波那契数列
        2、约瑟夫环
        3、找零钱问题
'''

'''
斐波那契数列
    0、1、2、3、5、8 ······
    Value（N） = Value（N - 1） + Value（N - 2）
'''

def fib(n):
    '''
    递归斐波那契
    :param n:
    :return:
    '''
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def dp_fib(n):
    '''
    动态规划斐波那契
    :param n:
    :return:
    '''
    if n <= 2:
        return n - 1
    target_1 = 0
    target = 1
    for _ in range(n - 2):
        target_1, target = target, target + target_1
    return target

def joseph(arr_list,king):
    '''
    递归约瑟夫环
    :param arr_list:
    :param king:
    :return:
    '''
    lengh = len(arr_list)
    if lengh == 1:
        return arr_list[0] + 1
    else:
        if lengh < king:
            return joseph(list(set(arr_list)^set([arr_list[king % lengh - 1]])),king)
        else:
            return joseph(arr_list[king:] + arr_list[:king - 1],king)

'''
找零钱问题
    故事的主人公叫做丁丁，他是一个十几岁的小男孩，机智聪颖，是某某杂货店的小学徒。在他生活的国度里，只流通面额为1,3,4的硬币。
这家店的店长，叫做老王，是个勤奋实干的中年人，每天都要跟钱打交道。 
    有一天，他心血来潮，叫住正在摆放货物的丁丁，对他说道：“丁丁，你不是学过计算机方面的算法吗？我这里正好有个问题，不知你能解答不？” 
一听到算法，丁丁的眼睛里闪出光芒，这正是自己的兴趣所在。于是，他连忙凑到柜台，好奇地问题：“什么问题啊？” 老王也不多说废话，他知道丁
丁的聪慧之处，直接了当地说道：“你看啊，每次顾客们买完东西付款后，我们都要找零给他们，我们这边所有的硬币（1,3,4）都是充足的，我想知道
一共有多少种找零方式？比如说找零为4的话，就有4=1+1+1+1=3+1=1+3=4共4种方式。” 
    乍听到这个问题，丁丁有点蒙圈了，因为4的情况是简单的，但是随着找零的面额增加，数量的变化就没有什么规律了。

测试样例：
[1,2,4],3,3
返回：2

解析：设dp[n][m]为使用前n中货币凑成的m的种数，那么就会有两种情况：

             使用第n种货币：dp[n-1][m]+dp[n-1][m-peney[n]]

              不用第n种货币：dp[n-1][m]，为什么不使用第n种货币呢，因为penney[n]>m。

        这样就可以求出当m>=penney[n]时 dp[n][m] = dp[n-1][m]+dp[n][m-peney[n]]，否则，dp[n][m] = dp[n-1][m]
                                    #########同斐波那契数列原理###########
'''

