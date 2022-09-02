from Ager.Ager_main import ager_main

from Elena_Pokalitsina.EP_main import ep_main


def main():
    print('ver. 1.52')
    select = int(input('Select what are you do:\n1. Elena Pokalitsina\n2. Ager\n'))
    if select == 1:
        ep_main()
    elif select == 2:
        ager_main()


if __name__ == '__main__':
    main()
