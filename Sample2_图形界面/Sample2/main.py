# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from dict import *
from generator import Window


def init():
    """
    初始化graph, path
    """
    for i in range(1, n + 1):
        row1 = [0]
        row2 = [0]
        for j in range(1, n + 1):
            row1.append(float('inf'))
            row2.append(j)
        graph.append(row1)
        path.append(row2)


def read1():
    """
    读取place_data.txt,创建字典使place和编号相对应
    """
    f = open('data/place_data.txt')
    data = f.readlines()
    for i in range(1, len(data)):
        li = data[i].strip().split(' ')
        key = int(li[0])
        value = li[1]
        place_dict[key] = value


def read2():
    """
    读取route_data.txt,建立邻接矩阵，在图中画出白色路线
    """
    f = open('data/route_data.txt')
    data = f.readlines()
    line = []
    for i in range(1, len(data)):
        num_list = data[i].strip().split(' ')
        a = 0
        b = 0
        distance = 0
        for num in range(0, 3):
            if num == 0:
                a = int(num_list[num])
            if num == 1:
                b = int(num_list[num])
            if num == 2:
                distance = int(num_list[num])
        graph[a][b] = distance
        graph[b][a] = distance
        line.append(cv.create_line(tuple(x_y_dict[a]), tuple(x_y_dict[b]), dash=(1, 70), fill="white", width=3))


def floyd():
    """
    计算最短路径并保存路径
    """
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j] = path[i][k]


def show_text():
    """
    显示图形界面中的文字
    """
    global text1
    global text2
    # 图片文字
    for i in range(1, 17):
        p = pos_dict[i].split(' ')
        x = int(p[0])
        y = int(p[1])
        x_y_dict[i].append(x)
        x_y_dict[i].append(y)
        place.append(cv.create_text((x, y), text=str(i) + '.' + place_dict[i], fill="white",
                                    font=("微软雅黑", 11, "bold underline")))
    # 欢迎文字
    welcome_text = tk.Label(window, text="欢迎使用广东外语外贸大学校园导航\n\nWelcome to The_GDUFS_Navigation\n\n\n",
                            fg="blue", font=("微软雅黑", 20, "bold"))
    welcome_text.place(x=580, y=70)
    # 指引文字
    help_text = tk.Label(window, text="依次点击下方图标后选择左侧地点以设定起点与终点\n\n\n",
                         font=("微软雅黑", 15, "bold"))
    help_text.place(x=590, y=260)
    # 请选择起点/终点 文字
    text1.place(x=700, y=380)
    text2.place(x=840, y=380)


def choose1():
    """
    用于判断是否开始选择起点
    """
    text1['text'] = '请选择起点'
    if text2['text'] == '请选择终点':
        text2['text'] = ''


def choose2():
    """
    用于判断是否开始选择终点
    """
    text2['text'] = '请选择终点'
    if text1['text'] == '请选择起点':
        text1['text'] = ''


def work(a_para, b_para):
    """
    确定起点和终点后给出最短路径长度、具体路径，并在图中标红路径
    :param a_para:起点
    :param b_para:终点
    """
    text = ""
    # noinspection PyBroadException
    try:
        if 1 <= a_para <= 16:
            if 1 <= b_para <= 16 and a_para != b_para and graph[a_para][b_para] != float('inf'):
                text += (place_dict[a_para] + " -> " + place_dict[b_para] + "\n最短路径长度 " + str(
                    graph[a_para][b_para]) + "米\n\n")
                text += "具体路径\n"
                path_detail = [0]
                while a_para != b_para:
                    path_detail.append(a_para)
                    a_para = path[a_para][b_para]
                path_detail.append(b_para)
                for cnt in range(1, len(path_detail) - 1):
                    place_string = str(path_detail[cnt]) + ' ' + str(path_detail[cnt + 1])
                    red_list.append(place_string)
                    cv.itemconfig(line_place_dict[place_string], fill="red")
                    text += (place_dict[path_detail[cnt]] + " -> " + place_dict[
                        path_detail[cnt + 1]] + "  :   " + str(
                        graph[path_detail[cnt]][path_detail[cnt + 1]]) + " 米\n")
            elif 1 <= b_para <= 16 and a_para == b_para:
                return "          " + place_dict[a_para] + " -> " + place_dict[
                    b_para] + "\n          最短路径长度" + " 0 米\n\n          你原地踏步干嘛(*^▽^*)\n"
            else:
                return "指令或数据错误，请重试\n"
        else:
            return "指令或数据错误，请重试\n"
    except Exception:
        return "指令或数据错误，请重试\n"
    return text


