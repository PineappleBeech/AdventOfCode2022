import requests

# put session cookie here
session = ""

def get_input(day: int) -> str:
    url = f"https://adventofcode.com/2022/day/{day}/input"
    cookies = {"session": session}
    return requests.get(url, cookies=cookies).text
