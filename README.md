# アーム角度を自動検出して動画に追加する。(Tkinterで使いやすい画像処理ツールを作る。）
https://github.com/sassa4771/Find_Angle_Tkinter/tree/main/main<br>
ここのファイルの中身説明↑

## このGitHubでできること
・角度・位置座標を自動検出したいアーム動画を処理して動画に骨組みを表示する。
<br><br>
<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex14.gif" alt="自動トラッキング完成動画イメージ" title="eye03"><br><br>
・本ツールを通して、Tkinterでできること（ファイル読み出し、動画トリミング、マウス追従、スライダー作成などなど）
<br><br>
<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex15.gif" alt="Tkinterできることイメージ" title="eye03"><br><br>

このFind Angleツールを作るまでに学んだ機能などをレッスンとして<br>
lesson1~27までまとめてあるので参考にしてみてください。<br>
https://github.com/sassa4771/Find_Angle_Tkinter/tree/main/tk_lesson<br>
<参考サイト：https://www.youtube.com/watch?v=sAu7uxW85_Y&list=PL1FgJUcJJ03sm4WuVCPMbT0RIf2uMmoAj&index=17>

## 目次
①Tkinterとは？<br>
②必要なライブラリ・動作環境<br>
③ツールの使い方とTkinterの機能紹介<br>
④Tkinter学び方(参考スクリプト付き)<br>
⑤本ツールの作り方（簡易版）<br>

