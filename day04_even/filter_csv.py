import csv

def read_csv(filename):
    matrix = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # 読み込んだ row は ["1","2","3"] のような文字列なので int に変換
            matrix.append([int(x) for x in row])
    return matrix

def filter_even(matrix):
    even_numbers = []
    for row in matrix:
        for n in row:
            if n % 2 == 0:
                even_numbers.append(n)
    return even_numbers

def write_even_csv(filename, numbers):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(numbers)

def main():
    matrix = read_csv("data.csv")
    print("元データ：", matrix)

    evens = filter_even(matrix)
    print("偶数だけ：", evens)

    write_even_csv("even_numbers.csv", evens)
    print("even_numbers.csv に書き出しました")

if __name__ == "__main__":
    main()