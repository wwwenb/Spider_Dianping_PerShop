
# 爬虫初始配置信息
class Config():

    def __init__(self):
        # 指定店家的url
        self.url = "http://www.dianping.com/shop/k3TAjojLVtokbIve"

        # chrome
        # self.cookie = "fspop=test; _lxsdk_cuid=17a0969dff0c8-0388ad2d3cb4a6-f7f1939-100200-17a0969dff1c8; _hc.v=b3171166-89e9-cfd3-0f8e-a0095a8e05a1.1623655573; s_ViewType=10; cy=3; cye=hangzhou; ua=dpuser_6185476995; ctu=2a2e1c4a49e422ece1e1b02dd418c7bdf50c02237fddb9a24f10519d325bdd4b; cityid=7; default_ab=shopreviewlist:A:1; uuid=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; iuuid=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; _lxsdk=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; _ga=GA1.2.570212981.1623985393; dplet=7b726db2fc4478d77327421678eb5e74; dper=c0f11e2ea064e9dae1103763a4c8446659960d2afef26c88d84d44d456b16e190682524a3230c681ab7cdc2f2b1112bd0647f2e6b9616ea6e5b4750b4984878c11750a7546f534f1f2a2f7c58e85d52e6b602f15a72f2c3e9be68edf23908706; ll=7fd06e815b796be3df069dec7836c3df; _lx_utm=utm_source=google&utm_medium=organic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1624070266,1624095737,1624101954,1624102009; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1624103876; _lxsdk_s=17a23e4227c-84c-345-f26||582"
        # self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

        # edge
        self.cookie = 'fspop=test; _lxsdk_cuid=1808f321848c8-0cd58583209bf2-49647e56-100200-1808f321848c8; _lxsdk=1808f321848c8-0cd58583209bf2-49647e56-100200-1808f321848c8; _hc.v=6e183f6c-d29b-4fb0-ff59-5a7dfe1f710c.1651669867; dplet=69a476a5163f6a321a98aa479058ec13; dper=90a35ab05d6bda7f4fa184c21ab998f323e7caff66b3f768116f273ec5dd72288aa3b695759de0bbcf0dc856cb28b9476b9c88d699c0febb92b346e1c2b5e3aabe55a647afddfac0fc65551ab49c55b08f89b57aa6aa0cde1b14cfde817340e9; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_6185476995; ctu=2a2e1c4a49e422ece1e1b02dd418c7bd86183f800f3adb56084a41fd3207247a; cy=3; cye=hangzhou; s_ViewType=10; WEBDFPID=wy46830w9wxy58381v5xy9888y17201w81905w1uy9z97958z500y6xv-1651851089747; _lxsdk_s=18094d81da0-338-8d8-8b0||504'
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"
        self.accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        self.accept_encoding = "gzip, deflate"
        self.cache_control = "max-age=0"

        self.host = "www.dianping.com"

        self.result_file = "./result.csv"
        self.result_add_user_rank = "./result_add_user_rank.csv"
        self.user_id_file = "./tmp/user_id.txt"
        self.start_count_file = "./tmp/start_count.txt"


spider_config = Config()