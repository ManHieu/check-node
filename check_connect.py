import socket


def check_connect(host, port, timeout=10):
    """
    Kiểm tra node có kết nối được không?
    """
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((host, port))
        s.close()
        return True
    except Exception as ex:
        print(ex)
        return False
