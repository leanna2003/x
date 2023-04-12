import csv
import matplotlib.pyplot as plt

# csv file name
filename = "data.csv"


# Step 1: Reading CSV File
def read_csv():
    """
    Read csv content and printing to terminal.
    """
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))
    # printing the field names
    print('Field names are: ' + ', '.join(field for field in fields))
    print('\nAll rows are:\n')
    for row in rows:
        # parsing each column of a row
        for col in row:
            print("%10s" % col, end="  |"),
        print('\n')


# Step 2: Total Sale
def yearly_sales():
    """
    Calculating total sales for each year and saving to text file.
    """

    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        final_sales_output = []
        # extracting each data row one by one
        year = None
        for row in csvreader:
            if 2012 <= int(row[0]) <= 2021:
                year_sales = 0
                for ind, col in enumerate(row):
                    if ind == 0:
                        year = col
                    else:
                        year_sales += int(col)
                final_sales_output.append(year + " : " + str(year_sales))

        with open('stats.txt', 'w') as f:
            f.write("Yearly sales analysis"'\n')
            for yearly_sales in final_sales_output:
                f.write(yearly_sales)
                f.write('\n')


# Step 3: Bar Plot
def total_sales_bar_plot():
    """
    Calculating total sales for each year and creating bar plot.
    """

    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        x = []
        y = []
        # extracting each data row one by one
        year = None
        for row in csvreader:
            if 2012 <= int(row[0]) <= 2021:
                year_sales = 0
                for ind, col in enumerate(row):
                    if ind == 0:
                        year = col
                    else:
                        year_sales += int(col)
                x.append(year)
                y.append(year_sales)

        plt.figure(1)
        plt.barh(x, y)
        plt.title("Product Sales Yearly")
        plt.xlabel("Sales")
        plt.ylabel("Years")
        plt.grid()
        plt.show()


# Step 4: Sale Estimation
def sales_estimation():
    """
    Comparing & analyzing the sales.
    """

    sales_jan_jun_21 = 0
    sales_jan_jun_22 = 0
    SGR = 0
    estimated_sales_analysis_jul_dec_22 = []

    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            if row[0] == "2021":
                sales_jan_jun_21 = sum(int(col) for col in row[1:7])
            elif row[0] == "2022":
                sales_jan_jun_22 = sum(int(col) for col in row[1:7])

        # Calculating sales growth rate
        SGR = (sales_jan_jun_22-sales_jan_jun_21)/sales_jan_jun_22

        with open('stats.txt', 'a') as f:
            f.write('\n'"Sales growth analysis"'\n')
            f.write("Sales growth rate(SGR) : " + str(SGR))
            f.write('\n')

    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # Estimated sale calculation based on SGR
        for row in csvreader:
            if row[0] == "2021":
                for ind, col in enumerate(row):
                    estimated_sales = (int(col) + int(col))*SGR
                    if ind == 7:
                        estimated_sales_analysis_jul_dec_22.append("Jul_2022 : " + str(estimated_sales))
                    elif ind == 8:
                        estimated_sales_analysis_jul_dec_22.append("Aug_2022 : " + str(estimated_sales))
                    elif ind == 9:
                        estimated_sales_analysis_jul_dec_22.append("Sep_2022 : " + str(estimated_sales))
                    elif ind == 10:
                        estimated_sales_analysis_jul_dec_22.append("Oct_2022 : " + str(estimated_sales))
                    elif ind == 11:
                        estimated_sales_analysis_jul_dec_22.append("Nov_2022 : " + str(estimated_sales))
                    elif ind == 12:
                        estimated_sales_analysis_jul_dec_22.append("Dec_2022 : " + str(estimated_sales))

        with open('stats.txt', 'a') as f:
            f.write('\n'"Monthly estimated sales analysis for Jul-Dec'22"'\n')
            for monthly_estimated_sales in estimated_sales_analysis_jul_dec_22:
                f.write(monthly_estimated_sales)
                f.write('\n')


# Step 5: Horizontal Bar Plot
def total_sales_horizontal_bar_plot():
    """
    Calculating total sales for each year and creating horizontal bar plot.
    """

    x_estimated_month = []
    y_estimated_sales = []
    SGR = 0

    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            if row[0] == "2021":
                sales_jan_jun_21 = sum(int(col) for col in row[1:7])
            elif row[0] == "2022":
                sales_jan_jun_22 = sum(int(col) for col in row[1:7])

        # Calculating sales growth rate
        SGR = abs((sales_jan_jun_22-sales_jan_jun_21)/sales_jan_jun_22)

    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # Estimated sale calculation based on SGR
        for row in csvreader:
            if row[0] == "2021":
                for ind, col in enumerate(row):
                    estimated_sales = (int(col) + int(col)) * SGR
                    if ind == 7:
                        x_estimated_month.append("Jul'22")
                        y_estimated_sales.append(estimated_sales)
                    elif ind == 8:
                        x_estimated_month.append("Aug'22")
                        y_estimated_sales.append(estimated_sales)
                    elif ind == 9:
                        x_estimated_month.append("Sep'22")
                        y_estimated_sales.append(estimated_sales)
                    elif ind == 10:
                        x_estimated_month.append("Oct'22")
                        y_estimated_sales.append(estimated_sales)
                    elif ind == 11:
                        x_estimated_month.append("Nov'22")
                        y_estimated_sales.append(estimated_sales)
                    elif ind == 12:
                        x_estimated_month.append("Dec'22")
                        y_estimated_sales.append(estimated_sales)

    plt.figure(1)
    plt.barh(x_estimated_month, y_estimated_sales)
    plt.title("Product Estimated Sales Monthly")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid()
    plt.show()


# Call Function
read_csv()
#yearly_sales()
#total_sales_bar_plot()
#sales_estimation()
#total_sales_horizontal_bar_plot()