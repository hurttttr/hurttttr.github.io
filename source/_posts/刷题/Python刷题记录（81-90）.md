---
title: Python刷题记录（81-90）
data: 2023-06-06 12:00:00
type: string
updated: 2023-06-06 12:00:00
tags: Python
categories: 刷题记录
---

题目来源PTA平台

[PAT (Basic Level) Practice （中文）](https://pintia.cn/problem-sets/994805260223102976)

-----------------------

## **1081 检查密码**

本题要求你帮助某网站的用户注册模块写一个密码合法性检查的小功能。该网站要求用户设置的密码必须由不少于6个字符组成，并且只能有英文字母、数字和小数点 `.`，还必须既有字母也有数字。

### 输入格式：

输入第一行给出一个正整数 N（≤ 100），随后 N 行，每行给出一个用户设置的密码，为不超过 80 个字符的非空字符串，以回车结束。

### 输出格式：

对每个用户的密码，在一行中输出系统反馈信息，分以下5种：

- 如果密码合法，输出`Your password is wan mei.`；
- 如果密码太短，不论合法与否，都输出`Your password is tai duan le.`；
- 如果密码长度合法，但存在不合法字符，则输出`Your password is tai luan le.`；
- 如果密码长度合法，但只有字母没有数字，则输出`Your password needs shu zi.`；
- 如果密码长度合法，但只有数字没有字母，则输出`Your password needs zi mu.`。

### 输入样例：

```in
5
123s
zheshi.wodepw
1234.5678
WanMei23333
pass*word.6
```

### 输出样例：

```out
Your password is tai duan le.
Your password needs shu zi.
Your password needs zi mu.
Your password is wan mei.
Your password is tai luan le.
```

### 思路：

> 先判断长度是否合法，合法后遍历并统计字母和数字的个数并判断是否又非法字符，最后判断字母和数字的个数

### 代码：

```python
N = int(input())
for i in range(N):
    t = input()
    if len(t) < 6:
        print('Your password is tai duan le.')
        continue
    else:
        a, b = 0, 0
        for j in t:
            if j.isdigit():
                a += 1
            elif j.isalpha():
                b += 1
            elif j != '.':
                print('Your password is tai luan le.')
                break
        else:
            if a > 0 and b > 0:
                print('Your password is wan mei.')
            elif a > 0:
                print('Your password needs zi mu.')
            elif b > 0:
                print('Your password needs shu zi.')
            continue

```

## **1082 射击比赛**

本题目给出的射击比赛的规则非常简单，谁打的弹洞距离靶心最近，谁就是冠军；谁差得最远，谁就是菜鸟。本题给出一系列弹洞的平面坐标(x,y)，请你编写程序找出冠军和菜鸟。我们假设靶心在原点(0,0)。

### 输入格式：

输入在第一行中给出一个正整数 N（≤ 10 000）。随后 N 行，每行按下列格式给出：

```
ID x y
```

其中 `ID` 是运动员的编号（由 4 位数字组成）；`x` 和 `y` 是其打出的弹洞的平面坐标(`x`,`y`)，均为整数，且 0 ≤ |`x`|, |`y`| ≤ 100。题目保证每个运动员的编号不重复，且每人只打 1 枪。

### 输出格式：

输出冠军和菜鸟的编号，中间空 1 格。题目保证他们是唯一的。

### 输入样例：

```in
3
0001 5 7
1020 -1 3
0233 0 -1
```

### 输出样例：

```out
0233 0001
```

### 思路：

> 用max和min的列表记录菜鸡和冠军的id和距靶心距离，最后输出即可

### 代码：

```python
N = int(input())
max, min = [0, 0], [0, 200]
for i in range(N):
    ID, x, y = map(int, input().split())
    t = (x**2+y**2)**0.5
    if t > max[1]:
        max = [ID, t]
    if t < min[1]:
        min = [ID, t]
print('%04d %04d' % (min[0], max[0]))

```

## **1083 是否存在相等的差**

给定 N 张卡片，正面分别写上 1、2、……、N，然后全部翻面，洗牌，在背面分别写上 1、2、……、N。将每张牌的正反两面数字相减（大减小），得到 N 个非负差值，其中是否存在相等的差？

### 输入格式：

输入第一行给出一个正整数 N（2 ≤ N ≤ 10 000），随后一行给出 1 到 N 的一个洗牌后的排列，第 i 个数表示正面写了 i 的那张卡片背面的数字。

### 输出格式：

按照“差值 重复次数”的格式从大到小输出重复的差值及其重复的次数，每行输出一个结果。

### 输入样例：

```in
8
3 5 8 6 2 1 4 7
```

### 输出样例：

```out
5 2
3 3
2 2
```

### 思路：

> 将每张牌的差值存入列表，利用collections中的Counter函数进行统计个数，按插值从大到小排序后输出个数大于1的

### 代码：

```python
from collections import Counter

N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.append(abs(i+1-lst[i]))
s = Counter(ans)
rst = []
for i in s:
    rst.append([i, s[i]])
rst.sort(key=lambda x: x[0], reverse=True)
for i in rst:
    if i[1] > 1:
        print(i[0], i[1])

```

## **1084 外观数列**

外观数列是指具有以下特点的整数序列：

```
d, d1, d111, d113, d11231, d112213111, ...
```

它从不等于 1 的数字 `d` 开始，序列的第 n+1 项是对第 n 项的描述。比如第 2 项表示第 1 项有 1 个 `d`，所以就是 `d1`；第 2 项是 1 个 `d`（对应 `d1`）和 1 个 1（对应 11），所以第 3 项就是 `d111`。又比如第 4 项是 `d113`，其描述就是 1 个 `d`，2 个 1，1 个 3，所以下一项就是 `d11231`。当然这个定义对 `d` = 1 也成立。本题要求你推算任意给定数字 `d` 的外观数列的第 N 项。

### 输入格式：

输入第一行给出 [0,9] 范围内的一个整数 `d`、以及一个正整数 N（≤ 40），用空格分隔。

### 输出格式：

在一行中给出数字 `d` 的外观数列的第 N 项。

### 输入样例：

```in
1 8
```

### 输出样例：

```out
1123123111
```

### 思路：

> 先建立列表[d,1]，然后循环N-1遍，每次遍历列表，统计个数然后加入列表
>
> N=1的时候单独考虑

### 代码：

```python
d, N = map(int, input().split())
if N==1:
    print(d)
else:
    ans = [d, 1]
    for i in range(2, N):
        t = []
        num = 1
        for j in range(len(ans)-1):
            if ans[j] == ans[j+1]:
                num += 1
            else:
                t.append(ans[j])
                t.append(num)
                num = 1
        t.append(ans[j+1])
        t.append(num)
        ans = t
    print(''.join(str(x)for x in ans))

```

## **1085 PAT单位排行**

每次 PAT 考试结束后，考试中心都会发布一个考生单位排行榜。本题就请你实现这个功能。

### 输入格式：

输入第一行给出一个正整数 N（≤105），即考生人数。随后 N 行，每行按下列格式给出一个考生的信息：

```
准考证号 得分 学校
```

其中`准考证号`是由 6 个字符组成的字符串，其首字母表示考试的级别：`B`代表乙级，`A`代表甲级，`T`代表顶级；`得分`是 [0, 100] 区间内的整数；`学校`是由不超过 6 个英文字母组成的单位码（大小写无关）。注意：题目保证每个考生的准考证号是不同的。

### 输出格式：

首先在一行中输出单位个数。随后按以下格式非降序输出单位的排行榜：

```
排名 学校 加权总分 考生人数
```

其中`排名`是该单位的排名（从 1 开始）；`学校`是全部按小写字母输出的单位码；`加权总分`定义为`乙级总分/1.5 + 甲级总分 + 顶级总分*1.5`的**整数部分**；`考生人数`是该属于单位的考生的总人数。

学校首先按加权总分排行。如有并列，则应对应相同的排名，并按考生人数升序输出。如果仍然并列，则按单位码的字典序输出。

### 输入样例：

```in
10
A57908 85 Au
B57908 54 LanX
A37487 60 au
T28374 67 CMU
T32486 24 hypu
A66734 92 cmu
B76378 71 AU
A47780 45 lanx
A72809 100 pku
A03274 45 hypu
```

### 输出样例：

```out
5
1 cmu 192 2
1 au 192 3
3 pku 100 1
4 hypu 81 2
4 lanx 81 2
```

### 思路：

> 输入后进行一定处理并存入字典，然后将字典转为列表按照成绩，人数，校名的顺序进行排序
>
> 最后遍历输出注意有并列的时候
>
> 但是我写测试点5超时，但是又和网上大佬写的差不多，实在搞不懂

### 代码：

```python
n = eval(input())

dit = {}  # 存入数据
for i in range(n):
    s = input().split()
    # 加权
    if s[0][0] == "A":
        score = int(s[1])
    if s[0][0] == "B":
        score = int(s[1])/1.5
    if s[0][0] == "T":
        score = int(s[1])*1.5

    school = s[2].lower()
    if school not in dit:
        dit[school] = dit.get(school, [0, 0])  # 这句收获贼大，原先没有想到用get()处理字典中存入数据
        dit_list = dit[school]  # 感觉好神奇
        dit_list[0] = score
        dit_list[1] = 1
    else:
        dit_list = dit[school]
        dit_list[0] += score
        dit_list[1] += 1

res_list = []  # 放到数组中再排序，节省操作，妙
for k, v in dit.items():
    res_list.append([k, int(v[0]), v[1]])
res_list = sorted(res_list, key=lambda x: (-x[1], x[2], x[0]))  # 有的升序，有的降序

print(len(dit))
con = 1
s = res_list[0][1]  # 用于存储排名
for i in range(len(res_list)):
    if s != res_list[i][1]:
        con = i+1  # 不是con+=1而是con=i+1解决并列问题
    print("%d %s %d %s" %
          (con, res_list[i][0], res_list[i][1], res_list[i][2]))
    s = res_list[i][1]

#超时代码
'''
import sys

N = int(input())
dic = {}
school_set = set()
for i in range(N):
    z, grade, s = sys.stdin.readline().split()
    grade, s = int(grade), s.lower()
    if z[0] == 'B':
        t = int(grade/1.5)
    elif z[0] == 'A':
        t = grade
    else:
        t = int(grade*1.5)
    if s in school_set:
        dic[s][0] += t
        dic[s][1] += 1
    else:
        school_set.add(s)
        dic[s] = [t, 1]
lst = []
for i, j in dic.items():
    lst.append([i, j[0], j[1]])
lst.sort(key=lambda x: (-x[1], x[2], x[0]))
print(len(lst))
current_grade, index = 0, 1
for i, j in enumerate(lst, start=1):
    if j[1] < current_grade:
        index = i
    sys.stdout.writelines('{} {} {} {}\n'.format(
        index, j[0], j[1], j[2]))
    current_grade = j[1]

'''
```

## **1086 就不告诉你**

做作业的时候，邻座的小盆友问你：“五乘以七等于多少？”你应该不失礼貌地围笑着告诉他：“五十三。”本题就要求你，对任何一对给定的正整数，倒着输出它们的乘积。

<img src="https://images.ptausercontent.com/0c3a4497-27c3-45ea-9c8e-5a1ab2df48af.jpg">

### 输入格式：

输入在第一行给出两个不超过 1000 的正整数 A 和 B，其间以空格分隔。

### 输出格式：

在一行中倒着输出 A 和 B 的乘积。

### 输入样例：

```in
5 7
```

### 输出样例：

```out
53
```

### 思路：

> 将答案转成字符串倒序在转会回nt去0即可

### 代码：

```python
a, b = map(int, input().split())
t = int(str(a*b)[::-1])
print(t)

```

## **1087 有多少不同的值**

当自然数 *n* 依次取 1、2、3、……、*N* 时，算式 ⌊*n*/2⌋+⌊*n*/3⌋+⌊*n*/5⌋ 有多少个不同的值？（注：⌊*x*⌋ 为取整函数，表示不超过 *x* 的最大自然数，即 *x* 的整数部分。）

### 输入格式：

输入给出一个正整数 *N*（2≤*N*≤104）。

### 输出格式：

在一行中输出题面中算式取到的不同值的个数。

### 输入样例：

```in
2017
```

### 输出样例：

```out
1480
```

### 思路：

> 使用set去重，最后len(set)即可

### 代码：

```python
N = int(input())
ans_set = set()
for i in range(1, N+1):
    ans_set.add(i//2+i//3+i//5)
print(len(ans_set))

```

## **1088 三人行**

子曰：“三人行，必有我师焉。择其善者而从之，其不善者而改之。”

本题给定甲、乙、丙三个人的能力值关系为：甲的能力值确定是 2 位正整数；把甲的能力值的 2 个数字调换位置就是乙的能力值；甲乙两人能力差是丙的能力值的 X 倍；乙的能力值是丙的 Y 倍。请你指出谁比你强应“从之”，谁比你弱应“改之”。

### 输入格式：

输入在一行中给出三个数，依次为：M（你自己的能力值）、X 和 Y。三个数字均为不超过 1000 的正整数。

### 输出格式：

在一行中首先输出甲的能力值，随后依次输出甲、乙、丙三人与你的关系：如果其比你强，输出 `Cong`；平等则输出 `Ping`；比你弱则输出 `Gai`。其间以 1 个空格分隔，行首尾不得有多余空格。

注意：如果解不唯一，则以甲的最大解为准进行判断；如果解不存在，则输出 `No Solution`。

### 输入样例 1：

```in
48 3 7
```

### 输出样例 1：

```out
48 Ping Cong Gai
```

### 输入样例 2：

```in
48 11 6
```

### 输出样例 2：

```out
No Solution
```

### 思路：

> 从99到10寻找符合的甲的值，在计算出乙和丙，比较输出即可

### 代码：

```python
def fun(a, b):
    if a > b:
        return 'Cong'
    elif a < b:
        return 'Gai'
    else:
        return 'Ping'


N, x, y = map(int, input().split())
for a in range(99, 10, -1):
    b = a % 10*10+a//10
    if abs(a-b)/x == b/y:
        print('{} {} {} {}'.format(a, fun(a, N), fun(b, N), fun(b/y, N)))
        break
else:
    print('No Solution')

```

### **1089 狼人杀-简单版**

以下文字摘自《灵机一动·好玩的数学》：“狼人杀”游戏分为狼人、好人两大阵营。在一局“狼人杀”游戏中，1 号玩家说：“2 号是狼人”，2 号玩家说：“3 号是好人”，3 号玩家说：“4 号是狼人”，4 号玩家说：“5 号是好人”，5 号玩家说：“4 号是好人”。已知这 5 名玩家中有 2 人扮演狼人角色，有 2 人说的不是实话，有狼人撒谎但并不是所有狼人都在撒谎。扮演狼人角色的是哪两号玩家？

本题是这个问题的升级版：已知 *N* 名玩家中有 2 人扮演狼人角色，有 2 人说的不是实话，有狼人撒谎但并不是所有狼人都在撒谎。要求你找出扮演狼人角色的是哪几号玩家？

### 输入格式：

输入在第一行中给出一个正整数 *N*（5≤*N*≤100）。随后 *N* 行，第 *i* 行给出第 *i* 号玩家说的话（1≤*i*≤*N*），即一个玩家编号，用正号表示好人，负号表示狼人。

### 输出格式：

如果有解，在一行中按递增顺序输出 2 个狼人的编号，其间以空格分隔，行首尾不得有多余空格。如果解不唯一，则输出最小序列解 —— 即对于两个序列 *A*=*a*[1],...,*a*[*M*] 和 *B*=*b*[1],...,*b*[*M*]，若存在 0≤*k*<*M* 使得 *a*[*i*]=*b*[*i*] （*i*≤*k*），且 *a*[*k*+1]<*b*[*k*+1]，则称序列 *A* 小于序列 *B*。若无解则输出 `No Solution`。

### 输入样例 1：

```in
5
-2
+3
-4
+5
+4
```

### 输出样例 1：

```out
1 4
```

### 输入样例 2：

```in
6
+6
+3
+1
-5
-2
+4
```

### 输出样例 2（解不唯一）：

```out
1 5
```

### 输入样例 3：

```in
5
-2
-3
-4
-5
-1
```

### 输出样例 3：

```out
No Solution
```

### 思路：

> 恕我太菜，想的脑壳痛，借用下柳婼大佬的思路，大佬yyds
>
> 每个人说的数字保存在v数组中，i从1～n、j从i+1～n遍历，分别假设i和j是狼人，a数组表示该人是狼人还是好人，等于1表示是好人，等于-1表示是狼人。k从1～n分别判断k所说的话是真是假，k说的话和真实情况不同（即v[k] \* a[abs(v[k])] < 0）则表示k在说谎，则将k放在lie数组中；遍历完成后判断lie数组，如果说谎人数等于2并且这两个说谎的人一个是好人一个是狼人（即a[lie[0]] + a[lie[1]] == 0）表示满足题意，此时输出i和j并return，否则最后的时候输出No Solution

### 代码：

```python
N = int(input())
v = [0]
f = 0
for i in range(N):
    v.append(int(input()))
for i in range(1, N+1):
    for j in range(i+1, N+1):
        lie = []
        a = [1]*(N+1)
        a[i] = a[j] = -1
        for k in range(1, N+1):
            if v[k]*a[abs(v[k])] < 0:
                lie.append(k)
        if len(lie) == 2 and a[lie[0]]+a[lie[1]] == 0:
            print(i, j)
            f = 1
            break
    if f == 1:
        break
if f == 0:
    print('No Solution')

```

## **1090 危险品装箱**

集装箱运输货物时，我们必须特别小心，不能把不相容的货物装在一只箱子里。比如氧化剂绝对不能跟易燃液体同箱，否则很容易造成爆炸。

本题给定一张不相容物品的清单，需要你检查每一张集装箱货品清单，判断它们是否能装在同一只箱子里。

### 输入格式：

输入第一行给出两个正整数：*N* (≤104) 是成对的不相容物品的对数；*M* (≤100) 是集装箱货品清单的单数。

随后数据分两大块给出。第一块有 *N* 行，每行给出一对不相容的物品。第二块有 *M* 行，每行给出一箱货物的清单，格式如下：

```
K G[1] G[2] ... G[K]
```

其中 `K` (≤1000) 是物品件数，`G[i]` 是物品的编号。简单起见，每件物品用一个 5 位数的编号代表。两个数字之间用空格分隔。

### 输出格式：

对每箱货物清单，判断是否可以安全运输。如果没有不相容物品，则在一行中输出 `Yes`，否则输出 `No`。

### 输入样例：

```in
6 3
20001 20002
20003 20004
20005 20006
20003 20001
20005 20004
20004 20006
4 00001 20004 00002 20003
5 98823 20002 20003 20006 10010
3 12345 67890 23333
```

### 输出样例：

```out
No
Yes
Yes
```

### 思路：

> 将不能共存的物品存入字典
>
> 这里使用dic[i]=dic.get(i,[])来进行列表的添加
>
> 随后先判断是否存在字典中，在判断其字典中的列表中的元素是否在清单中
>
> 暴力解决比较无脑

### 代码：

```python
N, M = map(int, input().split())
dic = {}
for i in range(N):
    a, b = input().split()
    dic[a] = dic.get(a, [])
    dic[a].append(b)
    dic[b] = dic.get(b, [])
    dic[b].append(a)
for i in range(M):
    f = 0
    t = input().split()
    for j in t[1:]:
        if j in dic:
            for k in dic[j]:
                if k in t:
                    f = 1
                    print('No')
                break
        if f == 1:
            break
    else:
        print('Yes')

```

