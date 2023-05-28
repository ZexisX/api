from time import sleep
import requests
import json
import urllib.parse

class RegAcc:
    def __init__(self, delay):
        self.taikhoan = ""
        self.matkhau = "@Khanh2007"
        self.sdt = "0964243159"
        self.email = ""
        self.accessToken = ""
        self.refreshToken = ""
        self.cookies = ""
        self.delay = delay

    def reg(self):
        headers = {
            'authority': 'metahome.digital',
            'accept': 'application/json',
            'accept-language': 'ko',
            'content-type': 'application/json',
            'origin': 'https://metahome.digital',
            'referer': 'https://metahome.digital/sign-up',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        }

        json_data = {
            'email': self.taikhoan,
            'password': self.matkhau,
            'confirmPassword': self.matkhau,
            'ageTerms': True,
            'termsOfUse': True,
            'privacy': True,
            'readRisk': True,
            'referralCode': 'I6E1AYFC49',
        }

        response = requests.post('https://metahome.digital/api/sign-up', headers=headers, json=json_data).text
        return response

    def login(self):
        cookies2 = {
            'account': '%7B%22account%22%3Anull%7D',
        }

        headers2 = {
            'authority': 'metahome.digital',
            'accept': 'application/json',
            'accept-language': 'ko',
            'content-type': 'application/json',
            'cookie': 'account=%7B%22account%22%3Anull%7D',
            'origin': 'https://metahome.digital',
            'referer': 'https://metahome.digital/sign-in',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        }

        json_data2 = {
            'email': self.taikhoan,
            'password': self.matkhau,
        }

        login = requests.post('https://metahome.digital/api/login', cookies=cookies2,headers=headers2, json=json_data2).json()
        if 'email' in login:
            self.email = login['email']
            self.accessToken = login['accessToken']
            self.refreshToken = login['refreshToken']
            cookiesacc = json.dumps({
                "account": {
                    "email": self.email,
                    "accessToken": self.accessToken,
                    "name": None
                }
            })
            self.cookies = urllib.parse.quote(cookiesacc)
        else:
            print('Đăng nhập không thành công')
            return

    def set(self):
        headers1 = {
            'authority': 'metahome.digital',
            'accept': 'application/json',
            'accept-language': 'ko',
            'authorization': self.refreshToken,
            'content-type': 'application/json',
            'cookie': f'account={self.cookies}',
            'origin': 'https://metahome.digital',
            'referer': 'https://metahome.digital/mypage',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        }

        json_data1 = {
            'name': 'Trương Ngọc Khánh',
            'country': 'KOREA',
            'phoneNumber': self.sdt,
        }

        response = requests.post('https://metahome.digital/api/account/phone-number', headers=headers1, json=json_data1).text
        print(f"Thành Công: {self.taikhoan} | {self.matkhau}")
        with open("thanhcong.txt", "a") as file:
            file.write(f"{self.taikhoan} | {self.matkhau}" + "\n")

    def run(self):
        with open("taikhoan.txt", "r") as file:
            for taikhoan in file:
                self.taikhoan = taikhoan.strip()
                response = self.reg()
                self.login()
                self.set()
                for i in range (self.delay,-1,-1):
                    print(f'Wait {i} seconds!  ',end = '\r')
                    sleep(1)

delay = int(input("Nhập Delay: "))
main = RegAcc(delay)
main.run()
