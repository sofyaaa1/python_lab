# -*- coding: utf8 -*-
import csv

def search_data(input_file, output_file):
    with open(output_file, 'w', newline='') as out_file:
        header = ['Country Name', '2019 [YR2019]']
        writer = csv.DictWriter(out_file, fieldnames=header)
        writer.writeheader()

    try:
        with open(input_file, 'r') as file:
            country = input('Введіть назви країн через крапку з комой: ').split(';')

            reader = csv.DictReader(file)
            for line in reader:
                if line['Country Name'] in country:
                    print(line['Country Name'], ':', line['2019 [YR2019]'])
                    with open(output_file, 'a', newline='') as out_file:
                        writer = csv.writer(out_file)
                        writer.writerow((line['Country Name'], line['2019 [YR2019]']))

    except:
        print(f'Файла з іменем - {input_file} не знайдено')


if __name__ == '__main__':

    input_file = 'b3bfd5c3-2b58-4f66-8e9f-7b0679a4997f_Data.csv'
    output_file = 'gdp_growth_2019.csv'

    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            print("Country Name: '2019 [YR2019]'")
            for line in reader:
                print(line['Country Name'], ':', line['2019 [YR2019]'])
    except:
        print(f'Файла з іменем - {input_file} не знайдено')

    search_data(input_file, output_file)
