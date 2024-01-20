import os
import sys
import platform
from sys import exit
if platform.system() == 'Windows':
    And = '&'
else:
    And = '&&'

othercmds = ''
items_list = ['machine', 'cpu', 'vga', 'display', 'hda', 'hdb', 'cdrom', 'fda', 'device', 'audiodev', 'netdev', 'smp', 'accel', 'm', 'L']
visuals = ['machine', 'cpu', 'vga', 'display', 'accel', 'device']
visual_values_list = {'machine':['q35', 'pc', 'ich9', 'piix'], 
                      'cpu':['IntelNehalem', 'qemu64', 'IntelPentium', 'IntelPentiumII', 'IntelPentiumIII', 'IntelHaswell', 'AMDEPYC', 'IntelXeonCascadelake', 'IntelCoreBroadwell', 'IntelXeonIceLake', 'IntelXeonIvyBridge', 'IntelCore2P9', 'IntelXeonSandyBridge', 'IntelCoreSkylake', 'IntelAtomSnowridge', 'IntelNehalem-C', 'IntelCore2Duo', 'IntelCoreDuo', 'IntelAtomN270'], 
                      'vga':['StandardVGA', 'Bochs', 'Cirrus54xx', 'VMwareSVGA', 'virtio-gpu'], 
                      'display':['sdl2'], 
                      'accel':['tcg', 'tcg-multi-thread', 'kvm', 'HAXM', 'Hyper-V', 'Hyper-V-no-irqchip', 'xen'], 
                      'device':['VMwareMouse', 'USBKeyboard', 'USBMouse', 'usb-piix3', 'usb-piix4', 'AppleUSBController', 'usb-ich9', 'ATIRage128']}
values_list =        {'machine':['q35', 'pc', 'q35', 'pc'], 
                      'cpu':['Nehalem', 'qemu64', 'pentium', 'pentium2', 'pentium3', 'Haswell', 'EPYC', 'Cascadelake-Server', 'Broadwell', 'Icelake-Server', 'IvyBridge', 'Penryn', 'SandyBridge', 'Skylake-Client', 'Snowridge', 'Westmere', 'core2duo', 'coreduo', 'n270'], 
                      'vga':['std', 'bochs', 'cirrus', 'vmware', 'virtio'], 
                      'display':['sdl'], 
                      'accel':['tcg', 'tcg,thread=multi', 'kvm', 'hax', 'whpx', 'whpx,kernel-irqchip=off', 'xen'], 
                      'device':['vmmouse', 'usb-kbd', 'usb-mouse', 'piix3-usb-uhci', 'piix4-usb-uhci', 'pci-ohci', 'ich9-usb-ehci1', 'ati-vga']}

try:
    with open('C:\\qemu-tui\\qemu-tui-pref.txt', 'r') as f:
        pref = f.read()
        pref = pref.split('\n')
except:
    print('no pref file')

try:
    qemu_path = pref[pref.index('qemu-path') + 1]
    if qemu_path[-1] != '\\':
        qemu_path = qemu_path + '\\'
except:
    print('bad pref file, no qemu-path')
# Config Stuffs
def read_config_file(File):
    output = {}
    with open(File, 'r') as f:
        config_file = f.read()
    config_file = config_file.split('\n')
    for i in range(len(config_file)):
        config_file[i] = config_file[i].split(' : ')
        if len(config_file[i]) != 2:
            print('Wrong Config File!')
            exit()
        output[config_file[i][0]] = config_file[i][1]

    return(output)

def check_n_fix_config_file(file=dict):
    global othercmds
    for i in file:
        if not i in items_list:
            print(i + 'not')
            return [1, file]
    for i in file:
        if i == 'device':
            file[i] = file[i].split(', ')
            for j in range(len(file[i])):
                try:
                    file[i][j] = values_list[i][visual_values_list[i].index(file[i][j])]
                except:
                    0
            for j in file[i]:
                othercmds = othercmds + ' -device ' + j                 
        #i = i.lower()
        elif i in visuals:
            if file[i] in visual_values_list[i]:
                file[i] = values_list[i][visual_values_list[i].index(file[i])]
    if 'device' in file:
        file.pop('device')
    return [0, file]
# QEMU Stuffs
def get_qemu_version(mode='simple'):
    try:
        os.system(f'cd {qemu_path} {And} qemu-system-x86_64 --version > ver.txt')
        with open(qemu_path + 'ver.txt', 'r') as f:
            if mode == 'simple':
                return f.read().split(' ')[3]
            elif mode == 'complex':
                return f.read().split('\n')[0].split(' ')[4][1:-2]
    except:
        print('bad qemu version')
        exit()
def create_launch_script(file=dict):
    cmd = f'cd {qemu_path} {And} qemu-system-x86_64 '
    for i in file[1]:
        cmd = cmd + '--' + i + ' ' + file[1][i] + ' '
    cmd = cmd + othercmds
    return cmd

def start_qemu_x86_64(file=dict, qemu_output=True):
    cmd = f'cd {qemu_path} {And} qemu-system-x86_64 '
    for i in file[1]:
        cmd = cmd + '--' + i + ' ' + file[1][i] + ' '
    cmd = cmd + othercmds
    print(f'Starting QEMU-{get_qemu_version()} with command\n{cmd}')
    if qemu_output == False:
        cmd = cmd + ' > nul'
    os.system(cmd)
    return cmd


# Only For Debugging, using # if building
# config = read_config_file('C:\QEMU-TUI\zVM00.qvm')
# config = check_n_fix_config_file(config)
# if config[0] == 0:
#     0
#     #print('No Error')
# else:
#     if not '--force-start' in sys.argv:
#         print('Error in config file')
#         exit()
# start_qemu_x86_64(config)


# For building, using # if debugging
if '--version' in sys.argv:
    print('QEMU-' + get_qemu_version() + ' and QEMU-Lite-Manager')
    exit()
if '--fversion' in sys.argv:
    print('   QEMU-' + get_qemu_version() + ' and QEMU-Lite-Manager')
    exit()
if '--launch' in sys.argv:
    config = read_config_file(sys.argv[sys.argv.index('--launch') + 1])
    config = check_n_fix_config_file(config)
    if config[0] == 0:
        0
        #print('No Error')
    else:
        if not '--force-start' in sys.argv:
            print('Error in config file')
            exit()
    start_qemu_x86_64(config)
if '--generate-bat' in sys.argv:
    config = read_config_file(sys.argv[sys.argv.index('--generate-bat') + 1])
    config = check_n_fix_config_file(config)
    if config[0] == 0:
        0
        #print('No Error')
        print(create_launch_script(config))