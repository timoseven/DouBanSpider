#-*- coding: UTF-8 -*-

import sys
import time
import urllib
import urllib.parse
import requests
import numpy as np
from bs4 import BeautifulSoup
from openpyxl import Workbook
from imp import reload
import re

reload(sys)
#sys.setdefaultencoding('utf8')



#Some User Agents
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}]


def douban_login():
    loginurl = 'https://accounts.douban.com/login'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    login_response = requests.get(url=loginurl,headers=headers)#获取登录界面的信息
    
    verifyCodeUrl = re.compile('<img id="captcha_image" src="(.*?)"',re.S).findall(login_response.text)[0]#通过正则拿到图片的url
    captcha_id = re.compile('id=(.*?)&',re.S).findall(verifyCodeUrl)[0]#获取表单中的url字段，同样用正则匹配
    verifyCodeResponse = requests.get(url=verifyCodeUrl,headers=headers)#获取验证码图片
    
    with open('im_code.jpg','wb') as f:
        f.write(verifyCodeResponse.content)#保存验证码
        f.close()
    captcha_solution = input("请输入验证码:")
    datas = {
        'source':'index_nav',
        'redir':'https://www.douban.com/',
        'form_email':'xxx',
        'form_password':'xxx',
        'captcha-solution':captcha_solution,
        'captcha-id':captcha_id,
        'login':'登录'
    }
    LoginPost = requests.post(url=loginurl,data=datas,headers=headers)


def book_spider(book_tag):
    page_num=0;
    book_list=[]
    try_times=0
    
    while(1):
        #url='http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/book?start=0' # For Test
        url='http://www.douban.com/tag/'+urllib.parse.quote(book_tag)+'/book?start='+str(page_num*15)
        time.sleep(np.random.rand()*5)
        
        #Last Version
        try:
            req = urllib.request.Request(url, headers=hds[page_num%len(hds)])
            req.add_header('Cookie', 'bid=dLa8VKz62II; gr_user_id=7252e962-4dec-4193-9a11-f6f15041afe1; _vwo_uuid_v2=DD190F064E7A6F013BED8DF723175DEB3|468e82a1cae5558df9d058e0071963ad; ll="108288"; douban-fav-remind=1; push_noty_num=0; push_doumail_num=0; \
                           douban-profile-remind=1; _ga=GA1.2.467025163.1555687286; __utmc=30149280; __utmv=30149280.203; viewed="6025290_26304954_4864832_26304087_26695174_4163938_1064223_1291204_6749832_6853203"; \
                           __utmz=30149280.1571151034.38.10.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; ap_v=0,6.0; \
                           _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1571193624%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fwww.douban.com%252Ftag%252FLinux%252Fbook%253Fstart%253D0%22%5D; _pk_ses.100001.8cb4=*; \
                           __utma=30149280.467025163.1555687286.1571191561.1571193625.40; dbcl2="2036823:uJUUjmrY0ZM"; ck=-4gZ; __utmt=1; _pk_id.100001.8cb4=768ff796c14c20f8.1563711055.25.1571194500.1571191560.; __utmb=30149280.8.10.1571193625')
            source_code = urllib.request.urlopen(req).read()
            plain_text=str(source_code)   
        except (urllib.request.HTTPError, urllib.request.URLError) as e:
            print (e)
            continue
  
        ##Previous Version, IP is easy to be Forbidden
        #source_code = requests.get(url) 
        #plain_text = source_code.text  
        
        soup = BeautifulSoup(plain_text, "html.parser")
        list_soup = soup.find('div', {'class': 'mod book-list'})
        
        try_times+=1;
        if list_soup==None and try_times<200:
            continue
        elif list_soup==None or len(list_soup)<=1:
            break # Break when no informatoin got after 200 times requesting
        
        for book_info in list_soup.findAll('dd'):
            title = book_info.find('a', {'class':'title'}).string.strip()
            desc = book_info.find('div', {'class':'desc'}).string.strip()
            desc_list = desc.split('/')
            book_url = book_info.find('a', {'class':'title'}).get('href')
            
            try:
                author_info = '作者/译者： ' + '/'.join(desc_list[0:-3])
            except:
                author_info ='作者/译者： 暂无'
            try:
                pub_info = '出版信息： ' + '/'.join(desc_list[-3:])
            except:
                pub_info = '出版信息： 暂无'
            try:
                rating = book_info.find('span', {'class':'rating_nums'}).string.strip()
            except:
                rating='0.0'
            try:
                #people_num = book_info.findAll('span')[2].string.strip()
                people_num = get_people_num(book_url)
                people_num = people_num.strip('人评价')
            except:
                people_num ='0'
            
            book_list.append([title,rating,people_num,author_info,pub_info])
            try_times=0 #set 0 when got valid information
        page_num+=1
        print ('Downloading Information From Page %d' % page_num)
#        print (type(book_list))
    return book_list


def get_people_num(url):
    #url='http://book.douban.com/subject/6082808/?from=tag_all' # For Test
    try:
        req = urllib.request.Request(url, headers=hds[np.random.randint(0,len(hds))])
        source_code = urllib.request.urlopen(req).read()
        plain_text=str(source_code)   
    except (urllib.request.HTTPError, urllib.request.URLError) as e:
        print (e)
    soup = BeautifulSoup(plain_text, "html.parser")
    people_num=soup.find('div',{'class':'rating_sum'}).findAll('span')[1].string.strip()
    return people_num


def do_spider(book_tag_lists):
    book_lists=[]
    for book_tag in book_tag_lists:
        book_list=book_spider(book_tag)
        book_list=sorted(book_list,key=lambda x:x[1],reverse=True)
        book_lists.append(book_list)
    return book_lists


def print_book_lists_excel(book_lists,book_tag_lists):
    wb=Workbook(write_only = True)
    ws=[]
    for i in range(len(book_tag_lists)):
        print(type(book_tag_lists[i]))
        ws.append(wb.create_sheet(title=book_tag_lists[i].encode('utf-8').decode('unicode_escape'))) #utf8->unicode
    for i in range(len(book_tag_lists)): 
        ws[i].append(['序号','书名','评分','评价人数','作者','出版社'])
        count=1
        for bl in book_lists[i]:
            ws[i].append([count,bl[0],float(bl[1]),int(bl[2]),bl[3],bl[4]])
            count+=1
    save_path='book_list'
    for i in range(len(book_tag_lists)):
        save_path+=('-'+book_tag_lists[i].encode('utf-8').decode('unicode_escape'))
    save_path+='.xlsx'
    wb.save(save_path)




if __name__=='__main__':
    #book_tag_lists = ['心理','判断与决策','算法','数据结构','经济','历史']
    #book_tag_lists = ['传记','哲学','编程','创业','理财','社会学','佛教']
    #book_tag_lists = ['思想','科技','科学','web','股票','爱情','两性']
    #book_tag_lists = ['计算机','机器学习','linux','android','数据库','互联网']
    #book_tag_lists = ['数学']
    #book_tag_lists = ['摄影','设计','音乐','旅行','教育','成长','情感','育儿','健康','养生']
    #book_tag_lists = ['商业','理财','管理']  
    #book_tag_lists = ['名著']
    #book_tag_lists = ['科普','经典','生活','心灵','文学']
    #book_tag_lists = ['科幻','思维','金融']
    #book_tag_lists = ['个人管理','时间管理','投资','文化','宗教']
    book_tag_lists = ['linux']
    book_lists=do_spider(book_tag_lists)
    print_book_lists_excel(book_lists,book_tag_lists)
    
