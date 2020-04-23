from utils import *
import re


def install():
    step('Cloning tpm from github',
         body=['Put ~/.tmux/plugins/tpm/tpm at the bottom of ~/.tmux.conf'])
    cmd([
        'git', 'clone', 'https://github.com/tmux-plugins/tpm',
        f'{home()}/.tmux/plugins/tpm'
    ])


def tmux_compatible():
    output = cmd(['tmux', '-V'])

    if not output:
        return False

    return semver_compare(re.findall('(\d+\.\d+)', output)[0] + '.0',
                          '1.9.0') != -1


if __name__ == "__main__":
    req = {'git': '2.17.0', 'bash': '4.4.20'}

    step('Checking requirements')
    step('Checking if tmux is compatible', level=1)

    if check_requirements(req) and tmux_compatible():
        install()
        print("Successfully completed the job.")
    else:
        eprint('Failed to meet all requirements')