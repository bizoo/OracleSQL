# Oracle utilities functions


def find_entities(view):
    """
    Return all 'create or replace' type and name in the script.
    """
    results = []
    positions = view.find_all(r'(?im)create\s+(?:or\s+replace\s+)?(?:force\s+)?(package(?:\s+body)?|procedure|function|trigger|view|type)\s+(\w+\.)?(\w+)', 0, "$1 $3", results)
    return dict((val.upper(), view.rowcol(pos.begin())[0]) for (pos, val) in zip(positions, results))


def find_body(view):
    """
    Find first package body declaration.
    """
    return view.find(r'(?im)create\s+(or\s+replace\s+)?package\s+body\s+', 0)