## ①Tkinterとは？
【Tkinterとは】
Tkinterとは、「ティーキンター」や「ティーケーインター」と呼ばれ、Window,Mac,Linuxといった<br>
主要なOSにも対応しているクロスプラットフォームなGUIライブラリです。<br>
(参考：https://www.acrovision.jp/service/data/?p=616)<br><br>

要するに<h3>GUIが作れる！</h3><br>

## ②必要なライブラリ・動作環境
【動作環境：(Let's Note)】<br>
OS:windows10 Pro<br>
CPU:Corei7<br>
メモリ:12GB<br>

【必要なライブラリ】<br>
・dlib
・opencv
・numpy
・PIL(Pillow)

<br><br>
【Anaconda環境データ】<br>
今回使用しているAnacondaの環境データ(yamlファイル）もGitにあるので利用してみてください。<br>
https://github.com/sassa4771/Find_Angle_Tkinter/tree/main/Anaconda%20Environment<br><br>

## ③ツールの使い方とTkinterの機能紹介
【ファイルを開く】<br>
まずは、ファイルを開きましょう。<br><br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[ファイル参照] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson23(Browsing%20A%20File).py<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex1.gif" alt="ファイルを開く" title="Tkinterでファイルを開く"><br><br>
<br>

【選択した動画の閲覧】<br>
no filterを選択して「Show Selected Video」を押すと表示することができる。<br><br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[ラジオボタン] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson8(Radio%20Button).py<br>
[ボタンと機能呼び出し] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson4(Button%20And%20Button%20Commands).py<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex2.gif" alt="選択した動画の閲覧" title="Tkinterでラジオボタン・フィルター処理呼び出し"><br><br>
<br>


【動画の縮小をする】<br>
ただこのままだと、元の動画が大きすぎるのでリサイズをします。<br>
スライダーを利用して、縮小割合を決定します。<br><br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[スライダー] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson27(Slider).py<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex3.gif" alt="動画の縮小をする" title="Tkinterで画像の縮小機能呼び出し"><br><br>
<br>


【フィルター処理した動画の閲覧】<br>
ラジオボタンで・フィルターなし・グレースケール・二値化の処理を選択して表示することができます。<br><br>
※二値化処理したものを輪郭抽出で自動追従しているため、背景が黒で、目標点が白でないといけない。<br>
フィルターに関して詳しくは、eyetrackのところで説明しています。<br>
Webカメラでeye tracking（アイトラッキング・視線計測）をする【Windows10】:https://github.com/sassa4771/eyetrack<br><br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[ボタンと機能呼び出し] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson4(Button%20And%20Button%20Commands).py<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex4.gif" alt="フィルター処理した動画の閲覧" title="Tkinterでラジオボタン・メソッド呼び出し"><br><br>
<br>

<br>
【動画の範囲トリミングする】<br>
自動トラッキングしたい点（白色のみトラッキング可能。背景は黒色がベスト）が移動する範囲をトリミングしましょう。<br>
※この処理は、目標点の追従する際に範囲を絞ってノイズが入るのを防ぐために行います。<br><br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[画像トリミング] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson25(Image_Triming).py<br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex5.gif" alt="画像をトリミングする" title="Tkinterで動画の範囲トリミング"><br><br>
<br>

【目標点を追従できているかを確認する】<br>
「Check Cut Range」を押して、トリミングした範囲で動画を表示します。<br>
「no filter」を選択した場合、目標点が赤枠で囲われていることを確認できる。<br>
この赤枠がほかの箇所にも表示されている場合は、トリミング範囲の修正が必要。または、動画の撮り直しや撮影環境の見直しが必要です。<br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[ボタンと機能呼び出し] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson4(Button%20And%20Button%20Commands).py<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex6.gif" alt="トリミングした動画を表示する" title="Tkinterでトリミング動画の表示"><br><br>
<br>

【児童追従が失敗する場合の例】<br>
仮にトリミング範囲を大きくしてみましょう。<br>
そうすると、目標点と思われる場所がプログラム上で判断できなくなってしまうため、手にも赤枠が表示されているのがわかると思います。<br>
これを避けるために、目標点の自動追従範囲を絞る必要があります。<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex7.gif" alt="目標点を追従できているかを確認する" title="Tkinterで目標点の追従を確認"><br><br>
<br>


【回転中心を決定する】<br>
次に、回転中心（Pivot）を決定します。<br>
「Put Pivot On Image」を押して、マウスをドラックすることで赤点を操作できます。<br>
その赤点を回転中心におきましょう。<br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[ボタンと機能呼び出し] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson4(Button%20And%20Button%20Commands).py<br>
[マウストラッキング] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson26(mouse_tracking).py<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex8.gif" alt="回転中心を決定する" title="Tkinterで画像をドラック。ドロップしよう"><br><br>
<br>


【角度表示を行う】<br>
ここまで出来たら、最後の処理を行いましょう。<br>
「Make Frame Image」を押すことで、処理された動画を確認することができます。<br><br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[ボタンと機能呼び出し] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson4(Button%20And%20Button%20Commands).py<br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex9.gif" alt="角度表示を行う" title="Tkinterで角度表示機能の呼び出し"><br><br>
<br>


【作成した動画を保存】<br>
「Video Save」にチェックを入れて、「Check Cut Range」を押すと、動画を保存できます。<br>
pythonのファイルがある場所に、今の日付時間のフォルダーを作成して、その中に保存されます。<br><br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[ボタンと機能呼び出し] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson4(Button%20And%20Button%20Commands).py<br>
[チェックボタン] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson7(Check%20Button).py<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex10.gif" alt="作成した動画を保存" title="Tkinterでトリミング動画の保存"><br><br>
<br>


【作成した動画をフレームごとに分けて画像で保存】<br>
「Frame Image Save」にチェックを入れて、「Check Cut Range」を押すと、動画をフレームごとに分けて画像で保存できます。<br>
pythonのファイルがある場所に、今の日付時間のフォルダーを作成して、その中に保存されます。<br><br>

このTkinter機能は、こちらのスクリプトを参考にしてください。<br>
[ラベル] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson2(Labels).py<br>
[ボタンと機能呼び出し] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson4(Button%20And%20Button%20Commands).py<br>
[チェックボタン] https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/tk_lesson/tk_lesson7(Check%20Button).py<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex11.gif" alt="作成した動画をフレームごとに分けて画像で保存" title="Tkinterでトリミング動画をフレームに分けて保存"><br><br>
<br>

【角度情報を数値で取得】<br>
動画で表示するだけでなく、数値で位置座標を取得したい場合はコマンドプロンプトから取得することができます。<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex12.gif" alt="角度情報を数値で取得" title="角度情報を数値で取得する"><br><br>
<br>

【最後に全体の確認】<br>
ここで最後に、全体の一連の流れを確認しましょう。<br><br>

<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex12.gif" alt="最後に全体の確認" title="最後に全体の確認"><br><br>
<br>

## ④Tkinter学び方(参考スクリプト付き)
本ツールで利用した機能などはlesson1~27までを用意しているので、チェックしてください。<br>
https://github.com/sassa4771/Find_Angle_Tkinter/tree/main/tk_lesson<br><br>

機能一つ一つを確認できるようにしてあるので、オリジナルを作るのに役立つと思います。<br>
<img src="https://github.com/sassa4771/Find_Angle_Tkinter/blob/main/Gif/ex16.gif" alt="Tkinter学び方(参考スクリプト付き)" title="Tkinter学び方(参考スクリプト付き)"><br><br>


## ⑤本ツールの作り方（簡易版）
本ツールのフィルターや画像処理に関しては、eyetrackのところで同じフィルターについて解説をしているので参考にしてください。<br>
https://github.com/sassa4771/eyetrack<br><br>

また、Tkinterの機能に関しても前章の「④Tkinter学び方(参考スクリプト付き)」ですべてできているので参考にしてください。
