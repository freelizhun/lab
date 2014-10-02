import subprocess
import signal


cmd = 'stat ./testfolder/*'
def subprocess_setup():
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

shell = False
_PIPE = subprocess.PIPE  # pylint: disable=E1101
obj = subprocess.Popen(cmd,
       stdin=_PIPE,
       stdout=_PIPE,
       stderr=_PIPE,
       close_fds=True,
       preexec_fn=subprocess_setup,
       shell=True)

_returncode = obj.returncode  # pylint: disable=E1101
print _returncode


