import unittest
import requests
import json
import sys
sys.path.append("../..")   # 统一将包的搜索路径提升到项目根目录下

from lib.read_excel import *
from lib.case_log import log_case_info
from config.config import *

class BaseCaseToken(unittest.TestCase):   # 继承unittest.TestCase
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), cls.__name__)

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):
        headers = {}
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        url2 = case_data.get('url2')
        token = requests.post(url=url2).json().get("token")
        headers["token"] = token
        args = case_data.get('data')
        expect_res = case_data.get('expect_res')
        data_type = case_data.get('data_type')

        if data_type.upper() == 'FORM':   # 表单格式请求
            res = requests.post(url=url, data=json.loads(args), headers=headers)
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertIn( expect_res, res.text)
        else:
            res = requests.post(url=url, json=json.loads(args), headers=headers)   # JSON格式请求
            log_case_info(case_name, url, args, json.dumps(json.loads(expect_res), sort_keys=True),
                          json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
            self.assertIn(json.loads(expect_res), res.json())
