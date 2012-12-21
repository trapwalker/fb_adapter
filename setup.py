#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" 
fb_adapter package is adapter for different Firebird RDBMS bindings (python).
    It works on Python 2.5+ (not include Python 3.x).
    Now supported bindings:
    - kinterbasdb
    - firebirdsql
    
    import fb_adapter
    with fb_adapter.connectCtx(uri='firebird://alice:secret@localhost:3050//foo/bar.fdb?charset=utf-8') as conn:
    cur = conn.cursor()
        cur.execute("select * from baz")
    
        for c in cur.itermap():
            print(c)
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import fb_adapter


classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(name='fb_adapter', 
        version=fb_adapter.__version__,
        description = 'Adapter to Firebird RDBMS bindings for python.', 
        url='http://github.com/sergyp/fb_adapter',
        classifiers=classifiers,
        keywords=['Firebird', 'kinterbasdb', 'firebirdsql', 'adapter', 'binding',],
        license='BSD',                                        
        author='Sergey Pankoff',
        author_email='svpmailbox@gmail.com',
        packages = ['fb_adapter'],
        long_description=__doc__,
)
