def generator(num):
    while True:
        num += 1
        yield num

if __name__ == '__main__':
    num = 10
    num = next(generator(num))
    print(next(generator(num)))