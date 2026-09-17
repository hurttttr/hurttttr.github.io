---
title: "第 4 篇：在 VSCode 里配环境，跑通第一个 Hello World"
date: 2026-09-16 10:30:00
updated: 2026-09-16 10:30:00
tags: [AI编程, WorkBuddy, VSCode, Python]
categories: [AI学习, AI编程环境搭建]
---

# 第 4 篇：在 VSCode 里配环境，跑通第一个 Hello World

> **一句话结论**
> 这一篇走「**手动路线**」：在 VSCode 里**打开文件夹 → 开终端 → 用 uv 建环境 → 写 hello_world.py → 点右上角 ▶ 按钮运行**。
> 最容易出错的一步是**「选解释器」**——选错就会出现「明明装了包却提示找不到」。
> 下一篇（第 5 篇）会走「**AI 路线**」：同样的事交给 WorkBuddy，你只管在 VSCode 里打开并点运行。

![VSCode 配置四步](/images/AI编程环境搭建/04-vscode-steps.svg)

---

## 一、先装 Python 扩展（只做一次）

**VSCode 本身不懂 Python**，装了这个扩展它才认识 `.py` 文件。

```
① 按 Ctrl + Shift + X 打开「扩展」面板
      ↓
② 搜索框输入：Python
      ↓
③ 找到发布者为【Microsoft】的那一个（安装量最高、带蓝色对勾）
      ↓
④ 点「安装」
```

装完之后，它会**自动带上**几个配套扩展：

| 扩展 | 作用 |
| :--- | :--- |
| **Python**（`ms-python.python`） | 核心：运行、调试、环境识别、Jupyter 支持 |
| **Pylance**（`ms-python.vscode-pylance`） | 智能补全、类型检查、跳转定义（体验提升最明显） |
| **Python Debugger**（`ms-python.debugpy`） | 调试支持 |

**命令行一次装齐（可选）：**

```powershell
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension charliermarsh.ruff
code --install-extension tamasfe.even-better-toml
```

**推荐搭配（不是必须，但很舒服）：**

| 扩展                             | 用途                          |
| :----------------------------- | :-------------------------- |
| **Ruff**（`charliermarsh.ruff`） | 极快的代码检查 + 格式化，和 uv 同一团队出品   |
| **Even Better TOML**           | 编辑 `pyproject.toml` 时有高亮和提示 |


---

## 二、在 VSCode 中打开文件夹

**先新建一个空文件夹当项目目录**（例如 `D:\Code\demo`），然后：

```
方式一：菜单栏「文件」→「打开文件夹」→ 选中你的项目目录
方式二：在资源管理器里右键该文件夹 → 「通过 Code 打开」
方式三：在该文件夹里打开终端，敲：code .
```

> ⚠️ **一定要「打开文件夹」，而不是「打开文件」。**
> VSCode 的解释器选择、终端工作目录、相对路径全都是基于「文件夹工作区」的。
> 只打开单个 `.py` 文件，右上角不会出现 ▶ 运行按钮，很多功能也会失效。

打开后，左侧「资源管理器」面板应该显示整个目录内容（空目录则显示文件夹名）。

---

## 三、启用集成终端

三种方式任选：

