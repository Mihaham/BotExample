import asyncio
from bot import main

#pyinstaller --onefile
# --hidden-import=asyncio
# --hidden-import=logging
# --hidden-import=time
# --hidden-import=apiclient
# --hidden-import=httplib2
# --hidden-import=oauth2client
# --hidden-import=pillow
# --hidden-import=pathlib
# --hidden-import=sys
# --hidden-import=aiogram
# --hidden-import=pyffmpeg
# --hidden-import=asyncio
# main.py

if __name__ == "__main__":
    asyncio.run(main())