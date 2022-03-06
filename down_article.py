import urllib.request
from parsel import Selector
page = 0
while page != 68:
    page += 1
    print('['+str(page)+']')
    src_html = open('page-'+str(page)+'.html').read()
    selector = Selector(src_html)
    links = selector.css('.item-title > a::attr(href)').getall()


    for link in links :
        print(str(link)+' …')
        article = urllib.request.urlopen(link).read().decode('utf8', 'ignore')

        #selector = Selector(article)
        #title = selector.css('.entry-title::text').get()
        #print(title)

        #pubdate = selector.css('::attr(datetime)').get()
        #print(pubdate)

        #content = selector.css('.entry-content').get()
        #print(content)


        f = open('./'+link.replace('https://laod.cn/', ''), 'w')
        f.write(article)
        f.close()
