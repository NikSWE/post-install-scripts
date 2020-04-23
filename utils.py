def step(title, level=0, body=[]):
    '''
    Print nicely formatted description of the step.

        Parameters:
            title (string): Heading of the step
            level (int): Indentation of the step (optional) (default = 0)
            body (string[]): Description of the step (optional) (default = [])
        
        Example:
            ==> Heading

                Body line 1
                Body line 2
    '''
    spaces = 2 * level * ' '
    print(spaces + '==> ' + title)

    if body:
        spaces += 4 * ' '
        print()
        for line in body:
            print(spaces + line)
        print()


def semver_compare(a, b):
    '''
    Compare two semantic version strings.

        Parameters:
            a (string): Semantic version string
            b (string): Semantic version string
        
        Returns:
            -1 (int): a is less than b
            0 (int): a is equal to b
            1 (int): a is greater than b
    '''
    pa = a.split('.')
    pb = b.split('.')

    for i in range(3):
        na = int(pa[i])
        nb = int(pb[i])

        if na > nb:
            return 1
        if na < nb:
            return -1
    return 0
