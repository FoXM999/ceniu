# Author:zqbin
# @Time:2023/9/21 16:36
# @Author:14988
# @Site:
# @File:04_udp_client.py
# @Software:PyCharm

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddress = ('127.0.0.1', 10000)
while 1:
    msg = input('>>: ').strip()
    if len(msg) != 0:
        s.sendto(msg.encode('utf8'), serverAddress)
        ret, address = s.recvfrom(1024)
        ret = ret.decode('utf8')
        print(ret)
        if ret in {'EXIT', 'QUIT'}:
            break

s.close()


