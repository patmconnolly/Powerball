import lib.lotto

class main:
    def __init__(self):
        x = lib.lotto.statistics(30)
        #Download CSV file
        x.collect()
        #Parse the numbers
        x.parse()
        #Statistical Analysis
        numbers = x.performStatistics()
        #Predict
        print("I predict the white balls will be..:")
        for i in range(5):
            print(numbers[i])
        print("With a Powerball of..: ",numbers[5])
        return None

if __name__ == '__main__':
    main()