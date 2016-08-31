# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the repronim package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Test invocation of repronim utilities "as is installed"
"""

from mock import patch
from .utils import ok_startswith, eq_, \
    ignore_nose_capturing_stdout, assert_cwd_unchanged

from repronim.cmd import Runner
from repronim.support.exceptions import CommandError

def check_run_and_get_output(cmd):
    runner = Runner()
    try:
        # suppress log output happen it was set to high values
        with patch.dict('os.environ', {'REPRONIM_LOGLEVEL': 'WARN'}):
            output = runner.run(["repronim", "--help"])
    except CommandError as e:
        raise AssertionError("'repronim --help' failed to start normally. "
                             "Exited with %d and output %s" % (e.code, (e.stdout, e.stderr)))
    return output

@ignore_nose_capturing_stdout
@assert_cwd_unchanged
def test_run_repronim_help():
    out, err = check_run_and_get_output("repronim --help")
    ok_startswith(out, "Usage: ")
    eq_(err, "")