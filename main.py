import pyautogui
import time
import keyboard

def read_positions_from_file(filename="positions.txt"):
    """从文件中读取按钮坐标"""
    positions = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            coords = line.strip().split(":")[1].split(",")
            x, y = int(coords[0].strip()), int(coords[1].strip())
            positions.append((x, y))
    return positions

def decimal_to_binary_list(number, bits=8):
    """将十进制数转换为指定位数的二进制数，返回一个按位列表"""
    binary_str = f"{number:0{bits}b}"  # 转换为指定位数的二进制字符串
    return [int(bit) for bit in binary_str]  # 返回一个包含每个位的列表

def perform_clicks(positions, binary_list, input_position):
    """根据二进制列表，点击相应按钮"""
    # 从高位到低位依次点击按钮，间隔0.01秒
    for i, bit in enumerate(binary_list):
        if bit == 1:
            print(f"点击按钮{i+1}，位置: {positions[i]}")
            pyautogui.click(positions[i])  # 只点击为1的按钮
        time.sleep(0.01)

    # 点击提交按钮
    print(f"点击提交按钮，位置: {positions[-1]}")
    pyautogui.click(positions[-1])

    # 恢复鼠标到初次按下的位置
    print(f"恢复鼠标到输入框初始位置：{input_position}")
    pyautogui.moveTo(input_position[0], input_position[1])

def wait_for_initial_click():
    """等待用户第一次按下鼠标，并记录该位置"""
    print("请点击输入框的位置以进行初始化...")
    while True:
        if pyautogui.mouseDown():
            initial_position = pyautogui.position()
            print(f"记录的初次输入框位置：{initial_position}")
            return initial_position

def main():
    # 读取保存的按钮坐标
    positions = read_positions_from_file()

    # 等待用户第一次点击，记录输入框位置
    input_position = wait_for_initial_click()

    print("\n按下 ESC 键可以退出程序。\n")

    # 无限循环，直到按下 ESC 键
    while True:
        if keyboard.is_pressed('esc'):
            print("检测到 ESC 键，程序结束。")
            break

        # 输入10进制数字
        decimal_number = int(input("请输入一个10进制数字: "))

        # 将输入的10进制数字转换为8位二进制数
        binary_list = decimal_to_binary_list(decimal_number)

        print(f"转换后的二进制数是: {''.join(map(str, binary_list))}")

        # 给出1秒的准备时间
        print("1秒后开始点击...")
        time.sleep(1)

        # 执行点击操作并恢复鼠标焦点到初次点击的位置
        perform_clicks(positions, binary_list, input_position)

if __name__ == "__main__":
    main()