def get_place(event):
    """
    在图中点击后确定所点击的地点
    :param event: “鼠标点击”这一事件
    """
    global pos
    px = event.x
    py = event.y
    if text1['text'] == '请选择起点':
        for red_line in red_list:
            cv.itemconfig(line_place_dict[red_line], fill="white")
        for p in x_y_dict:
            if x_y_dict[p][0] - 35 <= px <= x_y_dict[p][0] + 35 and \
                    x_y_dict[p][1] - 30 <= py <= x_y_dict[p][1] + 30:
                pos[0] = p
                start_text['text'] = str(p)
                cv.coords(start_img, px, py)
        text1['text'] = ''
    if text2['text'] == '请选择终点':
        for red_line in red_list:
            cv.itemconfig(line_place_dict[red_line], fill="white")
        for p in x_y_dict:
            if x_y_dict[p][0] - 35 <= px <= x_y_dict[p][0] + 35 and \
                    x_y_dict[p][1] - 30 <= py <= x_y_dict[p][1] + 30:
                pos[1] = p
                end_text['text'] = str(p)
                cv.coords(end_img, px, py)
        text2['text'] = ''
    if start_text['text'] != '' and end_text['text'] != '':
        pa = pos[0]
        pb = pos[1]
        text = work(pa, pb)
        start_text.pack_forget()
        end_text.pack_forget()
        route_text['text'] = text


if __name__ == "__main__":
    # 生成窗体
    generator = Window()
    cv = generator.cv
    window = generator.window
    # 展示路线的窗体
    fr = Frame(window, relief=RIDGE, borderwidth=5, width=500, height=500)
    fr.place(x=575, y=420)
    # 读取place_data.txt
    read1()
    # 初始化
    n = 16  # 边数
    graph = [[0]]  # 领接矩阵
    path = [[0]]  # 路径
    pos = [0, 0]
    init()
    # 显示文字
    place = []
    red_list = []
    text1 = tk.Label(window, text="", font=("微软雅黑", 15))
    text2 = tk.Label(window, text="", font=("微软雅黑", 15))
    show_text()
    # 读取route_data.txt
    read2()
    # floyd
    floyd()
    # 起点按钮
    start_bt = tk.PhotoImage(file='data/start.png')
    start_img = cv.create_image(-20, 0, image=start_bt)
    start = tk.Button(window, image=start_bt, command=choose1)
    start.place(x=735, y=310)
    # 终点按钮
    end_bt = tk.PhotoImage(file='data/end.png')
    end_img = cv.create_image(-20, 0, image=end_bt, )
    end = tk.Button(window, image=end_bt, command=choose2)
    end.place(x=876, y=310)
    # 文字设定
    start_text = tk.Label(window, text='', font=("微软雅黑", 15), borderwidth=2)
    end_text = tk.Label(window, text='', font=("微软雅黑", 15), borderwidth=2)
    route_text = tk.Label(fr, text='', font=("微软雅黑", 15))
    # 放置文字
    start_text.place(x=735, y=350)
    end_text.place(x=878, y=350)
    route_text.place(x=90, y=0)
    # 启动！
    window.bind('<ButtonPress-1>', get_place)
    cv.pack()
    window.mainloop()
