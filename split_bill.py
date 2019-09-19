# 割り勘アプリ
# 金額と人数を受け取り，割り勘結果を出力する


def calc(bill, num):
    return (bill // num), (bill % num)


def main():
    bill = int(input('金額 > '))
    num = int(input('人数 > '))
    bill_each, remain = calc(bill, num)
    # bill_each, remain = divmod(bill, num)
    print(f'一人当たりの支払い：{bill_each}　端数：{remain}')
    print(f'先輩は{bill_each + remain}円支払ってください')


if __name__ == '__main__':
    main()
