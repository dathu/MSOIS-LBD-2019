import urllib.request as urllib2
READ_API_KEY='1KRJLOAVLOO35BOI'
CHANNEL_ID='890424'

def main():

    #Enable any one, one-by-one
    

    #Read a Channel Field
    #http://api.thingspeak.com/channels/CHANNEL_ID/fields/filed_ID.FORMAT?api_key=CHANNEL_READ_API_KEY&results=NUMBER_OF_ENTRY_REQ
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/fields/1.json?api_key=%s&results=100"%(CHANNEL_ID,READ_API_KEY))
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/fields/2.xml?api_key=%s&results=100"%(CHANNEL_ID,READ_API_KEY))
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/fields/2.csv?api_key=%s&results=100"%(CHANNEL_ID,READ_API_KEY))

    #Read a Channel Feeds
    #http://api.thingspeak.com/channels/CHANNEL_ID/feeds.json?api_key=CHANNEL_READ_API_KEY&results=NUMBER_OF_ENTRY_REQ
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/872678/feeds.json?api_key=QV1JCIN57IYG7HQ0&results=20")
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/872678/feeds.xml?api_key=QV1JCIN57IYG7HQ0&results=20")
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/890424/feeds.csv?api_key=1KRJLOAVLOO35BOI&results=20")

    #Read a Channel status Update
    #https://api.thingspeak.com/channels/CHANNEL_ID/status.json?api_key=CHANNEL_READ_API_KEY&results=NUMBER_OF_ENTRY_REQ
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/872678/status.json?api_key=QV1JCIN57IYG7HQ0&results=20")
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/872678/status.xml?api_key=QV1JCIN57IYG7HQ0&results=20")
    #conn = urllib2.urlopen("http://api.thingspeak.com/channels/872678/status.csv?api_key=QV1JCIN57IYG7HQ0&results=20")

    response = conn.read()
    print("---------------------------")
    print(response)
    print("###############################")
    print("http status code=%s" % (conn.getcode()))
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    conn.close()


if __name__ == '__main__':
    main()
