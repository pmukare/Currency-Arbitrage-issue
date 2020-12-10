
@author: Pravin Mukare
"""

for i in range (1,101):
    if i%3 ==0 and i%5 == 0:
        print("ThreeFive")
    elif i%3 ==0:
        print("Three")
    elif i%5 ==0:
        print("Five")
    else:
        print(i)
        
        

input_data = [
2,
'1.1837 1.3829 0.6102',
'1.1234 1.2134 1.2311'
]



def calculateArbitrageProfit(input_data):
    
    output = []
    
    size = int(input_data[0])
    if size >= 1 and size <= 1000:
        for i in input_data[1:]:
            if len(i)> 0:
                quotes = i.split(' ')
                
                print(quotes)
                
                USD_EUR = int(quotes[0]) 
                EUR_GBP = int(quotes[1])
                GBP_USD = int(quotes[2])
                
                if (USD_EUR > 0.001 and USD_EUR <= 1000):
                    if (EUR_GBP > 0.001 and EUR_GBP <= 1000):
                        if (GBP_USD > 0.001 and GBP_USD <= 1000):
                            
                            USD = 100000
                            EUR = USD/USD_EUR
                            GBP = EUR/EUR_GBP
                            NEW_USD = GBP/GBP_USD
                            
                            if NEW_USD > USD:
                                output.append(round(NEW_USD))
                            else:
                                output.append(0)                            
                                
    return output
                            
                            

input_data
