import time

import requests

def get_book_id():
    cookies = {
        'PSTM': '1642410150',
        'BIDUPSID': '52D9C44F1F525155C55DDFFFEB4B3D00',
        '__yjs_duid': '1_96f9ea527363cd1ec4547ba2fd84d17d1642466587262',
        'BDUSS': 'QyRmVGVEVJcXQ0dFBOSmJnQzRJcFJBZ091YW1FWjZOQlhiSkt2bDlORlRrUmhpSVFBQUFBJCQAAAAAAAAAAAEAAAAQZ7vIs6S358bGwMvAssur0-MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFME8WFTBPFhSn',
        'BDUSS_BFESS': 'QyRmVGVEVJcXQ0dFBOSmJnQzRJcFJBZ091YW1FWjZOQlhiSkt2bDlORlRrUmhpSVFBQUFBJCQAAAAAAAAAAAEAAAAQZ7vIs6S358bGwMvAssur0-MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFME8WFTBPFhSn',
        'BAIDUID': '0ED0B687189B2C82FDF496702F30F214:FG=1',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'BDSFRCVID': 'uHDOJexroG38vSnDWEgbbokts2KKg9TTDYLtOwXPsp3LGJLVgMtPEG0Pt8i0Cou-dk83ogKK3gOTH4AF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
        'H_BDCLCKID_SF': 'fR-f_D_5fIvDqTrP-trf5DCShUFs0lLJB2Q-XPoO3K8WfxOkQhJphl-VhURJb5jiWKk8-UbgylRM8P3y0bb2DUA1y4vpKMrJLgTxoUJ2fnI2En7GqtOOe5tebPRiJ-b9Qg-J5lQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0bDP6j6Kbe5PVKgTa54cbb4o2WbCQ5nQT8pcN2b5oQTJb5Rbn0pb4Qn6aWbv2-KovOn0w3hOUWfAkXpJvQnJjt2JxaqRC5h6MVh5jDh3Me-cQLUnte43Wfn7y0hvctb3cShPmLfjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQheHAftjDffn3aQ5rtKRTffjrnhPF33T0UXP6-hnjy3bAOLfO83U3pSKjPhPRMKTDUyUt8Lp3RymJJ2-39LPO2hpRjyxv4bUu30-oxJpOJfIKj5b7aHRbObKOvbURvDP-g3-AJ3x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEVCP5JD_bbKvPKITD-tFO5eT22-usbRTi2hcHMPoosI895lbxQh-kbgca2-nJ-briab0XQUbUoqRHXnJi0btQDPvxBf7p52jJbp5TtUJMbbIxLPnhqt0feabyKMnitKv9-pP20lQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuejAbj6jWeaRabK6aKC5bL6rJabC3fqneXU6q2bDeQN-O-qJX3Nv40botabvMqIooyPtB3h0vWtvJWbbvLT7johRTWqR4ep6m0MonDh83eMuj3-RtHCnWVIOO5hvvhn3O3MAMLfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRFeoIt53j',
        'BDSFRCVID_BFESS': 'uHDOJexroG38vSnDWEgbbokts2KKg9TTDYLtOwXPsp3LGJLVgMtPEG0Pt8i0Cou-dk83ogKK3gOTH4AF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
        'H_BDCLCKID_SF_BFESS': 'fR-f_D_5fIvDqTrP-trf5DCShUFs0lLJB2Q-XPoO3K8WfxOkQhJphl-VhURJb5jiWKk8-UbgylRM8P3y0bb2DUA1y4vpKMrJLgTxoUJ2fnI2En7GqtOOe5tebPRiJ-b9Qg-J5lQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0bDP6j6Kbe5PVKgTa54cbb4o2WbCQ5nQT8pcN2b5oQTJb5Rbn0pb4Qn6aWbv2-KovOn0w3hOUWfAkXpJvQnJjt2JxaqRC5h6MVh5jDh3Me-cQLUnte43Wfn7y0hvctb3cShPmLfjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQheHAftjDffn3aQ5rtKRTffjrnhPF33T0UXP6-hnjy3bAOLfO83U3pSKjPhPRMKTDUyUt8Lp3RymJJ2-39LPO2hpRjyxv4bUu30-oxJpOJfIKj5b7aHRbObKOvbURvDP-g3-AJ3x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEVCP5JD_bbKvPKITD-tFO5eT22-usbRTi2hcHMPoosI895lbxQh-kbgca2-nJ-briab0XQUbUoqRHXnJi0btQDPvxBf7p52jJbp5TtUJMbbIxLPnhqt0feabyKMnitKv9-pP20lQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuejAbj6jWeaRabK6aKC5bL6rJabC3fqneXU6q2bDeQN-O-qJX3Nv40botabvMqIooyPtB3h0vWtvJWbbvLT7johRTWqR4ep6m0MonDh83eMuj3-RtHCnWVIOO5hvvhn3O3MAMLfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRFeoIt53j',
        'delPer': '0',
        'PSINO': '7',
        'ZD_ENTRY': 'baidu',
        'BAIDUID_BFESS': 'FC52D97C2CE255929EDA1A5B2E0ABF95:FG=1',
        'BDRCVFR[feWj1Vr5u3D]': 'I67x6TjHwwYf0',
        'Hm_lvt_bf1e478a71b02a743ab42bcfed9d1ff1': '1644845494',
        'H_PS_PSSID': '35835_35105_31254_35765_34584_35491_35871_35797_35322_26350_35882_35877_35744',
        'BA_HECTOR': 'al8hah0104058100da1h0kmkv0r',
        'Hm_lpvt_bf1e478a71b02a743ab42bcfed9d1ff1': '1644845772',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://dushu.baidu.com/catedetail?channel=%E7%94%B7%E9%A2%91&cate2=%E4%B8%9C%E6%96%B9%E7%8E%84%E5%B9%BB&query=%E4%B8%9C%E6%96%B9%E7%8E%84%E5%B9%BB',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
    }
    book_ids = []
    for page in range(1,17):
        params = (
            ('page', '6'),
            ('count', '10'),
            ('channel', '\u7537\u9891'),
            ('cate2', '\u4E1C\u65B9\u7384\u5E7B'),
            ('query', '\u4E1C\u65B9\u7384\u5E7B'),
        )

        response = requests.get('https://dushu.baidu.com/api/getCateDetail', headers=headers, params=params, cookies=cookies)
        datas = response.json()['data']['novelList']
        for data in datas:
            bookid = data['bookId']
            book_ids.append(bookid)
    return book_ids

