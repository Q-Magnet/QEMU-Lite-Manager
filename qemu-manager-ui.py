from os import system, path, get_terminal_size
from sys import argv
from platform import system as _s
from colorama import Back, Fore, init
from math import floor
init()
term_size = list(get_terminal_size())
class TUI:
    def printtitle(title=str, leng=-1):
        if leng == -1:
            leng = len(title)
        #├┤┬┴┼┌┐└┘─│
        #┌─┬─┐
        #│  │  │
        #├─┼─┤
        #└─┴─┘
        print(' '*2+'┌',end='')
        print('─'*floor((term_size[0]-4-leng)/2-1),end='')
        print('┤', end='')
        print(title, end='')
        print('├', end='')
        print('─'*floor((term_size[0]-4-leng)/2-1),end='')
        print('┐')
    def printtlns(text=str):
        text = text.split('\n')
        for i in text:
            print(' '*2+'│ ',end='')
            print(i,end='')
            print(' '*(term_size[0]-4-len(i)-2), end='')
            print('│')
    def printtbottom():
        print(' '*2+'└',end='')
        print('─'*(term_size[0]-5),end='')
        print('┘')
class color:
    def text(text, _fgc, _bgc='reset'):
        _fgc = _fgc.lower()
        _bgc = _bgc.lower()
        tx = text + Fore.RESET
        out = ''
        if _fgc == 'red':
            out = Fore.RED
        elif _fgc == 'blue':
            out = Fore.BLUE
        elif _fgc == 'green':
            out = Fore.GREEN
        elif _fgc == 'reset':
            out = Fore.RESET
        elif _fgc == 'yellow':
            out = Fore.YELLOW
        elif _fgc == 'cyan':
            out = Fore.CYAN
        elif _fgc == 'magneta':
            out = Fore.MAGENTA
        elif _fgc == 'white':
            out = Fore.WHITE
        if _bgc == 'red':
            out = out + Back.RED + tx
        elif _bgc == 'blue':
            out = out + Back.BLUE + tx
        elif _bgc == 'green':
            out = out + Back.GREEN + tx
        elif _bgc == 'reset':
            out = out + Back.RESET + tx
        elif _bgc == 'yellow':
            out = out + Back.YELLOW + tx
        elif _bgc == 'cyan':
            out = out + Back.CYAN + tx
        elif _bgc == 'magneta':
            out = out + Back.MAGENTA + tx
        elif _bgc == 'white':
            out = out + Back.WHITE + tx
        return out + Fore.RESET + Back.RESET
def finput(prompt):
    return input('   ' + prompt)
def fprint(txt):
    return print('   ' + txt)
if _s() == 'Windows':
    clear = 'cls'
    And = '&'
    cp = 'copy'
    dash = '\\'
    ls = 'dir /w '
else:
    clear = 'clear'
    And = '&&'
    cp = 'cp'
    dash = '/'
    ls = 'ls '

enter = 'Press Enter to continue'
title = '''QEMU-Lite-Manager'''
pages = {'Home':['This is the Home page of QEMU-Lite-Manager-UI.\nType numbers or letters to execute.\n1. Add VM\n2. Convert Virtual Machine File to Script\n3. Start VM\nG. Set QEMU path\nV. Version\nA. Exit', 'Home'], 
'Convert':['Enter VM Name needed to convert to .bat: ', 'Convert    A: Home'], 
'Add':['Enter Preset Name and VM Name', 'Add VM - A: Home'], 
'Start':['Enter VM Name: ', 'Start VM - A: Home'], 
'Version':['QEMU-Lite-Manager-UI', 'Version'], 
'Invalid':['Choice is invalid.\nPlease Retry', 'Invalid Choice'], 
'Successful':['Successfully executed command', 'Successful'], 
'Setpath':['Enter QEMU Path: ', 'Set QEMU Path']}
dir = path.dirname(argv[0])
# Init Add VM Menu
# print(f'cd {dir}{dash}Preset-{_s()} {And} {ls} *.qvm > {dir}{dash}temp.000')
system(f'cd {dir}{dash}Preset-{_s()} {And} {ls} *.qvm > {dir}{dash}temp.000')
with open(f'{dir}/temp.000', 'r') as file:
    file = file.read()
    if _s() == 'Windows':
        presets = file.split('\n')[5].split()
    else:
        presets = file.split()
    presets_p = '\n'.join(presets)
    pages['Add'] = ['Enter Preset Name and VM Name\n'+presets_p, 'Add VM - A: Home']
# Init Start VM Menu & Convert Menu
# print(f'cd {dir} {And} {ls} *.qvm > {dir}{dash}temp.001')
system(f'cd {dir} {And} {ls} *.qvm > {dir}{dash}temp.001')
with open(f'{dir}/temp.001', 'r') as file:
    file = file.read()
    if _s() == 'Windows':
        vms = file.split('\n')[5].split()
    else:
        vms = file.split()
    vms_p = '\n'.join(vms)
    pages['Start'] = ['Enter VM Name to start: \n'+vms_p, 'Start VM - A: Home']
    pages['Convert'] = ['Enter VM Name needed to convert to .bat: \n'+vms_p, 'Convert    A: Home']



page = 'Home'
while True:
    system(clear)
    term_size = list(get_terminal_size())
    TUI.printtitle(color.text('QEMU-Lite-Manager - ' + pages[page][1], 'blue'), len(pages[page][1]+'QEMU-Lite-Manager - '))
    #print(color.text(pages[page][1], 'blue', 'white')) # Print Title
    TUI.printtlns(pages[page][0])
    TUI.printtbottom()
    #print(pages[page][0]) # Print Content
    if page == 'Home':
        choice = finput('Enter your choice: ')
        if choice == '1':
            page = 'Add'
        elif choice == '2':
            page = 'Convert'
        elif choice == '3':
            page = 'Start'
        elif choice.lower() == 'a':
            exit()
        elif choice.lower() == 'g':
            page = 'Setpath'
        elif choice.lower() == 'v':
            page = 'Version'
    elif page == 'Add':
        choice = finput('Preset: ')
        if choice == 'A':
            page = 'Home'
        else:
            choice2 = finput('VM: ')
            if choice2 == 'A':
                page = 'Home'
            else:
                if choice in presets:
                    system(f'{cp} Preset-{_s()}{dash}{choice} {choice2}')
                    page == 'Successful'
                else:
                    page = 'Invalid'
    elif page == 'Convert':
        choice = finput('')
        if choice == 'A':
            page = 'Home'
        else:
            system(f'cd {dir} {And} qemu-manager --generate-bat {choice}')
        finput(enter)
        0
    elif page == 'Start':
        choice = finput('')
        system(f'cd {dir} {And} qemu-manager --launch {choice} --force-start')
        finput(enter)
        page = 'Home'
    elif page == 'Setpath':
        choice = finput('path: ')
        with open('qemu-tui-pref.txt', 'w') as f:
            f.write(f'qemu-path\n{choice}')
        page = 'Home'
    elif page == 'Version':
        system(f'cd {dir} {And} qemu-manager --fversion')
        finput(enter)
        page = 'Home'
    elif page == 'Invalid':
        finput(enter)
        page = 'Home'
    elif page == 'Successful':
        finput(enter)
        page = 'Home'