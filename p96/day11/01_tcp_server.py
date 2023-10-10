# Author:zqbin
# @Time:2023/9/21 15:13
# @Author:14988
# @Site:
# @File:01_tcp_server.py
# @Software:PyCharm

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 9999)
s.bind(address)
s.listen()
while 1:
    conn, clientAddress = s.accept()
    print('客户端%s:%d已经连接' % clientAddress)
    while 1:
        msg = conn.recv(1024)
        msg = msg.decode(encoding='utf-8')
        print(msg)
        msg = msg.upper()
        sendMsg = msg.encode('utf-8')
        conn.sendall(sendMsg)
        if msg in {'EXIT', 'QUIT'}:
            break

    conn.close()