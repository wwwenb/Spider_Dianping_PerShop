# coding=utf-8

import os
import re
import csv
import time

from save_file_utils import save_file_utils
from spider_config import spider_config
from request_utils import request_utils


class AddUserRank:
    def __init__(self):
        self.headers = {
            'User-Agent': spider_config.user_agent,
            'Cookie': spider_config.cookie,
            "Host": spider_config.host,
            "Accept": spider_config.accept,
            "Accept-Encoding": spider_config.accept_encoding
        }

        self.result_file = spider_config.result_add_user_rank

    def get_user_rank(self, url):
        print("爬取个人主页：" + str(url))
        r = None
        retry_count = 0
        while r is None and retry_count < 4:
            r = request_utils.get(url, headers=self.headers)
            if r is None:
                retry_count += 1
                if retry_count == 3:
                    print("重试3次还失败了，请验证后重试")
                    input()
                    retry_count = 0
                print("爬取失败，重试")
                time.sleep(3)
                continue



        save_file_utils.save_message("./tmp/user_info_page.html", r.text)

        user_rank = re.findall('<span title="" class="user-rank-rst urr-rank(.*?)"></span>', str(r.text))
        result = 0
        try:
            result = user_rank[0]
        except Exception as e:
            print(e)
            print("请验证后重试：" + str(url))
            input()
            return self.get_user_rank(url)

        return result

    def add_user_rank(self):
        with open(spider_config.result_file, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)

            start_count = 0
            if os.path.exists(spider_config.start_count_file):
                with open(spider_config.start_count_file, "r", encoding="utf-8") as f:
                    for line in f.readlines():
                        start_count = int(line.strip())
                        break

            i = -1
            for line in reader:
                i += 1
                if i < start_count:
                    continue

                if "匿名用户" == line[0] and line[17] != "":
                    line[17] = ""

                # 需要补齐用户等级
                if str(line[1]) == "0" and line[17] != "":
                    print(line)
                    time.sleep(4)
                    user_rank = self.get_user_rank(str(line[17]))
                    user_rank = float(user_rank) / 10
                    line[1] = str(user_rank)
                    print(line)

                save_file_utils.write_csv_row(spider_config.result_add_user_rank, line)
                save_file_utils.save_message(spider_config.start_count_file, str(i) + "\n")


if __name__ == "__main__":
    os.environ["http_proxy"] = "http://127.0.0.1:10809"
    os.environ["https_proxy"] = "http://127.0.0.1:10809"

    print("是否覆盖结果文件： 0 不覆盖 1 覆盖")
    mode = input().strip()

    if mode == "1" and os.path.exists(spider_config.result_add_user_rank):
        os.remove(spider_config.result_add_user_rank)

    AddUserRank().add_user_rank()