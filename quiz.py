import requests as r, re, os

class Quizziz:
    def __init__(self):
        self.api = r.Session()
        self.roomhash = None
        self.hostid = None

    def cekroom(self, roomcode):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'Content-Type': 'application/json'
        }

        data = {
            'roomCode': roomcode
        }

        resp = self.api.post('https://game.quizizz.com/play-api/v5/checkRoom', headers=headers, json=data)
        data = resp.json()
        self.roomhash = data['room']['hash']
        self.hostid = data['room']['hostSessionId']
        if self.roomhash:
            print(' [!] Get Roomhash')
            names = input(' [!] Display as: ')
            self.join(names)
        else:
            print(' [!] Not Valid Code')

    def join(self, names):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'Content-Type': 'application/json'
        }

        data = {
            "roomHash": self.roomhash,
            "authCookie": None,
            "ip": "XXXX", # Your Ip Here.
            "player": {
                "id": names,
                "origin": "web",
                "isGoogleAuth": False,
                "avatarId": 24,
                "startSource": "gameCode.typed",
                "expName": "main_main",
                "expSlot": "4",
                "uid": "b874ebba-a854-4830-8fca-1545fd8267ae",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
            },
            "powerupInternalVersion": "20",
            "serverId": "6585172d10afc20021e81ee7",
            "socketExperiment": "authRevamp",
            "socketId": "RrAUvx1Qd2mVRZ-xj1tF",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
        }

        resp = self.api.post('https://game.quizizz.com/play-api/v5/join', headers=headers, json=data)
        data = resp.json()
        os.system('cls')
        code = data['room']['code']
        print(f' [!] Name: {names} | Room: {code} \n')
        questions = data['room']['questions']
        for i, (question_id, question_data) in enumerate(questions.items(), start=1):
            question_text = re.sub(r'<[^>]+>', '', question_data['structure']['query']['text'])
            pilihan = [re.sub(r'<[^>]+>', '', option['text']) for option in question_data['structure']['options']]
            print(f" [{i}]: {question_text}")
            print(" == Pilihan:")
            for pil in pilihan:
                print(f"  - {pil}")
            print()

if __name__ == "__main__":
    bot = Quizziz()
    os.system('cls')
    roomcode = input(' [!] Room Code: ')
    bot.cekroom(roomcode)
  
