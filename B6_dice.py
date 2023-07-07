import random
from typing import List       # アノテーションを書く場合に必要

def roll_dice(side: int, times: int) -> List[int]:
    results = []

    for _ in range(times):
        dice = random.randint(1, side)
        results.append(dice)        # 出てきた数字を行5の空のリストに入れていくコードのこと
    
    return results

if __name__ == "__main__":
    n = int(input("サイコロの面の数は?: "))
    m = int(input("何回振りますか?: "))

    print(roll_dice(side=n, times=m))
    
