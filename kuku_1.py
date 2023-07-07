# def main():
#     for i in range(1, 10):
#         for j in range(1, 10):
#             product = i * j

#             print(f"{product}", end="") # end="" のおかげで改行されない
#         print()

# if __name__ == "__main__":
#     main()



kuku_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for kuku_first in kuku_1:
    for kuku_second in kuku_1:
        print(f"{kuku_first*kuku_second:4d}", end="")
    print()
