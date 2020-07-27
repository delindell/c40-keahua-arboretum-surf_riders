import time

class Loading:

    def load(self, char, n, speed, result):
        for num in range(0, n):
            print(f'{char}', end='', flush=True)
            time.sleep(speed)
        time.sleep(0.50)
        print(f'{result}')