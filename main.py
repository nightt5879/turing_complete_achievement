import pyautogui
import time

def read_positions_from_file(filename="positions.txt"):
    """从文件中读取按钮和提交按钮的坐标"""
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
    """根据二进制列表，点击相应按钮，提交后再点击一次以重置"""
    clicked_buttons = []  # 用于存储哪些按钮被点击了

    # 从高位到低位依次点击按钮，间隔0.01秒
    for i, bit in enumerate(binary_list):
        if bit == 1:
            # print(f"点击按钮{i + 1}，位置: {positions[i]}")
            pyautogui.click(positions[i])  # 只点击为1的按钮
            clicked_buttons.append(i)  # 记录被点击的按钮
        time.sleep(0.01)

    # 点击提交按钮
    print(f"点击提交按钮，位置: {positions[-1]}")
    pyautogui.click(positions[-1])

    # 再次点击之前被点击过的按钮以重置
    # for i in clicked_buttons:
    #     print(f"再次点击按钮{i + 1}，位置: {positions[i]}，以重置")
    #     pyautogui.click(positions[i])
    #     time.sleep(0.01)

    # 恢复鼠标到初次按下的位置
    print(f"恢复鼠标到输入框初始位置：{input_position}")
    pyautogui.moveTo(input_position[0], input_position[1])
    pyautogui.click()  # 模拟点击，方便继续输入

def record_input_window_position():
    """提示用户将鼠标移动到输入窗口，并等待2秒记录位置"""
    print("请将鼠标移动到输入窗口的位置，并保持不动，2秒后将记录位置...")
    time.sleep(2)  # 给用户2秒钟时间移动鼠标
    position = pyautogui.position()  # 记录当前位置
    print(f"输入窗口位置已记录: {position}")
    return position

def main():
    # 读取保存的按钮和提交按钮的坐标
    positions = read_positions_from_file()

    # 记录输入窗口位置
    input_position = record_input_window_position()

    while True:
        # 获取用户输入的数字
        user_input = input("请输入一个十进制数字并按回车键: ")

        # 确保输入的是有效的整数
        try:
            decimal_number = int(user_input)
        except ValueError:
            print("请输入一个有效的十进制整数！")
            continue

        # 将输入的十进制数字转换为8位二进制数
        binary_list = decimal_to_binary_list(decimal_number)

        print(f"转换后的二进制数是: {''.join(map(str, binary_list))}")

        # 给出1秒的准备时间
        # print("0.1秒后开始点击...")
        time.sleep(0.1)

        # 根据二进制位点击按钮，并恢复鼠标焦点到初次点击的位置
        perform_clicks(positions, binary_list, input_position)

        # 等待1秒后继续下一轮输入
        # time.sleep(1)

if __name__ == "__main__":
    main()
