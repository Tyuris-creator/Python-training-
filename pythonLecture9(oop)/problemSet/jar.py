class Jar:
    def __init__(self, capacity=12):
        self._cookie = 0
        self._capacity = capacity
        if self._capacity  < 0:
            raise ValueError

    def __str__(self):
        cookies = []
        i = 0
        if self._cookie == 0:
            return ""
        else:
            while i < self._cookie:
                cookies.append("🍪")
                i += 1
            return "".join(cookies)

    def deposit(self, n):
        if self._cookie + n > self._capacity:
            raise ValueError
        else:
            self._cookie += n
            return self._cookie

    def withdraw(self, n):
        if self._cookie - n < 0:
            raise ValueError
        else:
            self._cookie -= n
            return self._cookie

    @property
    def capacity(self):
        return self._capacity - self._cookie

    @property
    def size(self):
        return self._cookie

cookie1 = Jar(5)
print(cookie1.capacity)


