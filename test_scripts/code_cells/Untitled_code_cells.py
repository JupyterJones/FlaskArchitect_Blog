from logger_settings import api_logger
message = "hello world"
new_message = message.upper()
api_logger.info(new_message)

from logger_settings import api_logger

api_logger.info('hello world')

!cat logs/api.log

import random
printme = random.choice(["On {date}, {user} did la-dee-dah. ",
                         "{User} did la-dee-dah on {date}. "
                         ])
x="jack"
y = "today"
output1 = printme.format(user=x, date=y, User=x.upper())
print(output1)
output = printme.format(user=x, date=y, User=x.title())
output
api_logger.info(output)





