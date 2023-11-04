import cv2
# import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import *
import os
import numpy as np
import time
import pyautogui
from PIL import ImageFont, ImageDraw, Image
import pytesseract
import sys


#####################################
# 创建数据库
class record:
    def __init__(self):
        # 创建或打开一个数据库
        # check_same_thread 属性用来规避多线程操作数据库的问题
        self.conn = sqlite3.connect("recordinfo.db", check_same_thread=False)
        # 创建游标
        self.cursor = self.conn.cursor()
        # 建表
        self.conn.execute('create table if not exists record_table('
                          'id integer primary key autoincrement,'
                          'name varchar(30) ,'
                          'record_time timestamp)')

        self.conn.execute('create table if not exists name_table('
                          'id integer primary key autoincrement,'
                          'name varchar(30))')

        self.conn.execute('create table if not exists number_table('
                          'id integer primary key autoincrement,'
                          'name varchar(30) ,'
                          'mode varchar(30) ,'
                          'count integer)')

        self.conn.execute('create table if not exists information_table('
                          'id integer primary key autoincrement,'
                          'name varchar(30) ,'
                          'birthday varchar(30) ,'
                          'gender varchar(30) ,'
                          'common_mode varchar(30))')

        self.conn.execute('create table if not exists score_table('
                          'id integer primary key autoincrement,'
                          'song_name varchar(30) ,'
                          'name varchar(30) ,'
                          'score integer ,'
                          'Completion_degree varchar(30))')

    # 插入登入数据，包含时间和姓名
    def insert_record(self, name):
        self.conn.execute('insert into record_table values (null, ?, ?)', (name, datetime.now()))
        self.conn.commit()

    # 插入姓名数据，包含姓名（无用）
    def insert_name(self, name):
        self.conn.execute('insert into name_table values (null, ?)', [name])
        self.conn.commit()

    # 插入模式偏好信息，包含模式，姓名和使用次数
    def insert_number(self, name, mode, count):
        self.conn.execute('insert into number_table values (null, ?, ?, ?)', (name, mode, count))
        self.conn.commit()

    # 插入用户基本信息，包含姓名、生日、性别、常用模式
    def insert_information(self, name, birthday, gender, common_mode):
        self.conn.execute('insert into information_table values (null, ?, ?, ?, ?)',
                          (name, birthday, gender, common_mode))
        self.conn.commit()

    # 插入分数信息，包含歌曲名、姓名、分数、完成度
    def insert_score(self, song_name, name, score, Completion_degree):
        self.conn.execute('insert into score_table values (null, ?, ?, ?, ?)',
                          (song_name, name, score, Completion_degree))
        self.conn.commit()

    # 修改模式偏好数据，更改模式次数，用模式和姓名进行定位
    def update_number(self, name, mode, count):
        self.conn.execute('update number_table set count=:count where mode=:mode and name=:name ',
                          dict(count=count, mode=mode, name=name))
        self.conn.commit()

    # 修改用户基本信息，更改常用模式次数，姓名进行定位
    def update_information(self, name, common_mode):
        self.conn.execute('update information_table set common_mode=:common_mode where name=:name ',
                          dict(name=name, common_mode=common_mode))
        self.conn.commit()

    # 修改分数信息，更改分数、完成度数据，用歌曲名和姓名进行定位
    def update_score(self, song_name, name, score, Completion_degree):
        self.conn.execute(
            'update score_table set score=:score,Completion_degree=:Completion_degree where name=:name and song_name=:song_name',
            dict(name=name, song_name=song_name, score=score, Completion_degree=Completion_degree))
        self.conn.commit()

    # 搜索用户名
    def query_name(self):
        self.cursor.execute("select name from name_table")
        results = self.cursor.fetchall()
        name_list = []
        for i in results:
            i = list(i)
            name_list += i

        return name_list

    # 搜索模式次数
    def query_number(self, name, mode):
        self.cursor.execute("select count from number_table where mode=:mode and name=:name",
                            dict(name=name, mode=mode))
        results = self.cursor.fetchone()
        number_list = list(results)
        a = number_list[0]
        return a

    # 搜索用户信息
    def query_information(self, name):
        self.cursor.execute('select * from information_table where name=:name', dict(name=name))
        # self.cursor.execute('select * from information_table')
        results = self.cursor.fetchall()

        return results

    # 搜索用户歌曲分数
    def query_score(self, song_name, name):
        self.cursor.execute('select max(score) from score_table where song_name=:song_name and name=:name',
                            dict(song_name=song_name, name=name))
        # self.cursor.execute('select * from information_table')
        results = self.cursor.fetchone()
        score_list = list(results)
        a = score_list[0]
        return a

    # 搜索该歌曲所有分数
    def query_allscore(self, song_name):
        self.cursor.execute('select name,score from score_table where song_name=:song_name', dict(song_name=song_name))
        # self.cursor.execute('select * from information_table')
        results = self.cursor.fetchall()
        score_list = []
        for i in results:
            i = list(i)
            score_list += i
        return score_list

    # 查询排行榜
    def query_allscorelist(self, song_name):
        self.cursor.execute(
            'select name,score,Completion_degree from score_table where song_name=:song_name order by score desc',
            dict(song_name=song_name))  # 分数降序排序
        results = self.cursor.fetchall()
        return results

    def close(self):
        self.cursor.close()
        self.conn.close()


