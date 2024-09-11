---
title: Python刷题记录（51-60）
data: 2023-06-06 12:00:00
type: string
updated: 2023-06-06 12:00:00
tags: Python
categories: 刷题记录
---

题目来源PTA平台

[PAT (Basic Level) Practice （中文）](https://pintia.cn/problem-sets/994805260223102976)

-------------

## **1051 复数乘法**

复数可以写成 (*A*+*B**i*) 的常规形式，其中 *A* 是实部，*B* 是虚部，*i* 是虚数单位，满足 *i*2=−1；也可以写成极坐标下的指数形式 (*R*×*e*(*P**i*))，其中 *R* 是复数模，*P* 是辐角，*i* 是虚数单位，其等价于三角形式 *R*(cos(*P*)+*i*sin(*P*))。

现给定两个复数的 *R* 和 *P*，要求输出两数乘积的常规形式。

### 输入格式：

输入在一行中依次给出两个复数的 *R*1, *P*1, *R*2, *P*2，数字间以空格分隔。

### 输出格式：

在一行中按照 `A+Bi` 的格式输出两数乘积的常规形式，实部和虚部均保留 2 位小数。注意：如果 `B` 是负数，则应该写成 `A-|B|i` 的形式。

### 输入样例：

```in
2.3 3.5 5.2 0.4
```

### 输出样例：

```out
-8.68-8.23i
```

### 思路：

> 看不太懂计算过程，借鉴了网上的思路
>
> 唯一要点就是AB的值在-0.05~0的区间时输出0.00

### 代码：

```python
import math

R1, P1, R2, P2 = map(eval, input().split())
A = R1*R2*math.cos(P1)*math.cos(P2)-R1*R2*math.sin(P1)*math.sin(P2)
B = R1*R2*math.cos(P1)*math.sin(P2)+R2*R1*math.sin(P1)*math.cos(P2)
if -0.005 <= A < 0:
    print('0.00', end='')
else:
    print('%.2f' % A, end='')
if B >= 0:
    print('+%.2fi' % B)
elif -0.005 <= B < 0:
    print('+0.00i')
else:
    print('%.2fi' % B)

```

## **1052 卖个萌**

萌萌哒表情符号通常由“手”、“眼”、“口”三个主要部分组成。简单起见，我们假设一个表情符号是按下列格式输出的：

```
[左手]([左眼][口][右眼])[右手]
```

现给出可选用的符号集合，请你按用户的要求输出表情。

### 输入格式：

输入首先在前三行顺序对应给出手、眼、口的可选符号集。每个符号括在一对方括号 `[]`内。题目保证每个集合都至少有一个符号，并不超过 10 个符号；每个符号包含 1 到 4 个非空字符。

之后一行给出一个正整数 K，为用户请求的个数。随后 K 行，每行给出一个用户的符号选择，顺序为左手、左眼、口、右眼、右手——这里只给出符号在相应集合中的序号（从 1 开始），数字间以空格分隔。

### 输出格式：

对每个用户请求，在一行中输出生成的表情。若用户选择的序号不存在，则输出 `Are you kidding me? @\/@`。

### 输入样例：

```in
[╮][╭][o][~\][/~]  [<][>]
 [╯][╰][^][-][=][>][<][@][⊙]
[Д][▽][_][ε][^]  ...
4
1 1 2 2 2
6 8 1 5 5
3 3 4 3 3
2 10 3 9 3
```

### 输出样例：

```out
╮(╯▽╰)╭
<(@Д=)/~
o(^ε^)o
Are you kidding me? @\/@
```

### 思路：

> 编写一个函数取出[]中内容，判断序号是否合法在输出即可
>
> 需注意序号是否小于1，个数是否多余6，是否超过了符号集合的个数
>
> 但是python3做题会造成非零返回的错误，找到了网上大佬的文章并稍加修改后完美解决
>
> 地址：https://blog.csdn.net/u012949658/article/details/107474885

### 代码：

```python
import sys
l = []
for i in range(3):
    try:
        data = sys.stdin.buffer.readline()
    except:
        while True:
            a = 1
    d = []
    s = bytes()
    for j in range(len(data)-1):
        if data[j:j+1] == b'[':
            s = bytes()
            continue
        if data[j:j+1] == b']':
            d.append(s)
            continue
        s += data[j:j+1]
    l.append(d)

k = int(input())

for i in range(k):
    num = []
    try:
        for j in input().split():
            j = int(j)-1
            if j < 0:
                raise BufferError
            num.append(j)
        if len(num) != 5:
            raise BufferError
        if num[0] >= len(l[0]) or num[4] >= len(l[0]) or num[1] >= len(l[1]) or num[3] >= len(l[1]) or num[2] >= len(l[2]):
            raise BufferError
        result = l[0][num[0]]+b'('+l[1][num[1]]+l[2][num[2]] + \
            l[1][num[3]]+b')'+l[0][num[4]]+b'\n'
    except BufferError:
        result = b'Are you kidding me? @\/@\n'
    sys.stdout.buffer.write(result)

```

## **1053 住房空置率**

在不打扰居民的前提下，统计住房空置率的一种方法是根据每户用电量的连续变化规律进行判断。判断方法如下：

- 在观察期内，若存在超过一半的日子用电量低于某给定的阈值 *e*，则该住房为“可能空置”；
- 若观察期超过某给定阈值 *D* 天，且满足上一个条件，则该住房为“空置”。

现给定某居民区的住户用电量数据，请你统计“可能空置”的比率和“空置”比率，即以上两种状态的住房占居民区住房总套数的百分比。

### 输入格式：

输入第一行给出正整数 *N*（≤1000），为居民区住房总套数；正实数 *e*，即低电量阈值；正整数 *D*，即观察期阈值。随后 *N* 行，每行按以下格式给出一套住房的用电量数据：

*K* *E*1 *E*2 ... *E**K*

其中 *K* 为观察的天数，*E**i* 为第 *i* 天的用电量。

### 输出格式：

在一行中输出“可能空置”的比率和“空置”比率的百分比值，其间以一个空格分隔，保留小数点后 1 位。

### 输入样例：

```in
5 0.5 10
6 0.3 0.4 0.5 0.2 0.8 0.6
10 0.0 0.1 0.2 0.3 0.0 0.8 0.6 0.7 0.0 0.5
5 0.4 0.3 0.5 0.1 0.7
11 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1
11 2 2 2 1 1 0.1 1 0.1 0.1 0.1 0.1
```

### 输出样例：

```out
40.0% 20.0%
```

（样例解释：第2、3户为“可能空置”，第4户为“空置”，其他户不是空置。）

### 思路：

> 输入后判断就行了，难度不大，但是测试点2的数据有点大，原本采用eval函数进行偷懒，结果导致超时
>
> 验证得出eval函数比起一般的强制转换函数要慢几十倍，经量少用吧

### 代码：

```python
N, e, D = input().split()
N, e, D, maybeempty, empty = int(N), float(e), int(D), 0, 0
for i in range(N):
    t = input().split()
    count = 0
    for j in t[1:]:
        if float(j) < e:
            count += 1
    if count > int(t[0])//2:
        if int(t[0]) > D:
            empty += 1
        else:
            maybeempty += 1
print('%.1f%% %.1f%%' % (maybeempty/N*100, empty/N*100))

```

## **1054 求平均值** 

本题的基本要求非常简单：给定 *N* 个实数，计算它们的平均值。但复杂的是有些输入数据可能是非法的。一个“合法”的输入是 [−1000,1000] 区间内的实数，并且最多精确到小数点后 2 位。当你计算平均值的时候，不能把那些非法的数据算在内。

### 输入格式：

输入第一行给出正整数 *N*（≤100）。随后一行给出 *N* 个实数，数字间以一个空格分隔。

### 输出格式：

对每个非法输入，在一行中输出 `ERROR: X is not a legal number`，其中 `X` 是输入。最后在一行中输出结果：`The average of K numbers is Y`，其中 `K` 是合法输入的个数，`Y` 是它们的平均值，精确到小数点后 2 位。如果平均值无法计算，则用 `Undefined` 替换 `Y`。如果 `K` 为 1，则输出 `The average of 1 number is Y`。

### 输入样例 1：

```in
7
5 -3.2 aaa 9999 2.3.4 7.123 2.35
```

### 输出样例 1：

```out
ERROR: aaa is not a legal number
ERROR: 9999 is not a legal number
ERROR: 2.3.4 is not a legal number
ERROR: 7.123 is not a legal number
The average of 3 numbers is 1.38
```

### 输入样例 2：

```in
2
aaa -9999
```

### 输出样例 2：

```out
ERROR: aaa is not a legal number
ERROR: -9999 is not a legal number
The average of 0 numbers is Undefined
```

### 思路：

> 输入判断后判断是否合法，合法累加，不合法输出erroe即可
>
> 注意点：合法数据只有一个的时候输出number

### 代码：

```python
N = int(input())
t = input().split()
sum, num = 0, 0
for i in t:
    try:
        t = float(i)
        if t > 1000 or t < -1000 or (i.find('.') != -1 and len(i)-i.find('.') > 3):
            print('ERROR: %s is not a legal number' % i)
            continue
        sum += t
        num += 1
    except:
        print('ERROR: %s is not a legal number' % i)
if num == 0:
    print('The average of 0 numbers is Undefined')
elif num==1:
    print('The average of 1 number is %.2f' % sum)
else:
    print('The average of %d numbers is %.2f' % (num, sum/num))

```

## **1055 集体照**

拍集体照时队形很重要，这里对给定的 *N* 个人 *K* 排的队形设计排队规则如下：

- 每排人数为 *N*/*K*（向下取整），多出来的人全部站在最后一排；
- 后排所有人的个子都不比前排任何人矮；
- 每排中最高者站中间（中间位置为 *m*/2+1，其中 *m* 为该排人数，除法向下取整）；
- 每排其他人以中间人为轴，按身高非增序，先右后左交替入队站在中间人的两侧（例如5人身高为190、188、186、175、170，则队形为175、188、190、186、170。这里假设你面对拍照者，所以你的左边是中间人的右边）；
- 若多人身高相同，则按名字的字典序升序排列。这里保证无重名。

现给定一组拍照人，请编写程序输出他们的队形。

### 输入格式：

每个输入包含 1 个测试用例。每个测试用例第 1 行给出两个正整数 *N*（≤104，总人数）和 *K*（≤10，总排数）。随后 *N* 行，每行给出一个人的名字（不包含空格、长度不超过 8 个英文字母）和身高（[30, 300] 区间内的整数）。

### 输出格式：

输出拍照的队形。即K排人名，其间以空格分隔，行末不得有多余空格。注意：假设你面对拍照者，后排的人输出在上方，前排输出在下方。

### 输入样例：

```in
10 3
Tom 188
Mike 170
Eva 168
Tim 160
Joe 190
Ann 168
Bob 175
Nick 186
Amy 160
John 159
```

### 输出样例：

```out
Bob Tom Joe Nick
Ann Mike Eva
Tim Amy John
```

### 思路：

> 输入后按照高度和姓名进行排序
>
> 先计算每一排的人数，然后利用python中的insert和append函数进行头插和尾插，注意奇偶即可

### 代码：

```python
N, K = map(int, input().split())
lst = [input().split()for i in range(N)]
lst.sort(key=lambda x: (-int(x[1]), x[0]))
for i in range(K):
    if i == 0:
        t = N//K+N % K
    else:
        t = N//K
    rst = []
    if t % 2 == 0:
        for j in range(t):
            if j % 2 == 0:
                rst.append(lst.pop(0)[0])
            else:
                rst.insert(0, lst.pop(0)[0])
    else:
        rst.append(lst.pop(0)[0])
        for j in range(t-1):
            if j % 2 == 0:
                rst.insert(0, lst.pop(0)[0])
            else:
                rst.append(lst.pop(0)[0])
    print(' '.join(rst))

```



## **1056 组合数的和** 

给定 N 个非 0 的个位数字，用其中任意 2 个数字都可以组合成 1 个 2 位的数字。要求所有可能组合出来的 2 位数字的和。例如给定 2、5、8，则可以组合出：25、28、52、58、82、85，它们的和为330。

### 输入格式：

输入在一行中先给出 N（1 < N < 10），随后给出 N 个不同的非 0 个位数字。数字间以空格分隔。

### 输出格式：

输出所有可能组合出来的2位数字的和。

### 输入样例：

```in
3 2 8 5
```

### 输出样例：

```out
330
```

### 思路：

> 双重for循环轻松解决问题，注意别少和别多就行

### 代码：

```python
lst = list(map(int, input().split()))
sum = 0
for i in range(1, len(lst)):
    for j in range(1, len(lst)):
        if i != j:
            sum += lst[i]*10+lst[j]
print(sum)

```

## **1057 数零壹**

给定一串长度不超过 105 的字符串，本题要求你将其中所有英文字母的序号（字母 a-z 对应序号 1-26，不分大小写）相加，得到整数 N，然后再分析一下 N 的二进制表示中有多少 0、多少 1。例如给定字符串 `PAT (Basic)`，其字母序号之和为：16+1+20+2+1+19+9+3=71，而 71 的二进制是 1000111，即有 3 个 0、4 个 1。

### 输入格式：

输入在一行中给出长度不超过 105、以回车结束的字符串。

### 输出格式：

在一行中先后输出 0 的个数和 1 的个数，其间以空格分隔。注意：若字符串中不存在字母，则视为 N 不存在，也就没有 0 和 1。

### 输入样例：

```in
PAT (Basic)
```

### 输出样例：

```out
3 4
```

**鸣谢浙江工业大学之江学院石洗凡老师补充题面说明。**

### 思路：

> 用数组存储个数相加然后转二进制统计01个数即可
>
> 注意不存在字母输出`0 0`

### 代码：

```python
lst = input().upper()
a = [0]*26
for i in lst:
    if i.isalpha():
        a[ord(i)-65] += 1
sum = 0
for i, j in enumerate(a):
    sum += (i+1)*j
if sum == 0:
    print('0 0')
else:
    t = bin(sum)
    print(t[2:].count('0'), t[2:].count('1'))

```

## **1058 选择题**

批改多选题是比较麻烦的事情，本题就请你写个程序帮助老师批改多选题，并且指出哪道题错的人最多。

### 输入格式：

输入在第一行给出两个正整数 N（≤ 1000）和 M（≤ 100），分别是学生人数和多选题的个数。随后 M 行，每行顺次给出一道题的满分值（不超过 5 的正整数）、选项个数（不少于 2 且不超过 5 的正整数）、正确选项个数（不超过选项个数的正整数）、所有正确选项。注意每题的选项从小写英文字母 a 开始顺次排列。各项间以 1 个空格分隔。最后 N 行，每行给出一个学生的答题情况，其每题答案格式为 `(选中的选项个数 选项1 ……)`，按题目顺序给出。注意：题目保证学生的答题情况是合法的，即不存在选中的选项数超过实际选项数的情况。

### 输出格式：

按照输入的顺序给出每个学生的得分，每个分数占一行。注意判题时只有选择全部正确才能得到该题的分数。最后一行输出错得最多的题目的错误次数和编号（题目按照输入的顺序从 1 开始编号）。如果有并列，则按编号递增顺序输出。数字间用空格分隔，行首尾不得有多余空格。如果所有题目都没有人错，则在最后一行输出 `Too simple`。

### 输入样例：

```in
3 4 
3 4 2 a c
2 5 1 b
5 3 2 b c
1 5 4 a b d e
(2 a c) (2 b d) (2 a c) (3 a b e)
(2 a c) (1 b) (2 a b) (4 a b d e)
(2 b d) (1 e) (2 b c) (4 a b c d)
```

### 输出样例：

```out
3
6
5
2 2 3 4
```

### 思路：

> 用函数提取括号内的内容，与正确答案匹配，然后记录错题输就行了
>
> 题目不难就是有点繁琐
>
> 注意测试点1是没有人错的情况，测试点3超时使用sys函数的输入即可

### 代码：

```python
import sys


def fun(n):
    t = []
    for i, j in enumerate(n):
        if j == '(':
            k = i
        elif j == ')':
            t.append(n[k+1:i])
    return t


N, M = map(int, input().split())
lst = [sys.stdin.readline()for i in range(M)]
student = [sys.stdin.readline()for i in range(N)]
a = [0]*M
for i in student:
    ans = 0
    t = fun(i)
    for j in range(M):
        if t[j] == lst[j][4:-1]:
            ans += int(lst[j][0])
        else:
            a[j] += 1
    print(ans)
t = max(a)
if t == 0:
    print('Too simple')
else:
    print(t, end='')
    for i in range(M):
        if a[i] == t:
            print(' %d' % (i+1), end='')

```

## **1059 C语言竞赛**

C 语言竞赛是浙江大学计算机学院主持的一个欢乐的竞赛。既然竞赛主旨是为了好玩，颁奖规则也就制定得很滑稽：

- 0、冠军将赢得一份“神秘大奖”（比如很巨大的一本学生研究论文集……）。
- 1、排名为素数的学生将赢得最好的奖品 —— 小黄人玩偶！
- 2、其他人将得到巧克力。

给定比赛的最终排名以及一系列参赛者的 ID，你要给出这些参赛者应该获得的奖品。

### 输入格式：

输入第一行给出一个正整数 *N*（≤104），是参赛者人数。随后 *N* 行给出最终排名，每行按排名顺序给出一位参赛者的 ID（4 位数字组成）。接下来给出一个正整数 *K* 以及 *K* 个需要查询的 ID。

### 输出格式：

对每个要查询的 ID，在一行中输出 `ID: 奖品`，其中奖品或者是 `Mystery Award`（神秘大奖）、或者是 `Minion`（小黄人）、或者是 `Chocolate`（巧克力）。如果所查 ID 根本不在排名里，打印 `Are you kidding?`（耍我呢？）。如果该 ID 已经查过了（即奖品已经领过了），打印 `ID: Checked`（不能多吃多占）。

### 输入样例：

```in
6
1111
6666
8888
1234
5555
0001
6
8888
0001
1111
2222
8888
2222
```

### 输出样例：

```out
8888: Minion
0001: Chocolate
1111: Mystery Award
2222: Are you kidding?
8888: Checked
2222: Are you kidding?
```

### 思路：

> 用字典存储排名，减少查询时间
>
> 进行查询时按照要求进行输出，查询后排名置为-1表明查询过
>
> 按上述进行优化，可以避免超时

### 代码：

```python
def isprim(a):
    if a == 2:
        return 1
    elif a % 2 == 0 or a == 1:
        return 0
    else:
        for i in range(3, int(a**0.5)+2, 2):
            if a % i == 0:
                return 0
        return 1


N = int(input())
rank = {}
for i in range(N):
    name = input()
    rank[name] = i+1
K = int(input())
for i in range(K):
    t = input()
    if t in rank:
        if rank[t] == -1:
            s = t+': Checked'
        elif rank[t] == 1:
            s = t+': Mystery Award'
        else:
            if isprim(rank[t]) == 1:
                s = t+': Minion'
            else:
                s = t+': Chocolate'
        rank[t] = -1
    else:
        s = t+': Are you kidding?'
    print(s)

```

## **1060 爱丁顿数** 

英国天文学家爱丁顿很喜欢骑车。据说他为了炫耀自己的骑车功力，还定义了一个“爱丁顿数” *E* ，即满足有 *E* 天骑车超过 *E* 英里的最大整数 *E*。据说爱丁顿自己的 *E* 等于87。

现给定某人 *N* 天的骑车距离，请你算出对应的爱丁顿数 *E*（≤*N*）。

### 输入格式：

输入第一行给出一个正整数 *N* (≤105)，即连续骑车的天数；第二行给出 *N* 个非负整数，代表每天的骑车距离。

### 输出格式：

在一行中给出 *N* 天的爱丁顿数。

### 输入样例：

```in
10
6 7 6 9 3 10 8 2 7 8
```

### 输出样例：

```out
6
```

### 思路：

> 将距离按非升序排序，只要距离比第i天打，E就+1

### 代码：

```python
N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
ans = 0
for i in range(N):
    if lst[i] > i+1:
        ans += 1
print(ans)

```

