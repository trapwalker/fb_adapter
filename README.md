fb_adapter
==========

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

http://github.com/sergyp/fb_adapter/