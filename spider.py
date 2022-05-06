# coding=utf-8
import os
import re
import time
import random

from bs4 import BeautifulSoup
from logger_utils import logger_utils
from spider_config import spider_config
from request_utils import request_utils
from save_file_utils import save_file_utils


class Spider:
    def __init__(self):
        self.user_ids = []
        self.url = spider_config.url

        self.headers = {
            'User-Agent': spider_config.user_agent,
            'Cookie': spider_config.cookie,
            "Host": spider_config.host,
            "Accept": spider_config.accept,
            "Accept-Encoding": spider_config.accept_encoding
        }

        self.result_file = spider_config.result_file

        self.load_user_id()

    def load_user_id(self):
        if not os.path.exists(spider_config.user_id_file):
            return

        with open(spider_config.user_id_file, "r", encoding="utf-8") as f:
            for line in f.readlines():
                self.user_ids.append(line.strip())

    def get_css_content(self, html, url):
        # 获取保存字体信息的css链接
        css_links = re.search(r'<link rel="stylesheet" type="text/css" href="(//s3plus.meituan.net/v1/.*?.css)">', html)

        if css_links is None:
            logger_utils.error("获取css内容失败！请检查链接：%s" % url)
            print("验证完成后请输入任意字符继续")
            input()
            while True:
                print("是否更新一下内容？0 不更新 1 cookie 2 user-agent")
                ipt = input().strip()
                if ipt == "0":
                    break
                elif ipt == "1":
                    self.headers["Cookie"] = input().strip()
                elif ipt == "2":
                    self.headers["User-Agent"] = input().strip()
            return None, None

        css_link = "http:%s" % css_links.group(1)

        css_content = request_utils.get(css_link, headers=self.headers)

        return css_link, css_content.text

    def get_font_library(self, css_content, css_link):
        # 获取字体库链接
        svg_links = re.search(r'svgmtsi.*?(//s3plus.meituan.net/v1.*?svg)\);', css_content)

        if svg_links is None:
            logger_utils.error("查找字体库失败！请检查css链接:%s" % css_link)
            input()
            return None, None

        svg_link = "http:%s" % svg_links.group(1)

        svg_html = request_utils.get(svg_link, headers=self.headers)
        svg_text = svg_html.text

        save_file_utils.save_message("./tmp/svg.svg", svg_text)

        y_list = re.findall('<text x="0" y="(.*?)"', svg_text)
        text_list = re.findall('<text x="0" y=".*?">(.*?)</text>', svg_text)
        font_size = re.findall(r'font-size:(.*?)px;fill:#333;}', svg_text)[0]
        font_size = int(font_size)

        font_dict = {}
        for i in range(0, len(y_list)):
            for index, word in enumerate(text_list[i]):
                x = index * font_size
                y = int(y_list[i]) - 23
                font_dict["%s,%s" % (str(x), str(y))] = word

        return font_dict

    def get_user_rank(self, url):
        print("爬取个人主页：" + str(url))
        r = request_utils.get(url, headers=self.headers)
        page = BeautifulSoup(r.text, "html.parser")
        save_file_utils.save_message("./tmp/user_info_page.html", r.text)

        user_rank = re.findall('<span title="" class="user-rank-rst urr-rank(.*?)"></span>', str(r.text))
        result = 0
        try:
            result = user_rank[0]
        except Exception as e:
            print(e)
        return result

    def get_review_detail(self, review_url, html):
        page_review = BeautifulSoup(html, "html.parser")

        main_reviews = page_review.find_all("div", class_="main-review")
        user_photo_asides = page_review.find_all("a", class_="dper-photo-aside")

        for i, main_review in enumerate(main_reviews):
            reviews_info = []

            # 用户名
            user_name = main_review.find("div", class_="dper-info").text.strip()

            print("爬取用户: %s 的评论" % user_name)

            # 用户等级
            user_rank = 0
            user_url = ""
            try:
                sp = user_photo_asides[i]["href"].split("/")
                user_id = str(sp[2])
                if user_id in self.user_ids:
                    print("已存在，跳过： " + str(user_name) + "\n")
                    continue

                # time.sleep(4)
                user_url = "http://%s%s" % (spider_config.host, user_photo_asides[i]["href"])
                # while str(user_rank) == "0":
                #     user_rank = self.get_user_rank(user_url)
                #
                #     if str(user_rank) == "0":
                #         print("请前往验证：" + str(user_url) + "\n")
                #         print("请输入 0 已验证重新抓取 1 不验证继续\n")
                #         inp = input().strip()
                #         if inp == "0":
                #             continue
                #         elif inp == "1":
                #             break

                # user_rank = float(user_rank) / 10

                self.user_ids.append(user_id)
                save_file_utils.save_message(spider_config.user_id_file, user_id + "\n", mode="a")
            except Exception as e:
                print(e)

            print("user_rank: " + str(user_rank))

            # 发布时间
            review_time = main_review.find(class_="time")
            review_time = re.sub("\\s+", " ", review_time.text).strip()

            # 评论内容
            review_words = main_review.find("div", class_="review-words Hide")
            # 评论没有隐藏内容
            if review_words is None:
                review_words = main_review.find(class_="review-words").text
                review_words = review_words.strip()
            else:
                # 删除“收起评论”以及空白字符
                review_words = review_words.text.strip()[:-4].strip()

            # “喜欢的菜”数量，手机端是推荐的菜
            review_recommend_num = 0
            review_recommend = main_review.find("div", class_="review-recommend")
            if review_recommend is not None:
                a_recommend = review_recommend.find_all("a")
                review_recommend_num = len(a_recommend)

            # 评论总打分
            review_rank = main_review.find("div", class_="review-rank")
            score_star = re.findall('<span class="sml-rank-stars sml-str(.*?) star"></span>', str(review_rank))
            score_star = float(score_star[0]) / 10

            # 分维度评分，口味、环境、服务
            score_dim = [0, 0, 0]
            review_scores = review_rank.find_all("span", class_="item")
            for rs in review_scores:
                rs = re.sub("\\s+", "", rs.text).strip()
                sp = rs.split("：")
                if "口味" == sp[0]:
                    score_dim[0] = float(sp[1])
                elif "环境" == sp[0]:
                    score_dim[1] = float(sp[1])
                elif "服务" == sp[0]:
                    score_dim[2] = float(sp[1])

            # 点赞、回应、收藏数，手机端分别对应有帮助、评论和收藏
            num_prf = [0, 0, 0]
            actions_contents = main_review.find("span", class_="actions").contents
            i = -1
            for ac in actions_contents:
                if ac.name != "a" and ac.name != "em":
                    continue

                if ac.name == "a":
                    i += 1

                if ac.name == "em":
                    num_prf[i] = int(ac.text.strip()[1:-1])

                if i > 3:
                    break

            # 评论图片数
            picture_num = 0
            review_pictures = main_review.find(class_="review-pictures")
            if review_pictures is not None:
                a_num = review_pictures.find_all("a")
                picture_num = int(len(a_num))

            # 评论中”我们”，“我和”，“你”的数量
            num_keywords = [0, 0, 0]
            num_keywords[0] = int(review_words.count("我们"))
            num_keywords[1] = int(review_words.count("我和"))
            num_keywords[2] = int(review_words.count("你"))

            reviews_info.append([user_name, user_rank, review_time, score_star] + score_dim +
                                 [review_words, picture_num, review_recommend_num] + num_prf +
                                num_keywords + [review_url, user_url])
            save_file_utils.write_csv_rows(spider_config.result_file, reviews_info)

    def each_review_page(self, review_url):
        css_link, css_content = None, None
        # 获取css信息失败后，需要在浏览器验证后重新请求
        while css_content is None:
            r = request_utils.get(review_url, headers=self.headers)
            if r is None:
                continue
            html = r.text

            css_link, css_content = self.get_css_content(html, review_url)

        save_file_utils.save_message("./tmp/css.css", css_content)

        font_dict = self.get_font_library(css_content, css_link)

        # 将加密的字体替换成正常文字
        font_keys = re.findall('<svgmtsi class="(.*?)"></svgmtsi>', html)
        for fk in font_keys:
            pos_key = re.findall(r'.' + fk + '{background:-(.*?).0px -(.*?).0px;}', css_content)
            x = pos_key[0][0]
            y = pos_key[0][1]
            html = html.replace('<svgmtsi class="' + fk + '"></svgmtsi>', font_dict[x + ',' + y])

        save_file_utils.save_message("./tmp/page.html", html)

        self.get_review_detail(review_url, html)

    def each_shop_review(self, shop_url):
        all_review_url = "%s/%s" % (shop_url, "review_all")
        print("爬取：" + str(all_review_url))

        r = request_utils.get(all_review_url, headers=self.headers)
        save_file_utils.save_message("./tmp/all_reviews.html", r.text)
        page = BeautifulSoup(r.text, "html.parser")

        page_count = 0
        page_links = page.find_all("a", {"class": "PageLink"})

        # 获取店铺网页的页数
        for p in page_links:
            if str.isdigit(p.text):
                page_count = page_count if page_count > int(p.text) else int(p.text)

        print("review page count is: " + str(page_count))

        start_count = 1
        if os.path.exists(spider_config.start_count_file):
            with open(spider_config.start_count_file, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    start_count = int(line.strip())
                    break

        # 处理每个评论页
        for i in range(start_count, page_count + 1):
            review_url = "%s/%s" % (all_review_url, "p" + str(i))

            print("爬取网页: %s" % review_url)
            time.sleep(5 + random.randint(2, 4))

            self.each_review_page(review_url)
            save_file_utils.save_message(spider_config.start_count_file, str(i))

    def spider(self):
        self.each_shop_review(self.url)


if __name__ == "__main__":
    os.environ["http_proxy"] = "http://127.0.0.1:10809"
    os.environ["https_proxy"] = "http://127.0.0.1:10809"

    print("是否覆盖结果文件： 0 不覆盖 1 覆盖")
    mode = input().strip()

    if mode == "1" and os.path.exists(spider_config.result_file):
        os.remove(spider_config.result_file)
        if os.path.exists(spider_config.user_id_file):
            os.remove(spider_config.user_id_file)

        # 在开头写入utf-8编码的bom，防止excel双击打开时乱码
        csv_titles = ['\ufeff' + "用户id", "用户等级", "发布时间", "打分", "口味评分",
                      "环境评分", "服务评分", "评论", "图片数量", "推荐菜品数量", "有帮助数量",
                      "评论数量", "收藏数量", "评论中”我们“的数量", "评论中“我和”的数量",
                      "评论中“你”的数量", "评论页", "个人主页"]

        save_file_utils.write_csv_row(spider_config.result_file, csv_titles)

    save_file_utils.mkdir("./tmp")

    Spider().spider()
