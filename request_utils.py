import sys
import requests

from logger_utils import logger_utils


class RequestUtils:

    def __init__(self):
        pass

    def get(self, url, headers):
        # print(url)
        r = None
        try:
            r = requests.get(url, headers=headers)

            # 需要验证
            while r is None or "验证中心" in r.text or "页面不存在" in r.text or r.status_code != 200:
                logger_utils.warning("请复制连接 %s 到浏览器进行验证" % url)
                input()
                r = requests.get(url, headers=headers)
        except Exception as e:
            print(e)
            logger_utils.error("%s 网络连接失败！" % url)

        if r and r.status_code != 200:
            logger_utils.error("响应码不是200")
            print(r.status_code)
            print(r.content)

        return r


request_utils = RequestUtils()
