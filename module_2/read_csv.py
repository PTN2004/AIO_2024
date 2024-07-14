import pandas as pd
import numpy as np

df = pd.read_csv('module_2/data/advertising.csv')
data = df.to_numpy()
sales = data[:, 3]
max_sale = np.max(sales, keepdims=True)
print(max_sale, np.argmax(sales))

# mean TV colums
lenght = len(data[:0])
mean_tv = np.mean(data[:, 0])
print(f'The average value of the TV colunm is: {mean_tv}')

# count sales >= 20
count_sale = np.sum(sales >= 20)
print(f'The value of the sales colunm greater than or equal to 20 is {count_sale}')

# Calculate the average value of the Radio column that satisfies the condition that 
# the corresponding value on the Sales column is greater than or equal to 15
average = data[:, 1].mean(where=sales >= 15)
print(f'The average value of the Radio column that satisfies the condition that the corresponding value on the Sales column is greater than or equal to 15 is {average}')

# There is a value in the sales column where the value in the newspaper
#  column in that row is greater than or equal to the average of that column
average_newspaper_cl = data[:,2].mean()
sum_sales_cl = data[:,3].sum(where=data[:,2] >= average_newspaper_cl)

print(f'There is a value in the sales column where the value in the newspaper column in that row is greater than or equal to the average of that column {sum_sales_cl}')

# The new column is score
def new_column_condition(value, condition):
    if value > condition:
        return "Good"
    elif value < condition:
        return "Bad"
    else:
        return "Average"

average_sales_cl = sales.mean()
new_column_condition = np.vectorize(new_column_condition)
score1 = new_column_condition(sales, average_sales_cl)
print(f"Result of score1[7:10] = {score1[7:10]}")

# The new column with condition
distance_elemet_with_average = np.abs(sales - average_sales_cl)
value_near_idx = np.argmin(distance_elemet_with_average)
value_near_average = sales[value_near_idx]

scores2 = new_column_condition(sales, value_near_average)
print(f"Result of scores2[7:10] = {scores2[7:10]}")
