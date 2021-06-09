def _bold(str):
    return f"**{str}**"

def _spoiler(str):
    return f"||{str}||"

def main():
    print(_bold("今日の言葉"))
    print()
    print(f"{_bold('本日')}　{_spoiler('ほんじつ　[1]')}　{_spoiler('today; this day')}")
    print()
    print(f"では、{_bold('本日')}の練習はこれまでにします。")
    print(_spoiler(f"では、{_bold('ほんじつ')}の　れんしゅうは　これまでに　します。"))
    print(_spoiler(f"That will be all for {_bold('today')}'s practice."))

if __name__ == "__main__":
    main()
