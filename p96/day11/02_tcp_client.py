# Author:zqbin
# @Time:2023/9/21 15:25
# @Author:14988
# @Site:
# @File:02_tcp_client.py
# @Software:PyCharm

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 9999)
s.connect(address)
while 1:
    msg = input('>>：').strip()
    if len(msg) != 0:
        msg = msg.encode('utf-8')
        s.sendall(msg)
        ret = s.recv(1024)
        ret = ret.decode('utf-8')
        print(ret)
        if ret in {'EXIT', 'QUIT'}:
            break

s.close()
