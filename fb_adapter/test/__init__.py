import os
import sys
import unittest

here = os.path.dirname(__file__)
loader = unittest.defaultTestLoader

def suite():
    suite = unittest.TestSuite()
    for fn in os.listdir(here):
        if fn.startswith("test") and fn.endswith(".py"):
            modname = fn[:-3]
            print '---------', modname
            __import__(modname, level=0)
            module = sys.modules[modname]
            suite.addTest(loader.loadTestsFromModule(module))
    return suite

