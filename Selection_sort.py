import time
import re

def selection_sort(arr):
    n = len(arr)
    start_sort_time = time.time() 
    for i in range(n):
        max_idx = i  
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    end_sort_time = time.time()  
    print("Sorting Time: {:.6f} seconds".format(end_sort_time - start_sort_time))  
    return arr

def write_sorted_to_file(filename, sorted_data):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write("ID, Name\n")
        for row in sorted_data:
            file.write(f"{row[0]}, {row[1]}\n")

def extract_id_name_from_sql(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.search(r"\((\d+),\s*'([^']+)'", line)
            if match:
                id = int(match.group(1))
                name = match.group(2)
                data.append((id, name))
    return data

if __name__ == "__main__":
    sql_file = "province.sql"
    sorted_file = "selection_sorted_province.txt"

    extracted_data = extract_id_name_from_sql(sql_file)

    start = time.time()
    sorted_data = selection_sort(extracted_data)
    end = time.time()  
    print("Total Program Execution Time: {:.6f} seconds".format(end - start))

    write_sorted_to_file(sorted_file, sorted_data)
    print(f"Sorted data written to {sorted_file}")