#客户端
import socket
import time
from colorama import init,Fore,Back,Style
init(autoreset=True)

# 创建 socket 对象
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
#host = socket.gethostname()
host='193.112.8.137'
# 设置端口号
port = 9995
# 连接服务，指定主机和端口
c.connect((host, port))
address=(host, port)

while 1:
    #s=c.accept()
    print('')
    print('——————等待对手中——————')
    msg0 = c.recv(4096).decode('utf-8')  # 棋盘大于1024
    if msg0=='游戏结束！':
        print(msg0)
        msg00 = c.recv(1024).decode('utf-8')
        print(msg00)
        continue
    print(msg0)
    print('\n——————————————————')
    msg1 = c.recv(1024)#接收输入提示
    print (msg1.decode('utf-8'))
    time.sleep(0.5)
    comm = input('：')
    c.send(comm.encode('utf-8'))
    msg3 = c.recv(4096).decode('utf-8')#棋盘大于1024
    if msg3=='——————无效输入！请规范输入再次尝试！———————\r\n':
        print(msg3)
        continue
    else:
        print(msg3)

c.close()
