def test_import():
    import subprocess

def test_check_output():
    import subprocess
    assert callable(subprocess.check_output)
    ret = subprocess.check_output(['echo', 'hello world'])
    assert ret == b'hello world\n'

def test_Popen():
    import subprocess
    assert callable(subprocess.Popen)
    ret = subprocess.Popen(
        ['echo', 'hello world'],
        stdout=subprocess.PIPE).communicate()[0]
    assert ret == b'hello world\n'

def test_other_stuff_from_stdlib():
    import subprocess

    stuff_from_stdlib = [
        'CalledProcessError',
        'MAXFD',
        'PIPE',
        'Popen',
        'STDOUT',
        '__all__',
        '__doc__',
        '__file__',
        '__name__',
        '__package__',
        'call',
        'check_call',
        'list2cmdline',
    ]

    for name in stuff_from_stdlib:
        assert name in dir(subprocess)
