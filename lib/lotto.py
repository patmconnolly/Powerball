from urllib import request
import os
import lib.draw as draw

class statistics:
    def __init__(self, count=30):
        #History refers to how many historical draws to collect.
        #Taking absoloute value to eliminate any potential error.
        self.count = -1 * abs(count)
        
        #URL is from Texas Lottery, contains historical Powerball draws.
        '''
        The comma separated values file you can download here contains current and past winning numbers from all Powerball drawings held since Texas began participating in game drawings on February 3, 2010.

        The information in the file is organized in the following manner, one row for each drawing:

        Feb 3, 2010 to Jan 14, 2012:
        Game Name, Month, Day, Year, Num1, Num2, Num3, Num4, Num5, Powerball, Power Play

        Jan 18, 2012 to Jan 18, 2014:
        Game Name, Month, Day, Year, Num1, Num2, Num3, Num4, Num5, Powerball

        Jan 22, 2014 to present:
        Game Name, Month, Day, Year, Num1, Num2, Num3, Num4, Num5, Powerball, Power Play
        '''
        self.URL = "https://www.texaslottery.com/export/sites/lottery/Games/Powerball/Winning_Numbers/powerball.csv"
        
        self.localFile = str(os.path.dirname(os.path.realpath(__file__)))+"/powerballNumbers.csv"

        self.ballpit = []

        self.pick = [0, 0, 0, 0, 0, 0]
        self.picked = False

    def collect(self):
        request.urlretrieve(self.URL,self.localFile)
        return None

    def parse(self):
        #Opening file using with() method so file is closed when complete.
        with open(self.localFile) as file:
            for line in (file.readlines() [self.count:]):
                temp_container = line.split(",")
                if(len(temp_container)==11):
                    self.ballpit.append(draw.pull(temp_container[1], temp_container[2], temp_container[3], temp_container[4], temp_container[5], temp_container[6], temp_container[7], temp_container[8], temp_container[9], temp_container[10]))
                else:
                    self.ballpit.append(draw.pull(temp_container[1], temp_container[2], temp_container[3], temp_container[4], temp_container[5], temp_container[6], temp_container[7], temp_container[8], temp_container[9]))
        return None

    def performStatistics(self):
        if not self.picked:
            #Memory is cheap in this case so saving the extra lines of code by leaving 2 indexes as zero.
            whiteList = [0] * 70 # 1-69 are possible values
            redList = [0] * 27 # 1-26 are possible values

            for i in range(len(self.ballpit)):
                WB=self.ballpit[i].white()
                redList[int(self.ballpit[i].powerball())]+=1

            for i in range(len(WB)):
                whiteList[int(WB[i])]+=1

            for i in range(5): #Pick 5 numbers.
                index = whiteList.index(max(whiteList))
                self.pick[i] = index
                whiteList[index] = 0 #zero the list element to remove from play.

            self.pick[5] = redList.index(max(redList))
            self.picked = True
        return self.pick
        
