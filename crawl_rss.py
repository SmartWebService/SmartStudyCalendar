import feedparser
import ssl

urls = ("https://cs.kookmin.ac.kr/news/notice/rss", "http://www.rssground.com/services/facebook-rss/5da537e426be4/%EA%B5%AD%EB%AF%BC%EB%8C%80%ED%95%99%EA%B5%90%20%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4%EC%9C%B5%ED%95%A9%EB%8C%80%ED%95%99")
kmusw = "https://cs.kookmin.ac.kr/news/notice/rss"

def crawl_rss(url):
    d =  feedparser.parse("http://www.rssground.com/services/facebook-rss/5da537e426be4/%EA%B5%AD%EB%AF%BC%EB%8C%80%ED%95%99%EA%B5%90%20%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4%EC%9C%B5%ED%95%A9%EB%8C%80%ED%95%99")
    print(type(d))
    print(d.feed["title"])

    for e in d.entries :
        print("title = " + e.title )
        print("link = " + e.link )
        print("description = " + e.description )
        print("pubData = "+ str(e.published))


def main():
    for url in urls:
        crawl_rss(url)


def kmusw():
    kmusw = "https://cs.kookmin.ac.kr/news/notice/rss"
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    d =  feedparser.parse(kmusw)
    print(type(d))
    # print(d)
    # print(d.feed["title"])

    for e in d.entries :
        print("ss")
        print("title = " + e.title )
        print("link = " + e.link )
        print("description = " + e.description )
        print("pubData = "+ str(e.pubDate))

if __name__ == "__main__":
    # main()
    kmusw()


