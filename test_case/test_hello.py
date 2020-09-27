import random

import pytest

from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''


# def test_aaa(pub_data):
#     print(pub_data)

@pytest.mark.otto
def test_signup(pub_data):
    pub_data['username'] = '自动生成 字符串 1,6 数字 chen'
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "注册成功"  # 预期结果
    json_data = '''{
  "phone": "自动生成 手机号",
  "pwd": "aaa123",
  "rePwd": "aaa123",
  "userName": "${username}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)

@pytest.mark.otto
def test_login(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "登录成功"  # 预期结果
    json_data = '''{
  "pwd": "aaa123",
  "userName": "${username}"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token": "$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path, method=method, url=uri, pub_data=pub_data, status_code=status_code,
                             headers=headers, expect=expect, feature=feature, story=story, title=title,
                             json_data=json_data)

@pytest.mark.otto
def test_changepwd(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '修改密码'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/changepwd"  # 接口地址
    headers = {"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data = '''{
  "newPwd": "bbb123",
  "oldPwd": "aaa123",
  "reNewPwd": "bbb123",
  "userName": "${username}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)

@pytest.mark.otto
def test_validatelogon(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '登录验证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "登录成功"  # 预期结果
    json_data = '''{
  "pwd": "bbb123",
  "userName": "${username}"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token": "$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path, method=method, url=uri, pub_data=pub_data, status_code=status_code,
                             headers=headers, expect=expect, feature=feature, story=story, title=title,
                             json_data=json_data)

@pytest.mark.otto
def test_lock(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '冻结用户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/lock"  # 接口地址
    headers = {"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = "冻结成功"  # 预期结果
    data = {'userName': '${username}'}

    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token": "$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, data=data)

@pytest.mark.otto
def test_relogin(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '登录不可用验证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "登录失败,帐号被冻结"  # 预期结果
    json_data = '''{
  "pwd": "bbb123",
  "userName": "${username}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)

@pytest.mark.otto
def test_unLock(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '解冻用户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/unLock"  # 接口地址
    headers = {"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = "解冻成功"  # 预期结果
    data = {'userName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, data=data)

@pytest.mark.otto
def test_relogintwo(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '登录可用验证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data = '''{
  "pwd": "bbb123",
  "userName": "${username}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)

@pytest.mark.otto
def test_recharge(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "充值成功;账户余额10000000分"  # 预期结果
    json_data = '''{
  "accountName": "${username}",
  "changeMoney": 10000000
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)

@pytest.mark.otto
def test_getAccInfo(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询单个账户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params = {'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, params=params)

@pytest.mark.otto
def test_getBills(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询用户流水'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params = {'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, params=params)

@pytest.mark.otto
def test_charge(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '扣款'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data = '''{
  "accountName": "${username}",
  "changeMoney": "自动生成 数字 20,80"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)

@pytest.mark.otto
def test_getAccInfoTWO(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询单个账户2'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params = {'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, params=params)

@pytest.mark.otto
def test_getBillstwo(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询用户流水2'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params = {'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, params=params)


@pytest.mark.otto
def test_withdraw(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data = '''{
  "accountName": "${username}",
  "cardNo": "自动生成 字符串 17 数字 6",
  "changeMoney": "自动生成 数字 100,20000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)


def test_getAccInfothree(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询单个账户3'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params = {'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, params=params)


def test_getBillsthree(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询用户流水3'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params = {'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, params=params)


def test_accLock(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户冻结'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accLock"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data = {'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, data=data)


def test_rechargetwo(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '验证可否充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "该账户正处在冻结状态，无法充值"  # 预期结果
    json_data = '''{
  "accountName": "${username}",
  "changeMoney": 10000000
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)


def test_charge(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '验证扣款'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data = '''{
  "accountName": "${username}",
  "changeMoney": "自动生成 数字 20,80"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)


def test_accUnLock(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户解冻'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accUnLock"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data = {'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, data=data)


def test_rechargethree(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '验证可否充值3'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data = '''{
  "accountName": "${username}",
  "changeMoney": 10000000
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)


def test_withdrawthree(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户提现测试'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data = '''{
  "accountName": "${username}",
  "cardNo": "自动生成 字符串 17 数字 6",
  "changeMoney": "自动生成 数字 100,20000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)
