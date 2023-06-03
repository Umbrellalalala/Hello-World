# -*- coding: utf-8 -*-
import tkinter as tk


class Window:
    def __init__(self):
        pass
    # 窗口参数
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.title('广东外语外贸大学校园导航  The GDUFS Navigation')
    window.iconbitmap('logo.ico')
    width = 1080
    height = 1080
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    window_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(window_geo)
    # 画布
    cv = tk.Canvas(window, height=1080, width=1080)
    # 背景图片
    bg_img = tk.PhotoImage(file='S_img.png')
    bg = cv.create_image(0, 0, image=bg_img, anchor=tk.N + tk.W)