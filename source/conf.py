
# conf.py

# ... (文件顶部保持不变，如 Python 路径设置等) ...

# -- Project information -----------------------------------------------------

project = 'GTA1000 Series Documentation'
copyright = '2026, Giantec'
author = ''
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'myst_parser',
    'sphinx_simplepdf',  # Keep this extension for local build
]

source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

# -- MyST-Parser Configuration -----------------------------------------------
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
}
html_static_path = ['_static']
html_css_files = ['custom.css']

todo_include_todos = True
autosectionlabel_prefix_document = True

numfig = True
numfig_secnum_depth = 1
numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码 %s'
}

# -- Options for LaTeX output --------------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    
    # 彻底禁用自带的旧版双横线章节排版
    'fncychap': '',

    'preamble': r'''
% ==========================================
% Font Settings
% ==========================================
\usepackage{xeCJK}

\renewcommand{\familydefault}{\sfdefault}
\setmainfont{Noto Serif}
\setsansfont{Noto Sans}
\setmonofont{Noto Sans Mono}
\setCJKmainfont{Noto Serif CJK SC}
\setCJKsansfont{Noto Sans CJK SC}
\setCJKmonofont{Noto Sans CJK SC}

\xeCJKsetup{CJKmath=true}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt

% ==========================================
% NXP / 欧美经典硬件手册标题样式
% ==========================================
% ← [改动1] 新增 titlesec 和 xcolor 宏包，统一标题样式和字色
\usepackage{titlesec}
\usepackage{xcolor}

% Chapter（一级标题）：NXP 风格
% ← [改动1详解] 标签行和标题行都显式声明 \Huge，确保字号统一，加 \color{black} 统一为黑色
\titleformat{\chapter}[display]
  {\normalfont\sffamily\bfseries\color{black}\raggedright}
  {\Huge 第 \thechapter\ 章}
  {0.5ex}
  {\Huge}
  [\vspace{1ex}\titlerule]
\titlespacing*{\chapter}{0pt}{-30pt}{30pt}

% Section（二级标题）：黑色无衬线加粗
% ← [改动1] 二级标题也统一为黑色
\titleformat{\section}
  {\normalfont\sffamily\Large\bfseries\color{black}}
  {\thesection}
  {1em}
  {}

% Subsection（三级标题）：黑色无衬线加粗
% ← [改动1] 三级标题也统一为黑色
\titleformat{\subsection}
  {\normalfont\sffamily\large\bfseries\color{black}}
  {\thesubsection}
  {1em}
  {}

% Subsubsection（四级标题）：黑色无衬线加粗
% ← [改动1] 四级标题也统一为黑色
\titleformat{\subsubsection}
  {\normalfont\sffamily\normalsize\bfseries\color{black}}
  {\thesubsubsection}
  {1em}
  {}

% ==========================================
% 修复表格列宽分配不均导致表头文字截断
% ==========================================
\setlength{\tymin}{45pt}

% ==========================================
% 统一页脚样式：仅显示页码（右下角）
% ==========================================
% ← [改动3] 新增 fancyhdr 统一页脚样式
\usepackage{fancyhdr}
\pagestyle{fancy}

% 清空所有默认的页眉页脚内容（移除左边的章节标题等）
\fancyhf{}

% 仅在右下角显示页码
\fancyfoot[R]{\thepage}

% 移除页眉和页脚的分隔线
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% 【关键】让章节首页（plain 样式）也使用相同的简洁页脚
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[R]{\thepage}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}

% ==========================================
% Professional PDF Styling (Sphinx Setup)
% ==========================================
\sphinxsetup{
    hmargin={1in,1in},
    vmargin={1in,1in},
    TitleColor={rgb}{0,0,0},
    % ← [改动2] 链接颜色：调整为标准网页蓝 #0000CC
    % 原值 {0.0,0.3,0.7} (自定义深蓝) → 新值 {0.0,0.0,0.8} (标准网页蓝)
    InnerLinkColor={rgb}{0.0,0.0,0.8},
    OuterLinkColor={rgb}{0.0,0.0,0.8},
    verbatimwithframe=false,
    verbatimwrapslines=true,
}

% ==========================================
% Special Character Handling
% ==========================================
\usepackage{newunicodechar}
\newunicodechar{≥}{\ensuremath{\geq}}
\newunicodechar{≤}{\ensuremath{\leq}}
\newunicodechar{±}{\ensuremath{\pm}}
\newunicodechar{×}{\ensuremath{\times}}
\newunicodechar{÷}{\ensuremath{\div}}
\newunicodechar{≈}{\ensuremath{\approx}}
\newunicodechar{≠}{\ensuremath{\neq}}
\newunicodechar{µ}{\ensuremath{\mu}}
\newunicodechar{Ω}{\ensuremath{\Omega}}

% ==========================================
% 表格深度优化：修复溢出与表头加粗
% ==========================================
\renewcommand{\_}{\textunderscore\allowbreak}
\renewcommand{\sphinxstyletheadfamily}{\bfseries\sffamily}

% ==========================================
\newcommand{\PDFHideContent}[1]{}
% ==========================================

% ==========================================
% Force hide author and date on the cover page
% ==========================================
\makeatletter
\renewcommand{\author}[1]{\gdef\@author{}}
\renewcommand{\date}[1]{\gdef\@date{}}
\makeatother
% ==========================================
''',
    'extraclassoptions': 'openany,oneside',
    'figure_align': 'H',
}

latex_documents = [
    ('index', f'GTA1000_MicBoard_UserGuide_V{release}.tex', 'GTA1000 Series 语音板用户指南',
     '', 'manual'),
]

# -- Options for simplepdf output --------------------------------------------
simplepdf_title = project + '语音板用户指南'
simplepdf_use_toc = True
simplepdf_stylesheets = ['_static/simplepdf.css']
today = ''
