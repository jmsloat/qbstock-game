import requests
from pyquery import PyQuery as pq


def main():
    r = requests.get('http://www.espn.com/nfl/qbr/_/type/player-week/week/3')
    print(r.status_code)

    d = pq(r.content)

    for x in d('tr').items():
        print(x.html())
        name = x('a')
        print(name)


if __name__ == '__main__':
    main()
