# list  dict

# 1 请生成200以内的奇数元素的列表，其中能被5整除的元素除以该元素在列表中的下标

# 2 请把下面字典里的每一个value的值取出来，取法是,第一个key对应的取第1个，第二个取第二个，到第五个的时候需要取倒数第二个，依次下去
#  输出结果应该是 [0,3,5,9,2,3,51]
dict_a = {
    "a": [0, 1, 2, 3],
    "b": [2, 3, 4, 9],
    "c": [3, 4, 5, 7],
    "d": [5, 6, 7, 9],
    "e": [5, 10, 2, 10],
    "f": [5, 3, 2, 5],
    "h": [51, 13, 2, 5]
}

# 3 下面有两个字典，需要组成一个新的字典,第一个字典的value是第二个字典的key,新字典由第一个字典的key和第二个字典的value组成

dict_b = {
    "a": "b",
    "b": "c",
    "c": "d",
    "d": "f",
    "e": "e",
    "f": "a",
}

dict_c = {
    "a": [0, 1, 2, 3],
    "b": [2, 3, 4, 9],
    "c": [3, 4, 5, 7],
    "d": [5, 6, 7, 9],
    "e": [5, 10, 2, 10],
    "f": [5, 3, 2, 5],
}

# 4 由26个小写字母随机生成100个字母的字符串，统计每个字母出现的个数，输出字典，value按照从大到小的顺序排列输出

# 5 写一个函数判断列表是否是对称的(即从左边读和对边读都是一样的)

# 6 写一个函数，接受两个列表作为参数，返回这两个列表的交集（两个列表里都出现的函数）。

# 7 列表里面的元素去重

# 8 下面两个字符串要求生成一个列表,后面一个字符串的字符依次插到前一个的后面
str_a = "qizhenhudi"
str_b = "zkz"
# 生成的列表是  [q,z,i,k,z,z,h,z,e,k,n,z,h,z,u,k,d,z,i,z]

