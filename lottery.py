import requests
from bs4 import BeautifulSoup
import sys


def jackpot(numbers, lottery_results):
    result = {}
    for number in numbers:
        count = 0
        for row in lottery_results.values():
            for lottery_ in row:
                if str(number) in lottery_[-2:]:
                    count = count + 1
        result.update({number: count})
    return result


def get_jackpot():
    lotteryvn = requests.get("http://ketqua.net/")
    soup = BeautifulSoup(lotteryvn.text, "lxml")
    id_ = {"special prize": ["rs_0_0"], "first prize": ["rs_1_0"], "second prize": ["rs_2_0", "rs_2_1"], "three prize": ["rs_3_0", "rs_3_1", "rs_3_2"], "four prize": [
        "rs_4_0", "rs_4_1", "rs_4_2", "rs_4_3"], "fifth prize": ["rs_5_0", "rs_5_1", "rs_5_2"], "six prize": ["rs_6_0", "rs_6_1", "rs_6_2"], "last prize": ["rs_7_0", "rs_7_1", "rs_7_2", "rs_7_3"]}
    lottery_result = {}
    for name, ids in id_.items():
        result = []
        for id_s in ids:
            lotterys = soup.find("div", {"id": id_s}).text
            result.append(lotterys)
            lottery_result.update({name: result})

    return lottery_result


def main():
    numbers = sys.argv
    lottery_results = jackpot(numbers, get_jackpot())
    won = False
    for number, count in lottery_results.items():
        if count != 0:
            won = True
            break
    if won:
        for number, count in lottery_results.items():
            if count == 0:
                print(f"So {number} khong trung giai")
            else:
                print(f"So {number} trung {count} giai")
                won = True
    elif not won:
        for name, results in get_jackpot().items():
            print(name, end=": ")
            for result in results:
                print(result, end=" ")
            print(" ")


if __name__ == "__main__":
    main()
