'''
幼儿园有10个小朋友，把1 – 20中所有奇数数字的卡片分别发给这10个小朋友。
集合的时候小朋友们排成一排，组成一个由数字组成的字符串，如59731315….11917，
但是老师发现少了一个小朋友，你能帮忙找出少掉的那个小朋友吗？
1 3 5 7 9 11 13 15 17 19

// 1 7
// 3 2
// 5 2
// 7 2
// 9 2

思路：遍历字符串，统计出1 3 5 7 9的个数；
      判断1 3 5 7 9 出现的个数。
'''

data = "15971913151117"

ji = ["1","3","5","7","9","11","13","15","17","19"]

def cut(str_data,arr_list):
    if len(str_data) == 0:
        return arr_list[0]
    if len(arr_list) == 0:
        return None
    for i in range(len(arr_list)):
        if arr_list[i] in str_data:
            re = cut(str_data.replace(arr_list[i],"",1),arr_list[:i] + arr_list[i+1:])
            if re != None:
                return re
print(cut(data,ji))