| 方式 | 操作 |
| :--- | :--- |
| 快捷键 | <kbd>Ctrl</kbd> + <kbd>`</kbd>（反引号，在键盘左上角 Esc 下方） |
| 菜单 | 「终端」→「新建终端」 |
| 命令面板 | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> → 输入 `Terminal: Create New Terminal` |

终端会**自动定位到当前项目目录**，提示符类似：

```text
PS D:\Code\demo>
```

### 3.1 ⭐ 先做三项自检

在终端里依次跑这三条：

| # | 检查什么 | 命令 | 期望结果 |
| :---: | :--- | :--- | :--- |
| 1 | uv 在不在 | `uv --version` | 输出版本号 |
| 2 | Python 装没装 | `uv python list --only-installed` | 列出 3.12.x |
| 3 | 解释器路径 | `uv python find 3.12` | 输出解释器绝对路径 |

> ⚠️ **第 1 条报「无法将"uv"项识别为 cmdlet」怎么办？**
> 说明 PATH 没生效。**把 VSCode 完全关掉再开**——VSCode 会继承**启动那一刻**的环境变量，
> 只在 VSCode 里重开终端往往没用。

---

## 四、用终端完成 uv 环境配置

> 📖 **想先搞清 uv 是什么、它比 pip + venv 强在哪？** 见
> [第 3 篇 · 第一节「先认识 uv」](03-用WorkBuddy安装uv与Python3.12.md#sec-what-is-uv)。
> 本篇默认你已经知道 uv 是干嘛的，直接动手。

在终端里依次执行下面三条命令，**每条执行完再看下一条**。

### 4.1 第一步：初始化项目

```powershell
uv init --python 3.12
```

它会生成项目骨架：

```
demo/
├── .python-version     ← 固定本项目用 3.12
├── pyproject.toml      ← 项目配置与依赖清单
├── README.md
└── main.py             ← 示例入口文件
```

### 4.2 第二步：建虚拟环境

```powershell
uv venv --python 3.12
```

执行后项目里会出现 `.venv` 文件夹。**不用激活它**——`uv run` 会自动认。

> ⚠️ **命令报「No download found」？** 说明 3.12 没装上，回到 [第 3 篇](/2026/09/16/AI学习/AI编程环境搭建/03-用WorkBuddy安装uv与Python3.12/) 补装。

### 4.3 第三步：装个依赖试试

```powershell
uv add requests
```

看到 `Resolved ... Installed ...` 之类的输出就是成功了。

此时项目结构：

```
demo/
├── .venv/              ← 虚拟环境（不用管，也不要提交 Git）
├── .python-version     ← 固定的 Python 版本
├── pyproject.toml      ← 项目配置与依赖清单
├── uv.lock             ← 依赖版本锁文件
└── main.py
```

---

## 五、⭐ 选择解释器（最容易漏的一步）

**为什么重要**：VSCode 里可能同时有系统 Python、uv 装的 Python、多个虚拟环境。
**不指定的话它很可能用错**，结果就是「我明明装了包，代码却报 `ModuleNotFoundError`」。

```
① 按 Ctrl + Shift + P 打开命令面板
      ↓
② 输入并选择：Python: 选择解释器（Python: Select Interpreter）
      ↓
③ 在列表里找到带【.venv】标记的那一项
   形如：Python 3.12.x ('.venv': venv)  .\.venv\Scripts\python.exe
      ↓
④ 点它，选中
```

也可以用**状态栏**快速切换：VSCode 窗口**右下角**会显示当前解释器，点一下就能换。

> ✅ **判断有没有选对**：右下角显示的解释器路径里**应该包含 `.venv`**。

**可选：写进项目配置，避免每次手动选**

在项目根目录建 `.vscode/settings.json`：

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

---

## 六、写 hello_world.py

### 6.1 新建文件

在左侧「资源管理器」里点「新建文件」图标，命名为：

```
hello_world.py
```

> 💡 `.py` 后缀很重要 —— VSCode 靠它识别这是 Python 程序，才会启用语法高亮、补全和 ▶ 运行按钮。

### 6.2 写代码

```python
def main() -> None:
    msg = "Hello, World!"
    print(msg)
    print(f"当前 Python 版本：{__import__('sys').version.split()[0]}")
    print(f"解释器路径：{__import__('sys').executable}")


if __name__ == "__main__":
    main()
