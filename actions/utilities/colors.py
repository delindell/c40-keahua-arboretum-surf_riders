class Colors:

    def __init__(self):
        self.effects = {
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m',
            'ENDC':'\033[0m'
        }
        self.text_colors = {
            'HEADER': '\033[95m',
            'OKBLUE': '\033[94m',
            'OKGREEN': '\033[92m',
            'WARNING': '\033[93m',
            'FAIL': '\033[91m',
        }
        self.background_colors = {
            'BLACK': '\u001b[40m',
            'RED': '\u001b[41m',
            'GREEN': '\u001b[42m',
            'YELLOW': '\u001b[43m',
            'BLUE': '\u001b[44m',
            'MAGENTA': '\u001b[45m',
            'CYAN': '\u001b[46m',
            'WHITE': '\u001b[47m',
        }