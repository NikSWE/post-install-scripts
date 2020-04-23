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
