# -*- coding: utf-8 -*-
# @Time    : 2024/10/31 14:48:06
# @Author  : Kovan Gao
# @File    : ui_auto_wx
# @Description :

import pyautogui
import time
import uiautomation as auto
import subprocess
import pyperclip

class WxChat:
    def test1(self):
        width, height = pyautogui.size()
        print(f'Screen size: {width}x{height}')
        # pyautogui.moveTo(100, 100, duration=1)  # 移动到 (100, 100)，持续 1 秒
        # pyautogui.click()  # 在当前鼠标位置点击
        # pyautogui.click(300, 300)  # 点击坐标 (200, 200)
        # pyautogui.write('Hello, World!', interval=0.1)  # 输入文本，每个字符之间间隔 0.1 秒
        # screenshot = pyautogui.screenshot()
        # screenshot.save(r'C:\Users\indexvc\Desktop\screenshot.png')  # 保存截图
        # 打开记事本
        pyautogui.press('shift')
        pyautogui.hotkey('win', 'r')  # 打开运行窗口
        time.sleep(0.5)
        pyautogui.write('notepad')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(1)  # 等待记事本打开
        # 输入文本
        pyautogui.press('shift')
        pyautogui.write('Hello, this is a test.', interval=0.1)
        # 保存文件
        pyautogui.hotkey('ctrl', 's')  # 按下 Ctrl + S
        time.sleep(1)  # 等待保存窗口打开
        pyautogui.write(r'C:\Users\indexvc\Desktop\test111111111.txt')
        pyautogui.press('enter')

    def test2(self):
        subprocess.Popen(r'D:\Program Files (x86)\WXWork\WXWork.exe')
        auto.WindowControl(Depth=1, Name='企业微信')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        text = '这里是微信'
        pyperclip.copy(text)  # 复制到剪贴板
        auto.SendKeys("{Ctrl}v")
        time.sleep(0.3)
        auto.SendKeys('{enter}')
        chat_dialogues = ['今天的工作完成了呢','没有数据','你有看到最新的项目进展吗？','我正在处理这个问题，稍等一下。','请确认一下这个文件。','我们下周的会议定在哪里？','这个任务的截止日期是什么时候？',
            '有没有人负责这部分工作？','我需要更多的信息来继续。','谢谢你的帮助！','你能帮我看一下这个吗？','我会尽快回复你的。','这个问题我们需要讨论一下。',
            '请给我发一下相关的文档。','我已经更新了报告。','我们需要重新安排一下进度。','请确认一下我的理解是否正确。','我们需要一个新的计划来解决这个问题。',
            '你有空吗？我们可以聊一下。','这个方案看起来不错！'
        ]
        for chat_dialogue in chat_dialogues:
            pyperclip.copy(chat_dialogue)
            auto.SendKeys("{Ctrl}v")
            time.sleep(5)
            auto.SendKeys('{enter}')


if __name__ == '__main__':
    wx = WxChat()
    wx.test2()