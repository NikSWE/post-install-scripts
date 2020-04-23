from utils import *


def install():
    step('Cloning flutter from github',
         body=[
             'Run "flutter doctor" to install the engine\n',
             'You might need to restart your terminal'
         ])
    cmd([
        'git', 'clone', '-b', 'stable',
        'https://github.com/flutter/flutter.git', f'{home()}/.flutter-sdk'
    ])


if __name__ == "__main__":
    req = {'curl': '7.0.0', 'git': '2.0.0'}

    step('Checking requirements')

    if check_requirements(req):
        install()
        print("Successfully completed the job.")
    else:
        eprint('Failed to meet all requirements')