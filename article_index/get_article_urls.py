from parsel import Selector
page = 0
link_list = ''

while page != 68:
  page += 1
  print('['+str(page)+']')
  src_html = open('page-'+str(page)+'.html').read()
  selector = Selector(src_html)
  links = selector.css('.item-title > a::attr(href)').getall()
  
  for link in links:
    link = link + '\n'
    link_list = link_list + link
f = open('urls.txt', 'w')
f.write(link_list)
f.close()
