# -*- coding: utf-8 -*-
"""为每篇文章生成系列风格封面 SVG，并在 front-matter 插入 cover 字段。"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / 'source/images/covers'
OUT.mkdir(parents=True, exist_ok=True)

FONT = "'Microsoft YaHei','PingFang SC','Noto Sans SC',Arial,sans-serif"

# 配色：accent 主色 / tint 背景色 / wash 水印字色
PALETTES = {
    'guide':  ('#7C3AED', '#F5F3FF', '#EDE9FE'),
    'ai':     ('#4F46E5', '#EEF2FF', '#E0E7FF'),
    'sensor': ('#059669', '#ECFDF5', '#D1FAE5'),
    'algo':   ('#D97706', '#FFF7ED', '#FDE68A'),
    'git':    ('#EA580C', '#FFF7ED', '#FFEDD5'),
    'office': ('#0284C7', '#F0F9FF', '#E0F2FE'),
}

# (md 相对路径, slug, 色板, 徽标, 标题行列表, 副标题, 水印大字)
COVERS = [
    ('source/_posts/AI学习/README.md', 'ai-guide', 'guide',
     'AI 学习 · 教学文档', ['教学文档', '总导读'],
     'AI 编程环境搭建 × 传感器监控平台 · 两套零基础实战教程', 'AI'),
    ('source/_posts/AI学习/AI编程环境搭建/01-VSCode与WorkBuddy安装与汉化.md', 'ai-01', 'ai',
     'AI 编程环境搭建 · 第 1 篇', ['装好 VSCode 与 WorkBuddy', '并把界面换成中文'],
     '15 min · 零基础起步 · 免费积分全部领到手', '01'),
    ('source/_posts/AI学习/AI编程环境搭建/02-ZCode与WorkBuddy对比及模型选型.md', 'ai-02', 'ai',
     'AI 编程环境搭建 · 第 2 篇', ['认识 ZCode', '搞清工具与模型怎么选'],
     'WorkBuddy vs ZCode · GLM 套餐 vs DeepSeek API', '02'),
    ('source/_posts/AI学习/AI编程环境搭建/03-用WorkBuddy安装uv与Python3.12.md', 'ai-03', 'ai',
     'AI 编程环境搭建 · 第 3 篇', ['用 WorkBuddy 装好', 'uv 与 Python 3.12'],
     'uv 是什么 · 一条提示词装好整个环境', '03'),
    ('source/_posts/AI学习/AI编程环境搭建/04-VSCode终端配置环境与HelloWorld.md', 'ai-04', 'ai',
     'AI 编程环境搭建 · 第 4 篇', ['VSCode 终端配置环境', '跑通第一个 Hello World'],
     '打开文件夹 · 开终端 · uv 建环境 · 点运行', '04'),
    ('source/_posts/AI学习/AI编程环境搭建/05-用WorkBuddy配置工作区并运行代码.md', 'ai-05', 'ai',
     'AI 编程环境搭建 · 第 5 篇', ['用 WorkBuddy 配好工作区', '在 VSCode 里打开并运行'],
     'AI 路线 · 一条提示词建好一切', '05'),
    ('source/_posts/AI学习/传感器监控平台/README.md', 'sensor-guide', 'sensor',
     '传感器监控平台', ['系列导读'],
     '硬件清单 · RS485 组网 · 协议摘要 · 实战验收', '485'),
    ('source/_posts/AI学习/传感器监控平台/01-环境搭建与项目骨架.md', 'sensor-01', 'sensor',
     '传感器监控平台 · 第 1 篇', ['环境搭建', '与项目骨架'],
     'uv + Python 3.12 + pymodbus / FastAPI 全套依赖', '01'),
    ('source/_posts/AI学习/传感器监控平台/02-串口链路打通与模拟器.md', 'sensor-02', 'sensor',
     '传感器监控平台 · 第 2 篇', ['串口链路打通', '与本地模拟器'],
     '让 AI 读接口文档 · 串口工具 · 免硬件模拟', '02'),
    ('source/_posts/AI学习/传感器监控平台/03-真机接入与总线组网.md', 'sensor-03', 'sensor',
     '传感器监控平台 · 第 3 篇', ['真机接入', '与 RS485 总线组网'],
     '逐台改地址 · 统一波特率 · 485 集线器组网', '03'),
    ('source/_posts/AI学习/传感器监控平台/04-三个传感器驱动开发.md', 'sensor-04', 'sensor',
     '传感器监控平台 · 第 4 篇', ['三个传感器', '驱动开发（核心）'],
     '统一基类 · 三个驱动类 · 三个调试脚本', '04'),
    ('source/_posts/AI学习/传感器监控平台/05-实时采集与控制后端.md', 'sensor-05', 'sensor',
     '传感器监控平台 · 第 5 篇', ['实时采集', '与控制后端'],
     'FastAPI 轮询 · 缓存 · WebSocket 推送', '05'),
    ('source/_posts/AI学习/传感器监控平台/06-前端网页与联调测试.md', 'sensor-06', 'sensor',
     '传感器监控平台 · 第 6 篇', ['前端网页', '与联调测试'],
     '单文件网页 · pytest 自动化 · 整机验收清单', '06'),
    ('source/_posts/Git学习指南.md', 'git-guide', 'git',
     '学习笔记', ['Git 学习指南'],
     '环境准备 · 常用命令 · 团队协作工作流', 'Git'),
    ('source/_posts/Office安装教程.md', 'office-install', 'office',
     '程序安装 · 教程', ['Office 安装教程'],
     'Office Tool Plus · 一键部署与激活', 'Ofc'),
] + [
    (f'source/_posts/刷题/Python刷题记录（{rng}）.md', f'algo-{rng.replace("（", "").replace("）", "")}', 'algo',
     'Python · 刷题记录', [f'第 {rng} 题'],
     '题面复述 · 解题思路 · 参考代码 · 易错点', rng)
    for rng in ['1-10', '11-20', '21-30', '31-40', '41-50',
                '51-60', '61-70', '71-80', '81-90', '91-95']
]


def make_svg(pal_key, badge, title_lines, subtitle, mark):
    accent, tint, wash = PALETTES[pal_key]
    lines = ''
    if len(title_lines) == 1:
        lines = (f'<text x="80" y="400" font-size="66" font-weight="800" '
                 f'fill="#0F172A">{title_lines[0]}</text>')
    else:
        lines = (f'<text x="80" y="330" font-size="62" font-weight="800" '
                 f'fill="#0F172A">{title_lines[0]}</text>'
                 f'<text x="80" y="412" font-size="62" font-weight="800" '
                 f'fill="#0F172A">{title_lines[1]}</text>')
    bw = 36 + 26 * len(badge)  # 徽标宽度按字数粗略估算
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="1200" height="675" font-family="{FONT}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{tint}"/>
      <stop offset="1" stop-color="#F8FAFC"/>
    </linearGradient>
    <pattern id="dots" width="34" height="34" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="2" fill="#CBD5E1" opacity="0.4"/>
    </pattern>
  </defs>
  <rect width="1200" height="675" fill="url(#bg)"/>
  <rect width="1200" height="675" fill="url(#dots)"/>
  <circle cx="1130" cy="60" r="220" fill="{wash}" opacity="0.75"/>
  <circle cx="40" cy="660" r="170" fill="{wash}" opacity="0.65"/>
  <rect x="1152" y="595" width="24" height="24" rx="6" fill="{accent}"/>
  <rect x="1116" y="595" width="24" height="24" rx="6" fill="{accent}" opacity="0.45"/>
  <rect x="1080" y="595" width="24" height="24" rx="6" fill="{accent}" opacity="0.2"/>
  <text x="1130" y="450" text-anchor="end" font-size="230" font-weight="800" fill="{wash}">{mark}</text>
  <g>
    <rect x="80" y="88" width="{bw}" height="48" rx="24" fill="{accent}"/>
    <text x="{80 + bw / 2}" y="120" text-anchor="middle" font-size="24" font-weight="700" fill="#FFFFFF">{badge}</text>
  </g>
  <rect x="80" y="266" width="10" height="{160 if len(title_lines) > 1 else 78}" rx="5" fill="{accent}"/>
  {lines}
  <text x="80" y="500" font-size="27" fill="#64748B">{subtitle}</text>
  <line x1="80" y1="576" x2="1120" y2="576" stroke="#E2E8F0" stroke-width="2"/>
  <text x="80" y="618" font-size="24" font-weight="700" fill="#94A3B8">HuRTTTTR</text>
  <text x="196" y="618" font-size="24" fill="#94A3B8">· hurttttr.github.io</text>
</svg>
'''


for md_rel, slug, pal, badge, titles, sub, mark in COVERS:
    md = ROOT / md_rel
    svg_path = OUT / f'{slug}.svg'
    svg_path.write_text(make_svg(pal, badge, titles, sub, mark), encoding='utf-8')

    raw = md.read_text(encoding='utf-8')
    assert raw.startswith('---\n'), f'{md}: 没有 front-matter'
    cover_line = f'cover: /images/covers/{slug}.svg'
    if re.search(r'(?m)^cover:', raw):
        raw = re.sub(r'(?m)^cover:.*$', cover_line, raw)
    else:
        raw = re.sub(r'(?m)^(title:.*)$', r'\1\n' + cover_line, raw, count=1)
    md.write_text(raw, encoding='utf-8')
    print(f'OK {svg_path.name} -> {md.name}')

print(f'\n共生成 {len(COVERS)} 张封面')