#####################################
# 给图像加中文
def put_chinese_on_img(img, text, loc):
    """
    在图像上添加中文字符
    :param img:  图像
    :param text: 文本
    :param loc: 位置
    :return:
    """
    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)

    # PIL图片上打印汉字
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    draw.text(loc, text, (255, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体

    # PIL图片转cv2 图片
    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    return cv2charimg


#####################################
# 创建新人脸识别
def makeDir():
    if not os.path.exists("face_trainer"):
        os.mkdir("face_trainer")
    if not os.path.exists("FaceData"):
        os.mkdir("FaceData")


# 获取人脸图像并保存
def getFace(name: object):
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 设置双目的宽度
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 设置双目的高度
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    count = 0
    print("正在从摄像头录入新人脸信息: \n")
    while True:
        sucess, img = cap.read()  # 从摄像头读取图片
        img_left = img[0:480, 0:640]
        gray = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0))
            count += 1
            cv2.imencode('.jpg', gray[y: y + h, x: x + w])[1].tofile(
                'FaceData/User.' + name.get() + '.' + str(count) + '.jpg')
            cv2.imshow('image', img)
        # 保持画面的持续。
        pictur_num = 20
        cv2.waitKey(1)
        if count > pictur_num:
            break
        else:  # 控制台内输出进度条
            l = int(count / pictur_num * 50)
            r = int((pictur_num - count) / pictur_num * 50)
            print("\r" + "%{:.1f}".format(count / pictur_num * 100) + "=" * l + "->" + "_" * r, end="")
    print(" 人脸录入成功")
    cap.release()
    cv2.destroyAllWindows()


# 将人脸图像与标签绑定
def getImagesAndLabels(path, detector, usernames):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        username = os.path.split(imagePath)[-1].split(".")[1]
        id = 1
        for x in usernames:
            if username == x:
                break
            else:
                id += 1

        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x: x + w])
            ids.append(id)
    return faceSamples, ids


# 对得到的人脸图像和标签进行训练
def trainFace(names):
    # 人脸数据路径
    path = 'FaceData'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces, ids = getImagesAndLabels(path, detector, names)
    recognizer.train(faces, np.array(ids))
    recognizer.write(r'face_trainer\trainer.yml')


# 创建用户数据
def add_face(name, names, birthday, gender):
    mode1 = '二轴'
    mode2 = '四轴'
    mode3 = '六轴'
    mode4 = '九轴'
    mode5 = '舞立方'
    mode6 = '舞萌'
    makeDir()
    getFace(name)
    trainFace(names)
    user = record()
    user.insert_information(name.get(), birthday.get(), gender.get(), 0)
    user.insert_name(name.get())
    user.insert_number(name.get(), mode1, 0)
    user.insert_number(name.get(), mode2, 0)
    user.insert_number(name.get(), mode3, 0)
    user.insert_number(name.get(), mode4, 0)
    user.insert_number(name.get(), mode5, 0)
    user.insert_number(name.get(), mode6, 0)


