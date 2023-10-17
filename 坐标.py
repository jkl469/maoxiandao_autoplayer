import pyautogui

# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()

# 设置窗口尺寸
window_width, window_height = 1080, 1920

# 计算缩放比例
scale_x = screen_width / window_width
scale_y = screen_height / window_height

while True:
    # 获取当前鼠标位置
    mouse_x, mouse_y = pyautogui.position()

    # 计算在窗口上的坐标
    window_x = int(mouse_x / scale_x)
    window_y = int(mouse_y / scale_y)

    # 打印坐标
    print(f"Window coordinates: ({window_x}, {window_y})")

    # 延迟一段时间
    pyautogui.sleep(0.1)