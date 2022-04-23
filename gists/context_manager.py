import socket

def finally_instead_of_context_manager(host, port):
    """
    Using finally instead of context manager
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.send(b'Hello, world')
    finally:
        s.close()

# In Python, most resources that need to be closed have their own context manager... let's use it..
def context_manager_example(host, port):
    """
    Using context manager
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(b'Hello, world')
