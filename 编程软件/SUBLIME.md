# SUBLIME

> 向军大叔每晚八点在 [抖音 (opens new window)](https://live.douyin.com/houdunren)和 [bilibli (opens new window)](https://space.bilibili.com/282190994)直播

<img src="https://doc.houdunren.com/assets/img/xj.161cc3f2.jpg" alt="xj-small" style="zoom:40%;" />

sublime Text 是一个代码编辑器（Sublime Text 2 是收费软件，但可以无限期试用），也是 HTML 和散文先进的文本编辑器。Sublime Text 是由程序员 Jon Skinner 于 2008 年 1 月份所开发出来，它最初被设计为一个具有丰富扩展功能的[Vim (opens new window)](https://baike.baidu.com/item/Vim)。

Sublime Text 具有漂亮的用户界面和强大的功能，并且是一个跨平台的编辑器，同时支持[Windows (opens new window)](https://baike.baidu.com/item/Windows)、[Linux (opens new window)](https://baike.baidu.com/item/Linux)、[Mac OS X (opens new window)](https://baike.baidu.com/item/Mac OS X)等操作系统。

登录官网下载 https://www.sublimetext.com/

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#包管理)包管理

sublime 可以通过扩展包来丰富编码功能，扩展插件网站：https://packagecontrol.io/

**操作步骤**

1. 以下内容基于已经你已经在你的 SublimeText 中安装了 package control
2. 通过快捷键组合 ctrl+shift+P 唤出命令面板
3. 在面板中输入“install package”后回车
4. 接着输入插件名称如：“emmet” 回车即可（观察状态栏进度，晃动的等号）

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#软件风格)软件风格

风格包网站: https://packagecontrol.io](https://packagecontrol.io/)

风格包: Spacegray：

```text
https://packagecontrol.io/packages/Theme%20-%20Spacegray
```

1. Preferences > color scheme >theme-spacegray
2. Preferences-> setting 中设置以下

```text
"theme": "Spacegray.sublime-theme",
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme"
```

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#资源图标)资源图标

包地址：https://github.com/ihodev/a-file-icon

安装方式：

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Package Control: Install Package`
3. Find `A File Icon` and hit `Enter`

\##常用插件

1. emmet：快速编写 html/css https://docs.emmet.io
2. docblockr：代码注释提示插件 https://packagecontrol.io/packages/DocBlockr
3. sideBarEnhancements ：扩展左侧面板 https://packagecontrol.io/packages/SideBarEnhancements
4. SideBarTools：扩展左侧面板 https://packagecontrol.io/packages/SideBarTools
5. AdvancedNewFile：快速创建文件 ，使用 ctrl+alt+n 就可以快速创建文件
6. Local History：本地历史记录 https://packagecontrol.io/packages/Local%20History
7. Laravel 5 Artisan：laravel 命令行插件 https://packagecontrol.io/packages/Laravel%205%20Artisan 按 ctrol+shift+p 搜索并执行命令
8. Laravel 5 Snippets：laravel 代码片段 https://packagecontrol.io/packages/Laravel%205%20Snippets
9. Laravel Blade Highlighter：laravel blade 模板高亮 https://packagecontrol.io/packages/Laravel%20Blade%20Highlighter
10. Blade Snippets：blade 代码片段 https://packagecontrol.io/packages/Blade%20Snippets
11. Laravel Blade AutoComplete：自动识别 blade 父级模板内容 https://packagecontrol.io/packages/Laravel%20Blade%20AutoComplete
12. Bootstrap 3 Snippets：bootstrap 代码片段 https://github.com/JasonMortonNZ/bs3-sublime-plugin
13. Bootstrap 3 Autocomplete：bootstrap 样式提示 https://packagecontrol.io/packages/Bootstrap%203%20Autocomplete
14. Bootstrap 4 Snippets：bootstrap 代码提示 https://packagecontrol.io/packages/Bootstrap%204%20Snippets
15. Bootstrap 4 Autocomplete：bootstrap4 自动提示：https://packagecontrol.io/packages/Bootstrap%204%20Autocomplete
16. SCSS：scss 代码提示 https://packagecontrol.io/packages/SCSS
17. Sass：scss 语法高亮 https://packagecontrol.io/packages/Sass

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#less)LESS

安装 node [https://nodejs.org/zh-cn/(opens new window)](https://nodejs.org/zh-cn/)

**编译环境**

```text
npm install -g less@2.7.3
npm install -g less-plugin-clean-css
npm install -g less-plugin-autoprefix
```

> mac&linux 系统使用 sudo 安装

设置好之后，在命令行中输入 lessc，如果有如下提示则表示设置成功：

```text
C:\Users\hdxj>lessc
lessc.wsf: no input files
Usage:
Single file: cscript //nologo lessc.wsf input.less [output.css] [-compre
Directory:   cscript //nologo lessc.wsf inputdir outputdir [-compress]
```

**插件**

sublime 需要安装两个插件一个是编译 less 文件，一个是语法高亮

1. https://packagecontrol.io/packages/Less2Css
2. https://packagecontrol.io/packages/LESS

这时可以在 Sublime Text 中打开或者新建一个 less 文件，按下 Ctrl+S 保存，此时应该会在 less 文件的相同目录下生成同名的 css 文件。

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#格式化)格式化

首先通过以下路径打开用户按键绑定文件：

Preferences → Key Bindings – User

然后在其中添加以下代码（如果你有需要的话，其中的快捷键组合是可以自己定义的）：

```text
[
	//格式化代码,single_line参数删除时，格式化只影响当前光标所在行
	{"keys": ["ctrl+alt+l"], "command": "reindent" , "args": {"single_line": false}}
]
```

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#内容检索)内容检索

**快速查找**

默认情况下，Sublime Text 支持函数快速查找，按 Ctrl+Shift+R 打开查找面板，就可以快速定位函数所在的文件，如果安装了 emmet 插件将会失效，我们需要做以下操作进行修复。

编辑 emmet 插件配置项：

```text
{"disabled_keymap_actions": "reflect_css_value"}
```

**代码跟踪**

鼠标移动到函数上面，会自动显示方法的文件列表。或按 f12 键显示函数的文件列表

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#快捷键)快捷键

使用快捷键可以显著提高开发效率，所以还是有必要掌握的。

1. 搜索文件：ctrl+p 输入文件名
2. 搜索函数/方法：ctrl+p 输入`“文件名@方法名”` 如 User@show
3. 跳转到指定行：ctrl+p 输入`文件名:行号`,只输入: 时在当前文件跳转
4. 查找当前文件方法：ctrl+r
5. 返回/前进编辑位置：Alt + -、Alt + Shift + -
6. 切换标签页：Ctrl + PgUp、Ctrl + PgDn
7. 选中单词：Ctrl + D 连续按会选中页面中所有单词，以实现批量编辑
8. 以单词为单位快速移动光标：Ctrl + ←、Ctrl + →
9. 选中当前行：Ctrl + L
10. 跳转到第几行：Ctrl+G
11. 跳转到对应括号：Ctrl+M
12. 开关侧栏：Ctrl+K+B
13. 选中当前括号内容，重复可选着括号本身：Ctrl+Shift+M
14. 注释当前 html 标签块：Ctrl+Shift+/
15. 专注编写模式：Shift+F11
16. 分屏显示：Alt+Shift+数字
17. Ctrl+Enter 在下一行插入新行。举个栗子：即使光标不在行尾，也能快速向下插入一行。
18. Ctrl+Shift+Enter 在上一行插入新行。举个栗子：即使光标不在行首，也能快速向上插入一行。
19. Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。
20. Ctrl+Shift+] 选中代码，按下快捷键，展开代码。
# SUBLIME

> 向军大叔每晚八点在 [抖音 (opens new window)](https://live.douyin.com/houdunren)和 [bilibli (opens new window)](https://space.bilibili.com/282190994)直播

<img src="https://doc.houdunren.com/assets/img/xj.161cc3f2.jpg" alt="xj-small" style="zoom:40%;" />

sublime Text 是一个代码编辑器（Sublime Text 2 是收费软件，但可以无限期试用），也是 HTML 和散文先进的文本编辑器。Sublime Text 是由程序员 Jon Skinner 于 2008 年 1 月份所开发出来，它最初被设计为一个具有丰富扩展功能的[Vim (opens new window)](https://baike.baidu.com/item/Vim)。

Sublime Text 具有漂亮的用户界面和强大的功能，并且是一个跨平台的编辑器，同时支持[Windows (opens new window)](https://baike.baidu.com/item/Windows)、[Linux (opens new window)](https://baike.baidu.com/item/Linux)、[Mac OS X (opens new window)](https://baike.baidu.com/item/Mac OS X)等操作系统。

登录官网下载 https://www.sublimetext.com/

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#包管理)包管理

sublime 可以通过扩展包来丰富编码功能，扩展插件网站：https://packagecontrol.io/

**操作步骤**

1. 以下内容基于已经你已经在你的 SublimeText 中安装了 package control
2. 通过快捷键组合 ctrl+shift+P 唤出命令面板
3. 在面板中输入“install package”后回车
4. 接着输入插件名称如：“emmet” 回车即可（观察状态栏进度，晃动的等号）

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#软件风格)软件风格

风格包网站: https://packagecontrol.io](https://packagecontrol.io/)

风格包: Spacegray：

```text
https://packagecontrol.io/packages/Theme%20-%20Spacegray
```

1. Preferences > color scheme >theme-spacegray
2. Preferences-> setting 中设置以下

```text
"theme": "Spacegray.sublime-theme",
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme"
```

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#资源图标)资源图标

包地址：https://github.com/ihodev/a-file-icon

安装方式：

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Package Control: Install Package`
3. Find `A File Icon` and hit `Enter`

\##常用插件

1. emmet：快速编写 html/css https://docs.emmet.io
2. docblockr：代码注释提示插件 https://packagecontrol.io/packages/DocBlockr
3. sideBarEnhancements ：扩展左侧面板 https://packagecontrol.io/packages/SideBarEnhancements
4. SideBarTools：扩展左侧面板 https://packagecontrol.io/packages/SideBarTools
5. AdvancedNewFile：快速创建文件 ，使用 ctrl+alt+n 就可以快速创建文件
6. Local History：本地历史记录 https://packagecontrol.io/packages/Local%20History
7. Laravel 5 Artisan：laravel 命令行插件 https://packagecontrol.io/packages/Laravel%205%20Artisan 按 ctrol+shift+p 搜索并执行命令
8. Laravel 5 Snippets：laravel 代码片段 https://packagecontrol.io/packages/Laravel%205%20Snippets
9. Laravel Blade Highlighter：laravel blade 模板高亮 https://packagecontrol.io/packages/Laravel%20Blade%20Highlighter
10. Blade Snippets：blade 代码片段 https://packagecontrol.io/packages/Blade%20Snippets
11. Laravel Blade AutoComplete：自动识别 blade 父级模板内容 https://packagecontrol.io/packages/Laravel%20Blade%20AutoComplete
12. Bootstrap 3 Snippets：bootstrap 代码片段 https://github.com/JasonMortonNZ/bs3-sublime-plugin
13. Bootstrap 3 Autocomplete：bootstrap 样式提示 https://packagecontrol.io/packages/Bootstrap%203%20Autocomplete
14. Bootstrap 4 Snippets：bootstrap 代码提示 https://packagecontrol.io/packages/Bootstrap%204%20Snippets
15. Bootstrap 4 Autocomplete：bootstrap4 自动提示：https://packagecontrol.io/packages/Bootstrap%204%20Autocomplete
16. SCSS：scss 代码提示 https://packagecontrol.io/packages/SCSS
17. Sass：scss 语法高亮 https://packagecontrol.io/packages/Sass

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#less)LESS

安装 node [https://nodejs.org/zh-cn/(opens new window)](https://nodejs.org/zh-cn/)

**编译环境**

```text
npm install -g less@2.7.3
npm install -g less-plugin-clean-css
npm install -g less-plugin-autoprefix
```

> mac&linux 系统使用 sudo 安装

设置好之后，在命令行中输入 lessc，如果有如下提示则表示设置成功：

```text
C:\Users\hdxj>lessc
lessc.wsf: no input files
Usage:
Single file: cscript //nologo lessc.wsf input.less [output.css] [-compre
Directory:   cscript //nologo lessc.wsf inputdir outputdir [-compress]
```

**插件**

sublime 需要安装两个插件一个是编译 less 文件，一个是语法高亮

1. https://packagecontrol.io/packages/Less2Css
2. https://packagecontrol.io/packages/LESS

这时可以在 Sublime Text 中打开或者新建一个 less 文件，按下 Ctrl+S 保存，此时应该会在 less 文件的相同目录下生成同名的 css 文件。

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#格式化)格式化

首先通过以下路径打开用户按键绑定文件：

Preferences → Key Bindings – User

然后在其中添加以下代码（如果你有需要的话，其中的快捷键组合是可以自己定义的）：

```text
[
	//格式化代码,single_line参数删除时，格式化只影响当前光标所在行
	{"keys": ["ctrl+alt+l"], "command": "reindent" , "args": {"single_line": false}}
]
```

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#内容检索)内容检索

**快速查找**

默认情况下，Sublime Text 支持函数快速查找，按 Ctrl+Shift+R 打开查找面板，就可以快速定位函数所在的文件，如果安装了 emmet 插件将会失效，我们需要做以下操作进行修复。

编辑 emmet 插件配置项：

```text
{"disabled_keymap_actions": "reflect_css_value"}
```

**代码跟踪**

鼠标移动到函数上面，会自动显示方法的文件列表。或按 f12 键显示函数的文件列表

## [#](https://doc.houdunren.com/编程软件/sublime/sublime.html#快捷键)快捷键

使用快捷键可以显著提高开发效率，所以还是有必要掌握的。

1. 搜索文件：ctrl+p 输入文件名
2. 搜索函数/方法：ctrl+p 输入`“文件名@方法名”` 如 User@show
3. 跳转到指定行：ctrl+p 输入`文件名:行号`,只输入: 时在当前文件跳转
4. 查找当前文件方法：ctrl+r
5. 返回/前进编辑位置：Alt + -、Alt + Shift + -
6. 切换标签页：Ctrl + PgUp、Ctrl + PgDn
7. 选中单词：Ctrl + D 连续按会选中页面中所有单词，以实现批量编辑
8. 以单词为单位快速移动光标：Ctrl + ←、Ctrl + →
9. 选中当前行：Ctrl + L
10. 跳转到第几行：Ctrl+G
11. 跳转到对应括号：Ctrl+M
12. 开关侧栏：Ctrl+K+B
13. 选中当前括号内容，重复可选着括号本身：Ctrl+Shift+M
14. 注释当前 html 标签块：Ctrl+Shift+/
15. 专注编写模式：Shift+F11
16. 分屏显示：Alt+Shift+数字
17. Ctrl+Enter 在下一行插入新行。举个栗子：即使光标不在行尾，也能快速向下插入一行。
18. Ctrl+Shift+Enter 在上一行插入新行。举个栗子：即使光标不在行首，也能快速向上插入一行。
19. Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。
20. Ctrl+Shift+] 选中代码，按下快捷键，展开代码。