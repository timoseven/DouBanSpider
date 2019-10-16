import requests
import configparser

cp = ConfigParser.SafeConfigParser()
cp.read('.password')

loginurl = 'https://accounts.douban.com/login'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
data = {
    'source':'index_nav',
    'redir':'https://www.douban.com/',
    'form_email':'xxxx',
    'form_password':'xxxx',
    'login':'登录'
}
login_response = requests.post(url=loginurl,headers=headers)
print(login_response.text)
