import sys
from typing import Optional


# CLASSE ProgressBar
# Crea una barra di stato per monitorare l'avanzamento dei test
class ProgressBar:
    def __init__(self, max_value: float = 100.0):
        self.max_value = max_value
        self.current_value = 0.0
        self.print_status()

    def update(self, new_value):
        if(new_value):
            self.current_value = min(max(0.0, new_value), self.max_value)
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

