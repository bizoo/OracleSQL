=========================================================
Sublime Text 2 plackage for editing Oracle SQL and PL/SQL 
=========================================================

Language definition and execution utilities for Oracle PL/SQL files.

It is based on the bundle http://code.google.com/p/oracle-textmate-bundle/ 

Build
-----

To execute your PL/SQL source on your schema with ST2 Build command, you have to create a .sublime-build in your ST2 user folder file containing something like::

    {
        "target": "oracle_exec",
        "selector": "source.plsql.oracle",
        "variants":
        [
            {
                "name": "SCHEMA 1",
                "dsn": "USERNAME/PASSWORD@SCHEMANAME1"
            },
            {
                "name": "SCHEMA 2",
                "dsn": "USERNAME/PASSWORD@SCHEMANAME2"
            }
        ]
    }

