# 介绍
冒险岛枫之传说，游戏脚本，这段代码是参照https://github.com/anywhere2go/auto_player
将其进行了修改，能够在mytouch函数下选择区域进行文字识别，使得识别结果更准确
但是通过opencv的模板匹配，效果很差，只能通过touch函数点击了。

# 电脑连接雷电模拟器
首先下载雷电模拟器，然后进入adb.exe所在的文件夹，因为雷电模拟器自带adb，在当前文件夹输入cmd，启动adb服务，然后就可以跟模拟器互动了。
```python
adb connect 127.0.0.1:5555
```

# 实现功能
基本日常一键刷（richang()函数），以及换号；
星之力图挂机自动点击经验券，没有写点击符文。
混沌远征，军团长，普通远征实现了大半，剩下交给你们自己开发了；
做委托或者做等级任务还没实现，没精力了哈哈哈哈哈，且有点不会。

# 代码使用
在使用之前装好paddlehub这个库，opencv-python,其它需要的库自己装吧
```python
pip install paddlehub opencv-python
```
接下直接运行demo_yys.py就行了
