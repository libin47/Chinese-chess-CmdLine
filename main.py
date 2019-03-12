#!/usr/bin/env python
# -*- coding: utf-8 -*-

#象棋类
import os
from colorama import init,Fore,Back,Style
init(autoreset=True)

class chess(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

class chessboard(object):
    def __init__(self):
        #初始化棋盘
        self.winner = None
        chessboard = [[None for i in range(9)] for j in range(10)]
        chessboard[0][0], chessboard[0][1], chessboard[0][2], chessboard[0][3], chessboard[0][4], chessboard[0][5], chessboard[0][6], chessboard[0][7], chessboard[0][8], chessboard[2][1], chessboard[2][7], chessboard[3][0], chessboard[3][2], chessboard[3][4], chessboard[3][6], chessboard[3][8] = chess('車', 'red'),  chess('马', 'red'),  chess('象', 'red'),  chess('士', 'red'),  chess('帅', 'red'), chess('士', 'red'), chess('象', 'red'), chess('马', 'red'), chess('車', 'red'), chess('炮', 'red'), chess('炮', 'red'), chess('兵', 'red'), chess('兵', 'red'), chess('兵', 'red'), chess('兵', 'red'), chess('兵', 'red')  
        chessboard[9][0], chessboard[9][1], chessboard[9][2], chessboard[9][3], chessboard[9][4], chessboard[9][5], chessboard[9][6], chessboard[9][7], chessboard[9][8], chessboard[7][1], chessboard[7][7], chessboard[6][0], chessboard[6][2], chessboard[6][4], chessboard[6][6], chessboard[6][8] = chess('車', 'green'),  chess('马', 'green'),  chess('象', 'green'),  chess('士', 'green'),  chess('帅', 'green'), chess('士', 'green'), chess('象', 'green'), chess('马', 'green'), chess('車', 'green'), chess('炮', 'green'), chess('炮', 'green'), chess('兵', 'green'), chess('兵', 'green'), chess('兵', 'green'), chess('兵', 'green'), chess('兵', 'green')  
        self.board = chessboard
        
    def restart(self):
        # 重置棋局
        self.__init__()
        
    def display(self, mode):
        # 显示棋局
        chessboards = [['  ' for i in range(10)] for j in range(12)]
        i = 1
        while i<11 :
            chessboards[i][0] = str(11-i).zfill(2)
            i += 1
        i = 1
        while i<10 :
            chessboards[11][i] = str(10-i).zfill(2)
            i += 1
        if mode == 'red':
            for i in range(10):
                for j in range(9):
                    if self.board[i][j]:
                        if self.board[i][j].color=='red':
                            chessboards[10-i][9-j] ='\033[1;31;40m'+self.board[i][j].name+'\033[0m'
                        else:
                            chessboards[10-i][9-j] ='\033[1;32;40m'+self.board[i][j].name+'\033[0m'
                    else:
                        chessboards[10-i][9-j] = '十'
        elif mode == 'green':
            for i in range(10):
                for j in range(9):
                    if self.board[i][j]:
                        if self.board[i][j].color=='red':
                            chessboards[i+1][j+1] ='\033[1;31;40m'+self.board[i][j].name+'\033[0m'
                        else:
                            chessboards[i+1][j+1] ='\033[1;32;40m'+self.board[i][j].name+'\033[0m'
                    else:
                        chessboards[i+1][j+1] = '十'
        else:
            for i in range(10):
                for j in range(9):
                    chessboards[i+1][j+1]='666'
        chessstr = ''
        for i in range(12):
            for j in range(10):
                chessstr = chessstr+chessboards[i][j]
            chessstr = chessstr + '\n'
        return chessstr
    
    def check_end(self):
        # 检查是否结束 暂置
        num_boss = 0
        for i in range(10):
            for j in range(9):
                if self.board[i][j].name == '帅':
                    num_boss += 1
        if num_boss == 2:
            return False
        else:
            return True
            
    def __border_check(self, area, pos, color=None): 
        # 检查是否出界         
        if area==2:
            if color == None:
                if ((pos[0]<=2 and pos[0]>=0) or (pos[0]<=9 and pos[0]>=7)) and (pos[1]<=5 and pos[1]>=3):
                    return True
                else:
                    return False
            elif color == 'red':
                if (pos[0]<=2 and pos[0]>=0) and (pos[1]<=5 and pos[1]>=3):
                    return True
                else:
                    return False
            elif color == 'green':
                if (pos[0]<=9 and pos[0]>=7) and (pos[1]<=5 and pos[1]>=3):
                    return True
                else:
                    return False
        elif area==1:
            if color == None:
                print('error when check pos')
                return False
            elif color == 'red':
                if pos[0]<=4 and pos[0]>=0 and pos[1]<=8 and pos[1]>=0:
                    return True
                else:
                    return False
            elif color == 'green':
                if pos[0]<=9 and pos[0]>=5 and pos[1]<=8 and pos[1]>=0:
                    return True
                else:
                    return False
        elif area==0:
            if pos[0]<=9 and pos[0]>=0 and pos[1]<=8 and pos[1]>=0:
                return True
            else:
                return False
            
    def border_check(self, name, pos, color=None):
        # 边界检查
        if name == '帅':
            area = 2
            color = None
        elif name =='士' or name =='象':
            area = 1
        else:
            area = 0
        return self.__border_check(area, pos, color)
        
    def move_chess(self, color, start, end):
        chess = self.board[start[0]] [start[1]]
        # 初始点检查
        if self.board[start[0]] [start[1]]==None or self.board[start[0]] [start[1]].color!= color:
            return False
        # 落地点检查
        if not self.border_check(chess.name, end, color):
            return False
        if self.board[end[0]] [end[1]]!=None and self.board[end[0]] [end[1]].color==color:
            return False
        # 移动轨迹检查
        if chess.name=='帅':
            if abs(end[0]-start[0])+abs(end[1]-start[1])==1 or self.board[end[0]] [end[1]].name=='帅':
                return self.move(start, end)
        elif chess.name=='士':
            if abs(end[0]-start[0])==1 and abs(end[1]-start[1])==1:
                return self.move(start, end)
        elif chess.name=='象':
            if abs(end[0]-start[0])==2 and abs(end[1]-start[1])==2 and self.board[int((end[0]+start[0])/2)] [int((end[1]+start[1])/2)]==None:
                return self.move(start, end)
        elif chess.name=='马':
            if (abs(end[0]-start[0])==2 and abs(end[1]-start[1])==1 and self.board[int((end[0]+start[0])/2)] [start[1]]==None) or (abs(end[0]-start[0])==1 and abs(end[1]-start[1])==2 and self.board[start[0]] [int((end[1]+start[1])/2)]==None):
                return self.move(start, end)
        elif chess.name=='車':
            num = 0
            if abs(end[0]-start[0])>0 and end[1]==start[1]:
                for i in range(min(start[0], end[0])+1,max(start[0], end[0])):
                    if self.board[i] [start[1]]!=None:
                        num += 1
            elif abs(end[1]-start[1])>0 and end[0]==start[0]:
                for i in range(min(start[1], end[1])+1, max(start[1], end[1])):
                    if self.board[start[0]] [i]!=None:
                        num += 1
            if num == 0:
                return self.move(start, end)
        elif chess.name=='兵':
            if self.__border_check(1, start, chess.color):
                if (chess.color=='red' and end[0]-start[0]==1 and end[1]==start[1]) or (chess.color=='green' and end[0]-start[0]==-1 and end[1]==start[1]):
                    return self.move(start, end)
            else:
                if chess.color=='red':
                    if (end[0]-start[0]==1 and end[1]==start[1]) or (end[0]==start[0]==1 and abs(end[1]-start[1])==1):
                        self.move(start, end)
                        return True
                elif chess.color=='green':
                    if (end[0]-start[0]==-1 and end[1]==start[1]) or (end[0]==start[0]==1 and abs(end[1]-start[1])==1):
                        return self.move(start, end)
        elif chess.name=='炮':
            num = 0
            if abs(end[0]-start[0])>0 and end[1]==start[1]:
                for i in range(min(start[0], end[0])+1,max(start[0], end[0])):
                    if self.board[i] [start[1]]!=None:
                        num += 1
            elif abs(end[1]-start[1])>0 and end[0]==start[0]:
                for i in range(min(start[1], end[1])+1, max(start[1], end[1])):
                    if self.board[start[0]] [i]!=None:
                        num += 1
            if (num==0 and self.board[end[0]] [end[1]]==None) or (num==1 and self.board[end[0]] [end[1]]!=None and self.board[end[0]] [end[1]].color!=chess.color):
                return self.move(start, end)
        return False
                
    def move(self, start, end):
        # 移动棋子
        if self.board[end[0]] [end[1]]!=None and self.board[end[0]] [end[1]].name == '帅':
            self.winner = self.board[start[0]] [start[1]].color
        self.board[end[0]] [end[1]] = self.board[start[0]] [start[1]]
        self.board[start[0]] [start[1]] = None
        return True
        
    def str2pos(self, command, color):
        # 口令中提取start->end
        length = len(command)
        if length==4:
            if command[0]=='前'or command[0]=='后'or command[0]=='中'or command[0]=='1'or command[0]=='2'or command[0]=='3'or command[0]=='4'or command[0]=='5'or command[0]=='一'or command[0]=='二'or command[0]=='三'or command[0]=='四'or command[0]=='五':
                pre = command[0]
                chessname = command[1]
                local = None
                direction = command[2]
                vector = command[3]
            else:
                pre = None
                chessname = command[0]
                local = command[1]
                direction = command[2]
                vector = command[3]
        elif length==5:
            pre = command[0]
            chessname = command[1]
            local = command[2]
            direction = command[3]
            vector = command[4] 
        else:
            return False
        #elif command=='悔棋':
        try:
            local = int(local.replace('一','1').replace('二','2').replace('三','3').replace('四','4').replace('五','5').replace('六','6').replace('七','7').replace('八','8').replace('九','9').replace('十','10'))
            vector = int(vector.replace('一','1').replace('二','2').replace('三','3').replace('四','4').replace('五','5').replace('六','6').replace('七','7').replace('八','8').replace('九','9').replace('十','10'))
            chessname = chessname.replace('车','車').replace('馬','马').replace('仕','士').replace('砲','炮').replace('像','象').replace('卒','兵').replace('相','象').replace('将','帅')
        except :
            return False
        if chessname not in '車马象士帅兵炮':
            return False
        chess = []
        endpos = []
        if color == 'red':
            if local:
                for i in range(10):
                    if self.board[i][local-1] and self.board[i][local-1].name == chessname and self.board[i][local-1].color==color:
                        chess.append([i,local-1])
                if len(chess)==0:
                    return False
                elif len(chess)==1:
                    ches = chess[0]
                elif len(chess)==2:
                    if chess[0][1]!=chess[1][1]:
                        return False
                    if pre == '前':
                        ches = chess[1]
                    elif pre == '后':
                        ches = chess[0]
                    else:
                        return False
                elif len(chess)==3:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1]:
                        return False
                    if pre == '前'or pre =='1'or pre =='一':
                        ches = chess[2]
                    elif pre == '中'or pre =='二'or pre =='2':
                        ches = chess[1]
                    elif pre == '后'or pre =='3'or pre =='三':
                        ches = chess[0]
                    else:
                        return False
                elif len(chess)==4:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1] or chess[2][1]!=chess[3][1]:
                        return False
                    if pre=='一'or pre =='1'or pre =='2'or pre =='3'or pre =='4'or pre =='二'or pre =='三'or pre =='四':
                        pre = int(pre.replace('一','1').replace('二','2').replace('三','3').replace('四','4'))
                        ches = chess[4-pre]
                else:
                    return False
            else:
                for i in range(10):
                    for j in range(9):
                        if self.board[i][j].name == chessname:
                            chess.append(i, j)
                if len(chess)==0:
                    return False
                elif len(chess)==1:
                    ches = chess[0]
                elif len(chess)==2:
                    if chess[0][1]!=chess[1][1]:
                        return False
                    if pre == '前':
                        ches = chess[1]
                    elif pre == '后':
                        ches = chess[0]
                    else:
                        return False
                elif len(chess)==3:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1]:
                        return False
                    if pre == '前'or pre =='1'or pre =='一':
                        ches = chess[2]
                    elif pre == '中'or pre =='二'or pre =='2':
                        ches = chess[1]
                    elif pre == '后'or pre =='3'or pre =='三':
                        ches = chess[0]
                    else:
                        return False
                elif len(chess)==4:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1] or chess[2][1]!=chess[3][1]:
                        return False
                    if pre=='一'or pre =='1'or pre =='2'or pre =='3'or pre =='4'or pre =='二'or pre =='三'or pre =='四':
                        pre = int(pre.replace('一','1').replace('二','2').replace('三','3').replace('四','4'))
                        ches = chess[4-pre]
                elif len(chess)==5:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1] or chess[2][1]!=chess[3][1]:
                        return False
                    if pre=='一'or pre =='1'or pre =='2'or pre =='3'or pre =='4'or pre =='二'or pre =='三'or pre =='四'or pre =='五'or pre =='5':
                        pre = int(pre.replace('一','1').replace('二','2').replace('三','3').replace('四','4').replace('五','5'))
                        ches = chess[5-pre]
                else:
                    return False
            if ches:
                if chessname == '車' or chessname =='炮' or chessname =='兵' or chessname =='帅':
                    if direction == '进':
                        endpos.append([ches[0]+vector, ches[1]])
                    elif direction == '退':
                        endpos.append([ches[0]-vector, ches[1]])
                    elif direction == '平':
                        endpos.append([ches[0], vector-1])
                elif chessname == '马':
                    if direction == '进':
                        if abs(vector-ches[1]-1)==2:
                            endpos.append([ches[0]+1, vector-1])
                        elif abs(vector-ches[1]-1)==1:
                            endpos.append([ches[0]+2, vector-1])
                    elif direction == '退':
                        if abs(vector-ches[1]-1)==2:
                            endpos.append([ches[0]-1, vector-1])
                        elif abs(vector-ches[1]-1)==1:
                            endpos.append([ches[0]-2, vector-1])
                elif chessname == '象':
                    if direction == '进':
                        endpos.append([ches[0]+2, vector-1])
                    elif direction == '退':
                        endpos.append([ches[0]-2, vector-1])
                elif chessname == '士':
                    if direction == '进':
                        endpos.append([ches[0]+1, vector-1])
                    elif direction == '退':
                        endpos.append([ches[0]-1, vector-1])    
                else:
                    return False
        elif color == 'green':
            if local:
                for i in range(10):
                    if self.board[i][9-local] and self.board[i][9-local].name == chessname and self.board[i][9-local].color==color:
                        chess.append([i,9-local])
                if len(chess)==0:
                    return False
                elif len(chess)==1:
                    ches = chess[0]
                elif len(chess)==2:
                    if chess[0][1]!=chess[1][1]:
                        return False
                    if pre == '前':
                        ches = chess[0]
                    elif pre == '后':
                        ches = chess[1]
                    else:
                        return False
                elif len(chess)==3:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1]:
                        return False
                    if pre == '前'or pre =='1'or pre =='一':
                        ches = chess[0]
                    elif pre == '中'or pre =='二'or pre =='2':
                        ches = chess[1]
                    elif pre == '后'or pre =='3'or pre =='三':
                        ches = chess[2]
                    else:
                        return False
                elif len(chess)==4:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1] or chess[2][1]!=chess[3][1]:
                        return False
                    if pre=='一'or pre =='1'or pre =='2'or pre =='3'or pre =='4'or pre =='二'or pre =='三'or pre =='四':
                        pre = int(pre.replace('一','1').replace('二','2').replace('三','3').replace('四','4'))
                        ches = chess[pre-1]
                else:
                    return False
            else:
                for i in range(10):
                    for j in range(9):
                        if self.board[i][j].name == chessname:
                            chess.append(i, j)
                if len(chess)==0:
                    return False
                elif len(chess)==1:
                    ches = chess[0]
                elif len(chess)==2:
                    if chess[0][1]!=chess[1][1]:
                        return False
                    if pre == '前':
                        ches = chess[0]
                    elif pre == '后':
                        ches = chess[1]
                    else:
                        return False
                elif len(chess)==3:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1]:
                        return False
                    if pre == '前'or pre =='1'or pre =='一':
                        ches = chess[0]
                    elif pre == '中'or pre =='二'or pre =='2':
                        ches = chess[1]
                    elif pre == '后'or pre =='3'or pre =='三':
                        ches = chess[1]
                    else:
                        return False
                elif len(chess)==4:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1] or chess[2][1]!=chess[3][1]:
                        return False
                    if pre=='一'or pre =='1'or pre =='2'or pre =='3'or pre =='4'or pre =='二'or pre =='三'or pre =='四':
                        pre = int(pre.replace('一','1').replace('二','2').replace('三','3').replace('四','4'))
                        ches = chess[pre-1]
                elif len(chess)==5:
                    if chess[0][1]!=chess[1][1] or chess[1][1]!=chess[2][1] or chess[2][1]!=chess[3][1]:
                        return False
                    if pre=='一'or pre =='1'or pre =='2'or pre =='3'or pre =='4'or pre =='二'or pre =='三'or pre =='四'or pre =='五'or pre =='5':
                        pre = int(pre.replace('一','1').replace('二','2').replace('三','3').replace('四','4').replace('五','5'))
                        ches = chess[pre-1]
                else:
                    return False
            if ches:
                if chessname == '車' or chessname =='炮' or chessname =='兵' or chessname =='帅':
                    if direction == '进':
                        endpos.append([ches[0]-vector, ches[1]])
                    elif direction == '退':
                        endpos.append([ches[0]+vector, ches[1]])
                    elif direction == '平':
                        endpos.append([ches[0], 9-vector])
                elif chessname == '马':
                    if direction == '进':
                        if abs(vector-(9-ches[1]))==2:
                            endpos.append([ches[0]-1, 9-vector])
                        elif abs(vector-(9-ches[1]))==1:
                            endpos.append([ches[0]-2, 9-vector])
                    elif direction == '退':
                        if abs(vector-(9-ches[1]))==2:
                            endpos.append([ches[0]+1, 9-vector])
                        elif abs(vector-(9-ches[1]))==1:
                            endpos.append([ches[0]+2, 9-vector])
                elif chessname == '象':
                    if direction == '进':
                        endpos.append([ches[0]-2, 9-vector])
                    elif direction == '退':
                        endpos.append([ches[0]+2, 9-vector])
                elif chessname == '士':
                    if direction == '进':
                        endpos.append([ches[0]-1, 9-vector])
                    elif direction == '退':
                        endpos.append([ches[0]+1, 9-vector])
                else:
                    return False
        if len(endpos)==1:
            return [ches, endpos[0]]
        else:
            print('error!str to pos ,get the num of end pos is %i'%len(endpos))
            return False
