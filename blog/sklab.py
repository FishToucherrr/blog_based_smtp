from socket import *
from email.base64mime import body_encode
import time
import ssl

body="what the fuck?"
recvr="394704697@qq.com"
title="fuck tls"

msg = "\r\n "+ body
endMsg = "\r\n.\r\n"
# 选择一个邮件服务
mailServer = "smtp.qq.com"

# 发送方地址和接收方地址，from 和 to
# 发送方，验证信息，由于邮箱输入信息会使用base64编码，因此需要进行编码

purpose = ssl.Purpose.SERVER_AUTH
context = ssl.create_default_context(purpose,cafile=None)

serverPort = 465
# SMTP使用587号端口
rawSocket = socket(AF_INET, SOCK_STREAM)
rawSocket.connect((mailServer, serverPort))

ssl_sock=context.wrap_socket(rawSocket,server_hostname=mailServer)

# connect只能接收一个参数
# 从客户套接字中接收信息

recv = ssl_sock.recv(1024).decode()

print(recv)
if '220' != recv[:3]:
    print("220 reply not received from server.")

# 发送 HELO 命令并且打印服务端回复

heloCommand = "HELO Alice\r\n"

ssl_sock.send(heloCommand.encode()) # 随时注意对信息编码和解码

recv1 = ssl_sock.recv(1024).decode()

print(recv1)
if '250' != recv1[:3]:
    print("250 reply not received from server.")

username = "394704697@qq.com"
password = "czycqvciegurbihh"

user_pass_encode64 = body_encode(f"\0{username}\0{password}".encode('ascii'), eol='')
ssl_sock.sendall(f'AUTH PLAIN {user_pass_encode64}\r\n'.encode())
recv_auth = ssl_sock.recv(1024).decode()
print(recv_auth)


mailFrom = "MAIL FROM:<394704697@qq.com>\r\n"
ssl_sock.send(mailFrom.encode())
recv2 = ssl_sock.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)
rcptTo = "RCPT TO:<" + recvr + ">\r\n"
ssl_sock.send(rcptTo.encode())
recv3 = ssl_sock.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: "+recv3)
data = "DATA\r\n"
ssl_sock.send(data.encode())
recv4 = ssl_sock.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)
subject = "Subject: "+title+"\r\n\r\n" 
ssl_sock.send(subject.encode())
date = time.strftime("%a, %d %b %Y %H:%M:%S ", time.gmtime())
date = date + "\r\n\r\n"
ssl_sock.send(date.encode())
ssl_sock.send(msg.encode())
ssl_sock.send(endMsg.encode())
recv_msg = ssl_sock.recv(1024)
print("Response after sending message body:"+recv_msg.decode())
quit = "QUIT\r\n"
ssl_sock.send(quit.encode())
recv5 = ssl_sock.recv(1024)
print(recv5.decode())
ssl_sock.close()
