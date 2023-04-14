import csv

# Mở file CSV cần đọc
for i in range(5):
    with open('data/test.csv', 'r') as csv_file:
        # Tạo đối tượng reader để đọc từng dòng trong file CSV
        reader = csv.reader(csv_file)
        
        # Mở file CSV mới để ghi kết quả
        with open(f'data/data{i}.csv', 'w', newline='') as new_csv_file:
            # Tạo đối tượng writer để ghi kết quả vào file CSV mới
            writer = csv.writer(new_csv_file)
            
            # Đọc từng dòng trong file CSV cũ
            for row in reader:
                # Lấy giá trị đầu của mỗi dòng
                first_value = row[0]
                first_value = first_value.replace("-","/")
                try:
                    last_value = row[1][i]
                except:
                    last_value = '0'
                # Ghi kết quả vào file CSV mới với giá trị đầu và cuối cách nhau bởi dấu phẩy
                writer.writerow([first_value, last_value])
