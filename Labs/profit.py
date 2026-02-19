def main():
    print('Enter a filename: ', end = '')
    filein = input()
    
    fileinput = open(filein, 'r')

    numSales = 0
    profit = 0

    for line in fileinput:
        line = line.strip().split()
        numSales += 1
        
        for ele in line:
            if ele.isdigit():
                ele = int(ele)
                profit = profit + ele
    avgProfit = profit / numSales
    print('The profit from %d sales is $%.2f.' % (numSales, avgProfit))




if __name__ == "__main__":
    main()
