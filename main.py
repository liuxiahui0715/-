# -*- coding: utf-8 -*-
# import torch
# 根据视频帧数截图

import cv2
import argparse
# argparse 是 Python 的一个标准库，用于命令行参数的解析，这意味着我们无需在代码中手动为变量赋值，而是可以直接在命令行中向程序传递相应的参数，再由变量去读取这些参数。
import os

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Process pic')
    # 使用argparse的第一步是先创建一个ArgumentParser对象，该对象包含将命令行解析成Python数据类型所需的全部信息
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    # input为输入视频的路径 ，output为输出存放图片的路径
    args = parser.parse_args(['--input', r'G:\Project\python_pro\video_fram\04071520.mp4',
                              '--output', r'G:\Project\python_pro\video_fram\04071520'])
    return args

def process_video(i_video, o_video):
    cap = cv2.VideoCapture(i_video)
    # VideoCapture()中的参数若为0，则表示打开笔记本的内置摄像头
    # 若为视频文件路径，则表示打开视频

    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 获取视频总帧数
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
        cv2.imwrite(os.path.join(o_video, str(cnt) + expand_name), frame)


if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    print('Called with args:')
    print(args)
    process_video(args.input, args.output)
