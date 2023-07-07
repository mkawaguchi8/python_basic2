def show_kuku2(max_row: int, max_col: int) -> None:  #アノテーション()の中は他の人が見てわかるようにしているだけ
    for i in range(1, max_row + 1):
        for j in range(1, max_col + 1):
            product = i * j

            print(f"{product}", end="")

        print()


def main():  #ここから動き始める
    max_row = int(input("行列を入力してください: ")) 
    max_col = int(input("列数を入力してください: "))

    show_kuku2(max_row, max_col)

if __name__ == "__main__":
    main()

