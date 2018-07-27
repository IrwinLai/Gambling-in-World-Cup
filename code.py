import pandas as pd
import matplotlib.pyplot as plt

data2014 = pd.read_csv('worldcup_2014.csv')
data2018 = pd.read_csv('worldcup_2018.csv')

# use the same amount of money to buy each play 
def equal_capital(data):
    data['earning1'] = -10000
    data.loc[(data['win'] < data['lose'])&(data['result']=='l'),'earning1'] += 10000*data['lose']
    data.loc[(data['win'] > data['lose'])&(data['result']=='w'),'earning1'] += 10000*data['win']

    data['earning2'] = -10000
    data.loc[(data['win'] < data['lose'])&(data['result']=='w'),'earning2'] += 10000*data['win']
    data.loc[(data['win'] > data['lose'])&(data['result']=='l'),'earning2'] += 10000*data['lose']

    data['earning3'] = -10000
    data.loc[data['result']=='d','earning3'] += 10000*data['draw']
    
    data['capital1'] = data['earning1'].cumsum()
    data['capital2'] = data['earning2'].cumsum()
    data['capital3'] = data['earning3'].cumsum()

    plt.subplots(figsize = (7,3)) 
    data['capital1'].plot(label='1:weak')
    data['capital2'].plot(label='2:strong')
    data['capital3'].plot(label='3:draw')
    plt.legend(loc='best')
    plt.show()

    return 0

# buy each play for the same expectation
def equal_expectation(data):
    data['earning1'] = -10000
    data.loc[(data['win'] < data['lose'])&(data['result']=='l'),'earning1'] += 10000*data['lose']
    data.loc[(data['win'] > data['lose'])&(data['result']=='w'),'earning1'] += 10000*data['win']

    data['earning2'] = -10000
    data.loc[(data['win'] < data['lose'])&(data['result']=='w'),'earning2'] += 10000*data['win']
    data.loc[(data['win'] > data['lose'])&(data['result']=='l'),'earning2'] += 10000*data['lose']

    data['earning3'] = -10000
    data.loc[data['result']=='d','earning3'] += 10000*data['draw']
    
    data['capital1'] = data['earning1'].cumsum()
    data['capital2'] = data['earning2'].cumsum()
    data['capital3'] = data['earning3'].cumsum()

    plt.subplots(figsize = (7,3)) 
    data['capital1'].plot(label='1:weak')
    data['capital2'].plot(label='2:strong')
    data['capital3'].plot(label='3:draw')
    plt.legend(loc='best')
    plt.show()

    return 0

# buy the 'draw' and 'weak team will win' to make a 'strong team will not win'
def strong_not_win(data):

    data['earning1'] = -20000
    data.loc[(data['win'] > data['lose'])&(data['result']=='w'),'earning1'] += 10000*data['win']
    data.loc[(data['win'] < data['lose'])&(data['result']=='l'),'earning1'] += 10000*data['lose']
    data.loc[data['result']=='d','earning1'] += 10000*data['draw']
    
    plt.subplots(figsize = (7,3))
    data['capital1'] = data['earning1'].cumsum()
    data['capital1'].plot(label='strong dont win')
    plt.legend(loc='best')
    plt.show()

    return 0

# buy the play only when it could be a big upset
def big_upset(data):
    data['earning1'] = 0
    data.loc[(data['win'] >6) | (data['lose'] >6),'earning1'] = -10000
    data.loc[(data['win'] < data['lose']) & (data['lose']>6) & (data['result']=='l'),'earning1'] += 10000*data['lose']
    data.loc[(data['win'] > data['lose']) & (data['win']>6) &(data['result']=='w'),'earning1'] += 10000*data['win']
    
    plt.subplots(figsize = (7,3))
    data['capital1'] = data['earning1'].cumsum()
    data['capital1'].plot(label='big upset')
    plt.legend(loc='best')
    plt.show()
    
    return 0


equal_capital(data2018)

equal_expectation(data2018)

strong_not_win(data2014)

big_upset(data2014)
