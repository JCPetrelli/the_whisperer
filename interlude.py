import sys
from colorama import Fore, Style, init
init(autoreset=True)  # Initializes colorama to auto-reset color after each print

description = sys.argv[1]
pause = sys.argv[2].lower() == 'true'

# Print the description in cyan
print(Fore.CYAN + description)

# Optionally pause
if pause:
    input("Press Enter to continue...")

