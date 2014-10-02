import urllib2
 
FEED_URL = 'https://mail.google.com/mail/feed/atom'
 
def get_unread_msgs(user, passwd):
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='New mail feed',
        uri='https://mail.google.com',
        user='{user}@gmail.com'.format(user=user),
        passwd=passwd
    )
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed = urllib2.urlopen(FEED_URL)
    return feed.read()
 
##########
 
if __name__ == "__main__":
    import getpass
 
    user = 'jonahjun.wu'
    passwd ='2xuiuiji' 
    print get_unread_msgs(user, passwd)

    import untangle    # sudo pip install untangle
     
    xml = get_unread_msgs(user, passwd)
    print xml
    o = untangle.parse(xml)
    try:
        for e in o.feed.entry:
            title = e.title.cdata
            print e.title.cdata
            print e.summary.cdata
            print e.modified.cdata
            print e.author.name.cdata
            print e.author.email.cdata
            print '-----------------------------------'
    except IndexError:
        pass    # no new mail


