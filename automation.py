"""
python中的自动化
schedule requests
"""

import requests

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '+86 18342232709',
        'message':'Good morning',
        'key':'textbelt'
    })

    print(resp.json())

send_message()

