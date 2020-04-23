from utils import *


def install():
    step('Cloning vundle from github',
         body=['Source ~/.vim/bundle/Vundle.vim in your .vimrc'])
    cmd([
        'git', 'clone', 'https://github.com/VundleVim/Vundle.vim.git',
        f'{home()}/.vim/bundle/Vundle.vim'
    ])


if __name__ == "__main__":
    req = {'curl': '7.0.0', 'git': '2.17.0'}

    step('Checking requirements')

    if check_requirements(req):
        install()
        print("Successfully completed the job.")
    else:
        eprint('Failed to meet all requirements')