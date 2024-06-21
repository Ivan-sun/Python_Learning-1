

Python for Excel-xlwings 

# 工作表的操作

![image-20231007144941081](./Python for Excel-xlwings/image-20231007144941081.png)

<img src="./Python for Excel-xlwings/image-20231007170035692.png" alt="image-20231007170035692" style="zoom: 67%;" />

```VBA
Sub 宏1()
    With Selection.Font
        .Name = "宋体"
        .FontStyle = "常规"
        .Size = 11
        .Strikethrough = True
        .Superscript = False
        .Subscript = False
        .OutlineFont = False
        .Shadow = False
        .Underline = xlUnderlineStyleNone
        .ThemeColor = xlThemeColorLight1
        .TintAndShade = 0
        .ThemeFont = xlThemeFontMinor
    End With
End Sub
```

<font size=5 color='yellow'>字体中所有的格式调整都可以使用api 的方式进行调用 VBA对应的函数。VBA中xl 开头的变量均为常量，需要查询对应的常量值</font>

## <font size=6 color='pink'>api的调用</font>

 ![image-20231007170638910](./Python for Excel-xlwings/image-20231007170638910.png)

<img src="./Python for Excel-xlwings/image-20231007171248386.png" alt="image-20231007171248386" style="zoom:67%;" />

<img src="./Python for Excel-xlwings/image-20231007175131545.png" alt="image-20231007175131545" style="zoom:67%;" />

<img src="./Python for Excel-xlwings/image-20231007175157955.png" alt="image-20231007175157955" style="zoom:67%;" />

<img src="./Python for Excel-xlwings/image-20231007182413755.png" alt="image-20231007182413755" style="zoom:67%;" />

## 拆分工作表为独立工作簿

<font size=6 color="violet">xls 格式的 65536行 256列</font>

<font size=6 color="violet">xlsx 格式的 1048576行 16384列</font>

<font size=6>字体设置 </font>

<img src="D:\微信文件\WeChat Files\sunnyous\FileStorage\Temp\1696899295817.png" alt="1696899295817" style="zoom: 50%;" />

## <font color='pink'>aip 实现打开文件对话框</font>

![image-20231010131035337](./Python for Excel-xlwings/image-20231010131035337.png)

![image-20231010131107847](./Python for Excel-xlwings/image-20231010131107847.png)

## <font color='pink'>xlwings 实现批量工作簿h</font>

![image-20231010134332826](./Python for Excel-xlwings/image-20231010134332826.png)