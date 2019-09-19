def bmi_calc(h, w):
    return w / (h ** 2)


def main():
    height = float(input('身長を入力してください(cm)：'))
    height /= 100
    weight = float(input('体重を入力してください(kg)：'))

    print('あなたのBMIは {:.2f} です'.format(bmi_calc(height, weight)))


if __name__ == '__main__':
    main()