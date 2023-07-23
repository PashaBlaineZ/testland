import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("data.db")
cur = con.cursor()

time_list = []
cpu_usage_list = []
ram_usage_list = []


cur.execute("SELECT * from info ORDER BY TIME desc LIMIT 10")
rows = cur.fetchall()


for row in rows:
    time_list.append(row[0])
    cpu_usage_list.append(row[1])
    ram_usage_list.append(row[2])


print(time_list)
print(cpu_usage_list)

time_list.reverse()
cpu_usage_list.reverse()
ram_usage_list.reverse()

plt.plot(time_list, cpu_usage_list, ram_usage_list)
plt.xlabel('Время')
plt.ylabel('Проценты Загрузки CPU')
plt.show()
cur.close()