# -*- coding:UTF-8 -*-

import cv2
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from video_fram import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox,\
                            QFontDialog, QColorDialog, QSplashScreen


class mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.setFixedSize(610, 289)
        self.pushButton.clicked.connect(self.browse_video)
        self.pushButton_2.clicked.connect(self.browse_folder)
        self.pushButton_3.clicked.connect(self.process_video)
        self.file_path = ""
        self.folder_path= ""

    def browse_video(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, '选择输入视频文件', '', '视频文件 (*.mp4 *.avi *.mov)')
        if self.file_path:
            self.lineEdit.setText(self.file_path)

    def browse_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, '选择输出文件夹', '')
        if self.folder_path:
            self.lineEdit_2.setText(self.folder_path)

    def process_video(self):
        if self.file_path == "":
            QMessageBox.warning(self, '警告', '请重新选择视频文件！')
            return

        if self.folder_path == "":
            # QMessageBox.warning(self, '警告', '请重新选择输出文件夹！')
            self.folder_name = os.path.splitext(os.path.basename(self.file_path))[0]
            self.folder_path = os.path.join(os.path.dirname(self.file_path), self.folder_name)
            os.makedirs(self.folder_path)
            print(self.folder_path)


        cap = cv2.VideoCapture(self.file_path)
        # VideoCapture()中的参数若为0，则表示打开笔记本的内置摄像头
        # 若为视频文件路径，则表示打开视频

        num_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 获取视频总帧数
        print(num_frame)

        expand_name = '.jpg'
        if not cap.isOpened():
            print("Please check the path.")

        cnt = 0
        while 1:
            ret, frame = cap.read()
            # cap.read()表示按帧读取视频。ret和frame是获取cap.read()方法的两个返回值
            # 其中，ret是布尔值。如果读取正确，则返回TRUE；如果文件读取到视频最后一帧的下一帧，则返回False
            # frame就是每一帧的图像

            if not ret:
                break

            cnt += 1  # 从1开始计帧数
            cv2.imwrite(os.path.join(self.folder_path, str(cnt) + expand_name), frame)
        print("Finish.")
        QMessageBox.information(self, '完成', f'视频转图片已完成！共有{num_frame}帧！', QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mywindow()
    main.show()
    app.installEventFilter(main)
    sys.exit(app.exec_())