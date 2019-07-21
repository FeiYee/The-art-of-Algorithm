'''
搜索算法
    1、线性查找
    2、二分查找
    3、插值查找
    4、斐波那契查找 ： 斐波那契数列生成过程参考第五天动态规划详解
'''

def lineSeach(arr_list, target):
    '''
    线性
    :param arr_list:
    :param target:
    :return:
    '''
    for index, line in enumerate(arr_list):
        if target == line:
            return index
    return None

def binarySearch(arr_list, target, index_list = None):
    '''
    二分
    :param arr_list:
    :param target:
    :return:
    '''
    lengh = len(arr_list)
    if index_list == None:
        arr_list = sorted(arr_list)
        index_list = list(range(lengh))
    if lengh <= 0:
        return None
    elif arr_list[(lengh - 1) // 2] == target:
        return index_list[(lengh - 1) // 2]
    elif lengh == 1:
            return None
    elif arr_list[(lengh - 1) // 2] > target:
        return binarySearch(arr_list[:lengh // 2], target, index_list[:lengh // 2])
    else:
        return binarySearch(arr_list[lengh // 2 + 1:], target, index_list[lengh // 2 + 1:])

def interpolationSearch(arr_list, target, index_list = None):
    '''
    插值
    :param arr_list:
    :param target:
    :return:
    '''
    lengh = len(arr_list)
    if index_list == None:
        arr_list = sorted(arr_list)
        index_list = list(range(lengh))
    if lengh <= 0:
        return None
    else:
        interpola = int((target - arr_list[0]) / (arr_list[-1] - arr_list[0]) * (index_list[-1] - index_list[0]))
    if interpola >= lengh:
        return None
    elif arr_list[interpola] == target:
        return index_list[interpola]
    elif lengh == 1:
            return None
    elif arr_list[interpola] > target:
        return binarySearch(arr_list[:interpola], target, index_list[:interpola])
    else:
        return binarySearch(arr_list[interpola + 1:], target, index_list[interpola + 1:])

def dp_fib(n):
    '''
    斐波那契分割点
    :param n:
    :return:
    '''
    if n <= 2:
        return n - 1
    target_1 = 0
    target = 1
    while n > target:
        target_1, target = target, target + target_1
        # print(target)
    return target_1

def fibSearch(arr_list, target, index_list=None):
    '''
    斐波那契
    :param arr_list:
    :param target:
    :return:
    '''
    lengh = len(arr_list)
    if index_list == None:
        arr_list = sorted(arr_list)
        index_list = list(range(lengh))
    if lengh <= 0:
        return None
    elif arr_list[dp_fib(lengh)] == target:
        return index_list[dp_fib(lengh)]
    elif lengh == 1:
        return None
    elif arr_list[dp_fib(lengh)] > target:
        return binarySearch(arr_list[:dp_fib(lengh)], target, index_list[:dp_fib(lengh)])
    else:
        return binarySearch(arr_list[dp_fib(lengh) + 1:], target, index_list[dp_fib(lengh)+ 1:])
print(fibSearch([1,2,3,4,5,6,7,8,9],10))