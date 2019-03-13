# -*- coding: utf-8 -*-
from main import chessboard


#服务器
import os
import socket
import json
import threading
import time
import sys


def clear():
    os.system('cls')
def changeid(id):
    if id=='red':
        return 'green'
    elif id=='green':
        return 'red'
    else:
        return 'red'
        
        
if __name__ == '__main__':
    t = chessboard()
    id = 'red'   
    def handle():
        global id
        while 1:
            if t.winner:
                for c in socks:
                    msg = "游戏结束！"
                    c.send(msg.encode('utf-8'))
                time.sleep(2)
                for c in socks:
                    msg3 = "获胜者是%s方!\n\n————————游戏将于5s后重启————————"%id
                    c.send(msg3.encode('utf-8'))
                time.sleep(5)
                t.restart()
            if len(socks)!=2:
                continue
            for c in socks:
                tryagain = True
                while tryagain:
                    tt = t.display(id)
                    c.sendto(tt.encode('utf-8'), address)
                    print(tt)
                    msg1 = '现在轮到%s方：' % id + "\r\n"
                    c.send(msg1.encode('utf-8'))
                    command = c.recv(1024).decode('utf-8')
                    pos = t.str2pos(command, id)
                    # print(pos)
                    if pos and t.move_chess(id, pos[0], pos[1]):
                        json_string = t.display(id)
                        c.sendto(json_string.encode('utf-8'), address)
                        print(id+'方：')
                        print(command)
                        tryagain = False
                    else:
                        msg2 = '——————无效输入！请规范输入再次尝试！———————\r\n'
                        c.send(msg2.encode('utf-8'))
                        continue
                id = changeid(id)
                if t.winner:
                    break
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    # host = socket.gethostname()
    host='193.112.8.137'
    port = 9995
    # 绑定端口号
    s.bind((host, port))
    address=(host, port)
    # 设置最大连接数，超过后排队
    s.listen(2)
    socks=[]
    th = threading.Thread(target=handle)
    th.start()
    while 1:
        c, addr = s.accept()
        print('connected from:', addr)
        socks.append(c)
    s.close()