# import os
# name = input('请输入你要创建的文件名:')
# filename =f"./{name}/baz.txt"
# os.makedirs(os.path.dirname(filename), exist_ok=True)
# with open(filename,"w") as f:
#     f.write("FOOBAR")
#     f.close()
import asyncio#异步库
import requests
import aiohttp#异步请求库
import aiofiles#异步下载库
import json
import os


# https://dushu.baidu.com/api/pc/getCatalog?data={book_id:4305596118}
# https://dushu.baidu.com/api/pc/getChapterContent?data={book_id:4315646974,cid:4315646974|10166918,need_bookinfo:1}

#异步请求c_id并下载到本地
async def aioDownload(b_id,cid,title,book_name):
    data = {f"book_id":b_id,
            "cid":f'{b_id}|{cid}',
            "need_bookinfo":"1"
            }
    data = json.dumps(data)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dict = await resp.json()
            filename = f'./{book_name}/{title}'
            os.makedirs(os.path.dirname(filename),exist_ok=True)
            async with aiofiles.open(filename,'w',encoding='utf-8')as f:
                await f.write(dict['data']['novel']['content'])

# 同步亲求b_id并获得b_id进行异步请求
async def get_cid(url):
    resp = requests.get(url)
    items = resp.json()['data']['novel']['items']
    tasks = []
    for item in items:
        cid = item['cid']
        title = item['title']
        print(cid,title)
        tasks.append(aioDownload(b_id,cid,title,book_name))
    await asyncio.wait(tasks)

# 启动函数
if __name__ == '__main__':
    b_ids = get_book_id()
    print(b_ids)
    for b_id in b_ids:
        # b_id = b_ids[3]
        try:
            print('开始爬取的bookid为:',b_id)
            get_detail_url = 'https://dushu.baidu.com/api/pc/getDetail?data={%22book_id%22:%22'+b_id+'%22}'
            resp = requests.get(get_detail_url)
            book_name = resp.json()['data']['novel']['book_name']
            url = 'https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%22'+b_id+'%22}'
            asyncio.run(get_cid(url))
            time.sleep(3)
        except:
            continue




