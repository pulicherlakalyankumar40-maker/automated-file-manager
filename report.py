import csv
import os
def generate_report(data):
    os.makedirs('reports', exist_ok=True)
    with open('reports/file_report.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File Name', 'Extension', 'Size (bytes)', 'Date Organized', 'Destination Folder'])
        for row in data:
            writer.writerow(row)