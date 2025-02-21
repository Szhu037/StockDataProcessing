import csv
from collections import defaultdict

def process_stock_data(file_path):
    company_volume = defaultdict(int)
    company_dollar_volume = defaultdict(float)
    company_closing_price = {}
    hourly_volume = defaultdict(int)
    total_volume = 0
    total_dollar_volume = 0
    max_trade = 0
    unique_companies = set()
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        
        for row in reader:
            timestamp, ticker, price, volume = row
            price, volume = float(price), int(volume)
            
            # Track total volume and dollar volume
            company_volume[ticker] += volume
            company_dollar_volume[ticker] += price * volume
            
            # Track closing price
            company_closing_price[ticker] = price
            
            # Track max single trade value
            max_trade = max(max_trade, price * volume)
            
            # Track total volume and dollar volume
            total_volume += volume
            total_dollar_volume += price * volume
            
            # Track hourly volume
            hour = timestamp.split()[1].split(':')[0]
            hourly_volume[hour] += volume
            
            # Track unique companies
            unique_companies.add(ticker)
    
    # Compute required values
    highest_volume_company = max(company_volume, key=company_volume.get)
    lowest_dollar_volume_company = min(company_dollar_volume, key=company_dollar_volume.get)
    lowest_hourly_volume = min(hourly_volume, key=hourly_volume.get)
    avg_volume = total_volume / len(unique_companies) if unique_companies else 0
    
    return (
        highest_volume_company, 
        avg_volume, 
        max_trade, 
        lowest_hourly_volume, 
        (total_volume, total_dollar_volume), 
        len(unique_companies), 
        lowest_dollar_volume_company, 
        company_closing_price
    )

process_stock_data("ticker_data.csv")