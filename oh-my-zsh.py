from utils import *


def install():
    step('Cloning oh-my-zsh from github',
         body=[
             'Run this to change your default shell', 'chsh -s $(which zsh)\n',
             'Make sure to update your .zshrc\n',
             'Download template: https://del.dog/zsh-template'
         ])
    cmd([
        'git', 'clone', 'https://github.com/ohmyzsh/ohmyzsh.git',
        f'{home()}/.oh-my-zsh'
    ])


if __name__ == "__main__":
    req = {'curl': '7.0.0', 'git': '1.7.2', 'zsh': '4.3.9'}

    step('Checking requirements')

    if check_requirements(req):
        install()
        print("Successfully completed the job.")
    else:
        eprint('Failed to meet all requirements')