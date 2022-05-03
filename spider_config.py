
# 爬虫初始配置信息
class Config():

    def __init__(self):
        # 指定店家的url
        self.url = "http://www.dianping.com/shop/k3TAjojLVtokbIve"

        # chrome
        # self.cookie = "fspop=test; _lxsdk_cuid=17a0969dff0c8-0388ad2d3cb4a6-f7f1939-100200-17a0969dff1c8; _hc.v=b3171166-89e9-cfd3-0f8e-a0095a8e05a1.1623655573; s_ViewType=10; cy=3; cye=hangzhou; ua=dpuser_6185476995; ctu=2a2e1c4a49e422ece1e1b02dd418c7bdf50c02237fddb9a24f10519d325bdd4b; cityid=7; default_ab=shopreviewlist:A:1; uuid=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; iuuid=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; _lxsdk=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; _ga=GA1.2.570212981.1623985393; dplet=7b726db2fc4478d77327421678eb5e74; dper=c0f11e2ea064e9dae1103763a4c8446659960d2afef26c88d84d44d456b16e190682524a3230c681ab7cdc2f2b1112bd0647f2e6b9616ea6e5b4750b4984878c11750a7546f534f1f2a2f7c58e85d52e6b602f15a72f2c3e9be68edf23908706; ll=7fd06e815b796be3df069dec7836c3df; _lx_utm=utm_source=google&utm_medium=organic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1624070266,1624095737,1624101954,1624102009; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1624103876; _lxsdk_s=17a23e4227c-84c-345-f26||582"
        # self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

        # edge
        self.cookie = '_lxsdk_cuid=17a0969dff0c8-0388ad2d3cb4a6-f7f1939-100200-17a0969dff1c8; _hc.v=b3171166-89e9-cfd3-0f8e-a0095a8e05a1.1623655573; s_ViewType=10; ctu=2a2e1c4a49e422ece1e1b02dd418c7bdf50c02237fddb9a24f10519d325bdd4b; uuid=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; iuuid=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; _lxsdk=D4CD3F578C621AC0C97AE2C54B46C969411990BC9F962777CCF032333A6D6FBB; _ga=GA1.2.570212981.1623985393; thirdtoken=340bca8e-b4c8-4672-ba03-496aa5631903; _thirdu.c=66fefa76ffc6a5e2ec63f06ee3240508; ua=dpuser_6185476995; uamo=15848933632; pvhistory="6L+U5ZuePjo8L3N1Z2dlc3QvZ2V0SnNvbkRhdGE/ZGV2aWNlX3N5c3RlbT0+OjwxNjUxNTkxNzI1ODgxXV9b"; m_flash2=1; cityid=1; _lx_utm=utm_source=google&utm_medium=organic; WEBDFPID=777155w214825y9z102193u0v59ux2yy8191z10w840979586yy228uz-1651678230422; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1651591898; dplet=6e4d0243b07c5b8d252ca4dcdf4771a9; dper=90a35ab05d6bda7f4fa184c21ab998f39527236436552ce83ea882722a5bdf01c89256a1cae597f5e916d321a7c5a3e1e76282025c8151fb6e7a2adc6bf7d1088868f90bdb8c7a1d217ca8b4f20145cf9cfb724825f938e3cc0652b3bd3ebe25; ll=7fd06e815b796be3df069dec7836c3df; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1651591984; _lxsdk_s=1808a8b5974-db2-f67-1d1||119'
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        self.accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        self.accept_encoding = "gzip, deflate"
        self.cache_control = "max-age=0"

        self.host = "www.dianping.com"

        self.result_file = "./result.csv"

spider_config = Config()