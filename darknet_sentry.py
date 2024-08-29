import random as r, socket as s

def _1(ip):
    while True:
        a = [str(r.randint(0, 255)) for _ in range(4)]
        ip = '.'.join(a)
        if not (a[0] == "127" or a[0] == "10" or (a[0] == "172" and 16 <= int(a[1]) <= 31) or (a[0] == "192" and a[1] == "168")):
            break
    return ip

def _2(ip):
    try:
        c = s.create_connection((ip, 80), timeout=1)
        c.close()
        return True
    except (s.timeout, s.error):
        return False

def _3():
    while True:
        i = _1('')
        if _2(i):
            print(i)

if __name__ == "__main__":
    _3()