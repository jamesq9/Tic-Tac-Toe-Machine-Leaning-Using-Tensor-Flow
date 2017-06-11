import random

def getData(filename):
    
    x = []
    y = []

    lines = [line.rstrip('\n') for line in open(filename)]
    for line in lines:
        data = list(map(int,line.split()))
        x.append(data[:9])
        y.append(data[9:])
    c = list(zip(x, y))
    random.shuffle(c)
    x, y = zip(*c)
    return x,y

def work( train = "./data/training.txt", test = "./data/test.txt"):
    train_x, train_y = getData(train)
    test_x, test_y = getData(test)
    #print(test_x[0] , test_y[0])
    return train_x, train_y, test_x, test_y

if __name__ == "__main__":
    work()