"""
Monkeypatch in subprocess.check_output for Python < 2.7
"""

import os
import types


def import_from_stdlib(name):
    import code # arbitrary module which stays in the same dir as subprocess
    stdlibdir, _ = os.path.split(code.__file__)
    pyfile = os.path.join(stdlibdir, name + '.py')
    result = types.ModuleType(name)
    mydict = execfile(pyfile, result.__dict__)
    return result

_subprocess_stdlib = import_from_stdlib('subprocess')

if "check_output" not in dir(_subprocess_stdlib):
    def check_output(*popenargs, **kwargs):
        if 'stdout' in kwargs:
            raise ValueError('stdout argument not allowed, it will be overridden.')
        process = _subprocess_stdlib.Popen(stdout=_subprocess_stdlib.PIPE, *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            raise _subprocess_stdlib.CalledProcessError(retcode, cmd)
        return output

# copy some functions from subprocess.py, but rebind the global dictionary
for name in dir(_subprocess_stdlib):
    func = getattr(_subprocess_stdlib, name)
    globals()[name] = func
    # globals()[name] = rebind_globals(func)

# Clean up namespace to make it look more like stdlib subprocess
del name, func, import_from_stdlib
