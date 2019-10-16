import requests
import configparser

cp = configparser.SafeConfigParser()
cp.read('.passwd')
un=cp.get('douban', 'username')
pw=cp.get('douban', 'password')

loginurl = 'https://accounts.douban.com/login'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
data = {
    'source':'index_nav',
    'redir':'https://www.douban.com/',
    'form_email':"un",
    'form_password':"pw",
    'login':'登录'
}
login_response = requests.post(url=loginurl,headers=headers)
print(login_response.text)
