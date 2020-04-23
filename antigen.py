from utils import *


def install():
    step('Downloading antigen from main repository')
    output = cmd(['curl', '-L', 'git.io/antigen'])

    step('Creating antigen.zsh', body=['Source ~/.antigen.zsh in your .zshrc'])
    with open(home() + '/.antigen.zsh', 'w') as f:
        f.write(output)


if __name__ == "__main__":
    req = {'zsh': '4.3.11', 'git': '2.17.0'}

    step('Checking requirements')

    if check_requirements(req):
        install()
        print("Successfully completed the job.")
    else:
        eprint('Failed to meet all requirements')