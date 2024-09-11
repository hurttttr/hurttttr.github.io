---
title: Git学习指南
data: 2024-05-20 12:00:00
type: string
updated: 2024-05-20 12:00:00
tags: GitHub
categories: 学习笔记
---

## 环境准备

1. git安装
2. Windows环境安装posh-git（mac：iTerm2+Zsh+oh-my-zsh+Agnoster）
   1. https://zhuanlan.zhihu.com/p/616602512

## 配置

配置用户名（全局）

```
git config --global user.name 'hurttttr'
```

配置邮箱（全局）

```
git config --global user.email '945399100@qq.com'
```

保存配置

```
git config --global credential.helper store
```

查看所有配置

```
git config --global --list
```

## 常用命令

```shell
#初始化仓库
git init [name]  
#查看仓库状态
git statu
#添加到暂存区
git add
#提交
git commit -m "内容"
git commit -am "内容" #提交到暂存区和版本库
#查看提交记录
git log
#查看操作历史记录
git relog
#版本回退
git reset
#查看暂存区内容
git ls-files
#查看差异
git diff
#删除暂存区文件
git rm
git rm --cached #只删除暂存区文件，本地文件保留
#查看远程仓库
git remote -v
git remote add [仓库别名] [地址]
#推送到远程仓库
git push -u [远程仓库名] [分支名] #默认origin main
#拉去远程仓库内容，并自动进行合并
git pull [远程仓库名] [远程分支名]:[本地分支名]
#分支
git branch #查看分支
git branch [新分支名] #创建分支
git branch -d [branch-name] #删除指定的已合并分支
git branch -D [branch-name] #强制删除分支
#返回时间点
git checkout -b [branch-name] [commit-code]
```

## 工作区和文件状态

- 工作区
  - .git所在目录
  - git add 提交到暂存区
- 暂存区
  - .git/index
  - git commit提交到本地仓库
- 本地仓库
  - .git/object

### 文件状态

- 未跟踪（untrack）
  - git add 可以将状态变成未修改/已暂存
- 未修改（unmodified）
  - git rm可以将状态变成未跟踪
- 已修改（modified）
  - git checkout 可以将状态变为未修改
- 已暂存（staged）
  - git reset可以将状态变为已修改
  - git commit可以将状态变为未修改

## 回退版本

- git reset --soft

  - 回退到某一版本，保留工作区和暂存区的所有内容

- git reset --hard

  - 回退到某一版本，丢弃工作区和暂存区的所有内容

  - ```shell
    git reset --hard HEAD^ # HEAD^表示上一个版本
    ```

- git reset --mixed

  - 回退到某一版本，只工作区所有内容

## 查看差异

- 查看工作区、暂存区和本地仓库之间的差异

- 默认比较查看工作区和暂存区的差异

- 比较工作区和版本库之间差异`git diff HEAD`

- 比较暂存区和版本库之间差异`git diff --cached`

- 比较版本库之间差异`git diff 版本1 版本2`

- 比较当前版本和上一个版本的差异`git diff HEAD~(HEAD^) HEAD`

  - HEAD~2 表示之前的第二个版本、

- 比较某个文件当前版本和上一个版本的差异`git diff HEAD~(HEAD^) HEAD filename`

- 比较分支的差异`git diff dev master`


## 删除文件

- 直接删除文件，然后`git add .`删除暂存区内容
- （推荐）使用`git rm`直接删除
  - 同时删除暂存区和工作区内容

## .gitignore文件

需要忽略的文件

> 系统或软件自动生成文件
>
> 编译产生的中间文件和结果文件
>
> 运行时生成日志文件、缓存文件、临时文件
>
> 涉及身份、密码、口令、密钥的敏感文件

- 使用
  - 生成`.gitignore`文件
  - 写入需要忽略的文件，支持通配符
  - 文件夹格式以`/`结尾
  
- 生效前题，这个文件不能是已经被追踪的文件

- 按行从上到下逐行匹配

- 常用忽略模板https://github.com/github/gitignore

## 分支

- 查看分支`git branch` 

- 创建分支`git branch [新分支名]` 
- 切换分支`git checkout/switch [分支名]` 
  - git checkout还具有恢复文件的功能，建议使用`git switch`(>2.32)

- 合并分支`git merge [被合并分支] `，将被合并分支合并到当前分支
  - 合并后会自动产生一次提交
  - `git log --graph --oneline --decorate --all` 查看分支图

- 删除分支`git branch -d [branch-name]`需要已经合并后
  - `git branch -D [branch-name] `强制删除，可删除未合并的分支

- 合并产生冲突后要手动修改冲突文件并再次提交
  - 使用`git merge --abort`中断合并


## rebase变基

- `git rebase [branch-name] `会把当前分支的提交记录合并到指定分支的末尾

