import socket
import threading

HOST = '127.0.0.1'
PORT = 5556

nickname = input("닉네임을 입력하세요: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("서버와의 연결이 끊어졌습니다.")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input()}"
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
