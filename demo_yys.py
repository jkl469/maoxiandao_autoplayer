import os

from auto_player import Player, adb
from auto_ocr_player import OCR_Player
import time
#beibao的位置（1852，53），日常玩法（1720，478），日常进度(1486,182)
#立即前往的位置(1492,660)匹配到了加上276的偏移量  ，入场(1680,986)

#OCR文字识别  桌面模式（不能遮挡游戏窗口）
myplayer = OCR_Player(accuracy=0.65, adb_mode=True)



def change(name = '光之魔导师'):
    time.sleep(1)
    beibao = myplayer.find_touch(['beibao'], area=[0, 20, 80, 100])
    if not beibao:
        myplayer.touch((1850, 80))
    time.sleep(1)
    # myplayer.find_touch(['huanhao'])
    myplayer.touch((1780, 1000))
    time.sleep(1)
    find = myplayer.my_touch([f'{name}'])
    if not find:
        print("meiyouzhaodao")
        myplayer.drag((1040, 520), (1344, 250))
        time.sleep(1)
    myplayer.my_touch([f'{name}'])
    time.sleep(1)
    myplayer.my_touch(['变更'],area=[80,100,50,80])
    time.sleep(10)
    myplayer.find_touch(['chahao2'], area=[0, 30, 70, 100])
    myplayer.find_touch(['chahao3'], area=[0, 30, 70, 100])
    myplayer.find_touch(['chahao3'], area=[0, 30, 70, 100])
    myplayer.find_touch(['chahao2'], area=[0, 30, 70, 100])
    myplayer.find_touch(['chahao2'], area=[0, 30, 70, 100])
    myplayer.find_touch(['chahao3'], area=[0, 30, 70, 100])
    myplayer.find_touch(['chahao3'], area=[0, 30, 70, 100])
    myplayer.find_touch(['chahao2'], area=[0, 30, 70, 100])
    # myplayer.touch((1800, 80))
    time.sleep(1)

def xiuxi(name = '精英副本'):
    if name == '材料副本':
        time.sleep(120)
    elif name == '精英副本':
        time.sleep(120)
    elif name == '奈特的金字塔':
        time.sleep(180)
    elif name =='周常副本':
        time.sleep(60)
    elif name == '进化系统':
        time.sleep(380)
    elif name == '金钩海兵王':
        time.sleep(140)
    elif  name == '次元入侵':
        time.sleep(300)
    elif name =='唐云的料理教室':
        time.sleep(60)
    else:
        pass

def richangfuben(name='精英副本',people = '光之魔导师'):
    time.sleep(1)
    cailiao, jinxing = 0, 0
    start = time.time()
    while True:
        if not jinxing:
            beibao = myplayer.find_touch(['beibao'],area=[0,20,80,100])
            if not beibao:
                myplayer.touch((1850, 80))
            time.sleep(1)
            beibaoagain = myplayer.my_touch(['日常玩法'],area=[0,50,80,100])
            if not beibaoagain:
                myplayer.touch((1850, 80))
                time.sleep(1)
                myplayer.my_touch(['日常玩法'], area=[0, 50, 80, 100])
            time.sleep(1)
            myplayer.my_touch(['日常进度'],area=[0,30,50,100])
            time.sleep(1)
            if name in ['金钩海兵王', '次元入侵']:
                myplayer.drag((1344, 864), (1344, 540))
            time.sleep(1)
            myplayer.my_touch([f'{name}'],area=[30,100,45,80])
            time.sleep(1)
            if name == '唐云的料理教室':
                myplayer.touch((1464, 340)) #选料理
            if (people != '光之魔导师') and name =='精英副本':
                myplayer.touch((100, 550))
            if (people != '光之魔导师') and name =='材料副本':
                myplayer.touch((100, 450))
            myplayer.my_touch(['入场'],area=[80,100,70,100])
            time.sleep(1)
            myplayer.my_touch(['快速组队'],area=[80,100,70,100])
            time.sleep(1)
            if name == '唐云的料理教室':
                myplayer.touch((830, 760))  # 选三个怪物
                myplayer.touch((1120, 760))
                myplayer.touch((1290, 760))
            else:
                myplayer.find_touch(['jiahao'])
                time.sleep(0.1)
                myplayer.find_touch(['jiahao'])
                time.sleep(0.1)
                myplayer.find_touch(['jiahao'])
                myplayer.find_touch(['jiahao'])
            myplayer.my_touch(['确定'],area=[50,100,50,80])
            time.sleep(1)
            myplayer.my_touch(['确定'], area=[80, 100, 40, 80])
            myplayer.my_touch(['入场'],area=[80,100,40,100])
            jinxing = 1
            xiuxi(name)
        # if name == '金钩海兵王':
        #     jinpai = myplayer.my_touch(['竞拍'])
        #     while(jinpai):
        #         meile = myplayer.my_touch(['竞拍'])
        #         if not meile:
        #             break
        end = time.time()
        if(end - start > 480):
            return
        finish = myplayer.my_touch(['退出']) or myplayer.my_touch(['退出'],area=[50,80,20,50])
        # myplayer.my_touch(['放弃'])
        if(finish):
            time.sleep(1)
            return
        time.sleep(5)

