import cv2
import numpy as numpy
import dlib
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


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Find Angle Tool")
        self.iconbitmap('./icon.ico')
        self.minsize(640,400)
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
        self.check_Video.place(x = self.rp_x + 450, y = self.lp7+3)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length=620, mode='determinate')
        self.progress_bar.place(x = self.rp_x, y = self.lp8)

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
                     
    def DrawLine(self):
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
                width = int(W/resize_value)
                height = int(H/resize_value)
                fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
                video = cv2.VideoWriter(new_dir_path + '/movie.mp4', fourcc, frame_rate, (width, height))

            # 座標
            f_x = 0
            f_y = 0

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
                        f_x = int(x+w/2)+white_trim_y
                        f_y = int(y+h/2)+white_trim_x
                                
                        #　回転中心の表示
                        # cv2.circle(first_frame_trim, (x, y), 5, (0, 255, 0), 2)
                        
                        print("Current Frame：" + str(frame_num) + ", Rotation Position：(" + str(f_x) + "," + str(f_y) + ")" + ", Pivot Position：(" + str(self.pivot_x) + "," + str(self.pivot_y) + ")")
                
                #　支点の表示
                cv2.circle(frame, (c_x, c_y), 2, (0, 0, 255), 5)
                #　回転中心の表示
                cv2.circle(frame, (f_x, f_y), 2, (0, 255, 255), 5)
                #　線を引く
                cv2.line(frame, (c_x, c_y), (f_x, f_y), (255, 255, 255), thickness=2, lineType=cv2.LINE_4)
                #　画像の表示    
                # cv2.imshow("frame_trim",first_frame_trim)
                # cv2.imshow("frame",frame)

                
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