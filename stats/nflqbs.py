import requests

def main():
    r = requests.get('http://www.nfl.com/stats/categorystats?tabSeq=1&season=2017&seasonType=PRE&d-447263-n=1&d-447263-o=2&d-447263-p=1&statisticPositionCategory=QUARTERBACK&d-447263-s=PASSING_PASSER_RATING')
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    main()