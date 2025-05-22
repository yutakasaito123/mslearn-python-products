import csv
csv_file = open('example.csv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
csv_writer.writerow(['Name', 'Age', 'City'])
csv_writer.writerow(['Alice', 30, 'New York'])
csv_writer.writerow(['Bob', 25, 'Los Angeles'])
csv_file.close()

