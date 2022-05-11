class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_method(self):
        self.__c = 40
        print('public method', self.__c)
        self.__private_method()

    def __private_method(self):
        print('private')


hello = Hello('Muhammad')
print(hello.public_method())