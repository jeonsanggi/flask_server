import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from flaskr.module import dbModule
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font',family=font_name)

class ReviewCnt():
    def draw(self, Review,Color):
        print(Review)
        data = list(Review['Date'])
        month=[]

        for i in range(0,len(data)):

            month_tmp = data[i].split('.')
            month.append(month_tmp[1])

        Jan=month.count('01')
        Feb=month.count('02')
        Mar=month.count('03')
        Apr=month.count('04')
        May=month.count('05')
        Jun=month.count('06')
        Jul=month.count('07')
        Aug=month.count('08')
        Sep=month.count('09')
        Oct=month.count('10')
        Nov=month.count('11')
        Dec=month.count('12')


        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec])

        fig = plt.gcf() #변경한 곳
        fig.set_size_inches(7,5)
        fig.savefig('flaskr/static/images/'+Color+'.png')
        fig.clf()
        plt.clf()
