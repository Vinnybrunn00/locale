import argparse
from rich.console import Console
from rich.progress import track
from rich import print
import os, sys

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--find')
arg = parser.parse_args()
argument = arg.find

console = Console()

USER = os.environ['USERPROFILE']
PATH = 'C:\'

def findFile(path: str, prompt: str, user: str):
    if prompt == None:
        print('[yellow]usage[/]: loc [--find file]\n\npositional arguments:\n   -f, --find, Busca por arquivo especificado')
        sys.exit()
    for root, _, file in track(os.walk(path), f'Buscando por {prompt}...'):
        for arquivos in file:
            joinPath = os.path.join(root, arquivos)
            with open(f'{user}\\Desktop\\logfile.log', 'a') as log:
                log.write(f'\n> {joinPath}')
            if prompt in arquivos:
                all_path = os.path.join(root, arquivos)
                yield all_path
                
if __name__ == '__main__':
    if not sys.platform != 'win32':
        unpack = findFile(PATH, argument, USER)
        for find in unpack:
            print(f'{find}\n')
    else:
        print('Este script so funciona no windows')
