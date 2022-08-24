'''
FilePath: game.py
Author: LiRunze
Date: 2022-08-23 20:31:46
LastEditors: LiRunze
LastEditTime: 2022-08-23 20:38:57
Description: 
'''

import os
import sys
import numpy
import random
import pygame

"""
Form(): 窗口的设置
Action(): 用户行为: 按键/鼠标
InitGame(): 游戏初始化
CreatNum(): 随机在一个位置生成一个数
GetEmpty(): 获取空白方格
MoveUp(): 向上移动
MoveDown(): 向下移动
MoveLeft(): 向左移动
MoveRight(): 向右移动
JudgeGameOver(): 判断游戏是否结束
JudgeGameSuccess(): 判断游戏是否成功
Paint(): 绘制表格
"""

class Game2048(object):

