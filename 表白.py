from tkinter import *
from tkinter import messagebox
import smtplib
window = Tk()
#设置窗口大小，宽x高
window.geometry('350x200')
#设置窗口的位置，基于屏幕的坐标 相对位置+x轴+y轴
window.geometry("+650+250")
#设置窗口的标题
window.title('我帅吗？')
#设置标签
a = Label(window,text='小朋友',font=('微软雅黑',15))
#网格式的显示 默认第0行第0列
a.grid()
b = Label(window,text='我是不是很帅呢？',font=('微软雅黑',15))
#网格式的显示  设置行列，上下左右对齐方式N S W E  这里靠左
b.grid(row=1,column=1,sticky=W)
#新窗口
def new():
    # Toplevel是一个独立的窗口， TK已经是最大的窗口了，所有的窗口都在tk下
    love =Toplevel(window)
    love.geometry('300x150+800+450')
    label = Label(love,text='我觉得你也很漂亮哦',font=('微软雅黑',24))
    #类似grid()
    label.pack()
    btn = Button(love,text='确定',width=10,height=2,command=like)
    btn.pack()
#点击帅气触发
def like():
    like =Toplevel(window)  #创建一个对话框，属于window
    like.geometry('300x150+800+450')  #设置窗口大小和位置
    label = Label(like,text='加个微信呗~',font=('微软雅黑',24)) #显示的文字
    label.pack()
    #entry和文本框一样，它可以将输入的东西显示成某个字符，
    entry = Entry(like,font=('微软雅黑',24),fg='red')
    entry.pack()
    global text
    text=entry.get()
    btn = Button(like,text='确定',width=10,height=2,command=jiaweix)
    btn.pack()
    print(text)
#加微信
def jiaweix():
    jia = Toplevel(window)
    jia.geometry('300x150+800+500')
    jia.title('一定要加哦')
    c = Label(jia,text='16888521888',font=('微软雅黑',15))
    c.pack()
    btn3 =Button(jia,text='不加是小狗',width=10,height=2,command=colssweind)
    btn3.pack()
#关闭所有窗口
def colssweind():
    window.destroy()
#新建第二个窗口
def two():
    dislove =Toplevel(window)
    dislove.geometry('300x150+800+450')
    Label2=Label(dislove,text='再给你一次机会',font=('微软雅黑',20))
    Label2.pack()
    but4=Button(dislove,text="好的吧",font=('微软雅黑',15),command=dislove.destroy)
    but4.pack(side=LEFT)
    but5=Button(dislove,text='不需要',font=('微软雅黑',15),command=three)
    but5.pack(side=RIGHT)
def three():
    dislove =Toplevel(window)
    dislove.geometry('300x150+800+500')
    Label2=Label(dislove,text='回答错误，再来',font=('微软雅黑',20))
    Label2.pack()
    but4=Button(dislove,text="你真帅",font=('微软雅黑',15),command=dislove.destroy)
    but4.pack(side=LEFT)
    but5=Button(dislove,text='我不来',font=('微软雅黑',15),command=four)
    but5.pack(side=RIGHT)
def four():
    dislove =Toplevel(window)
    dislove.geometry('300x150+800+550')
    Label2=Label(dislove,text='再皮老子锤死你',font=('微软雅黑',20))
    Label2.pack()
    but4=Button(dislove,text="你真帅",font=('微软雅黑',15),command=dislove.destroy)
    but4.pack(side=LEFT)
    but5=Button(dislove,text='我不怂',font=('微软雅黑',15),command=five)
    but5.pack(side=RIGHT)
def five():
    dislove =Toplevel(window)
    dislove.geometry('300x150+800+600')
    Label2=Label(dislove,text='好了，你没机会了',font=('微软雅黑',20))
    Label2.pack()
    but4=Button(dislove,text="你真帅",font=('微软雅黑',15),command=dislove.destroy)
    but4.pack()
#设置两个按钮
#第一个按钮，宽高，点击之后会触发command的new方法
btn1 = Button(window,text='帅气',font=('微软雅黑',18),command=new)
btn1.grid(row=4,column=1,sticky=W)
#第二个按钮
btn2 = Button(window,text='不帅',font=('微软雅黑',18),command=two)
btn2.grid(row=4,column=2,sticky=W)

