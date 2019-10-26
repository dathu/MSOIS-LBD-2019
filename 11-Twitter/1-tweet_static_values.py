#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = " Temprature Exceeds turn on Fan Buddy!"

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey =  'v8rxhrmuJ1PcBdPci5h9lSeoz'
apiSecret = '9sIBEMj5tgfIkLFwlq5twNPqnGa0hemN4UbSO9XbPqz7kbh883'
accessToken =  '927831224944435201-O7POC0moUMz8OEe4FhZQiw3vnKCZLed'
accessTokenSecret = 'LCU8sUfyoXEDuRRBH8yUaPFBQBqcg7Z8c4tWKznVvn0dD'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
