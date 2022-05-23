from environment import OWNER_ID, ALIVE_NAME
from jmthon import jmthon

USERID = jmthon.uid if OWNER_ID == 0 else OWNER_ID
hmention = f"<a href = tg://user?id={USERID}>{ALIVE_NAME}</a>"
