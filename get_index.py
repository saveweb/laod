import urllib.request
import urllib.parse
from parsel import Selector

page = 0
api = 'https://laod.cn/wp-admin/admin-ajax.php'
end_flag = 0

while end_flag != 1:
    page += 1
    print(page)
    post = {
        "action": "wpcom_load_posts",
        "page": page,
        "type": "default",
        "exclude": ""
    }
    post = urllib.parse.urlencode(post).encode('utf8')
    request = urllib.request.Request(api, post)
    reponse = urllib.request.urlopen(request).read().decode('utf8', 'ignore')

    if len(str(reponse)) <= 5:
        end_flag = 1
        print('End!')
    else:
            f = open('./page-'+str(page)+'.html','w')
            f.write(reponse)
            f.close()
