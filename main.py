import socket

# Получить имя сокета от пользователя
socket_name = input("Введите имя сокета: ")

# Создать сетевой сокет
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print(f"Ошибка создания сокета: {e}")
    exit(1)

# Подключиться к серверу
try:
    sock.connect(("localhost", 8000))
except socket.error as e:
    print(f"Ошибка подключения к серверу: {e}")
    exit(1)

# Отправить имя сокета серверу
try:
    sock.send(socket_name.encode())
except socket.error as e:
    print(f"Ошибка отправки данных: {e}")
finally:
    # Закрыть сокет
    sock.close()

print("Имя сокета отправлено на сервер.")
