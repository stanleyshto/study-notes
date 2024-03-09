from matplotlib import pyplot as plt
import random, os

os.chdir('D:/myfiles/Study Notes/Python')

ages_x = [i for i in range(25,36)]
dev_y = [ random.randint(10000,50000) for i in range(0, 11)]
plt.plot(ages_x, dev_y, label='All Devs', color='g', linestyle='--')  #define the data value of a data series and create the label for the data series

py_dev_y = [ random.randint(20000,70000) for i in range(0, 11)]
plt.plot(ages_x, py_dev_y, label='Python Devs', color='#436E0F')

plt.legend()  #label for each data series
plt.xlabel('Ages') #label of x-axis
plt.ylabel('Median Salary (USD)') #label of y-axis
plt.title('Median Salary (USD) by Age') # chart title
plt.tight_layout()

plt.savefig('./graph1.png')  #use this commoand to save the chart

plt.show()  #use this commoand to show the chart

# bar chart
plt.bar(ages_x, py_dev_y, label='Python Devs', color='#436E0F')
plt.bar(ages_x, dev_y, label='All Devs', color='b', linestyle='--')
plt.legend()  #label for each data series
plt.xlabel('Ages') #label of x-axis
plt.ylabel('Median Salary (USD)') #label of y-axis
plt.title('Median Salary (USD) by Age') # chart title

plt.show()  #use this commoand to show the chart
