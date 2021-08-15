import os

from ..config.ExecVarsSample import ExecVars

dburl = os.environ.get("DATABASE_URL", None)
if dburl is None:
    dburl = ExecVars.DATABASE_URL


if "mongo" in dburl:
    pass
else:
    pass
