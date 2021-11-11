def noCandles(specs):
    
    candle = specs[0]
    days = specs[1]
    
    Candles = days + ((days * (days + 1))/2)
    print('{0} {1}'.format(candle, int(Candles)))

n = int(input())
for i in range(n):
    
    _specs = [int(j) for j in input().split()]
    noCandles(_specs)
