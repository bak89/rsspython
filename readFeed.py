import requests
import xmltodict
import time

from tinydb import TinyDB

RSS_FEED_URL = "http://feeds.bbci.co.uk/news/world/rss.xml"

db_path="news_{}.json".format(int(time.time()))
print("Fetching news from BBC News...")

rss_content = requests.get(RSS_FEED_URL).text
parsed_feed = xmltodict.parse(rss_content)

print('Found %d items in RSS feed.' % (len(parsed_feed['rss']['channel']['item'])))

db = TinyDB(db_path)
for item in parsed_feed['rss']['channel']['item']:
    db.insert(item)

print('Stored %d items in DB.' % (len(parsed_feed['rss']['channel']['item'])))
print("First item:\n")
print(db.get(doc_id=1))
