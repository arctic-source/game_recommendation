import csv


def append_to_csv(file_name_results, steam_id):
    with open(file_name_results, mode='a', newline='') as f:
        writer_object = csv.writer(f, delimiter=',')
        writer_object.writerow([steam_id])