#制作关窗点击事件
def closewindow():
    #messagebox.showinfo()出现一个提示框,title标题,message显示的信息
    messagebox.showinfo(title='警告',message='不许关闭，好好回答')
window.protocol("WM_DELETE_WINDOW",closewindow)
#设置循环，不然窗口无法显示出来
window.mainloop()

import random
from math import sin, cos, pi, log
from tkinter import *

CANVAS_WIDTH = 640  # 画布的宽
CANVAS_HEIGHT = 480  # 画布的高
CANVAS_CENTER_X = CANVAS_WIDTH / 2  # 画布中心的X轴坐标
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2  # 画布中心的Y轴坐标
IMAGE_ENLARGE = 11  # 放大比例
HEART_COLOR = "#ff0000"  # 心的颜色，这个是中国红


def heart_function(t, shrink_ratio: float = IMAGE_ENLARGE):
    """
    “爱心函数生成器”
    :param shrink_ratio: 放大比例
    :param t: 参数
    :return: 坐标
    """
    # 基础函数
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))

    # 放大
    x *= shrink_ratio
    y *= shrink_ratio

    # 移到画布中央
    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y

    return int(x), int(y)


def scatter_inside(x, y, beta=0.15):
    """
    随机内部扩散
    :param x: 原x
    :param y: 原y
    :param beta: 强度
    :return: 新坐标
    """
    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())

    dx = ratio_x * (x - CANVAS_CENTER_X)
    dy = ratio_y * (y - CANVAS_CENTER_Y)

    return x - dx, y - dy


def shrink(x, y, ratio):
    """
    抖动
    :param x: 原x
    :param y: 原y
    :param ratio: 比例
    :return: 新坐标
    """
    force = -1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6)  # 这个参数...
    dx = ratio * force * (x - CANVAS_CENTER_X)
    dy = ratio * force * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy


def curve(p):
    """
    自定义曲线函数，调整跳动周期
    :param p: 参数
    :return: 正弦
    """
    # 可以尝试换其他的动态函数，达到更有力量的效果（贝塞尔？）
    return 2 * (2 * sin(4 * p)) / (2 * pi)


class Heart:
    """
    爱心类
    """

    def __init__(self, generate_frame=20):
        self._points = set()  # 原始爱心坐标集合
        self._edge_diffusion_points = set()  # 边缘扩散效果点坐标集合
        self._center_diffusion_points = set()  # 中心扩散效果点坐标集合
        self.all_points = {}  # 每帧动态点坐标
        self.build(2000)

        self.random_halo = 1000

        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.calc(frame)

    def build(self, number):
        # 爱心
        for _ in range(number):
            t = random.uniform(0, 2 * pi)  # 随机不到的地方造成爱心有缺口
            x, y = heart_function(t)
            self._points.add((x, y))

        # 爱心内扩散
        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = scatter_inside(_x, _y, 0.05)
                self._edge_diffusion_points.add((x, y))

        # 爱心内再次扩散
        point_list = list(self._points)
        for _ in range(4000):
            x, y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.17)
            self._center_diffusion_points.add((x, y))

    @staticmethod
    def calc_position(x, y, ratio):
        # 调整缩放比例
        force = 1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.520)  # 魔法参数

        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)

        return x - dx, y - dy

    def calc(self, generate_frame):
        ratio = 10 * curve(generate_frame / 10 * pi)  # 圆滑的周期的缩放比例

        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))

        all_points = []

        # 光环
        heart_halo_point = set()  # 光环的点坐标集合
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)  # 随机不到的地方造成爱心有缺口
            x, y = heart_function(t, shrink_ratio=11.6)  # 魔法参数
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in heart_halo_point:
                # 处理新的点
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))

        # 轮廓
        for x, y in self._points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 3)
            all_points.append((x, y, size))

        # 内容
        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        for x, y in self._center_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_points[generate_frame] = all_points

    def render(self, render_canvas, render_frame):
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)


def draw(main: Tk, render_canvas: Canvas, render_heart: Heart, render_frame=0):
    render_canvas.delete('all')
    render_heart.render(render_canvas, render_frame)
    main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)


if __name__ == '__main__':
    root = Tk()  # 一个Tk
    canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    canvas.pack()
    heart = Heart()  # 心
    draw(root, canvas, heart)  # 开始画画~
    root.mainloop()