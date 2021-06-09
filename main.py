import requests
from requests.models import Response

def _bold(str):
    return f"**{str}**"

def _spoiler(str):
    return f"||{str}||"

def main():
    selected_word = input("Which word would you like to use? > ")
    r: Response = requests.get(f'https://jisho.org/api/v1/search/words?keyword={selected_word}')

    if r.status_code != 200:
        print(f"Request to Jisho failed.")
        print(f"Status code: {r.status_code}")
        print(r.reason)
        return

    reading = r.json()['data'][0]['japanese'][0]['reading']
    pitch = 1
    definition = r.json()['data'][0]['senses'][0]['english_definitions']

    wide_space = "　"
    print(_bold("今日の言葉"))
    print()
    print(
        _bold(selected_word) +
        wide_space +
        _spoiler(f'{reading}　[{pitch}]') +
        wide_space +
        _spoiler(f'{definition}')
    )
    print()
    print(f"では、{_bold('本日')}の練習はこれまでにします。")
    print(_spoiler(f"では、{_bold('ほんじつ')}の　れんしゅうは　これまでに　します。"))
    print(_spoiler(f"That will be all for {_bold('today')}'s practice."))

if __name__ == "__main__":
    main()
