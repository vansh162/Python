import numpy as np
import pandas as pd
    
class RetailAnalyzer:
    def __init__(self):
        self.data = None
        
    def load_data(self,file_path):
            self.data = pd.read_csv(file_path)
            print("Checking for missing values.....")
            if self.data.isnull().values.any():
                print("Total Missing values found: ")
                print(self.data.isnull().sum())
            else:
                print("No missing values found.")
            
            for col in self.data.columns:
                if self.data[col].dtype in [np.float64, np.int64]:
                    self.data[col].fillna(0, inplace=True)
                else:
                    self.data[col].fillna("Unknown", inplace=True)
            print("Missing values handled")

        
    
    def calculate_metrics(self):
        if self.data is None:
            print("No data found.....")
            return
        
        required_columns = {"Sales","Product","Date"}
        if not required_columns.issubset(self.data.columns):
            print(f"Missing required columns: {required_columns - set(self.data.columns)}")
            return
        
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')
        self.data.dropna(subset=['Date'], inplace=True)
        
        self.data['Sales_Percentage'] = np.round(
            self.data['Sales'] / self.data['Sales'].sum() * 100, 2
        )
        
        self.data.sort_values(by='Date', inplace=True)
        self.data['Growth_Rate'] = np.round(
            self.data['Sales'].pct_change().fillna(0) * 100, 2
        )
        
        print("Computed Metrics Added: ")
        print(self.data[['Date', 'Sales', 'Sales_Percentage', 'Growth_Rate']].head())
        
        total_sales = self.data["Sales"].sum()
        avg_sales = self.data["Sales"].mean()
        most_popular_product = self.data["Product"].value_counts().idxmax()
        print(f"Total Sales: {total_sales}")
        print(f"Average Sales: {avg_sales}")
        print(f"Most Popular Product: {most_popular_product}")
        
    def filter_data(self,condition):
        if self.data is None:
            print("No data found.....")
            return
        
        try:
            filtered = self.data.query(condition)
            print(f"Filtered Data ({len(filtered)} records: )")
            print(filtered.head())
            return filtered
        except Exception as e:
            print("Error in filter condition: ",str(e))
            
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
            group_columns.append(self.data['Date'].dt.to_period('M'))

        if not group_columns:
            print("No groupable columns (Product, Category, Date) found.")
            return

        aggregated = self.data.groupby(group_columns).agg({'Sales': 'sum'}).reset_index()
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
    print("File loaded successfully.....")
    analyzer.load_data("retail_sales.csv")
    analyzer.calculate_metrics()
    analyzer.aggregate_sales()
    analyzer.display_summary()
    
else:
    print("End of the program......")
    exit()