def richang():
    # 还要赏月
    # change('光之魔导师')
    # richangfuben('唐云的料理教室')
    # richangfuben('精英副本')
    # # richangfuben('精英副本')
    # richangfuben('材料副本')
    # richangfuben('材料副本')
    # richangfuben('奈特的金字塔')
    # richangfuben('周常副本')
    # richangfuben('次元入侵')
    # richangfuben('进化系统')
    # richangfuben('次元入侵')
    # richangfuben('金钩海兵王')
    #
    #
    # name = '火毒魔导师'
    # change(name)
    # richangfuben('唐云的料理教室')
    # richangfuben('精英副本')
    # richangfuben('材料副本')
    # richangfuben('奈特的金字塔')
    # richangfuben('周常副本')
    # richangfuben('进化系统')
    # richangfuben('金钩海兵王')

    # name = '墨玄'
    # change('墨玄')
    # richangfuben('唐云的料理教室')
    # richangfuben('精英副本')
    # richangfuben('材料副本')
    # richangfuben('奈特的金字塔')
    # richangfuben('周常副本')
    # richangfuben('进化系统')
    # richangfuben('金钩海兵王')

    name = '冰雷魔导师'
    # change('冰雷魔导师')
    richangfuben('唐云的料理教室')
    richangfuben('精英副本',name)
    richangfuben('材料副本')
    richangfuben('奈特的金字塔')
    richangfuben('周常副本')
    richangfuben('进化系统')
    richangfuben('金钩海兵王')

def yuanzheng():
    jinxing = 0
    name = '扎昆'
    while True:
        if not jinxing:
            beibao = myplayer.find_touch(['beibao'],area=[0,20,80,100])
            if not beibao:
                myplayer.touch((1850, 80))
            time.sleep(1)
            beibaoagain = myplayer.my_touch(['日常玩法'], area=[0, 50, 80, 100])
            if not beibaoagain:
                myplayer.touch((1850, 80))
                time.sleep(1)
                myplayer.my_touch(['日常玩法'], area=[0, 50, 80, 100])
            time.sleep(1)
            find = myplayer.my_touch(['道具获得顺序'], area=[0, 25, 0, 25],touch = False)
            if not find:
                myplayer.my_touch(['顺序'], area=[0, 25, 0, 25])
                myplayer.my_touch(['道具获得顺序'], area=[20, 40, 0, 25])
            jinxing=1
            myplayer.my_touch(['展开对决'], area=[25, 50, 35, 50])
        location = {'扎昆':(300,200), '龙王':(700,200), '品克缤':(1200,200), '女王':(1650,200)}
        myplayer.touch(location[f'{name}'])
        myplayer.my_touch(['困难'], area=[45, 60, 0, 20])
        myplayer.my_touch(['快速组队'], area=[25, 100, 75, 100])
        myplayer.drag((288,864),(588,864))#向右走
        myplayer.my_touch(['主题公园'])
        myplayer.touch((1748, 816))#放l技能

        myplayer.touch((1850, 440))#退出
        myplayer.my_touch(['返回主页'], area=[50, 100, 40, 60])


if __name__ == '__main__':
    richang()
    # yuanzheng()

    # while True:
    #     myplayer.touch((1500, 540))
    #     time.sleep(1)
    #     flag = myplayer.my_touch(['取消'], area=[80, 100, 20, 50])
    #     if not flag:
    #         time.sleep(870)
    #     time.sleep(15)