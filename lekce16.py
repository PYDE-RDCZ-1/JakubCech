import csv
import numpy as np


average_salaries = []

with open("average_salary.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        average_salaries.append(int(row[1]))

print(average_salaries)

salaries_array = np.array(average_salaries)

mean_salary = np.mean(salaries_array)

median_salary = np.median(salaries_array)

smer_odchylka = round(np.std(salaries_array), 2)

print("Mean: ", mean_salary)
print("Median: ", median_salary)
print("Smerodatna odchylka: ", smer_odchylka)