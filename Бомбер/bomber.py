import requests

phone = "9637328400"

sokolov = requests.post("https://sokolov.ru/api/v4/profile/user/send-code/",
                        data = {"data": {"type": "login", "attributes": {"phone": "7" + phone}}},
                        headers={
                            'accept-language':'ru,en;q=0.9',
                            'connection':'keep-alive',
                            'host':'sokolov.ru',
                            'origin':'https://sokolov.ru',
                            'referer':'https://sokolov.ru/?ysclid=m33d9c9nqt582513970&utm_referrer=https%3A%2F%2Fyandex.ru%2F'})
lerua = requests.post("https://api.lemanapro.ru/customers/ausweis-general/otp/web/authentication-code",
                        data = {'"login"': '"+7' + phone + '"'},
                        headers={
                            'accept-language':'ru,en;q=0.9',
                            'client-id':'p0527624d9274fe184e71edbc9d1f88f',
                            'connection':'keep-alive',
                            'host':'api.lemanapro.ru',
                            'origin':'https://auth.lemanapro.ru',
                            'referer':'https://auth.lemanapro.ru/',
                            'x-api-key':'fIpqjiDT1dYhOa4k6SbvUO8tRTFjcGxi'})
print(sokolov, sokolov.text)
print(lerua, lerua.text)
