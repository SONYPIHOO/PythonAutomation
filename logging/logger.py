#Levels of logging
# 1. notset (level code - 0)
# 2. debug (level code - 10) - it is purly for devlopper
# 3. info (level code - 20)
# 4. warnings (level code - 30)
# 5.error (level code - 40)
# 6. critical (level code - 50)

import logging
logging.basicConfig(level=logging.CRITICAL)
#default level is set to warning (code-30)
logging.debug("This is debug logger")
logging.info("This is info logger")
logging.warning("This is warning logger")
logging.error("This is error logger")
logging.critical("This is critical logger")

