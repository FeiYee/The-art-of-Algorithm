from random import randint
from time import time
import gc

def bubbleSort(arr_list):
    '''
    冒泡排序
    :param arr_list:
    :return:
    '''
    lengh = len(arr_list)
    for _ in arr_list[1:]:
        for i in range(lengh - 1):
            if arr_list[i] > arr_list[i + 1]:
                arr_list[i], arr_list[i + 1] = arr_list[i + 1], arr_list[i]
    return arr_list

def selectionSort(arr_list):
    '''
    选择排序
    :param arr_list:
    :return:
    '''
    lengh = len(arr_list)
    for i in range(lengh):
        h_index = i
        for j,num in enumerate(arr_list[i:] ):
            if arr_list[h_index] > num:
                h_index = i + j
        arr_list[i], arr_list[h_index] = arr_list[h_index], arr_list[i]
    return arr_list

def insertionSort(arr_list):
    '''
    插入排序
    :param arr_list:
    :return:
    '''
    lengh = len(arr_list)
    for i in range(1,lengh):
        for j in range(i):
            if arr_list[i - j - 1] > arr_list[i - j]:
                arr_list[i - j - 1], arr_list[i - j] = arr_list[i - j], arr_list[i - j - 1]
            else:
                break
    return arr_list

def shellSort(arr_list,gap = None):
    '''
    希尔排序
    :param arr_list:
    :return:
    '''
    lengh = len(arr_list)
    if gap == None:
        gap = lengh // 2
    elif gap <= 1:
        return arr_list
    else:
        gap //= 2
    for i in range(gap):
        new_arr = list()
        arr_index = list()
        for j in range(lengh // gap + 1):
            if i + j*gap < lengh:
                new_arr.append(arr_list[i + j*gap])
                arr_index.append(i + j*gap)
        new_arr = insertionSort(new_arr)
        for j,after_index in enumerate(arr_index):
            arr_list[after_index] = new_arr[j]
    arr_list = shellSort(arr_list,gap)
    return arr_list

def mergeSort(arr_list):
    '''
    归并排序
    :param arr_list:
    :return:
    '''
    lengh = len(arr_list)
    n = lengh // 2
    temp = list()
    if lengh > 2:
        arr_list[:n] = mergeSort(arr_list[:n])
        arr_list[n:] = mergeSort(arr_list[n:])
    # 排序过程
    left = arr_list[:len(arr_list) // 2]
    right = arr_list[len(arr_list) // 2:]
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            temp.append(left.pop(0))
        else:
            temp.append(right.pop(0))
    temp += left + right
    return temp

def quickSort(arr_list):
    '''
    快速排序
    :param arr_list:
    :return:
    '''
    lengh = len(arr_list)
    if lengh < 2:
        return arr_list
    pivot = arr_list[randint(0,lengh - 1)]
    arr_list.remove(pivot)
    left = list()
    right = list()
    for j in range(lengh - 1):
            if arr_list[j] >= pivot:
                right.append(arr_list[j])
            else:
                left.append(arr_list[j])
    return quickSort(left) + [pivot] + quickSort(right)

def getTree(arr_list):
    '''
    生成二叉树
    :param arr_list:
    :return:  ID:[ Value, father ID, left ID, right ID]
    '''
    lengh = len(arr_list)

    tree_list = dict()
    for i in range(lengh):
        if i == 0:
            # 根节点
            father_id = None
        elif i % 2 == 0:
            # 右子节点
            father_id = (i - 2) // 2
            tree_list[father_id]["Right"] = i
        else:
            # 左子节点
            father_id = (i - 1) // 2
            tree_list[father_id]["Left"] = i

        tree_list[i] = {  "Value": arr_list[i],
                          "Father": father_id,
                          "Left": None,
                          "Right": None}
    return tree_list

def getMaxTree(tree,index):
    f_index = tree[index]["Father"]
    if f_index != None and tree[index]["Value"] <= tree[f_index]["Value"]:
        tree[f_index]["Value"], tree[index]["Value"] = tree[index]["Value"], tree[f_index]["Value"]
        if tree[f_index]["Right"] != None:
            l_index = tree[f_index]["Left"]
            if tree[index]["Value"] <= tree[l_index]["Value"]:
                tree[l_index]["Value"], tree[index]["Value"] = tree[index]["Value"], tree[l_index]["Value"]
        getMaxTree(tree,f_index)

def inPlaceSort(tree,lengh):
    for i in range(lengh):
        i = lengh - i
        getMaxTree(tree,i)
    return tree

def heapSort(arr_list):
    '''
    堆排序
    :param arr_list:
    :return:
    '''
    tree = getTree(arr_list)
    arr_list = list()
    while len(tree.keys()) != 0:
        inPlaceSort(tree, len(tree.keys()) - 1)
        tree[0]["Value"], tree[len(tree.keys()) - 1]["Value"] = tree[len(tree.keys()) - 1]["Value"], tree[0]["Value"]
        arr_list.append(tree.pop(len(tree.keys()) - 1)["Value"])
    return arr_list

def countingSort(arr_list):
    '''
    计数排序
    :param arr_list:
    :return:
    '''
    max_num = max(arr_list)
    min_num = min(arr_list)
    temp = dict()
    for i in range(min_num,max_num + 1):
        temp[i] = 0
    for line in arr_list:
        temp[line] += 1

    del arr_list
    gc.collect()
    arr_list = list()
    for i in range(min_num,max_num + 1):
        arr_list += [i for _ in range(temp[i])]
    return arr_list


# 生成随机数序列
num = list()
for i in range(2000):
    num.append(randint(0,45678))


now_tim = time()
print(sorted(num)[:50])
after_time = time() - now_tim
print("Python：",after_time)
now_tim = time()
print(bubbleSort(num)[:50])
after_time = time() - now_tim
print("冒泡：",after_time)
now_tim = time()
print(selectionSort(num)[:50])
after_time = time() - now_tim
print("选择：",after_time)
now_tim = time()
print(insertionSort(num)[:50])
after_time = time() - now_tim
print("插入：",after_time)
now_tim = time()
print(shellSort(num)[:50])
after_time = time() - now_tim
print("希尔：",after_time)
now_tim = time()
print(mergeSort(num)[:50])
after_time = time() - now_tim
print("归并：",after_time)
now_tim = time()
print(quickSort(num)[:50])
after_time = time() - now_tim
print("快排：",after_time)
now_tim = time()
print(heapSort(num)[:50])
after_time = time() - now_tim
print("堆排：",after_time)
now_tim = time()
print(countingSort(num)[:50])
after_time = time() - now_tim
print("计数：",after_time)
