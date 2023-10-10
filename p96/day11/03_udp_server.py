# Author:zqbin
# @Time:2023/9/21 16:36
# @Author:14988
# @Site:
# @File:03_udp_server.py
# @Software:PyCharm

import socket
# 1. 创建套接字对象
# socket.SOCK_DGRAM   UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2. 绑定本地IP和端口
address = ("127.0.0.1", 10000)
s.bind(address)
# 3. 收发数据
while 1:
    msg, clientAddress = s.recvfrom(1024)
    print(msg.decode(encoding="utf8"))
    s.sendto(msg.upper(), clientAddress)
# 4. 关闭套接字