---
title: Python刷题记录（91-95）
data: 2023-06-06 12:00:00
type: string
updated: 2023-06-06 12:00:00
tags: Python
categories: 刷题记录
---

题目来源PTA平台

[PAT (Basic Level) Practice （中文）](https://pintia.cn/problem-sets/994805260223102976)

-------------

## **1091 N-自守数**

如果某个数 *K* 的平方乘以 *N* 以后，结果的末尾几位数等于 *K*，那么就称这个数为“*N*-自守数”。例如 3×922=25392，而 25392 的末尾两位正好是 92，所以 92 是一个 3-自守数。

本题就请你编写程序判断一个给定的数字是否关于某个 *N* 是 *N*-自守数。

### 输入格式：

输入在第一行中给出正整数 *M*（≤20），随后一行给出 *M* 个待检测的、不超过 1000 的正整数。

### 输出格式：

对每个需要检测的数字，如果它是 *N*-自守数就在一行中输出最小的 *N* 和 NK^2^ 的值，以一个空格隔开；否则输出 `No`。注意题目保证 *N*<10。

### 输入样例：

```in
3
92 5 233
```

### 输出样例：

```out
3 25392
1 25
No
```

### 思路：

> 题目限制了N<10，硬解就行了

### 代码：

```python
M = int(input())
N = list(map(int, input().split()))
for n in N:
    for j in range(1, 10):
        t = n**2*j
        ln = len(str(n))
        lt = len(str(t))
        if str(n) == str(t)[lt-ln:lt]:
            print(j, t)
            break
    else:
        print('No')

```

## **1092 最好吃的月饼**

月饼是久负盛名的中国传统糕点之一，自唐朝以来，已经发展出几百品种。

<img src="https://images.ptausercontent.com/fcb325a0-7090-4bf4-acb0-d4d7ea832f27.jpg">

若想评比出一种“最好吃”的月饼，那势必在吃货界引发一场腥风血雨…… 在这里我们用数字说话，给出全国各地各种月饼的销量，要求你从中找出销量冠军，认定为最好吃的月饼。

### 输入格式：

输入首先给出两个正整数 *N*（≤1000）和 *M*（≤100），分别为月饼的种类数（于是默认月饼种类从 1 到 *N* 编号）和参与统计的城市数量。

接下来 *M* 行，每行给出 *N* 个非负整数（均不超过 1 百万），其中第 *i* 个整数为第 *i* 种月饼的销量（块）。数字间以空格分隔。

### 输出格式：

在第一行中输出最大销量，第二行输出销量最大的月饼的种类编号。如果冠军不唯一，则按编号递增顺序输出并列冠军。数字间以 1 个空格分隔，行首尾不得有多余空格。

### 输入样例：

```in
5 3
1001 992 0 233 6
8 0 2018 0 2008
36 18 0 1024 4
```

### 输出样例：

```out
2018
3 5
```

### 思路：

> 用列表记录每种销量，最后输出最大值和最大值的下标加一即可

### 代码：

```python
N, M = map(int, input().split())
lst = [0]*N
for i in range(M):
    t = list(map(int, input().split()))
    for j in range(N):
        lst[j] += t[j]
print(max(lst))
ans = []
for i in range(N):
    if lst[i] == max(lst):
        ans.append(i+1)
print(' '.join(str(x) for x in ans))

```

## **1093 字符串A+B**

给定两个字符串 *A* 和 *B*，本题要求你输出 *A*+*B*，即两个字符串的并集。要求先输出 *A*，再输出 *B*，但**重复的字符必须被剔除**。

### 输入格式：

输入在两行中分别给出 *A* 和 *B*，均为长度不超过 106的、由可见 ASCII 字符 (即码值为32~126)和空格组成的、由回车标识结束的非空字符串。

### 输出格式：

在一行中输出题面要求的 *A* 和 *B* 的和。

### 输入样例：

```in
This is a sample test
to show you_How it works
```

### 输出样例：

```out
This ampletowyu_Hrk
```

### 思路：

> 合并两个字符串，然后用一个127长度的列表标记是否输出过即可，用set应该也可以

### 代码：

```python
A = input()
B = input()
C = A+B
f = [0]*127
for i in C:
    if f[ord(i)] == 0:
        print(i, end='')
        f[ord(i)] = 1

```

## **1094 谷歌的招聘**

2004 年 7 月，谷歌在硅谷的 101 号公路边竖立了一块巨大的广告牌（如下图）用于招聘。内容超级简单，就是一个以 .com 结尾的网址，而前面的网址是一个 10 位素数，这个素数是自然常数 e 中最早出现的 10 位连续数字。能找出这个素数的人，就可以通过访问谷歌的这个网站进入招聘流程的下一步。

<img src="https://images.ptausercontent.com/57148679-d574-4f49-b048-775c6c07791c.jpg">

自然常数 e 是一个著名的超越数，前面若干位写出来是这样的：e = 2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642**7427466391**932003059921... 其中粗体标出的 10 位数就是答案。

本题要求你编程解决一个更通用的问题：从任一给定的长度为 L 的数字中，找出最早出现的 K 位连续数字所组成的素数。

### 输入格式：

输入在第一行给出 2 个正整数，分别是 L（不超过 1000 的正整数，为数字长度）和 K（小于 10 的正整数）。接下来一行给出一个长度为 L 的正整数 N。

### 输出格式：

在一行中输出 N 中最早出现的 K 位连续数字所组成的素数。如果这样的素数不存在，则输出 `404`。注意，原始数字中的前导零也计算在位数之内。例如在 200236 中找 4 位素数，0023 算是解；但第一位 2 不能被当成 0002 输出，因为在原始数字中不存在这个 2 的前导零。

### 输入样例 1：

```in
20 5
23654987725541023819
```

### 输出样例 1：

```out
49877
```

### 输入样例 2：

```in
10 3
2468024680
```

### 输出样例 2：

```out
404
```

### 思路:

> 对字符串进行切片然后转换成int型判断是否为素数即可
>
> 要注意循环的范围是否包含最后一位，此外0023这种情况要输出0023

### 代码：

```python
L, K = map(int, input().split())
N = input()
for i in range(L-K+1):
    t = N[i:i+K]
    int_t = int(t)
    if int_t == 2:
        print(t)
        break
    elif int_t == 1 or int_t % 2 == 0 or int_t == 0:
        continue
    else:
        for j in range(3, int(int_t**0.5)+2, 2):
            if int_t % j == 0:
                break
        else:
            print(t)
            break
else:
    print('404')

```

## **1095 解码PAT准考证**

PAT 准考证号由 4 部分组成：

- 第 1 位是级别，即 `T` 代表顶级；`A` 代表甲级；`B` 代表乙级；
- 第 2~4 位是考场编号，范围从 101 到 999；
- 第 5~10 位是考试日期，格式为年、月、日顺次各占 2 位；
- 最后 11~13 位是考生编号，范围从 000 到 999。

现给定一系列考生的准考证号和他们的成绩，请你按照要求输出各种统计信息。

### 输入格式：

输入首先在一行中给出两个正整数 *N*（≤104）和 *M*（≤100），分别为考生人数和统计要求的个数。

接下来 *N* 行，每行给出一个考生的准考证号和其分数（在区间 [0,100] 内的整数），其间以空格分隔。

考生信息之后，再给出 *M* 行，每行给出一个统计要求，格式为：`类型 指令`，其中

- `类型` 为 1 表示要求按分数非升序输出某个指定级别的考生的成绩，对应的 `指令` 则给出代表指定级别的字母；
- `类型` 为 2 表示要求将某指定考场的考生人数和总分统计输出，对应的 `指令` 则给出指定考场的编号；
- `类型` 为 3 表示要求将某指定日期的考生人数分考场统计输出，对应的 `指令` 则给出指定日期，格式与准考证上日期相同。

### 输出格式：

对每项统计要求，首先在一行中输出 `Case #: 要求`，其中 `#` 是该项要求的编号，从 1 开始；`要求` 即复制输入给出的要求。随后输出相应的统计结果：

- `类型` 为 1 的指令，输出格式与输入的考生信息格式相同，即 `准考证号 成绩`。对于分数并列的考生，按其准考证号的字典序递增输出（题目保证无重复准考证号）；
- `类型` 为 2 的指令，按 `人数 总分` 的格式输出；
- `类型` 为 3 的指令，输出按人数非递增顺序，格式为 `考场编号 总人数`。若人数并列则按考场编号递增顺序输出。

如果查询结果为空，则输出 `NA`。

### 输入样例：

```in
8 4
B123180908127 99
B102180908003 86
A112180318002 98
T107150310127 62
A107180908108 100
T123180908010 78
B112160918035 88
A107180908021 98
1 A
2 107
3 180908
2 999
```

### 输出样例：

```out
Case 1: 1 A
A107180908108 100
A107180908021 98
A112180318002 98
Case 2: 2 107
3 260
Case 3: 3 180908
107 2
123 2
102 1
Case 4: 2 999
NA
```

### 思路：

> 用ABT三个列表存储三个级别的考生
>
> kc列表存储每个考场的人数和总分
>
> dic字典存储查询时间的考场和考场人数
>
> 优化到我的极限了还是超时，有空再来看吧

### 代码：

```python
import sys


def type1(n):
    if len(n) == 0:
        sys.stdout.writelines('NA\n')
    else:
        n.sort(key=lambda x: (-int(x[1]), x[0]))
        for i in n:
            sys.stdout.writelines('%s %s\n' % (i[0], i[1]))


def type2(t, kc):
    if kc[int(t[1])][0] != 0:
        sys.stdout.writelines('{} {}\n'.format(
            kc[int(t[1])][0], kc[int(t[1])][1]))
    else:
        sys.stdout.writelines('NA\n')


def type3(t, lst):
    dic = {}
    for j in lst:
        time = j[0][4:10]
        bj = j[0][1:4]
        if time == t[1]:
            dic[bj] = dic.get(bj, 0)+1
    if len(dic) == 0:
        sys.stdout.writelines('NA\n')
    else:
        res_lst = []
        for i in dic:
            res_lst.append([i, dic[i]])
        res_lst.sort(key=lambda x: (-x[1], x))
        for i in res_lst:
            sys.stdout.writelines('{} {}\n'.format(
                i[0], i[1]))


def main():
    N, M = map(int, input().split())
    kc = [[0, 0]for i in range(1000)]
    lst = []
    A = []
    B = []
    T = []
    for i in range(N):
        a, b = sys.stdin.readline().split()
        lst.append([a, b])

        if a[0] == 'A':
            A.append([a, b])
        elif a[0] == 'B':
            B.append([a, b])
        elif a[0] == 'T':
            T.append([a, b])

        k = int(a[1:4])
        kc[k][0] += 1
        kc[k][1] += int(b)

    lst.sort(key=lambda x: (-int(x[1]), x[0]))

    for i in range(1, M+1):
        t = sys.stdin.readline().split()
        print('Case %d: %s %s' % (i, t[0], t[1]))

        if t[0] == '1':
            if t[1] == 'A':
                type1(A)
            elif t[1] == 'B':
                type1(B)
            elif t[1] == 'T':
                type1(T)
        elif t[0] == '2':
            type2(t, kc)
        else:
            type3(t, lst)


main()

```

