import time

class Typer:

    def animate(self, str, speed):
        for c in str:
            print(c, end='', flush=True)
            time.sleep(speed)
