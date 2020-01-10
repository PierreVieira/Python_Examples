"""
\033[0;33;44m
    style;text;back
"""


def white(param):
    return f'\033[0;30m{param}\033[m'


def red(param):
    return f'\033[0;31m{param}\033[m'


def green(param):
    return f'\033[0;32m{param}\033[m'


def yellow(param):
    return f'\033[0;33m{param}\033[m'


def blue(param):
    return f'\033[0;34m{param}\033[m'


def pruple(param):
    return f'\033[0;35m{param}\033[m'


def cyan(param):
    return f'\033[0;36m{param}\033[m'


def grey(param):
    return f'\033[0;37m{param}\033[m'


cores = [white('branco'), red('vermelho'), green('verde'), yellow('amarelo'), blue('azul'), pruple('roxo'), cyan('ciano'), grey('cinza')]
print('{:>22}{:>28}'.format('\033[1;30mTEXT/BACK\033[m', '\033[1;30mCODE\033[m'))
n = 30
for cor in cores:
    print(f'{cor:>20}                 {n}')
    n += 1
print('\n')
print("\033[4;30;45mHello world!\033[m")
