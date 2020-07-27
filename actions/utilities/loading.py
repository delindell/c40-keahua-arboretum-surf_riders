import time

class Loading:

    def load(self, char, n, result):
        for num in range(0, n):
            print(f'{char}', end='', flush=True)
            time.sleep(0.25)
        time.sleep(0.50)
        print(f'{result}')