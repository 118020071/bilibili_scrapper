import requests, random, time, openpyxl, datetime, concurrent.futures, threading, bs4
requests.urllib3.disable_warnings()
def getText(name):
    returnlist = []
    
    with open(name, "r") as f:
        while True:
            a = f.readline()
            if len(a) == 0:
                break
            a = a.replace("\n", "")
            returnlist.append(a)
    
    return returnlist

g_headers = getText("userAgent.txt")
proxyList = getText("proxy.txt")
proxyIndex = 0
BVList = getText("bv_file.txt")
print("BVList length: ", len(BVList))
data_list = []

# while True:
#     try:
#         fake_user_agent = { "User-Agent": g_headers[random.randint(0, len(g_headers)-1)]}
#         proxy_num = proxyList[proxyIndex%len(proxyList)]
#         proxyIndex += 1
#         proxy = { "http": "http://"+proxy_num}

#         html = requests.post(
#             url = "https://www.baidu.com",
#             headers = fake_user_agent,
#             proxies = proxy,
#             timeout = 2,
#             verify = False
#         )
#         break
#     except:
#         continue

# print(bs4.BeautifulSoup(html.text, "html.parser"))

def get_json(url, timeout=2):

    global g_headers, proxyList, proxyIndex

    fake_user_agent = { "User-Agent": g_headers[random.randint(0, len(g_headers)-1)]}
    proxy_num = proxyList[proxyIndex%len(proxyList)]
    proxyIndex += 1
    proxy = { "http": "http://"+proxy_num}

    while True:
        try:
            html = requests.get(
                url = url,
                headers = fake_user_agent,
                proxies = proxy,
                timeout = timeout,
                verify=False
            )
            break
        except:
            # proxyList.remove(proxy)
            # print(proxy)
            fake_user_agent = { "User-Agent": g_headers[random.randint(0, len(g_headers)-1)]}
            proxy_num = proxyList[proxyIndex%len(proxyList)]
            proxyIndex += 1
            proxy = { "http": "http://"+proxy_num}

    response_data = html.json() # as type: dictionary

    return response_data.get("data")

def get_data(bvid):
    global data_list

    url = "https://api.bilibili.com/x/web-interface/archive/stat?bvid="+str(bvid)

    while True:
        data = get_json(url)

        if data != "none" and data != "None" and data != None:
            # print(data)
            data_list.append(data)
            break
        # else:
            # print(bvid, "retry")

def main(max_thread):
    global BVList

    # for i in range(len(BVList)):
    #     get_data(BVList[i])
    #     print("%d/%d"%(i,len(BVList)), end='\r')
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_thread) as executor:
        future_to_url = [executor.submit(get_data, bvid) for bvid in BVList]

        i = 0
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                print("Done", i, end='\r')
                i += 1
            except:
                print("Page %d generate exception"%future_to_url.index(future))

    executor.shutdown(wait=True)

main(1000)
print(data_list)
print(len(data_list))


