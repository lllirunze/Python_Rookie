'''
FilePath: game.py
Author: LiRunze
Date: 2022-08-23 20:31:46
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-08-30 05:34:08
Description: 
'''

from email.errors import MultipartInvariantViolationDefect
from operator import truediv
import os
from pickletools import markobject
import sys
import numpy
import random
import pygame

"""
Form():             窗口的设置
Action():           用户行为: 按键/鼠标
InitGame():         游戏初始化
CreatNum():         随机在一个位置生成一个数
GetEmpty():         获取空白方格
MoveUp():           向上移动
MoveDown():         向下移动
MoveLeft():         向左移动
MoveRight():        向右移动
JudgeGameOver():    判断游戏是否结束
JudgeGameSuccess(): 判断游戏是否成功
Paint(): 绘制表格
"""

class Game2048(object):

    # 初始化函数
    def __init__(self, screen_width, screen_height, block_gap, block_size, block_arc):
        """
        param screen_width:     Width of the form
        param screen_height:    Height of the form
        param block_gap:        Gap between two blocks
        param block_size:       Size of a block
        param size:             Dimension of matrix
        param martix:           Zero matrix
        param is_over:          Sign of the end of the game
        param is_success:       Sign of the success of the game
        param form:             The form
        param score:            score
        param title_font:       Title type and size of form
        param score_font:       Scores type and size
        param tips_font:        Tips type and type
        param font:             The numberes
        param isadd:            Add number or not
        """

        # 窗口
        self.screen_width   = screen_width
        self.screen_height  = screen_height
        self.block_gap      = block_gap
        self.block_size     = block_size
        self.block_arc      = block_arc
        self.size           = 4
        self.martix         = []
        self.form           = ''

        # 其他
        self.is_over        = False # 游戏是否结束
        self.is_success     = False # 游戏是否成功
        self.score          = 0     # 分数
        self.isadd          = True  # 是否添加数字
        self.block_color    = {     # 方块颜色
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46)
        }
        self.nums_color = {
            # 0: (0, 0, 0),
            0: (205, 193, 180),
            2: (0, 0, 0),
            4: (0, 0, 0),
            8: (255, 255, 255),
            16: (255, 255, 255),
            32: (255, 255, 255),
            64: (255, 255, 255),
            128: (255, 255, 255),
            256: (255, 255, 255),
            512: (255, 255, 255),
            1024: (255, 255, 255),
            2048: (255, 255, 255)
        }

        # 字体
        self.title_font     = ''    # 窗口标题字体类型及大小: 2048
        self.score_font     = ''    # 分数字体类型及大小
        self.tips_font      = ''    # 说明字体类型及大小
        self.font           = ''    # 数字字体


    # 窗口的设置
    def Form(self):
        """
        init():                     初始化所有导入的 pygame 模块
        display.set_caption(title): 设置窗口的标题
        display.set_mode():         初始化一个准备显示的窗口或屏幕
        display.update():           使绘制的显示到窗口上
        """
        pygame.init()
        pygame.display.set_caption("Game2048")
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.form = pygame.display.set_mode([self.screen_width, self.screen_height], 0, 0)
        self.InitGame()             # 矩阵的初始化

        while True:
            self.Action()           # 用户行为：按键/鼠标
            self.Paint()            # 表格绘制
            pygame.display.update()


    # 用户行为：按键/鼠标
    def Action(self):
        '''
        pygame.event.get():         获取所有消息并将其从队列中删除
        pygame.QUIT():              窗口右上角的退出键
        sys.exit():                 通过抛出异常的形式来终止进程
        pygame.KEYDOWN():           按下按键
        pygame.KEYUP():             释放按键
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.InitGame()
                if event.key == pygame.K_UP and self.is_over == False:
                    self.MoveUp()
                if event.key == pygame.K_DOWN and self.is_over == False:
                    self.MoveDown()
                if event.key == pygame.K_LEFT and self.is_over == False:
                    self.MoveLeft()
                if event.key == pygame.K_RIGHT and self.is_over == False:
                    self.MoveRight()


    # 游戏初始化
    def InitGame(self):
        
        self.score      = 0
        self.is_over    = False
        self.is_success = False
        self.martix     = numpy.zeros([self.size, self.size])

        # 随机生成两个数
        for i in range(2):
            self.isadd = True
            self.CreateNum()


    # 随机在一个位置生成一个数
    def CreateNum(self):

        list = self.GetEmpty()
        if list and self.isadd:
            '''
            随机出现数字
            2, 4出现概率3:1
            random.randint(m, n): 随机生成[m, n]
            '''
            value = 4 if random.randint(0,3)%3==0 else 2
            # 获取随机位置下标
            x, y = random.sample(list, 1)[0]
            # 在随机位置上生成随机数字
            self.martix[x][y] = value
            self.isadd = False


    # 获取空白方格
    def GetEmpty(self):
        
        list = []
        for i in range(4):
            for j in range(4):
                if self.martix[i][j] == 0:
                    list.append([i, j])
        return list


    # 向上移动
    def MoveUp(self):
        '''
        向上移动，只需要考虑第二行到第四行
        共分为两种情况:
        1. 当前数字上边无空格，即上边值为0
            a. 当前数字与上边数字相等，合并
            b. 当前数字与上边数字不相等，continue
        2. 当前数字上边有空格，即上边值为0，上移
        '''
        for j in range(4):
            index = 0
            for i in range(1, 4):
                if self.martix[i][j] > 0:
                    if self.martix[i][j] == self.martix[index][j]:
                        # 当前数字 == 上边数字
                        self.score             += self.martix[i][j] + self.martix[index][j]
                        self.martix[index][j]   = self.martix[i][j] + self.martix[index][j]
                        self.martix[i][j]       = 0
                        index                  += 1
                        self.isadd              = True
                    # 当前数字与上边数字不相等，continue可以省略不写
                    elif self.martix[index][j] == 0:
                        # 当前数字上边有0
                        self.martix[index][j]   = self.martix[i][j]
                        self.martix[i][j]       = 0
                        self.isadd              = True
                    else:
                        index += 1
                        if self.martix[index][j] == 0:
                            self.martix[index][j]   = self.martix[i][j]
                            self.martix[i][j]       = 0
                            self.isadd              = True


    # 向下移动
    def MoveDown(self):
        '''
        向下移动，只需要考虑第一行到第三行
        共分为两种情况:
        1. 当前数字下边无空格，即下边值为0
            a. 当前数字与下边数字相等，合并
            b. 当前数字与下边数字不相等，continue
        2. 当前数字下边有空格，即下边值为0，下移
        '''
        for j in range(4):
            index = 3
            for i in range(2, -1, -1):
                if self.martix[i][j] > 0:
                    if self.martix[i][j] == self.martix[index][j]:
                        self.score             += self.martix[i][j] + self.martix[index][j]
                        self.martix[index][j]   = self.martix[i][j] + self.martix[index][j]
                        self.martix[i][j]       = 0
                        index                  -= 1
                        self.isadd              = True
                    elif self.martix[index][j] == 0:
                        self.martix[index][j]   = self.martix[i][j]
                        self.martix[i][j]       = 0
                        self.isadd              = True
                    else:
                        index -= 1
                        if self.martix[index][j] == 0:
                            self.martix[index][j]   = self.martix[i][j]
                            self.martix[i][j]       = 0
                            self.isadd              = True
                        

    # 向左移动
    def MoveLeft(self):
        """
        向左移动，只需考虑第二列到第四列
        共分为两种情况:
        1、当前数字左边无空格，即左边值不为0
            a. 当前数字与左边数字相等，合并
            b. 当前数字与左边数字不相等，continue
        2、当前数字左边有空格，即左边值为0，左移
        """
        for i in range(4):
            index = 0
            for j in range(1, 4):
                if self.martix[i][j] > 0:
                    if self.martix[i][j] == self.martix[i][index]:
                        # 当前数字 == 左边数字
                        self.score             += self.martix[i][j] + self.martix[i][index]
                        self.martix[i][index]   = self.martix[i][j] + self.martix[i][index]
                        self.martix[i][j]       = 0
                        index                  += 1
                        self.isadd              = True
                    # 当前数字与左边数字不相等，continue 可以省略不写
                    elif self.martix[i][index] == 0:
                        # 当前数字左边有0
                        self.martix[i][index]   = self.martix[i][j]
                        self.martix[i][j]       = 0
                        self.isadd              = True
                    else:
                        index += 1
                        if self.martix[i][index] == 0:
                            self.martix[i][index]   = self.martix[i][j]
                            self.martix[i][j]       = 0
                            self.isadd              = True


    # 向右移动
    def MoveRight(self):
        """
        向右移动，只需考虑第一列到第三列
        共分为两种情况:
        1、当前数字右边无空格，即右边值不为 0
            a. 当前数字与右边数字相等，合并
            b. 当前数字与右边数字不相等，continue
        2、当前数字右边有空格，即右边值为 0， 右移
        """
        for i in range(4):
            index = 3
            for j in range(2, -1, -1):
                if self.martix[i][j] > 0:
                    if self.martix[i][j] == self.martix[i][index]:
                        # 当前数字 == 右边数字
                        self.score             += self.martix[i][j] + self.martix[i][index]
                        self.martix[i][index]   = self.martix[i][j] + self.martix[i][index]
                        self.martix[i][j]       = 0
                        index                  -= 1
                        self.isadd              = True
                    # 当前数字与左边数字不相等，continue 可以省略不写
                    elif self.martix[i][index] == 0:
                        # 当前数字右边有0
                        self.martix[i][index]   = self.martix[i][j]
                        self.martix[i][j]       = 0
                        self.isadd              = True
                    else:
                        index -= 1
                        if self.martix[i][index] == 0:
                            self.martix[i][index]   = self.martix[i][j]
                            self.martix[i][j]       = 0
                            self.isadd              = True
                            

    # 判断游戏是否结束
    def JudgeGameOver(self):
        zerolist = self.GetEmpty()
        if zerolist:
            return False
        
        for i in range(3):
            for j in range(3):
                if self.martix[i][j] == self.martix[i][j+1]:
                    return False
                if self.martix[i][j] == self.martix[i+1][j]:
                    return False
        if self.martix[3][3] == self.martix[3][2]:
            return False
        if self.martix[3][3] == self.martix[2][3]:
            return False
        
        return True
    

    # 判断游戏是否胜利
    def JudgeGameSuccess(self):
        if self.martix.max() == 2048:
            return True
        return False

    # 绘制表格
    def Paint(self):
        '''
        fill(color):                填充某一种颜色
        pygame.font.get_fonts():    获取字体样式
        pygame.font.Font.render():  在一个新的Surface对象上绘制文本
        '''
        self.form.fill((220, 220, 220))
        
        # 添加标题
        pygame.font.init()
        self.title_font = pygame.font.SysFont('幼圆', 50, True)
        title_text      = self.title_font.render('2048', True, (0,0,0))
        self.form.blit(title_text, (50,10))
        
        # 添加分数
        pygame.draw.rect(self.form, (128,128,128), (250,0,120,60))
        self.score_font = pygame.font.SysFont('幼圆', 28, True)
        score_text      = self.score_font.render('得分', True, (0,0,0))
        self.form.blit(score_text, (275,0))
        digital_score   = self.score_font.render(str(int(self.score)), True, (255,250,250))
        self.form.blit(digital_score, (280,30))
        
        # 添加游戏说明
        self.tips_font  = pygame.font.SysFont('sinsunnsimsun', 20)
        tips_text       = self.tips_font.render('操作: 上下左右, 按Esc重新开始', True, (0,0,0))
        self.form.blit(tips_text, (25,70))
        
        # 绘制方格
        for i in range(4):
            for j in range(4):
                x = j*self.block_size + (j+1)*self.block_gap
                y = i*self.block_size + (i+1)*self.block_gap
                value = int(self.martix[i][j])
                pygame.draw.rect(self.form, self.block_color[value], (x+5, y+100, self.block_size, self.block_size), border_radius=self.block_arc)
                
                # 数字字体即大小
                if value < 10:
                    self.font   = pygame.font.SysFont('simsunnsimsun', 46, True)  # 数字2、4、8
                    value_text  = self.font.render(str(value), True, self.nums_color[value])
                    self.form.blit(value_text, (x + 35, y + 120))
                elif value < 100:
                    self.font   = pygame.font.SysFont('simsunnsimsun', 40, True)  # 数字16, 32, 64
                    value_text  = self.font.render(str(value), True, self.nums_color[value])
                    self.form.blit(value_text, (x + 25, y + 120))
                elif value < 1000:
                    self.font   = pygame.font.SysFont('simsunnsimsun', 34, True)  # 数字128, 256, 512
                    value_text  = self.font.render(str(value), True, self.nums_color[value])
                    self.form.blit(value_text, (x + 15, y + 120))
                else:
                    self.font   = pygame.font.SysFont('simsunnsimsun', 28, True)  # 数字1024, 2048
                    value_text  = self.font.render(str(value), True, self.nums_color[value])
                    self.form.blit(value_text, (x + 5, y + 120))

        # 新增数字
        self.CreateNum()
        
        # 如果游戏结束
        self.is_over = self.JudgeGameOver()
        if self.is_over:
            over_font       = pygame.font.SysFont('simsunnsimsun', 60, True)
            str_text        = over_font.render('Game Over!', True, (255,255,255))
            self.form.blit(str_text, (30,220))
            
        # 如果游戏胜利
        self.is_success = self.JudgeGameSuccess()
        if self.is_success:
            success_font    = pygame.font.SysFont('simsunnsimsun', 60, True)
            str_text        = success_font.render('Success!', True, (178,34,34))
            self.form.blit(str_text, (10,220))
            
