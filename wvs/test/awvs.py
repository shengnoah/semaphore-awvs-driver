class AWVS:
    def __init__(self, domain):
		self.flg = True
		self.domain = domain

    def send(self, level):
		return 5
	
    def login(param):
        import urllib2
        import ssl
        import json
        ssl._create_default_https_context = ssl._create_unverified_context
        url_login="https://localhost:3443/api/v1/me/login"
        
        send_headers_login={
                'Host': 'localhost:3443',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json;charset=utf-8'
                }
        data_login='{"email":"","password":"","remember_me":false}'
        req_login = urllib2.Request(url_login,headers=send_headers_login)
        response_login = urllib2.urlopen(req_login,data_login)
        xauth = response_login.headers['X-Auth']
        COOOOOOOOkie = response_login.headers['Set-Cookie']
        print COOOOOOOOkie,xauth
        return True

    def addTagert(param):
        url="https://localhost:3443/api/v1/targets"
        urllist=open('list.txt','r')
        formaturl=urllist.readlines()
        send_headers2={ 
        'Host':'servers:3443',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type':'application/json;charset=utf-8',
        'X-Auth':xauth,
        'Cookie':COOOOOOOOkie,
        }
        
        try:
            for i in formaturl:
                target_url='http://'+i.strip()
                data='{"description":"222","address":"'+target_url+'","criticality":"10"}'
                req = urllib2.Request(url,headers=send_headers2)
                response = urllib2.urlopen(req,data)
                jo=eval(response.read())
                target_id=jo['target_id']
            
         
            url_scan="https://localhost:3443/api/v1/scans"
            headers_scan={
           'Host': 'localhost:3443',
           'Accept': 'application/json, text/plain, */*',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate, br',
           'Content-Type': 'application/json;charset=utf-8',
           'X-Auth':xauth,
           'Cookie':COOOOOOOOkie,
            }
            data_scan='{"target_id":'+'\"'+target_id+'\"'+',"profile_id":"11111111-1111-1111-1111-111111111111","schedule":{"disable":false,"start_date":null,"time_sensitive":false},"ui_session_id":"66666666666666666666666666666666"}'
            req_scan=urllib2.Request(url_scan,headers=headers_scan)
            response_scan=urllib2.urlopen(req_scan,data_scan)
            print response_scan.read()
            
        except Exception,e:
            print e
        return True
