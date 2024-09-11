---
title: Python刷题记录（61-70）
data: 2023-06-06 12:00:00
type: string
updated: 2023-06-06 12:00:00
tags: Python
categories: 刷题记录
---

题目来源PTA平台

[PAT (Basic Level) Practice （中文）](https://pintia.cn/problem-sets/994805260223102976)

------------

## **1061 判断题**

判断题的评判很简单，本题就要求你写个简单的程序帮助老师判题并统计学生们判断题的得分。

### 输入格式：

输入在第一行给出两个不超过 100 的正整数 N 和 M，分别是学生人数和判断题数量。第二行给出 M 个不超过 5 的正整数，是每道题的满分值。第三行给出每道题对应的正确答案，0 代表“非”，1 代表“是”。随后 N 行，每行给出一个学生的解答。数字间均以空格分隔。

### 输出格式：

按照输入的顺序输出每个学生的得分，每个分数占一行。

### 输入样例：

```in
3 6
2 1 3 3 4 5
0 0 1 0 1 1
0 1 1 0 0 1
1 0 1 0 1 0
1 1 0 0 1 1
```

### 输出样例：

```out
13
11
12
```

### 思路：

> 没啥好说的套循环硬算就完事

### 代码：

```python
N, M = map(int, input().split())
value = list(map(int, input().split()))
rightans = list(map(str, input().split()))
for i in range(N):
    ans = 0
    t = list(map(str, input().split()))
    for j in range(M):
        if t[j] == rightans[j]:
            ans += value[j]
    print(ans)
```

## **1062 最简分数** 

一个分数一般写成两个整数相除的形式：*N*/*M*，其中 *M* 不为0。最简分数是指分子和分母没有公约数的分数表示形式。

现给定两个不相等的正分数 *N*1/*M*1 和 *N*2/*M*2，要求你按从小到大的顺序列出它们之间分母为 *K* 的最简分数。

### 输入格式：

输入在一行中按 *N*/*M* 的格式给出两个正分数，随后是一个正整数分母 *K*，其间以空格分隔。题目保证给出的所有整数都不超过 1000。

### 输出格式：

在一行中按 *N*/*M* 的格式列出两个给定分数之间分母为 *K* 的所有最简分数，按从小到大的顺序，其间以 1 个空格分隔。行首尾不得有多余空格。题目保证至少有 1 个输出。

### 输入样例：

```in
7/18 13/20 12
```

### 输出样例：

```out
5/12 7/12
```

### 思路：

> 将分式转换成小数，用一个for循环找到以K为分母中所有符合要求的分子，求分子和分母的最大公约数，为1时输出

### 代码：

```python
def fun(n):
    index = n.find('/')
    t = int(n[:index])/int(n[index+1:])
    return t


def gcd(a, b):
    while(b != 0):
        t = a % b
        a = b
        b = t
    return a


a, b, c = input().split()
a = fun(a)
b = fun(b)
c = int(c)
if a > b:
    a, b = b, a
ans = []
for i in range(1, c):
    if a < i/c < b:
        t = gcd(c, i)
        if t == 1:
            ans.append('{}/{}'.format(int(i/t), int(c/t)))
print(' '.join(ans))

```

## **1063 计算谱半径**

在数学中，矩阵的“谱半径”是指其特征值的模集合的上确界。换言之，对于给定的 *n* 个复数空间的特征值 { *a*1+*b*1*i*,⋯,*a**n*+*b**n**i* }，它们的模为实部与虚部的平方和的开方，而“谱半径”就是最大模。

现在给定一些复数空间的特征值，请你计算并输出这些特征值的谱半径。

### 输入格式：

输入第一行给出正整数 N（≤ 10 000）是输入的特征值的个数。随后 N 行，每行给出 1 个特征值的实部和虚部，其间以空格分隔。注意：题目保证实部和虚部均为绝对值不超过 1000 的整数。

### 输出格式：

在一行中输出谱半径，四舍五入保留小数点后 2 位。

### 输入样例：

```in
5
0 1
2 0
-1 0
3 3
0 -3
```

### 输出样例：

```out
4.24
```

### 思路：

> 常规思路，输入每个然后求模，找出最大值即可

### 代码：

```python
n = int(input())
max = 0
for i in range(n):
    a, b = map(int, input().split())
    t = (a**2+b**2)**0.5
    if t > max:
        max = t
print("{:.2f}".format(max))

```

## **1064 朋友数**

如果两个整数各位数字的和是一样的，则被称为是“朋友数”，而那个公共的和就是它们的“朋友证号”。例如 123 和 51 就是朋友数，因为 1+2+3 = 5+1 = 6，而 6 就是它们的朋友证号。给定一些整数，要求你统计一下它们中有多少个不同的朋友证号。

### 输入格式：

输入第一行给出正整数 N。随后一行给出 N 个正整数，数字间以空格分隔。题目保证所有数字小于 104。

### 输出格式：

首先第一行输出给定数字中不同的朋友证号的个数；随后一行按递增顺序输出这些朋友证号，数字间隔一个空格，且行末不得有多余空格。

### 输入样例：

```in
8
123 899 51 998 27 33 36 12
```

### 输出样例：

```out
4
3 6 9 26
```

### 思路：

> 使用sum(map(int,i))的方法快速求个位数字和，set去重，排序后转换成str使用join输出

### 代码：

```python
N = int(input())
lst = input().split()
s = set()
for i in range(N):
    s.add(sum(map(int, lst[i])))
print(len(s))
print(' '.join(str(x) for x in sorted(s)))

```

## **1065 单身狗**

“单身狗”是中文对于单身人士的一种爱称。本题请你从上万人的大型派对中找出落单的客人，以便给予特殊关爱。

### 输入格式：

输入第一行给出一个正整数 N（≤ 50 000），是已知夫妻/伴侣的对数；随后 N 行，每行给出一对夫妻/伴侣——为方便起见，每人对应一个 ID 号，为 5 位数字（从 00000 到 99999），ID 间以空格分隔；之后给出一个正整数 M（≤ 10 000），为参加派对的总人数；随后一行给出这 M 位客人的 ID，以空格分隔。题目保证无人重婚或脚踩两条船。

### 输出格式：

首先第一行输出落单客人的总人数；随后第二行按 ID 递增顺序列出落单的客人。ID 间用 1 个空格分隔，行的首尾不得有多余空格。

### 输入样例：

```in
3
11111 22222
33333 44444
55555 66666
7
55555 44444 10000 88888 22222 11111 23333
```

### 输出样例：

```out
5
10000 23333 44444 55555 88888
```

### 思路：

> 将cp存入列表，访客存入集合（网上大佬们说集合查询更快）
>
> 遍历cp列表并将其中一对都存在访客集合中的去除，剩下的就是单身狗
>
> 同时使用sys库的输入，测试点3、4无超时

### 代码：

```python
import sys

N = int(input())
cp = [sys.stdin.readline().split()for i in range(N)]
M = int(input())
lst = set(sys.stdin.readline().split())
for i in cp:
    if i[0] in lst and i[1] in lst:
        lst.remove(i[0])
        lst.remove(i[1])
cnt = len(lst)
print(cnt)
if cnt != 0:
    print(' '.join(sorted(lst)))

```

## **1066 图像过滤**

图像过滤是把图像中不重要的像素都染成背景色，使得重要部分被凸显出来。现给定一幅黑白图像，要求你将灰度值位于某指定区间内的所有像素颜色都用一种指定的颜色替换。

### 输入格式：

输入在第一行给出一幅图像的分辨率，即两个正整数 *M* 和 *N*（0<*M*,*N*≤500），另外是待过滤的灰度值区间端点 *A* 和 *B*（0≤*A*<*B*≤255）、以及指定的替换灰度值。随后 *M* 行，每行给出 *N* 个像素点的灰度值，其间以空格分隔。所有灰度值都在 [0, 255] 区间内。

### 输出格式：

输出按要求过滤后的图像。即输出 *M* 行，每行 *N* 个像素灰度值，每个灰度值占 3 位（例如黑色要显示为 `000`），其间以一个空格分隔。行首尾不得有多余空格。

### 输入样例：

```in
3 5 100 150 0
3 189 254 101 119
150 233 151 99 100
88 123 149 0 255
```

### 输出样例：

```out
003 189 254 000 000
000 233 151 099 000
088 000 000 000 255
```

### 思路：

> 将像素点输入值tmp列表中，只要在A~B的范围就替换为T，然后输出即可

### 代码：

```python
M, N, A, B, T = map(int, input().split())
for i in range(M):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if A <= tmp[j] <= B:
            tmp[j] = T
    print(' '.join('{:03}'.format(x)for x in tmp))

```

## **1067 试密码**

当你试图登录某个系统却忘了密码时，系统一般只会允许你尝试有限多次，当超出允许次数时，账号就会被锁死。本题就请你实现这个小功能。

### 输入格式：

输入在第一行给出一个密码（长度不超过 20 的、不包含空格、Tab、回车的非空字符串）和一个正整数 N（≤ 10），分别是正确的密码和系统允许尝试的次数。随后每行给出一个以回车结束的非空字符串，是用户尝试输入的密码。输入保证至少有一次尝试。当读到一行只有单个 # 字符时，输入结束，并且这一行不是用户的输入。

### 输出格式：

对用户的每个输入，如果是正确的密码且尝试次数不超过 N，则在一行中输出 `Welcome in`，并结束程序；如果是错误的，则在一行中按格式输出 `Wrong password: 用户输入的错误密码`；当错误尝试达到 N 次时，再输出一行 `Account locked`，并结束程序。

### 输入样例 1：

```in
Correct%pw 3
correct%pw
Correct@PW
whatisthepassword!
Correct%pw
#
```

### 输出样例 1：

```out
Wrong password: correct%pw
Wrong password: Correct@PW
Wrong password: whatisthepassword!
Account locked
```

### 输入样例 2：

```in
cool@gplt 3
coolman@gplt
coollady@gplt
cool@gplt
try again
#
```

### 输出样例 2：

```out
Wrong password: coolman@gplt
Wrong password: coollady@gplt
Welcome in
```

### 思路：

> 用死循环来进行控制，当密码正确、‘#’或者次数耗尽退出循环

### 代码：

```python
passwd, N = input().split()
N = int(N)
while True:
    t = input()
    if t == '#':
        break
    if t == passwd:
        print('Welcome in')
        break
    else:
        print('Wrong password: %s' % t)
    N -= 1
    if N == 0:
        print('Account locked')
        break

```

## **1068 万绿丛中一点红**

对于计算机而言，颜色不过是像素点对应的一个 24 位的数值。现给定一幅分辨率为 *M*×*N* 的画，要求你找出万绿丛中的一点红，即有独一无二颜色的那个像素点，并且该点的颜色与其周围 8 个相邻像素的颜色差充分大。

### 输入格式：

输入第一行给出三个正整数，分别是 *M* 和 *N*（≤ 1000），即图像的分辨率；以及 TOL，是所求像素点与相邻点的颜色差阈值，色差超过 TOL 的点才被考虑。随后 *N* 行，每行给出 *M* 个像素的颜色值，范围在 [0,224) 内。所有同行数字间用空格或 TAB 分开。

### 输出格式：

在一行中按照 `(x, y): color` 的格式输出所求像素点的位置以及颜色值，其中位置 `x` 和 `y` 分别是该像素在图像矩阵中的列、行编号（从 1 开始编号）。如果这样的点不唯一，则输出 `Not Unique`；如果这样的点不存在，则输出 `Not Exist`。

### 输入样例 1：

```in
8 6 200
0      0       0        0        0          0           0        0
65280      65280    65280    16711479 65280    65280    65280    65280
16711479 65280    65280    65280    16711680 65280    65280    65280
65280      65280    65280    65280    65280    65280    165280   165280
65280      65280       16777015 65280    65280    165280   65480    165280
16777215 16777215 16777215 16777215 16777215 16777215 16777215 16777215
```

### 输出样例 1：

```out
(5, 3): 16711680
```

### 输入样例 2：

```in
4 5 2
0 0 0 0
0 0 3 0
0 0 0 0
0 5 0 0
0 0 0 0
```

### 输出样例 2：

```out
Not Unique
```

### 输入样例 3：

```in
3 3 5
1 2 3
3 4 5
5 6 7
```

### 输出样例 3：

```out
Not Exist
```

### 思路：

> 首先用一个dic字典记录每个颜色出现的次数，然后开始判断像素点
>
> 首先出现次数超过一次的跳过，然后判断这个像素点与周围的象素差是否超过TOL，超过记录，最后判断记录个数，超过1个跳出循环结束
>
> 输出的时候判断个数：
>
> 0：输出Not Exist
>
> 1：输出(x, y): color
>
> \>1: 输出Not Unique
>
> 注：判断个数与像素差的判断语句分开写，以减少执行次数
>
> **边缘的也需要考虑**

### 代码：

```python
def judge(i, j, M, N, TOL):
    global lst
    dir = [[-1, 0], [-1, 1], [-1, -1], [0, 1],
           [0, -1], [1, 0], [1, -1], [1, 1]]
    for k in range(8):
        tx = i+dir[k][0]
        ty = j+dir[k][1]
        if 0 <= tx < N and 0 <= ty < M and abs(lst[i][j]-lst[tx][ty]) <= TOL:
            return False
    return True


M, N, TOL = map(int, input().split())
lst = [list(map(int, input().split()))for i in range(N)]
t = {}
for i in range(N):
    for j in range(M):
        t[lst[i][j]] = t.get(lst[i][j], 0)+1
x, y = 0, 0
cnt = 0
for i in range(0, N):
    for j in range(0, M):
        if t[lst[i][j]] != 1:
            continue
        if judge(i, j, M, N, TOL):
            cnt += 1
            x = i+1
            y = j+1
            if cnt > 1:
                break
    if cnt > 1:
        break
if cnt == 0:
    print('Not Exist')
elif cnt > 1:
    print('Not Unique')
else:
    print('(%d, %d): %d' %
          (y, x, lst[x-1][y-1]))

```

## **1069 微博转发抽奖**

小明 PAT 考了满分，高兴之余决定发起微博转发抽奖活动，从转发的网友中按顺序每隔 N 个人就发出一个红包。请你编写程序帮助他确定中奖名单。

### 输入格式：

输入第一行给出三个正整数 M（≤ 1000）、N 和 S，分别是转发的总量、小明决定的中奖间隔、以及第一位中奖者的序号（编号从 1 开始）。随后 M 行，顺序给出转发微博的网友的昵称（不超过 20 个字符、不包含空格回车的非空字符串）。

注意：可能有人转发多次，但不能中奖多次。所以如果处于当前中奖位置的网友已经中过奖，则跳过他顺次取下一位。

### 输出格式：

按照输入的顺序输出中奖名单，每个昵称占一行。如果没有人中奖，则输出 `Keep going...`。

### 输入样例 1：

```in
9 3 2
Imgonnawin!
PickMe
PickMeMeMeee
LookHere
Imgonnawin!
TryAgainAgain
TryAgainAgain
Imgonnawin!
TryAgainAgain
```

### 输出样例 1：

```out
PickMe
Imgonnawin!
TryAgainAgain
```

### 输入样例 2：

```in
2 3 5
Imgonnawin!
PickMe
```

### 输出样例 2：

```out
Keep going...
```

### 思路：

> 输入后第S位为第一个，然后每隔N个判断是否已经获奖，已获奖就跳过，最后无人获奖输出`Keep going...`

### 代码：

```python
M, N, S = map(int, input().split())
lst = []
cnt = N-1
for i in range(0, M):
    t = input()
    S -= 1
    if S > 0:
        continue
    cnt += 1
    if N == cnt:
        if t not in lst:
            lst.append(t)
            cnt = 0
        else:
            cnt -= 1
if len(lst) == 0:
    print('Keep going...')
else:
    for i in lst:
        print(i)

```

## **1070 结绳**

给定一段一段的绳子，你需要把它们串成一条绳。每次串连的时候，是把两段绳子对折，再如下图所示套接在一起。这样得到的绳子又被当成是另一段绳子，可以再次对折去跟另一段绳子串连。每次串连后，原来两段绳子的长度就会减半。

<img src="https://images.ptausercontent.com/46293e57-aa0e-414b-b5c3-7c4b2d5201e2.jpg">

给定 *N* 段绳子的长度，你需要找出它们能串成的绳子的最大长度。

### 输入格式：

每个输入包含 1 个测试用例。每个测试用例第 1 行给出正整数 *N* (2≤*N*≤104)；第 2 行给出 *N* 个正整数，即原始绳段的长度，数字间以空格分隔。所有整数都不超过104。

### 输出格式：

在一行中输出能够串成的绳子的最大长度。结果向下取整，即取为不超过最大长度的最近整数。

### 输入样例：

```in
8
10 15 12 3 4 13 1 15
```

### 输出样例：

```out
14
```

### 思路：

> 将所有绳子按非递减排序，每次取出最短的2个进行串联，串完的绳子加入第一个比他长的绳子前面没有比他长的就加入最后，经过N-1次操作最后的就是绳子的最大长度

### 代码：

```python
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
for i in range(N-1):
    a = lst.pop(0)
    b = lst.pop(0)
    t = int((a+b)/2)
    for j in range(len(lst)):
        if lst[j] > t:
            lst.insert(j, t)
            break
    else:
        lst.append(t)
print(lst[0])

```

