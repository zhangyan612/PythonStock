# KDJ calculation formula
def KDJCalculation(K1, D1, high, low, close):
    # input last K1, D1, max value, min value and current close value
    #count = 9
    a = 1.0/3
    b = 1.0/3
    low_price = low #low.min() #min(list1)
    high_price = high #high.max() #max(list1)
    current_close = close
    if high_price!=low_price:
        RSV = (current_close-low_price)/(high_price-low_price)*100
    else:
        RSV = 50
    K2=(1-a)*K1+a*RSV
    D2=(1-b)*D1+b*K2
    J2 = 3*K2-2*D2
    #log.info("Daily K1: %s, D1: %s, K2: %s, D2: %s, J2: %s" % (K1,D1,K2,D2,J2))
    return K1,D1,K2,D2,J2