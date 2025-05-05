import socket
import threading

HOST = '127.0.0.1'
PORT = 5556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message, _client=None):
    for client in clients:
        if client != _client:
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"{nickname} 님이 나갔습니다.".encode('utf-8'))
                nicknames.remove(nickname)
            break

def receive():
    print("서버가 실행 중입니다...")
    while True:
        client, address = server.accept()
        print(f"새 연결: {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"닉네임: {nickname}")
        broadcast(f"{nickname} 님이 입장했습니다.".encode('utf-8'))
        client.send('서버에 연결되었습니다!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def admin_input():
    while True:
        message = input()
        if message.strip():
            broadcast(f"관리자: {message}".encode('utf-8'))
            print(f"관리자(나): {message}")  # 서버 콘솔에도 출력

# 서버 수신 및 관리자 입력 스레드 시작
threading.Thread(target=receive).start()
threading.Thread(target=admin_input).start()
