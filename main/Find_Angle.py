import cv2
import numpy as numpy
import math
from PIL import Image
import os
import datetime

# tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import Image, ImageTk
import tk_cut_class
import tk_mouse_tracking_class
import tk_Rtrim_class


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Find Angle Tool")
        self.iconbitmap('./icon.ico')
        self.minsize(640,420)
        # self.configure(background = '#4D4D4D')

        # Parts Position
        self.rp_x = 10   #Reference Position
        self.rp_y = 10   #Reference Position
        # y axis
        self.lp1 = 0+self.rp_y
        self.p1 = 30+self.rp_y
        self.lp2 = 60+self.rp_y
        self.p2 = 90+self.rp_y
        self.lp3 = 120+self.rp_y
        self.p3 = 140+self.rp_y
        self.lp4 = 200+self.rp_y
        # self.p4 = 210+self.rp_y
        self.lp5 = 240+self.rp_y
        self.p5 = 270+self.rp_y
        self.lp6 = 280+self.rp_y
        self.lp7 = 320+self.rp_y
        self.lp8 = 360+self.rp_y

        # Rotation Trim
        self.trim_topx = 500
        self.trim_topy = 300
        self.trim_botx = 800
        self.trim_boty = 1000
        self.trim_bool = False

        # finish level
        self.first_l = False
        self.second_l = False
        self.third_l = False
        self.forth_l = False
        self.fifth_l = False    

        self.filename =""
        self.radValues = 0

        # Save Data 
        self.write_bool = BooleanVar()
        self.video_bool = BooleanVar()
        self.rotation_bool = BooleanVar()
        self.angle = StringVar()
        
        # cut range value
        self.topx, self.topy, self.botx, self.boty = 0, 0, 0, 0
        self.rect_id = None

        # pivot value
        self.pivot_x ,self.pivot_y = 0, 0

        # ----first column----
        # Label1
        self.label1 = ttk.Label(self, text = "Select Your Video")
        self.label1.place(x = self.rp_x, y = self.lp1)

        # file braws
        self.button_open_file()

        # Label2
        self.label2 = ttk.Label(self, text = "Not Selected")
        self.label2.configure(foreground = 'red')
        self.label2.place(x = self.rp_x + 100, y = self.p1 + 3)

        # ----second column----
        # radio
        self.radioButton()
        
        # ----third column----z
        # slider
        self.label_resize = ttk.Label(self, text = "Resize Value")
        self.label_resize.place(x = self.rp_x, y = self.lp3)
  
        self.resize = Scale(self, from_=1, to=10, orient=HORIZONTAL)
        self.resize.place(x = self.rp_x, y = self.p3)

        self.label_resize_explain1 = ttk.Label(self, text = "More than 1000px Image, you can resize.")
        self.label_resize_explain1.place(x = self.rp_x + 120, y = self.p3)
        self.label_resize_explain2 = ttk.Label(self, text = "Ex. If you choose 2, Resolution will be 1/2.")
        self.label_resize_explain2.place(x = self.rp_x + 120, y = self.p3+20)

        # ----forth column----
        # start button
        self.button_start = ttk.Button(self, text = "Show Selected Video",command = self.ShowImage)
        self.button_start.place(x = self.rp_x, y = self.lp4)

        # Log
        self.label3 = ttk.Label(self, text = "Show Your Image With Filter Selected")
        self.label3.place(x = self.rp_x + 150, y = self.lp4+3)
        
        # ----fifth column----
        # cit button
        self.button_cut = ttk.Button(self, text = "Cut Frame Image",command = self.CutImage)
        self.button_cut.place(x = self.rp_x, y = self.lp5)

        # Log
        self.label_cut = ttk.Label(self, text = "Select Cut Range")
        self.label_cut.place(x = self.rp_x + 150, y = self.lp5+3)
        
        # check button
        self.button_check_cut = ttk.Button(self, text = "Check Cut Range", command=self.CheckCut)
        self.button_check_cut.place(x = self.rp_x + 350, y = self.lp5)
        
        # Check Log
        self.label_check_cut = ttk.Label(self, text = "")
        self.label_check_cut.place(x = self.rp_x + 450, y = self.lp5+3)

        # ----sixth column----
        # button
        self.button_pivot = ttk.Button(self, text = "Put Pivot On Image",command=self.SetPivot)
        self.button_pivot.place(x = self.rp_x, y = self.lp6)

        # Log
        self.label_pivot = ttk.Label(self, text = "Put Pivot On Image")
        self.label_pivot.place(x = self.rp_x + 150, y = self.lp6+3)

        # ----seventh column----
        # button
        self.button_make_frame = ttk.Button(self, text = "Make Frame Image", command=self.DrawLine)
        self.button_make_frame.place(x = self.rp_x, y = self.lp7)

        # Log
        self.label_make_frame = ttk.Label(self, text = "Make Frame Image")
        self.label_make_frame.place(x = self.rp_x + 150, y = self.lp7+3)
        
        # Frame Image Save Check
        self.check_Frame = ttk.Checkbutton(self, text = "Frame Image Save", variable=self.write_bool)
        self.check_Frame.place(x = self.rp_x + 300, y = self.lp7+3)
                
        # Save Video
        self.check_Video = ttk.Checkbutton(self, text = "Video Save", variable=self.video_bool)
        self.check_Video.place(x = self.rp_x + 430, y = self.lp7+3)
        
        # Rotation
        self.check_Rotation = ttk.Checkbutton(self, text = "Rotation", variable=self.rotation_bool)
        self.check_Rotation.place(x = self.rp_x + 520, y = self.lp7+3)

        # Angle Input Label
        self.label_AngleImput = ttk.Label(self, text = "Angle:")
        self.label_AngleImput.place(x = self.rp_x + 540, y = self.lp7+25)

        # Angle Input
        self.AngleImputText = ttk.Entry(self, width = 5, textvariable = self.angle)
        self.AngleImputText.place(x = self.rp_x + 580, y = self.lp7+25)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length=620, mode='determinate')
        self.progress_bar.place(x = self.rp_x, y = self.lp8+15)

    def ShowImage(self):
        if(self.first_l == False):     
            self.label3.configure(text = "Please Select File")
            self.label3.configure(foreground = 'red')

        elif(self.second_l == False):
            self.label3.configure(text = "Please Select Filter")
            self.label3.configure(foreground = 'red')

        else:
            radSelected = self.radValues.get()
            resize_value = self.resize.get()

            cap = cv2.VideoCapture(self.filename)

            # Image Width
            W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            # Image Height
            H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            # All Frame
            count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            
            self.label3.configure(text = "All Frame： " + str(count) + ",Height： " + str(H) + ",Width： " + str(W))
            self.label3.configure(foreground = 'black')

            i=0
            while (cap.isOpened()):
                # 大きすぎる画像を処理するのに必要
                # cv2.namedWindow("output", cv2.WINDOW_NORMAL)  
                frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES)
                _, frame = cap.read()
                # frame = cv2.imread('a.PNG')

                # if(frame_num > end_frame):
                #     break

                if(frame is None):
                    break
                # リサイズ
                if(W > 1000):
                    frame = cv2.resize(frame, (int(W/resize_value), int(H/resize_value)))                    # Resize 
                
                
                if(radSelected == 1):
                    cv2.imshow("frame", frame)
                    cv2.waitKey(15)
                    i += 1

                elif(radSelected == 2):
                    # グレースケール化          
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("frame", frame_gray)
                    cv2.waitKey(15)
                    i += 1
                elif(radSelected == 3):
                    # グレースケール化          
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    #平滑化（ぼかし）Smoothing
                    first_frame_trim_gray_Smoothing = cv2.GaussianBlur(frame_gray,(7,7),0)

                    # 2値化処理
                    thresh = 180
                    maxval = 255
                    _,frame_BW = cv2.threshold(first_frame_trim_gray_Smoothing,thresh,maxval,cv2.THRESH_BINARY)

                    cv2.imshow("frame", frame_BW)
                    cv2.waitKey(15)
                    i += 1
                else:
                    self.label3.configure(text = "Error")
                    self.label3.configure(foreground = 'red')
    
    def CheckCut(self):
        if(self.first_l == False):     
            self.label_check_cut.configure(text = "Please Select File")
            self.label_check_cut.configure(foreground = 'red')

        elif(self.second_l == False):
            self.label_check_cut.configure(text = "Please Select Filter")
            self.label_check_cut.configure(foreground = 'red')

        elif(self.third_l == False):
            self.label_check_cut.configure(text = "Please Set Cut Range")
            self.label_check_cut.configure(foreground = 'red')

        else:
            self.label_check_cut.configure(text = "")
            self.label_check_cut.configure(foreground = 'Black')

            # 【変更可能な変数】
            # --------------------- 
            if(self.boty > self.topy):
                # 白点トリミングサイズ
                white_trim_width = self.boty - self.topy       #left:60 ,right:60
                # 白点トリミング位置
                white_trim_x = self.topy         #left:100 ,right:300
            else:
                white_trim_width = self.topy - self.boty       #left:60 ,right:60
                white_trim_x = self.boty         #left:100 ,right:300
            
            if(self.botx > self.topx):
                white_trim_height = self.botx - self.topx     #left:120,right:120
                white_trim_y = self.topx            #left:0 ,right:0
            else:
                white_trim_height = self.topx - self.botx   #left:120,right:120
                white_trim_y = self.botx            #left:0 ,right:0
            # ---------------------
            
            radSelected = self.radValues.get()
            resize_value = self.resize.get()

            cap = cv2.VideoCapture(self.filename)

            # Image Width
            W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            # Image Height
            H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            # All Frame
            count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            
            self.label3.configure(text = "All Frame： " + str(count) + ",Height： " + str(H) + ",Width： " + str(W))
            self.label3.configure(foreground = 'black')

            # 座標
            f_x = 0
            f_y = 0

            i=0
            while (cap.isOpened()):
                # 大きすぎる画像を処理するのに必要
                # cv2.namedWindow("output", cv2.WINDOW_NORMAL)  
                frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES)
                _, frame = cap.read()
                # frame = cv2.imread('a.PNG')

                # if(frame_num > end_frame):
                #     break

                if(frame is None):
                    break
                # リサイズ
                if(W > 1000):
                    frame = cv2.resize(frame, (int(W/resize_value), int(H/resize_value)))                    # Resize 
                
                #　トリミング範囲補正
                first_frame_trim = frame[white_trim_x:white_trim_x + white_trim_width,white_trim_y:white_trim_y + white_trim_height]
                
                if(radSelected == 1):
                    # グレースケール化          
                    first_frame_trim_gray = cv2.cvtColor(first_frame_trim, cv2.COLOR_BGR2GRAY)
                    
                    #平滑化（ぼかし）Smoothing
                    first_frame_trim_gray_Smoothing = cv2.GaussianBlur(first_frame_trim_gray,(7,7),0)

                    # 2値化処理
                    thresh = 180
                    maxval = 255
                    _,frame_BW = cv2.threshold(first_frame_trim_gray_Smoothing,thresh,maxval,cv2.THRESH_BINARY)

                    #輪郭の表示
                    _, first_frame_trim_gray_Smoothing_bw_contours, _ = cv2.findContours(frame_BW, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    first_frame_trim_gray_Smoothing_bw_contours = sorted(first_frame_trim_gray_Smoothing_bw_contours, key=lambda x: cv2.contourArea(x), reverse=False) #輪郭が一番小さい順に並べる
                    for cnt in first_frame_trim_gray_Smoothing_bw_contours:
                            (x, y, w, h) = cv2.boundingRect(cnt)
                            cv2.drawContours(first_frame_trim, [cnt], -1, (0,0,255),1) #輪郭の表示
                            # cv2.circle(first_frame_trim, (int(x+w/2), int(y+h/2)), 2, (255, 0, 0), 5) #円で表示
                            #代入→元の画像の座標に変換
                            f_x = int(x+w/2)+white_trim_y
                            f_y = int(y+h/2)+white_trim_x
                                    
                            #　回転中心の表示
                            # cv2.circle(first_frame_trim, (x, y), 5, (0, 255, 0), 2)
                            
                            # print("今のフレーム：" + str(frame_num))
                            # print("first_frame_trimの中心座標：(" + str(f_x) + "," + str(f_y) + ")")
                    
                    
                    cv2.imshow("frame", first_frame_trim)
                    cv2.waitKey(15)
                    i += 1

                elif(radSelected == 2):
                    # グレースケール化          
                    frame_gray = cv2.cvtColor(first_frame_trim, cv2.COLOR_BGR2GRAY)
                    
                    cv2.imshow("frame", frame_gray)
                    cv2.waitKey(15)
                    i += 1
                elif(radSelected == 3):
                    # グレースケール化          
                    first_frame_trim_gray = cv2.cvtColor(first_frame_trim, cv2.COLOR_BGR2GRAY)
                    
                    #平滑化（ぼかし）Smoothing
                    first_frame_trim_gray_Smoothing = cv2.GaussianBlur(first_frame_trim_gray,(7,7),0)

                    # 2値化処理
                    thresh = 180
                    maxval = 255
                    _,frame_BW = cv2.threshold(first_frame_trim_gray_Smoothing,thresh,maxval,cv2.THRESH_BINARY)

                    cv2.imshow("frame", frame_BW)
                    cv2.waitKey(15)
                    i += 1
                else:
                    self.label_check_cut.configure(text = "Error")
                    self.label_check_cut.configure(foreground = 'red')
    
    def Filter_Frame(self):
        if(self.rotation_bool.get()):
            self.TrimImage()
        else:
            self.DrawLine()

    def DrawLine(self):
        
        def get_angle(x1, y1, x2, y2, x3, y3):
            angle = (math.atan2(y1 - y2, x1 - x2) - math.atan2(y3 - y2, x3 - x2)) / math.pi * 180

            return angle

        if(self.first_l == False):     
            self.label_make_frame.configure(text = "Please Select File")
            self.label_make_frame.configure(foreground = 'red')

        elif(self.second_l == False):
            self.label_make_frame.configure(text = "Please Select Filter")
            self.label_make_frame.configure(foreground = 'red')

        elif(self.third_l == False):
            self.labellabel_make_frame_check_cut.configure(text = "Please Set Cut Range")
            self.label_make_frame.configure(foreground = 'red')

        elif(self.forth_l == False):
            self.label_make_frame.configure(text = "Please Set Pivot Position")
            self.label_make_frame.configure(foreground = 'red')

        else:
            # 【変更可能な変数】
            # --------------------- 
            if(self.boty > self.topy):
                # 白点トリミングサイズ
                white_trim_width = self.boty - self.topy       #left:60 ,right:60
                # 白点トリミング位置
                white_trim_x = self.topy         #left:100 ,right:300
            else:
                white_trim_width = self.topy - self.boty       #left:60 ,right:60
                white_trim_x = self.boty         #left:100 ,right:300
            
            if(self.botx > self.topx):
                white_trim_height = self.botx - self.topx     #left:120,right:120
                white_trim_y = self.topx            #left:0 ,right:0
            else:
                white_trim_height = self.topx - self.botx   #left:120,right:120
                white_trim_y = self.botx            #left:0 ,right:0

            c_x = self.pivot_x
            c_y = self.pivot_y
            
            # ---------------------------------                
            # 回転ゲイン
            rot_gain = 0              #left:75 ,right:105
            # 最終トリミングサイズ
            trim_width = 200            #left:150 ,right:150
            trim_height = 450           #left:300 ,right:300
            # 最終トリミング位置
            trim_x = 0                  #left:0 ,right:0
            trim_y = 450                #left:250 ,right:350
            # ---------------------------------
            # ---------------------

            if(self.write_bool.get() or self.video_bool.get()):
                dt_now = datetime.datetime.now()
                new_dir_path = './' + str(dt_now.strftime('%Y_%m_%d_%H_%M_%S'))
                os.mkdir(new_dir_path)

            radSelected = self.radValues.get()
            resize_value = self.resize.get()

            cap = cv2.VideoCapture(self.filename)

            # Image Width
            W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            # Image Height
            H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            # All Frame
            count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            
        
            if(self.video_bool.get() == True):
                # 動画作成用変数
                frame_rate = 30.0
                if(self.rotation_bool.get()):
                    width = int(trim_width)
                    height = int(trim_height)
                else:    
                    width = int(W/resize_value)
                    height = int(H/resize_value)

                fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
                video = cv2.VideoWriter(new_dir_path + '/movie.mp4', fourcc, frame_rate, (width, height))

            # 座標
            f_x = 0
            f_y = 0
            s_x = 0
            s_y = 0

            i=0
            while (cap.isOpened()):
                # プログラスバー
                self.progress_bar["value"] = i * 100 / count + 5
                self.progress_bar.update()

                # 大きすぎる画像を処理するのに必要
                # cv2.namedWindow("output", cv2.WINDOW_NORMAL)  
                frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES)
                _, frame = cap.read()
                # frame = cv2.imread('a.PNG')

                # if(frame_num > end_frame):
                #     break

                if(frame is None):
                    # プログラスバー
                    self.progress_bar["value"] = 100
                    self.progress_bar.update()
                    break
                # リサイズ
                if(W > 1000):
                    frame = cv2.resize(frame, (int(W/resize_value), int(H/resize_value)))                    # Resize 
                
                #　トリミング範囲補正
                first_frame_trim = frame[white_trim_x:white_trim_x + white_trim_width,white_trim_y:white_trim_y + white_trim_height]

                # グレースケール化          
                first_frame_trim_gray = cv2.cvtColor(first_frame_trim, cv2.COLOR_BGR2GRAY)
                
                #平滑化（ぼかし）Smoothing
                first_frame_trim_gray_Smoothing = cv2.GaussianBlur(first_frame_trim_gray,(7,7),0)

                # 2値化処理
                thresh = 180
                maxval = 255
                _,frame_BW = cv2.threshold(first_frame_trim_gray_Smoothing,thresh,maxval,cv2.THRESH_BINARY)

                #輪郭の表示
                _, first_frame_trim_gray_Smoothing_bw_contours, _ = cv2.findContours(frame_BW, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                first_frame_trim_gray_Smoothing_bw_contours = sorted(first_frame_trim_gray_Smoothing_bw_contours, key=lambda x: cv2.contourArea(x), reverse=False) #輪郭が一番小さい順に並べる
                for cnt in first_frame_trim_gray_Smoothing_bw_contours:
                        (x, y, w, h) = cv2.boundingRect(cnt)
                        cv2.drawContours(first_frame_trim, [cnt], -1, (0,0,255),1) #輪郭の表示
                        # cv2.circle(first_frame_trim, (int(x+w/2), int(y+h/2)), 2, (255, 0, 0), 5) #円で表示
                        #代入→元の画像の座標に変換
                        s_x = int(x+w/2)+white_trim_y
                        s_y = int(y+h/2)+white_trim_x
                                
                        #　回転中心の表示
                        # cv2.circle(first_frame_trim, (x, y), 5, (0, 255, 0), 2)
                        
                        print("Current Frame：" + str(frame_num) + ", Rotation Position：(" + str(s_x) + "," + str(s_y) + ")" + ", Pivot Position：(" + str(self.pivot_x) + "," + str(self.pivot_y) + ")")
                
                #　支点の表示
                cv2.circle(frame, (c_x, c_y), 2, (0, 0, 255), 5)
                #　回転中心の表示
                cv2.circle(frame, (s_x, s_y), 2, (0, 255, 255), 5)
                #　線を引く
                cv2.line(frame, (c_x, c_y), (s_x, s_y), (255, 255, 255), thickness=2, lineType=cv2.LINE_4)
                #　画像の表示    
                # cv2.imshow("frame_trim",first_frame_trim)
                # cv2.imshow("frame",frame)

                if(frame_num == 0):
                    f_x = s_x
                    f_y = s_y

            # 回転処理
                if(self.rotation_bool.get()):     

                    if(self.angle.get() != ""):
                        rot_gain = int(self.angle.get())

                    h, w = frame.shape[:2]

                    if(h>w):
                        w=h
                    else:
                        h=w

                    # 回転角の指定(二フレーム以降)
                    if(frame_num > 0):
                        angle = get_angle(s_x,s_y,c_x,c_y,f_x,f_y) + rot_gain
                        print('角度：{:.1f}°'.format(angle))
                        angle_rad = angle/180.0*numpy.pi
                    else:
                        # 回転角の指定
                        angle = 0 + rot_gain
                        angle_rad = angle/180.0*numpy.pi

                    # 回転後の画像サイズを計算
                    w_rot = w+100
                    h_rot = h+100
                    size_rot = (w_rot, h_rot)

                    # 元画像の中心を軸に回転する
                    center = (c_x, c_y)
                    scale = 1.0
                    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

                    # 平行移動を加える (rotation + translation)
                    affine_matrix = rotation_matrix.copy()
                    affine_matrix[0][2] = affine_matrix[0][2] -c_x + w_rot/2
                    affine_matrix[1][2] = affine_matrix[1][2] -c_y + h_rot/2

                    first_rot = cv2.warpAffine(frame, affine_matrix, size_rot, flags=cv2.INTER_CUBIC)
                    
                    # if(self.trim_topx > self.trim_botx):
                    #     trim_x = self.trim_topx
                    #     trim_width = self.trim_topx - self.trim_botx
                    # else:
                    #     trim_x = self.trim_botx
                    #     trim_width = self.trim_botx - self.trim_topx

                    # if(self.trim_topy > self.trim_boty):
                    #     trim_y = self.trim_topy
                    #     trim_height = self.trim_topy - self.trim_boty
                    # else:
                    #     trim_y = self.trim_boty
                    #     trim_height = self.trim_boty - self.trim_topy

                    # 最後のトリミング
                    frame = first_rot[trim_x:trim_x + trim_height,trim_y:trim_y+trim_width]

                
                cv2.imshow("frame", frame)
                
                if(self.write_bool.get() == True):
                    # 処理画像の表示と保存
                    cv2.imwrite(new_dir_path + "/frame_" + str(i) + ".png", frame)
                
                if(self.video_bool.get() == True):
                    # 動画へフレーム追加
                    video.write(frame) 

                cv2.waitKey(15)
                i += 1

            if(self.write_bool.get() == True):
                print("Complete Saving Frame Image")

            if(self.video_bool.get() == True):            
                # 動画出力
                video.release()
                print("Complete Saving Video")

            
            self.label_make_frame.configure(text = "Complete")
            self.label_make_frame.configure(foreground = 'Blue')
    
    # うまくいかない↓  
    def TrimImage(self):
        
        def get_angle(x1, y1, x2, y2, x3, y3):
            angle = (math.atan2(y1 - y2, x1 - x2) - math.atan2(y3 - y2, x3 - x2)) / math.pi * 180

            return angle

        if(self.first_l == False):     
            self.label_make_frame.configure(text = "Please Select File")
            self.label_make_frame.configure(foreground = 'red')

        elif(self.second_l == False):
            self.label_make_frame.configure(text = "Please Select Filter")
            self.label_make_frame.configure(foreground = 'red')

        elif(self.third_l == False):
            self.labellabel_make_frame_check_cut.configure(text = "Please Set Cut Range")
            self.label_make_frame.configure(foreground = 'red')

        elif(self.forth_l == False):
            self.label_make_frame.configure(text = "Please Set Pivot Position")
            self.label_make_frame.configure(foreground = 'red')

        else:
            # 【変更可能な変数】
            # --------------------- 
            if(self.boty > self.topy):
                # 白点トリミングサイズ
                white_trim_width = self.boty - self.topy       #left:60 ,right:60
                # 白点トリミング位置
                white_trim_x = self.topy         #left:100 ,right:300
            else:
                white_trim_width = self.topy - self.boty       #left:60 ,right:60
                white_trim_x = self.boty         #left:100 ,right:300
            
            if(self.botx > self.topx):
                white_trim_height = self.botx - self.topx     #left:120,right:120
                white_trim_y = self.topx            #left:0 ,right:0
            else:
                white_trim_height = self.topx - self.botx   #left:120,right:120
                white_trim_y = self.botx            #left:0 ,right:0

            c_x = self.pivot_x
            c_y = self.pivot_y
            # ---------------------

            radSelected = self.radValues.get()
            resize_value = self.resize.get()

            cap = cv2.VideoCapture(self.filename)

            # Image Width
            W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            # Image Height
            H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            # All Frame
            count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            

            # 座標
            f_x = 0
            f_y = 0
            s_x = 0
            s_y = 0

            i=0
            while (cap.isOpened()):
                
                # 大きすぎる画像を処理するのに必要
                # cv2.namedWindow("output", cv2.WINDOW_NORMAL)  
                frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES)
                _, frame = cap.read()
                # frame = cv2.imread('a.PNG')

                if(frame_num == 0):
                    # リサイズ
                    if(W > 1000):
                        frame = cv2.resize(frame, (int(W/resize_value), int(H/resize_value)))                    # Resize 
                    
                    #　トリミング範囲補正
                    first_frame_trim = frame[white_trim_x:white_trim_x + white_trim_width,white_trim_y:white_trim_y + white_trim_height]

                    cv2.imshow("frame",first_frame_trim)
                    # グレースケール化          
                    first_frame_trim_gray = cv2.cvtColor(first_frame_trim, cv2.COLOR_BGR2GRAY)
                    
                    #平滑化（ぼかし）Smoothing
                    first_frame_trim_gray_Smoothing = cv2.GaussianBlur(first_frame_trim_gray,(7,7),0)

                    # 2値化処理
                    thresh = 180
                    maxval = 255
                    _,frame_BW = cv2.threshold(first_frame_trim_gray_Smoothing,thresh,maxval,cv2.THRESH_BINARY)

                    #輪郭の表示
                    _, first_frame_trim_gray_Smoothing_bw_contours, _ = cv2.findContours(frame_BW, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    first_frame_trim_gray_Smoothing_bw_contours = sorted(first_frame_trim_gray_Smoothing_bw_contours, key=lambda x: cv2.contourArea(x), reverse=False) #輪郭が一番小さい順に並べる
                    for cnt in first_frame_trim_gray_Smoothing_bw_contours:
                            (x, y, w, h) = cv2.boundingRect(cnt)
                            cv2.drawContours(first_frame_trim, [cnt], -1, (0,0,255),1) #輪郭の表示
                            # cv2.circle(first_frame_trim, (int(x+w/2), int(y+h/2)), 2, (255, 0, 0), 5) #円で表示
                            #代入→元の画像の座標に変換
                            s_x = int(x+w/2)+white_trim_y
                            s_y = int(y+h/2)+white_trim_x
                                    
                            #　回転中心の表示
                            # cv2.circle(first_frame_trim, (x, y), 5, (0, 255, 0), 2)
                            
                            print("Current Frame：" + str(frame_num) + ", Rotation Position：(" + str(s_x) + "," + str(s_y) + ")" + ", Pivot Position：(" + str(self.pivot_x) + "," + str(self.pivot_y) + ")")
                    
                    #　支点の表示
                    cv2.circle(frame, (c_x, c_y), 2, (0, 0, 255), 5)
                    #　回転中心の表示
                    cv2.circle(frame, (s_x, s_y), 2, (0, 255, 255), 5)
                    #　線を引く
                    cv2.line(frame, (c_x, c_y), (s_x, s_y), (255, 255, 255), thickness=2, lineType=cv2.LINE_4)
                    #　画像の表示    
                    # cv2.imshow("frame_trim",first_frame_trim)
                    # cv2.imshow("frame",frame)

                    if(frame_num == 0):
                        f_x = s_x
                        f_y = s_y

                # 回転処理   
                    # ---------------------------------                
                    # 回転ゲイン
                    rot_gain = 0              #left:75 ,right:105
                    # 最終トリミングサイズ
                    trim_width = 600*3            #left:150 ,right:150
                    trim_height = 400*2           #left:300 ,right:300
                    # 最終トリミング位置
                    trim_x = 0                  #left:0 ,right:0
                    trim_y = 0                #left:250 ,right:350
                    # ---------------------------------

                    if(self.angle.get() != ""):
                        rot_gain = int(self.angle.get())

                    h, w = frame.shape[:2]

                    if(h>w):
                        w=h
                    else:
                        h=w

                    # 回転角の指定(二フレーム以降)
                    if(frame_num > 0):
                        angle = get_angle(s_x,s_y,c_x,c_y,f_x,f_y) + rot_gain
                        print('角度：{:.1f}°'.format(angle))
                        angle_rad = angle/180.0*numpy.pi
                    else:
                        # 回転角の指定
                        angle = 0 + rot_gain
                        angle_rad = angle/180.0*numpy.pi

                    # 回転後の画像サイズを計算
                    w_rot = w+100
                    h_rot = h+100
                    size_rot = (w_rot, h_rot)

                    # 元画像の中心を軸に回転する
                    center = (c_x, c_y)
                    scale = 1.0
                    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

                    # 平行移動を加える (rotation + translation)
                    affine_matrix = rotation_matrix.copy()
                    affine_matrix[0][2] = affine_matrix[0][2] -c_x + w_rot/2
                    affine_matrix[1][2] = affine_matrix[1][2] -c_y + h_rot/2

                    first_rot = cv2.warpAffine(frame, affine_matrix, size_rot, flags=cv2.INTER_CUBIC)
                
                    # トリミングクラス呼び出し        
                    # CRTT = tk_Rtrim_class.Create_Rotation_Trim_Tool(self.cv2pil(first_rot), self)
                    
    def radioButton(self):
        self.radValues = IntVar()

        self.label_filter = ttk.Label(self, text = "select Filter")
        self.label_filter.place(x = self.rp_x, y = self.lp2)

        red1 = ttk.Radiobutton(self, text = "no filter", value =1, variable = self.radValues, command=self.Second_Level_On)
        red1.place(x = self.rp_x, y = self.p2)

        red2 = ttk.Radiobutton(self, text = "gray scale", value =2, variable = self.radValues, command=self.Second_Level_On)
        red2.place(x = self.rp_x + 100, y = self.p2)

        red3 = ttk.Radiobutton(self, text = "binary", value =3, variable = self.radValues, command=self.Second_Level_On)
        red3.place(x = self.rp_x + 200, y = self.p2)

    def Second_Level_On(self):
        self.second_l = True
    
    def CutImage(self):
        if(self.first_l == False):     
            self.label_cut.configure(text = "Please Select File")
            self.label_cut.configure(foreground = 'red')
        else:
            resize_value = self.resize.get()
            
            cap = cv2.VideoCapture(self.filename)
            _, frame = cap.read()

            # Image Width
            W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            # Image Height
            H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

            # リサイズ
            if(W > 1000):
                frame = cv2.resize(frame, (int(W/resize_value), int(H/resize_value)))  

            CICT = tk_cut_class.Create_Image_Cut_Tool(self.cv2pil(frame), self)

    def SetPivot(self):
        if(self.first_l == False):     
            self.label_pivot.configure(text = "Please Select File")
            self.label_pivot.configure(foreground = 'red')
        else:
            resize_value = self.resize.get()
            
            cap = cv2.VideoCapture(self.filename)
            _, frame = cap.read()

            # Image Width
            W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            # Image Height
            H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

            # リサイズ
            if(W > 1000):
                frame = cv2.resize(frame, (int(W/resize_value), int(H/resize_value)))  

            SPP = tk_mouse_tracking_class.Set_Pivot_Position(self.cv2pil(frame), self)

    def button_open_file(self):
        self.button = ttk.Button(self, text = "Browse A File" ,command = self.fileDialog)
        self.button.place(x = self.rp_x, y = self.p1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "./", title = "Select A File", filetype = (("mp4", "*.mp4"),("All Files", "*.*")))
        
        if(self.filename != ""):
            self.first_l = True
            self.label2.configure(text = self.filename)
            self.label2.configure(foreground = 'black')
        
    def cv2pil(self,image):
        ''' OpenCV型 -> PIL型 '''
        new_image = image.copy()
        if new_image.ndim == 2:  # モノクロ
            pass
        elif new_image.shape[2] == 3:  # カラー
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
        elif new_image.shape[2] == 4:  # 透過
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
        new_image = Image.fromarray(new_image)
        return new_image

    def ShowNum(self):
        print(self.pivot_x)

if __name__ == "__main__":
    root = Root()
    root.mainloop()