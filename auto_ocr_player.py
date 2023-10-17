# coding: utf-8
from auto_player import Player
import paddlehub as hub

class OCR_Player(Player):
    """docstring for OCR_player"""
    def __init__(self, accuracy=0.6, adb_mode=False, adb_num=0):
        super(OCR_Player, self).__init__(accuracy, adb_mode, adb_num)
        self.ocr = hub.Module(name="chinese_ocr_db_crnn_mobile", enable_mkldnn=True)
        self.accuracy = accuracy

    def read(self, debug=False):
        screen = self.screen_shot()
        imgs = [screen,]
        results = self.ocr.recognize_text(
                            images=imgs,         # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
                            use_gpu=False,            # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
                            output_dir='ocr_result',  # 图片的保存路径，默认设为 ocr_result；
                            visualization=debug,       # 是否将识别结果保存为图片文件；
                            box_thresh=self.accuracy,           # 检测文本框置信度的阈值；
                            text_thresh=self.accuracy)          # 识别中文文本置信度的阈值；
        data = results[0]['data']
        return data

    def find_touch_ocr(self, key_list, debug=False):
        data = self.read(debug)
        key_list = [key_list,]if type(key_list) == str else key_list
        re = False
        for key in key_list:
            if key[0] == 's':
                key = key[1:]
                found = [e for e in data if key == e['text']]
            else:
                found = [e for e in data if key in e['text']]
            msg = f'目标：{key},  找到数量：{len(found)}'
            print(msg)
            if found:
                p1, _, p2, _ = found[0]['text_box_position']
                (x1, y1), (x2, y2) = p1, p2
                center = (int((x1+x2)/2), int((y1+y2)/2))
                self.touch(center)
                # self.drag(center,center)
                re = key
                break
        return re

    def exist(self, key_list, debug=False):
        data = self.read(debug)
        key_list = [key_list,]if type(key_list) == str else key_list
        re = []
        for key in key_list:
            if key[0] == 's':
                key = key[1:]
                found = [e for e in data if key == e['text']]
            else:
                found = [e for e in data if key in e['text']]
            msg = f'目标：{key},  找到数量：{len(found)}'
            print(msg)
            re.append(len(found))
        re = re[0] if len(re) == 1 else re
        return re

    def my_touch(self, key_list, area=None , touch = True):
        screen = self.screen_shot()
        if area:
            screen, start = self.cut(screen, area)
        imgs = [screen,]
        results = self.ocr.recognize_text(
                            images=imgs,         # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
                            use_gpu=False,            # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
                            output_dir='ocr_result',  # 图片的保存路径，默认设为 ocr_result；
                            visualization=False,       # 是否将识别结果保存为图片文件；
                            box_thresh=self.accuracy,           # 检测文本框置信度的阈值；
                            text_thresh=self.accuracy)          # 识别中文文本置信度的阈值；
        data = results[0]['data']
        key_list = [key_list,]if type(key_list) == str else key_list
        re = False
        for key in key_list:
            if key[0] == 's':
                key = key[1:]
                found = [e for e in data if key == e['text']]
            else:
                found = [e for e in data if key in e['text']]
            msg = f'目标：{key},  找到数量：{len(found)}'
            print(msg)
            if found:
                if not touch:
                    return True
                p1, _, p2, _ = found[0]['text_box_position']
                (x1, y1), (x2, y2) = p1, p2
                if richang(key):
                    center = (int(x1), int((y1+y2)/2))
                else:
                    center = (int((x1+x2)/2), int((y1+y2)/2))
                loc_pos = list(center)
                if area:  # 从裁剪后的坐标还原回裁前的坐标
                    loc_pos[0]+= start[0]
                    loc_pos[1]+= start[1]
                    loc_pos = tuple(loc_pos)
                a, b = loc_pos[0], loc_pos[1]
                if richang(key):
                    a += 471
                    print((a,b))
                self.touch((a, b))  # 同一目标多个结果时只点第一个
                # self.touch(center)
                # self.drag(center,center)
                re = key
        return re



def richang(key):
    if key in ['材料副本', '唐云的料理教室', '精英副本', '奈特的金字塔', '周常副本', '进化系统', '金钩海兵王', '次元入侵']:
        return True
    return False

def yuanzheng(key):
    if key in ['材料副本', '精英副本', '奈特的金字塔', '周常副本', '进化系统', '金钩海兵王', '次元入侵']:
        return True
    return False