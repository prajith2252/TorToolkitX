import os

from ..config.ExecVarsSample import ExecVars

dburl = os.environ.get("DATABASE_URI", None)
if dburl is None:
    dburl = ExecVars.DATABASE_URI


if "mongo" in dburl:
    pass
else:
    pass