###################################################
# 人脸检测
def check(names):
    cam = cv2.VideoCapture(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 设置双目的宽度
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 设置双目的高度
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face_trainer/trainer.yml")
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    while True:
        ret, img = cam.read()
        img_left = img[0:480, 0:640]
        gray = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10, minSize=(int(minW), int(minH)))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            idnum, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if confidence < 100:
                username = names[idnum - 1]
                confidence = "{0}%".format(round(100 - confidence))
                # img = put_chinese_on_img(img, str(username), (x + 5, y - 5))
                # cv2.putText(img, str(username), (x + 5, y - 5), font, 1, (0, 0, 255), 1)
                # cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (0, 0, 0), 1)
                # cv2.imshow('camera', img)

                time.sleep(1)

                record().insert_record(username)  # 签到信息插入数据库
                a = username
                # cam.release()
                # cv2.destroyAllWindows()
                return a
            else:
                a = 2  # a=2用来判断是否识别到身份，用于下面代码创建人脸录入界面
                print("unknow")
                cam.release()
                cv2.destroyAllWindows()
                return a

        # cv2.imshow('camera', img)
        # k = cv2.waitKey(10)
        # if k == 27:
        #     break


#######################################################
# gui设计
class APP:
    def __init__(self):

        self.root = Tk()
        self.root.title('FACE')
        self.root.geometry('%dx%d' % (480, 420))

        # 数据库实例创建
        self.mydb = record()

        self.createFirstPage()

        # 新录入的人的姓名
        self.name = StringVar()
        mainloop()

    def createFirstPage(self):
        # self.usernames 是 用户名字组成的列表
        self.usernames = []
        self.usernames = self.mydb.query_name()
        if len(self.usernames) != 0:
            a = check(self.usernames)
            if a == 2:
                self.page1 = Frame(self.root)
                self.page1.grid()
                Label(self.page1, height=4, text='人脸识别系统', font=('粗体', 20)).grid(columnspan=2)
                self.button12 = Button(self.page1, width=18, height=2, text="录入新的人脸", bg='green', font=("宋", 12),
                                       relief='raised', command=self.createSecondPage)
                self.button12.grid(row=1, column=0, padx=25, pady=10)
                self.button13 = Button(self.page1, width=18, height=2, text="游客模式", bg='gray', font=("宋", 12),
                                       relief='raised', command=self.quitMain)
                self.button13.grid(row=1, column=1, padx=25, pady=10)
            else:
                name = a
                mode1 = '二轴'
                mode2 = '四轴'
                mode3 = '六轴'
                mode4 = '九轴'
                mode5 = '舞立方'
                mode6 = '舞萌'
                a1 = self.mydb.query_number(name, mode1)
                a2 = self.mydb.query_number(name, mode2)
                a3 = self.mydb.query_number(name, mode3)
                a4 = self.mydb.query_number(name, mode4)
                a5 = self.mydb.query_number(name, mode5)
                a6 = self.mydb.query_number(name, mode6)
                self.counter1 = IntVar()  # 创建一个整型变量对象
                self.counter1.set(a1)  # 置其初值为0
                self.counter2 = IntVar()
                self.counter2.set(a2)
                self.counter3 = IntVar()
                self.counter3.set(a3)
                self.counter4 = IntVar()
                self.counter4.set(a4)
                self.counter5 = IntVar()
                self.counter5.set(a5)
                self.counter6 = IntVar()
                self.counter6.set(a6)
                self.page4 = Frame(self.root)
                self.page4.grid()
                Label(self.page4, height=3, text='欢迎使用', font=('粗体', 20)).grid(columnspan=3)
                # Label(self.page4, height=3, textvariable=self.counter1, font=("Arial Bold", 10)).grid(columnspan=3)
                self.button14 = Button(self.page4, width=18, height=2, text="二轴", bg='green', font=("宋", 12),
                                       relief='raised', command=lambda: self.erzhou(a))
                self.button14.grid(row=1, column=0, padx=25, pady=10)
                self.button15 = Button(self.page4, width=18, height=2, text="四轴", bg='gray', font=("宋", 12),
                                       relief='raised', command=lambda: self.sizhou(a))
                self.button15.grid(row=1, column=1, padx=25, pady=10)
                self.button16 = Button(self.page4, width=18, height=2, text="六轴", bg='green', font=("宋", 12),
                                       relief='raised', command=lambda: self.liuzhou(a))
                self.button16.grid(row=2, column=0, padx=25, pady=10)
                self.button17 = Button(self.page4, width=18, height=2, text="九轴", bg='gray', font=("宋", 12),
                                       relief='raised', command=lambda: self.jiuzhou(a))
                self.button17.grid(row=2, column=1, padx=25, pady=10)
                self.button18 = Button(self.page4, width=18, height=2, text="舞立方", bg='green', font=("宋", 12),
                                       relief='raised', command=lambda: self.wulifang(a))
                self.button18.grid(row=3, column=0, padx=25, pady=10)
                self.button19 = Button(self.page4, width=18, height=2, text="舞萌", bg='gray', font=("宋", 12),
                                       relief='raised', command=lambda: self.wumeng(a))
                self.button19.grid(row=3, column=1, padx=25, pady=10)
                self.button20 = Button(self.page4, width=18, height=2, text="截图", bg='green', font=("宋", 12),
                                       relief='raised', command=lambda: self.jietu(a))
                self.button20.grid(row=4, column=0, padx=25, pady=10)
                self.button21 = Button(self.page4, width=18, height=2, text="退出", bg='gray', font=("宋", 12),
                                       relief='raised', command=self.quitMain)
                self.button21.grid(row=4, column=1, padx=25, pady=10)
        else:
            self.page1 = Frame(self.root)
            self.page1.grid()
            Label(self.page1, height=4, text='人脸识别系统', font=('粗体', 20)).grid(columnspan=2)
            self.button12 = Button(self.page1, width=18, height=2, text="录入新的人脸", bg='green', font=("宋", 12),
                                   relief='raised', command=self.createSecondPage)
            self.button12.grid(row=1, column=0, padx=25, pady=10)
            self.button13 = Button(self.page1, width=18, height=2, text="游客模式", bg='gray', font=("宋", 12),
                                   relief='raised', command=self.quitMain)
            self.button13.grid(row=1, column=1, padx=25, pady=10)

    def createSecondPage(self):
        self.camera = cv2.VideoCapture(1)
        self.page1.grid_forget()
        self.page2 = Frame(self.root)
        self.page2.pack()
        Label(self.page2, text='欢迎使用人脸识别系统', font=('粗体', 20)).pack()
        # 输入姓名的文本框
        # self.name = StringVar()
        self.birthday = StringVar()
        self.gender = StringVar()
        self.Label01 = Label(self.page2, text='姓名', font=('宋', 18)).pack()
        self.text1 = Entry(self.page2, textvariable=self.name, width=20, font=('宋', 18)).pack()
        self.Label02 = Label(self.page2, text='生日', font=('宋', 18)).pack()
        self.text2 = Entry(self.page2, textvariable=self.birthday, width=20, font=('宋', 18)).pack()
        self.Label03 = Label(self.page2, text='性别', font=('宋', 18)).pack()
        self.text3 = Entry(self.page2, textvariable=self.gender, width=20, font=('宋', 18)).pack()

        # 确认名字的按钮
        self.button21 = Button(self.page2, text='确认', bg='white', font=("宋", 12),
                               relief='raised', command=lambda: add_face(self.name, self.usernames, self.birthday,
                                                                        self.gender))
        self.button21.pack(padx=5, pady=5)

        # 返回按钮
        self.button22 = Button(self.page2, text="返回", bg='white', font=("宋", 12),
                               relief='raised', command=self.backFirst)
        self.button22.pack(padx=10, pady=10)

    def backFirst(self):
        self.page2.pack_forget()
        self.root.geometry('400x300')
        self.page1.grid()

    def quitMain(self):
        sys.exit(0)

    #####################################
    # 判断常玩游戏模式
    def pdcommon_mode(self, name):
        mode1 = '二轴'
        mode2 = '四轴'
        mode3 = '六轴'
        mode4 = '九轴'
        mode5 = '舞立方'
        mode6 = '舞萌'
        a1 = self.mydb.query_number(name, mode1)
        a2 = self.mydb.query_number(name, mode2)
        a3 = self.mydb.query_number(name, mode3)
        a4 = self.mydb.query_number(name, mode4)
        a5 = self.mydb.query_number(name, mode5)
        a6 = self.mydb.query_number(name, mode6)
        list1 = [a1, a2, a3, a4, a5, a6]
        num = max(list1)
        self.mydb.cursor.execute('select mode from number_table where count=:count', dict(count=num))
        results = self.mydb.cursor.fetchone()
        number_list = list(results)
        result = number_list[0]
        self.mydb.update_information(name, common_mode=result)
        return result, num

    def erzhou(self, a):
        mode = '二轴'
        name = a
        self.counter1.set(self.counter1.get() + 1)
        # self.mydb.insert_number(name, mode, self.counter1.get())
        self.mydb.update_number(name, mode, self.counter1.get())
        print('当前模式：二轴已使用{}次'.format(self.mydb.query_number(name, mode)))
        print('常用模式：{}'.format(self.pdcommon_mode(name)[0]), '使用了{}次'.format(self.pdcommon_mode(name)[1]))

    def sizhou(self, a):
        mode = '四轴'
        name = a
        self.counter2.set(self.counter2.get() + 1)
        # self.mydb.insert_number(name, mode, self.counter2.get())
        self.mydb.update_number(name, mode, self.counter2.get())
        print('当前模式：四轴已使用{}次'.format(self.mydb.query_number(name, mode)))
        print('常用模式：{}'.format(self.pdcommon_mode(name)[0]), '使用了{}次'.format(self.pdcommon_mode(name)[1]))

    def liuzhou(self, a):
        mode = '六轴'
        name = a
        self.counter3.set(self.counter3.get() + 1)
        # self.mydb.insert_number(name, mode, self.counter3.get())
        self.mydb.update_number(name, mode, self.counter3.get())
        print('当前模式：六轴已使用{}次'.format(self.mydb.query_number(name, mode)))
        print('常用模式：{}'.format(self.pdcommon_mode(name)[0]), '使用了{}次'.format(self.pdcommon_mode(name)[1]))

    def jiuzhou(self, a):
        mode = '九轴'
        name = a
        self.counter4.set(self.counter4.get() + 1)
        # self.mydb.insert_number(name, mode, self.counter4.get())
        self.mydb.update_number(name, mode, self.counter4.get())
        print('当前模式：九轴已使用{}次'.format(self.mydb.query_number(name, mode)))
        print('常用模式：{}'.format(self.pdcommon_mode(name)[0]), '使用了{}次'.format(self.pdcommon_mode(name)[1]))

    def wulifang(self, a):
        mode = '舞立方'
        name = a
        self.counter5.set(self.counter5.get() + 1)
        # self.mydb.insert_number(name, mode, self.counter5.get())
        self.mydb.update_number(name, mode, self.counter5.get())
        print('当前模式：舞立方已使用{}次'.format(self.mydb.query_number(name, mode)))
        print('常用模式：{}'.format(self.pdcommon_mode(name)[0]), '使用了{}次'.format(self.pdcommon_mode(name)[1]))

    def wumeng(self, a):
        mode = '舞萌'
        name = a
        self.counter6.set(self.counter6.get() + 1)
        # self.mydb.insert_number(name, mode, self.counter6.get())
        self.mydb.update_number(name, mode, self.counter6.get())
        print('当前模式：舞萌已使用{}次'.format(self.mydb.query_number(name, mode)))
        print('常用模式：{}'.format(self.pdcommon_mode(name)[0]), '使用了{}次'.format(self.pdcommon_mode(name)[1]))

    #######################################################
    # 截图分数识别
    def jietu(self, a):
        name = a
        img = pyautogui.screenshot(region=[280, 700, 180, 180])  # x,y,w,h
        img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)  # cvtColor用于在图像中不同的色彩空间进行转换,用于后续处理。
        score_img = pyautogui.screenshot(region=[1230, 270, 200, 50])
        score_img = cv2.cvtColor(np.asarray(score_img), cv2.COLOR_RGB2BGR)
        Completion_degree_img = pyautogui.screenshot(region=[1510, 270, 100, 50])
        Completion_degree_img = cv2.cvtColor(np.asarray(Completion_degree_img), cv2.COLOR_RGB2BGR)
        cv2.imwrite('screenshot.jpg', img)
        # cv2.imwrite('fenshu.jpg', score_img)
        # cv2.imwrite('wangchengdu.jpg', Completion_degree_img)

        score = pytesseract.image_to_string(score_img, lang="eng")
        Completion_degree = pytesseract.image_to_string(Completion_degree_img, lang="eng")

        # flags=0
        # 灰色读入目标图像
        targetPath = 'screenshot.jpg'
        trainingImage = cv2.imread(targetPath, flags=0)
        # 灰色读所有模板图片
        templatePath = 'test/'
        icons = os.listdir(templatePath)
        iconMatch = dict({'name': '未识别', 'value': 0})
        for icon in icons:
            queryImage = cv2.imread(templatePath + icon, 0)
            # 使用SIFT 检测角点
            sift = cv2.xfeatures2d.SIFT_create()
            kp1, des1 = sift.detectAndCompute(queryImage, None)
            kp2, des2 = sift.detectAndCompute(trainingImage, None)
            # 设置FLANN匹配器参数，定义FLANN匹配器，使用 KNN 算法实现匹配
            indexParams = dict(algorithm=0, trees=5)
            searchParams = dict(checks=50)
            flann = cv2.FlannBasedMatcher(indexParams, searchParams)
            matches = flann.knnMatch(des1, des2, k=2)

            # 根据matches生成相同长度的matchesMask列表，列表元素为[0,0]
            matchesMask = [[0, 0] for i in range(len(matches))]
            matchNumber = 0
            # 去除错误匹配, 此处阈值设定为0.7
            for i, (m, n) in enumerate(matches):
                if m.distance < 0.7 * n.distance:
                    matchesMask[i] = [1, 0]
                    matchNumber = matchNumber + 1

            # 将图像显示
            # matchColor是两图的匹配连接线，连接线与matchesMask相关
            # singlePointColor是勾画关键点
            drawParams = dict(matchColor=(0, 255, 0), matchesMask=matchesMask[:50], flags=0)
            resultImage = cv2.drawMatchesKnn(queryImage, kp1, trainingImage, kp2, matches[:50], None, **drawParams)

            if matchNumber > iconMatch['value']:
                iconMatch['name'] = icon.split('_')[0]
                iconMatch['value'] = matchNumber
        if iconMatch['value'] < 50:
            mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
            print(mkfile_time)
            cv2.imwrite('test/{}.jpg'.format(mkfile_time), img)
            self.mydb.insert_score(mkfile_time, name, score, Completion_degree)
        else:
            try:
                result = self.mydb.query_score(iconMatch['name'], name)
                if int(score) >= int(result):
                    self.mydb.update_score(iconMatch['name'], name, score, Completion_degree)
            except TypeError:
                self.mydb.insert_score(iconMatch['name'], name, score, Completion_degree)

        self.page3 = Frame(self.root)
        self.page4.grid_forget()
        self.root.geometry('700x360')
        self.page3.pack()
        Label(self.page3, text='排行榜', bg='white', fg='red', font=('宋体', 25)).pack(side=TOP, fill='x')
        # 签到信息查看视图
        self.checkDate = ttk.Treeview(self.page3, show='headings', column=('sid', 'name', 'score', 'Completion_degree'))
        self.checkDate.column('sid', width=100, anchor="center")
        self.checkDate.column('name', width=150, anchor="center")
        self.checkDate.column('score', width=150, anchor="center")
        self.checkDate.column('Completion_degree', width=150, anchor="center")

        self.checkDate.heading('sid', text='排名')
        self.checkDate.heading('name', text='名字')
        self.checkDate.heading('score', text='分数')
        self.checkDate.heading('Completion_degree', text='完成度')

        # 插入数据
        self.records = list(self.mydb.query_allscorelist(iconMatch['name']))  # 将元组转化为列表
        self.score = []
        for i in range(len(self.records)):
            self.scorelist = list(self.records[i])  # 将元组转化为列表
            self.scorelist.insert(0, i + 1)  # 在列表中增加排名序号
            self.score.append(self.scorelist)  # 将增加排名序号的列表加入新列表中

        for i in self.score:
            self.checkDate.insert('', 'end', values=i)  # 将列表中数据填入查看窗口

        # y滚动条
        yscrollbar = Scrollbar(self.page3, orient=VERTICAL, command=self.checkDate.yview)
        self.checkDate.configure(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side=RIGHT, fill=Y)

        self.checkDate.pack(expand=1, fill=BOTH)

        # 返回按钮
        Button(self.page3, width=20, height=2, text="返回", bg='gray', font=("宋", 12),
               relief='raised', command=self.backMain).pack(padx=20, pady=20)

    # 返回
    def backMain(self):
        self.root.geometry('480x420')
        self.page3.pack_forget()
        self.page4.grid()


if __name__ == '__main__':
    demo = APP()
