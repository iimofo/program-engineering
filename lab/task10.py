import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(['№', 'Секунда', 'Микросекунда']) 
    
    for i in range(1, 301): 
        current_time = datetime.datetime.now()
        
        writer.writerow([
            i, 
            current_time.second, 
            current_time.microsecond
        ])
        
        time.sleep(0.01)