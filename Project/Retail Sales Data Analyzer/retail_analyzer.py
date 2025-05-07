import numpy as np
import pandas as pd

class RetailAnalyzer:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
        print("Checking for missing values.....")
        
        if self.data.isnull().values.any():
            print("Total Missing values found: ")
            print(self.data.isnull().sum())
        else:
            print("No missing values found.")

        for col in self.data.columns:
            if self.data[col].dtype in [np.float64, np.int64]:
                self.data[col] = self.data[col].fillna(0)
            else:
                self.data[col] = self.data[col].fillna("Unknown")
        
        print("Missing values handled")

    def calculate_metrics(self):
        if self.data is None:
            print("No data found.....")
            return

        required_columns = {"Total Sales", "Product", "Date"}
        if not required_columns.issubset(self.data.columns):
            print(f"Missing required columns: {required_columns - set(self.data.columns)}")
            return

        self.data["Date"] = pd.to_datetime(self.data["Date"], format="%d-%m-%Y", errors="coerce")
        self.data.dropna(subset=["Date"], inplace=True)

        self.data["Total Sales"] = pd.to_numeric(self.data["Total Sales"], errors="coerce").fillna(0)

        total_sales_sum = self.data["Total Sales"].sum()
        if total_sales_sum > 0: 
            self.data["Sales_Percentage"] = np.round(
                (self.data["Total Sales"] / total_sales_sum) * 100, 2
            )
        else:
            self.data["Sales_Percentage"] = 0

        self.data.sort_values(by="Date", inplace=True)
        
        self.data["Growth_Rate"] = self.data["Total Sales"].pct_change()
        self.data["Growth_Rate"] = np.round(
            self.data["Growth_Rate"].fillna(0) * 100, 2
        )

        print("Computed Metrics Added: ")
        print(self.data[["Date", "Total Sales", "Sales_Percentage", "Growth_Rate"]].head())

        total_sales = self.data["Total Sales"].sum()
        avg_sales = self.data["Total Sales"].mean()
        most_popular_product = self.data["Product"].value_counts().idxmax()
        print(f"Total Sales: {total_sales}")
        print(f"Average Sales: {avg_sales}")
        print(f"Most Popular Product: {most_popular_product}")

    def filter_data(self, condition):
        if self.data is None:
            print("No data found.....")
            return

        try:
            filtered = self.data.query(condition)
            print(f"Filtered Data ({len(filtered)} records):")
            print(filtered.head())
            return filtered
        except Exception as e:
            print("Error in filter condition:", str(e))

    def aggregate_sales(self):
        if self.data is None:
            print("No data found.....")
            return

        group_columns = []

        if 'Product' in self.data.columns:
            group_columns.append('Product')
        if 'Category' in self.data.columns:
            group_columns.append('Category')
        if 'Date' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'], format="%d-%m-%Y", errors='coerce')
            self.data['Month'] = self.data['Date'].dt.to_period('M')
            group_columns.append('Month')

        if not group_columns:
            print("No groupable columns (Product, Category, Date) found.")
            return

        self.data["Total Sales"] = pd.to_numeric(self.data["Total Sales"], errors="coerce").fillna(0)
        
        aggregated = self.data.groupby(group_columns).agg({'Total Sales': 'sum'}).reset_index()
        print("Aggregated Sales Data: ")
        print(aggregated.head())
        return aggregated

    def display_summary(self):
        if self.data is None:
            print("No data found.....")
            return
        
        print("Data Summary: ")
        print(self.data.describe(include="all"))
        print("Data Info: ")
        print(self.data.info())

analyzer = RetailAnalyzer()

ans = input("Do you want to input data from retail_sales.csv file?\nAnswer in yes or no: ").lower()
if ans == "yes":
    file_path = "retail_sales.csv"
    analyzer.load_data(file_path)
    analyzer.calculate_metrics()
    analyzer.aggregate_sales()
    analyzer.display_summary()
else:
    print("End of the program......")
    exit()
