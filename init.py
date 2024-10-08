import pyautogui
import time

def save_position(label):
    """提示用户点击鼠标以记录当前位置"""
    pyautogui.alert(f"请移动到 {label} 的位置，等待2s自动记录")
    # 等待用户点击鼠标并获取当前坐标
    time.sleep(2)  # 稍微等待一下，以防用户没有立即点击
    x, y = pyautogui.position()
    pyautogui.alert(f"{label} 的坐标已保存: ({x}, {y})")
    return (x, y)

def write_positions_to_file(positions, filename="positions.txt"):
    """将坐标列表写入文件"""
    with open(filename, "w") as file:
        for i, pos in enumerate(positions, start=1):
            file.write(f"按钮{i}坐标: {pos[0]}, {pos[1]}\n")
        file.write(f"提交按钮坐标: {positions[-1][0]}, {positions[-1][1]}\n")
    pyautogui.alert(f"\n所有坐标已保存到 {filename} 文件中！")

def main():
    # 用于保存二进制位按钮的位置列表
    positions = []

    # 依次保存从高位到低位的 8 个二进制位按钮位置
    for i in range(1, 9):
        label = f"第 {i} 个二进制位按钮（从高位到低位）"
        pos = save_position(label)
        positions.append(pos)

    # 保存提交按钮的位置
    submit_pos = save_position("提交按钮")
    positions.append(submit_pos)

    # 将所有位置保存到文件
    write_positions_to_file(positions)

if __name__ == "__main__":
    main()
