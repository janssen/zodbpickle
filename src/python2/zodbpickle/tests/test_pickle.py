import unittest

class TestImportability(unittest.TestCase):

    def test_Pickler(self):
        from zodbpickle.pickle import Pickler

    def test_Unpickler(self):
        from zodbpickle.pickle import Unpickler

    def test_load(self):
        from zodbpickle.pickle import load

    def test_loads(self):
        from zodbpickle.pickle import load

    def test_dump(self):
        from zodbpickle.pickle import dumps

    def test_dumps(self):
        from zodbpickle.pickle import dumps


def test_suite():
    import sys
    from .test_pickle_2 import test_suite
    return unittest.TestSuite((
        test_suite(),
        unittest.makeSuite(TestImportability),
    ))