```

打字时可以留意：**输入 `msg.` 的时候会弹出可用的方法列表**，这就是 Pylance 在工作。

按 <kbd>Ctrl</kbd> + <kbd>S</kbd> 保存。

---

## 七、⭐ 用 Python 插件「点一下」运行代码

这是本篇的重点——**不用记命令，点鼠标就能跑**。

### 方式一：点右上角的 ▶ 播放键（最推荐）

编辑器**右上角**有一组按钮：

```
  ▶  ⊞  ⋯
  │
  └─ 「运行 Python 文件」
```

点那个 **▶**，VSCode 会在下方弹出终端，自动用你选好的解释器执行，输出类似：

```text
PS D:\Code\demo> & D:/Code/demo/.venv/Scripts/python.exe d:/Code/demo/hello_world.py
Hello, World!
当前 Python 版本：3.12.x
解释器路径：D:\Code\demo\.venv\Scripts\python.exe
```

### 方式二：右键运行

在编辑区**右键** → 「在终端中运行 Python 文件」（Run Python File in Terminal）。

### 方式三：只运行选中的几行

选中若干行 → 按 <kbd>Shift</kbd> + <kbd>Enter</kbd>，只把选中部分送到终端执行。
调试小片段非常好用（这个快捷键来自 Python 扩展）。

### 方式四：调试运行

按 <kbd>F5</kbd> → 选择「Python File」，带调试器运行（见第九节）。

### 补充：终端里用 uv 跑（和虚拟环境天然对齐）

```powershell
uv run hello_world.py
```

> 💡 **什么时候用哪种？**
> 点 ▶ 最省事，**前提是解释器选对了**；`uv run` 不依赖解释器选择，永远用项目 `.venv`，**更不容易出错**。

---

## 八、期望的输出

![终端里期望看到的输出](/images/AI编程环境搭建/04-hello-flow.svg)

```text
Hello, World!
当前 Python 版本：3.12.x
解释器路径：D:\Code\demo\.venv\Scripts\python.exe
```

> ✅ **重点看第三行**：路径里带着 `.venv`，说明 VSCode 用的确实是**项目自己的虚拟环境**，而不是系统 Python。
> 如果这里显示的是 `C:\Users\...\AppData\Local\Programs\Python\...`，说明解释器没选对，回到第五节重选。

---

## 九、试试调试（F5）

调试是 VSCode 相比记事本最大的优势，**值得花 5 分钟体验一次**。

### 9.1 打断点

在代码行号**左侧的空白区域点一下**，会出现一个**红点**，这就是断点。

### 9.2 启动调试

按 <kbd>F5</kbd> → 选「Python File」。程序会在断点处**暂停**，此时：

| 区域 | 你能看到什么 |
| :--- | :--- |
| 左侧「变量」面板 | 当前所有变量的值 |
| 左侧「监视」面板 | 手动添加想盯住的表达式 |
| 顶部调试工具栏 | 继续 / 单步跳过 / 单步进入 / 重启 / 停止 |
| 下方「调试控制台」 | 直接输入表达式求值 |

### 9.3 常用快捷键

| 快捷键 | 作用 |
| :--- | :--- |
| <kbd>F5</kbd> | 开始 / 继续调试 |
| <kbd>F9</kbd> | 在当前行打 / 取消断点 |
| <kbd>F10</kbd> | 单步跳过（不进入函数） |
| <kbd>F11</kbd> | 单步进入（进入函数内部） |
| <kbd>Shift</kbd>+<kbd>F5</kbd> | 停止调试 |

---

## 十、本篇验证清单

| # | 检查项 | 怎么确认 | 通过标准 |
| :---: | :--- | :--- | :--- |
| 1 | Python 扩展已装 | 扩展面板里 Python 显示「已安装」 | ✅ |
| 2 | 项目以文件夹方式打开 | 左侧资源管理器显示整个目录 | ✅ |
| 3 | 终端能定位到项目目录 | 提示符显示项目路径 | ✅ |
| 4 | uv 自检通过 | 三项自检都有正常输出 | ✅ |
| 5 | 虚拟环境已创建 | 项目里存在 `.venv` 文件夹 | ✅ |
| 6 | **解释器已选对** | 右下角路径包含 `.venv` | ✅ |
| 7 | 依赖可用 | `uv run python -c "import requests; print(requests.__version__)"` | 输出版本号 |
| 8 | hello_world.py 能运行 | 点 ▶ 后终端输出 `Hello, World!` | ✅ |
| 9 | 用的是项目环境 | 输出的解释器路径含 `.venv` | ✅ |
| 10 | 断点能停住 | F5 后程序在红点处暂停 | ✅ |

---

## 十一、常见问题

**Q1：搜索扩展一直转圈 / 装不上？**
多为网络问题。多试几次；或在扩展面板右上角 `...` 菜单里切换商店源；公司网络可能需要配代理。

**Q2：右上角没有 ▶ 按钮？**
两个原因：**没装 Python 扩展**，或者**当前文件不是 `.py`**（或没保存）。先确认文件名后缀和保存状态。

**Q3：运行报 `ModuleNotFoundError: No module named 'xxx'`，但我明明装了？**
**99% 是解释器选错了。** 按第五节重新选带 `.venv` 的解释器。
核对方法：终端运行 `uv run python -c "import sys; print(sys.executable)"`，看输出路径和右下角显示的是否一致。

**Q4：右下角显示不了解释器？**
说明当前窗口没打开文件夹，或 Python 扩展没装好。先「文件 → 打开文件夹」，再确认扩展已安装。

**Q5：终端里 `uv` 或 `python` 找不到？**
VSCode 继承的是**启动时**的环境变量。装完 uv 后如果没重启过 VSCode，它可能还不知道。**完全退出 VSCode 再打开**即可。

**Q6：终端里 `python` 不是我要的版本？**
Windows 上可能有多个 Python。推荐 `uv run python xxx.py`，它自动用项目 `.venv` 里的解释器，绕开这个坑。

**Q7：中文输出乱码？**
终端执行 `chcp 65001` 切到 UTF-8。

**Q8：`.venv` 要不要提交到 Git？**
**不要。** 在项目根目录建 `.gitignore`，加上：

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

**Q9：`.venv` 被我删了怎么办？**
重建即可，`pyproject.toml` 和 `uv.lock` 里有完整依赖清单：

```powershell
uv sync
```

---

## 十二、你已经会手动配环境了，下一步让 AI 来

本篇你亲手走完了：**打开文件夹 → 开终端 → uv init/venv → 选解释器 → 写代码 → 点 ▶ 运行**。

[第 5 篇](/2026/09/16/AI学习/AI编程环境搭建/05-用WorkBuddy配置工作区并运行代码/) 会做**完全相同的事**，区别是：
**环境配置和代码都让 WorkBuddy 生成**，你只需要在 VSCode 里打开它建好的工作区、点一下运行。
对比着看，你就能明白「AI 到底替你省了哪几步」。

---

## 十三、参考链接

| 名称 | 链接 |
| :--- | :--- |
| VSCode 官网下载 | <https://code.visualstudio.com/> |
| 官方教程：Getting Started with Python in VS Code | <https://code.visualstudio.com/docs/python/python-tutorial> |
| Python 扩展官方文档 | <https://code.visualstudio.com/docs/python/python-tutorial#_install-the-python-extension> |
| uv 官方文档（环境部分） | <https://docs.astral.sh/uv/> |

---

⬅️ 上一篇：[第 3 篇 · 用 WorkBuddy 安装 uv 与 Python 3.12](/2026/09/16/AI学习/AI编程环境搭建/03-用WorkBuddy安装uv与Python3.12/)　|　➡️ 下一篇：[第 5 篇 · 用 WorkBuddy 配置工作区并运行代码](/2026/09/16/AI学习/AI编程环境搭建/05-用WorkBuddy配置工作区并运行代码/)
