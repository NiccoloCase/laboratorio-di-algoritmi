import sys
import time
from typing import Optional

class ProgressBar:
    def __init__(self, max_value: float = 100.0):
        self.max_value = max_value
        self.current_value = 0.0
        self.print_status()

    def update(self, new_value: Optional[float] = None):
        if new_value is not None:
            self.current_value = min(max(0.0, new_value), self.max_value)
        else:
            self.current_value += 20.0  # Incremento predefinito
            self.current_value = min(self.current_value, self.max_value)

        self.print_status()

    def complete(self):
        self.current_value = self.max_value
        self.print_status()

    def print_status(self):
        progress = self.current_value / self.max_value
        progress_percent = int(progress * 100)
        bar_length = 50
        filled_length = int(bar_length * progress)
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        sys.stdout.write('\rProgress |{}| {}% Complete'.format(bar, progress_percent))
        sys.stdout.flush()

if __name__ == "__main__":
    progress_bar = ProgressBar()

    # Simula l'avanzamento della barra di stato
    for _ in range(5):
        time.sleep(1)
        progress_bar.update()

    # Completa la barra di stato
    progress_bar.complete()

    print("\nProcesso completato!")
