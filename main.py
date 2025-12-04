
import os
import sys

# garante que a pasta `src` esteja disponível nos imports quando o programa for
# executado diretamente (terminal) ou pelo VS Code (launch.json também define PYTHONPATH).
ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_PATH = os.path.join(ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from Menu import menu


def main():
    # inicia o menu interativo
    menu()


if __name__ == "__main__":
    main()
