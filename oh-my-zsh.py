from utils import *


def install():
    step('Installing oh-my-zsh',
         body=['Restart your terminal for changes to take effect'])
    cmd([
        'sh', '-c',
        '"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"',
        '""', '--unattended'
    ])


if __name__ == "__main__":
    req = {'curl': '7.0.0', 'git': '1.7.2', 'zsh': '4.3.9'}

    step('Checking requirements')

    if check_requirements(req):
        install()
        print("Successfully completed the job.")
    else:
        eprint('Failed to meet all requirements')