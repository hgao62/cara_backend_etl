from extract_data import get_stock_history 

def main():
    google = get_stock_history('goog')
    print(google)



if __name__ =="__main__":
    main()