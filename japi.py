import urllib
import json
import urllib.request

def getStockData(symbol):

    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + \
        symbol + "&apikey=4YS6EOFJ8540DDAO"
    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()
    return responseString


def main():
    f = open("japi.out", "a")
    sym = input("Please enter a stock symbol: ")
    while sym != "quit":
        data = getStockData(sym)
        print(f, data)
        stockdict = json.loads(data)
        stockprice = stockdict['Global Quote']['05. price']
        stockprice = stockprice[:-2]
        print("The current price of", sym, "is: $" + stockprice)
        f.write(data)
        sym = input("Please enter a stock symbol: ")
    f.close()
    print("Stock Quotes retrieved succesfully!")
    


if __name__ == "__main__":
    main()