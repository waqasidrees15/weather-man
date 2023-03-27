import sys
from colored import fg

months_with_full_name = {1: "January",
                         2: "February",
                         3: "March",
                         4: "April",
                         5: "May",
                         6: "June",
                         7: "July",
                         8: "August",
                         9: "September",
                         10: "October",
                         11: "November",
                         12: "December",
                                          }

months = {1: "Jan",
          2: "Feb",
          3: "Mar",
          4: "Apr",
          5: "May",
          6: "Jun",
          7: "Jul",
          8: "Aug",
          9: "Sep",
          10: "Oct",
          11: "Nov",
          12: "Dec"
                       }


def task1(year):
    try:
        days_data = []
        for month in months:
            with open(f"lahore_weather/lahore_weather_{year}_{months[month]}.txt") as file:
                months_data = []
                for line in file:
                    months_data.append(line.rstrip())

                for i in range(1, len(months_data) - 2):
                    d = months_data[i + 1].split(",")
                    days_data.append(d)

        max_temp_data_list = []
        min_temp_data_list = []
        humid_data_list = []
        max_temp_year_data = {}
        min_temp_year_data = {}
        humid_year_data = {}
        for value in days_data:
            if value[1] != "" or value[3] != "" or value[7] != "":
                max_temp_year_data[int(value[1])] = value[0]
                min_temp_year_data[int(value[3])] = value[0]
                humid_year_data[int(value[7])] = value[0]
                max_temp_data_list.append(int(value[1]))
                min_temp_data_list.append(int(value[3]))
                humid_data_list.append(int(value[7]))

        max_temp = max(max_temp_data_list)
        min_temp = min(min_temp_data_list)
        humid = max(humid_data_list)

        full_name_month_for_max = int(max_temp_year_data[max_temp].split("-")[int(1)])
        full_name_month_for_min = int(min_temp_year_data[min_temp].split("-")[int(1)])
        full_name_month_for_humid = int(humid_year_data[humid].split("-")[int(1)])

        print(
            f"""Highest: {max_temp}C on {months_with_full_name[full_name_month_for_max]} {max_temp_year_data[max_temp].split("-")[2]} """)
        print(
            f"""Lowest: {min_temp}C on {months_with_full_name[full_name_month_for_min]} {min_temp_year_data[min_temp].split("-")[2]}""")
        print(
            f"""Humid: {humid}% on {months_with_full_name[full_name_month_for_humid]} {humid_year_data[humid].split("-")[2]}""")
    except:
        print("""you have enter an wrong input. your input must be like -e year,
or you have enter an wrong year try 1997-2011""")


def task2(year_month):
    try:
        year, month = year_month.split("/")
        days_data = []
        with open(f"lahore_weather/lahore_weather_{year}_{months[int(month)]}.txt") as file:
            months_data = []
            for line in file:
                months_data.append(line.rstrip())

            for i in range(1, len(months_data) - 2):
                d = months_data[i + 1].split(",")
                days_data.append(d)

        mean_temp_data_list = []
        humid_data_list = []
        for value in days_data:
            if value[2] != "" or value[8] != "":
                mean_temp_data_list.append(int(value[2]))
                humid_data_list.append(int(value[8]))
        try:
            mean_temp_max = max(mean_temp_data_list)
            mean_temp_min = min(mean_temp_data_list)
            humid = max(humid_data_list)
        except:
            print("Data not available")
        else:
            print(f"Highest Average: {mean_temp_max}C")
            print(f"Lowest Average: {mean_temp_min}C")
            print(f"Average Humidity: {humid}%")
    except:
        print("""you have enter an wrong input. your input must be like -a year/month,
or you have enter an wrong year or month try 1997-2011""")


def task3(year_month):
    try:
        year, month = year_month.split("/")
        days_data = []
        with open(f"lahore_weather/lahore_weather_{year}_{months[int(month)]}.txt") as file:
            months_data = []
            for line in file:
                months_data.append(line.rstrip())
            for i in range(1, len(months_data) - 2):
                d = months_data[i + 1].split(",")
                days_data.append(d)

        print(f"{months_with_full_name[int(month)]} {year}")
        for value in days_data:
            if value[1] != "" or value[3] != "":
                date = value[0].split("-")[2]
                print(
                    f'''{fg("white")}{date} {fg("red")}{''.join(["+" for _ in range(int(value[1]))])} {fg("white")} {value[1]}C''')
                print(
                    f'''{fg("white")}{date} {fg("blue")}{''.join(["+" for _ in range(int(value[3]))])} {fg("white")}{value[3]}C''')
    except:
        print("""you have enter an wrong input. your input must be like -c year/month,
or you have enter an wrong year or month try 1997-2011""")


def task4(year_month):
    try:
        year, month = year_month.split("/")
        days_data = []
        with open(f"lahore_weather/lahore_weather_{year}_{months[int(month)]}.txt") as file:
            months_data = []
            for line in file:
                months_data.append(line.rstrip())
            for i in range(1, len(months_data) - 2):
                d = months_data[i + 1].split(",")
                days_data.append(d)

        print(f"{months_with_full_name[int(month)]} {year}")
        for value in days_data:
            if value[1] != "" or value[3] != "":
                date = value[0].split("-")[2]
                print(
                    f''' {fg("white")}{date} {fg("blue")}{''.join(["+" for _ in range(int(value[3]))])}{fg("red")}{''.join(["+" for _ in range(int(value[1]))])} {fg("white")}{value[3]}C - {value[1]}C''')
    except:
        print("""you have enter an wrong input. your input must be like -d year/month,
or you have enter an wrong year or month try 1997-2015""")


n = (sys.argv)
if n[1] == '-e':
    task1(n[2])
elif n[1] == '-a':
    task2(n[2])
elif n[1] == "-c":
    task3(n[2])
elif n[1] == '-d':
    task4(n[2])
