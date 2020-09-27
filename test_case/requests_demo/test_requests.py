import allure
import requests
# def test_no_params():
#     # r=requests.get("https://www.baidu.com/")
#     sess = requests.session()
#     r = sess.request(method='get',url='https://www.baidu.com/')
#     r = sess.request(method='get', url='https://www.baidu.com/')
#     print(r.text)
@allure.feature('get请求')
@allure.story('有参数')
@allure.title('用例名1')
def test_get_params(pub_data):
    s = {"token":pub_data["token"]}
    ph = {'phone':'13245626037'}
    a = requests.request('GET','http://qa.yansl.com:8084/cst/getCustomer',params=ph,headers=s)
    print(a.text)

@allure.feature('get请求')
@allure.story('下载文件')
@allure.title('用例名2')
def test_get_file(pub_data):
    p = {'pridCode':'63803y'}
    h = {'token':pub_data['token']}
    r = requests.request('GET','http://qa.yansl.com:8084/product/downProdRepertory',params=p,headers=h)
    with open('aa.xls','wb') as f:
        f.write(r.content)


@allure.feature('post请求')
@allure.story('有参数')
@allure.title('用例名3')
def test_post_json():
    data = {'pwd':'abc123','userName':'tuu653'}
    r = requests.post('http://qa.yansl.com:8084/login',json=data)
    print(r.text)

@allure.feature('post请求')
@allure.story('有参数')
@allure.title('用例名4')
def test_post_formdata(pub_data):
    data = {'userName':'tan242743'}
    h = {'token':pub_data['token']}
    r = requests.post('http://qa.yansl.com:8084/user/lock',data=data,headers=h)
    print(r.text)


@allure.feature('post请求')
@allure.story('下载文件')
@allure.title('用例名5')
def test_post_upload_file(pub_data):
    data = {'file':open('aa.xls','rb')}
    h = {'token':pub_data['token']}
    r = requests.post('http://qa.yansl.com:8084/product/uploaprodRepertory',files=data,headers=h)
    print(r.text)






