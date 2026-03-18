
import os

# 定义所有文件的路径和内容
PROJECT_FILES = {
    "requirements.txt": r"""
# Sphinx 核心
sphinx==7.2.6
# Read the Docs 主题
sphinx-rtd-theme==2.0.0
# 支持 Markdown
myst-parser==2.0.0
""",

    "source/conf.py": r"""
project = '产品硬件技术文档'
copyright = '2026, YourCompany'
author = 'Hardware Team'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'myst_parser',
]

source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

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
""",

    "source/index.rst": r"""
.. _main-index:

==============================
产品硬件技术文档
==============================

欢迎查阅公司已量产硬件产品的技术文档。

.. toctree::
   :maxdepth: 2
   :caption: GTA01 Series 开发板文档

   gta01/user_guide
""",

    "source/gta01/user_guide.rst": r"""
.. _gta01-user-guide:

==============================
使用指南
==============================

欢迎使用 GTA01 Series 开发板，以下是详细的使用说明。

.. contents:: 本页目录
   :local:
   :depth: 2

----

1. 功能描述
==============================
概述 GTA01 Series 开发板的定位、核心架构、主要性能指标和适用场景。

2. 板卡布局与模块说明
==============================
.. figure:: /_static/images/board_layout.png
   :align: center
   :width: 80%

   图 1：GTA01 Series 板卡布局图

（此处可以补充文字说明各个丝印对应的模块功能）

3. 硬件连接
==============================
描述引脚定义、供电方式、通信接口接线方式以及外部模块的连接指导。

4. 典型应用
==============================
列举使用该开发板可以完成的典型项目、适用行业及案例参考。

5. 注意事项
==============================
- ⚠️ 首次使用前请仔细检查电源接口，避免正负极接反。
- ⚡ 操作核心元件时请注意静电防护，佩戴防静电手环。
- 🔄 固件烧录期间严禁断开 USB 连接线。
""",

    "Makefile": r"""
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
""",

    "make.bat": r"""
@ECHO OFF
pushd %~dp0
if "%SPHINXBUILD%" == "" ( set SPHINXBUILD=sphinx-build )
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
:end
popd
""",

    "source/_static/custom.css": r"""
.wy-table-responsive table td,
.wy-table-responsive table th {
    white-space: normal !important;
    padding: 8px 12px !important;
}
.wy-nav-content { max-width: 900px !important; }
""",

    "source/_templates/layout.html": r"""
{% extends "!layout.html" %}
{% block footer %}
{{ super() }}
<div style="text-align: center; padding: 10px 0; font-size: 12px; color: #888;">
    内部技术文档 · 仅限公司内部使用 · {{ copyright }}
</div>
{% endblock %}
""",

    ".readthedocs.yaml": r"""
version: 2
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
sphinx:
  configuration: source/conf.py
python:
  install:
    - requirements: requirements.txt
""",

    ".gitignore": r"""
build/
venv/
__pycache__/
.DS_Store
"""
}

def create_project():
    print("🚀 开始按照新架构生成 Sphinx 在线文档工程...")
    
    # 1. 生成所有文件
    for file_path, content in PROJECT_FILES.items():
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  ✅ 创建文件: {file_path}")

    # 2. 创建图片空目录
    img_dir = "source/_static/images"
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    with open(os.path.join(img_dir, ".gitkeep"), "w", encoding="utf-8") as f:
        f.write("")
    print(f"  ✅ 创建目录: {img_dir}")

    print("\n🎉 工程生成完毕！")
    print("-" * 40)
    print("👉 下一步请执行：")
    print("   1. 编译文档： make html  (Windows 下运行 make.bat html)")
    print("   2. 预览效果： 浏览器打开 build/html/index.html")

if __name__ == "__main__":
    create_project()
