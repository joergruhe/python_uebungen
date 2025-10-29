class meineklasse:
    def __init__(self):
        print('Test-Klasse initialisiert.')
        self._x = 100

    @property
    def x (self):
        print('Methode x aufgerufen.')
        return self._x
    @x.setter
    def x(self, value):
        print('Methode set_x aufgerufen.')
        self._x = value






if __name__ == '__ main __':
    print('Das Skript wird direkt ausgeführt.')
else:
    print('Das Skript wird als Modul importiert.')
    test_instance = meineklasse()
    print(test_instance.x)
    test_instance.x = 200
    print(test_instance.x)
