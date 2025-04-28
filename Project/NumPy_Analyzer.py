import numpy as np

class DataAnalytics:
    def _init_(self):
        self.array = None

    def create_array(self):
        print("Array Creation:")
        print("Select the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.array = np.array(elements)
        elif choice == 2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            elements = list(map(int, input(f"Enter {rows * cols} elements separated by space: ").split()))
            self.array = np.array(elements).reshape(rows, cols)
        elif choice == 3:
            dim1 = int(input("Enter size of 1st dimension: "))
            dim2 = int(input("Enter size of 2nd dimension: "))
            dim3 = int(input("Enter size of 3rd dimension: "))
            elements = list(map(int, input(f"Enter {dim1 * dim2 * dim3} elements separated by space: ").split()))
            self.array = np.array(elements).reshape(dim1, dim2, dim3)
        else:
            print("Invalid choice!")

        print("Array created successfully:")
        print(self.array)
        self.index_slice_menu()

    def index_slice_menu(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                idx = tuple(map(int, input("Enter index/indices separated by space: ").split()))
                try:
                    if len(idx) == self.array.ndim:
                        print(f"Element at {idx}: {self.array[idx]}")
                    else:
                        print("Number of indices does not match array dimensions.")
                except Exception as e:
                    print(f"Indexing error: {e}")
            elif choice == 2:
                self.slice_array()
            elif choice == 3:
                break
            else:
                print("Invalid choice!")

    def slice_array(self):
        if self.array is None:
            print("No array available.")
            return

        print(f"Array:\n{self.array}")

        try:
            if self.array.ndim == 1:
                range_input = input("Enter the slicing range for 1D array (start:end): ").strip()
                start, end = map(int, range_input.split(':'))
                sliced = self.array[start:end]
                print(f"Sliced Array:\n{sliced}")

            elif self.array.ndim == 2:
                row_range = input("Enter the row range (start:end): ").strip()
                col_range = input("Enter the column range (start:end): ").strip()
                row_start, row_end = map(int, row_range.split(':'))
                col_start, col_end = map(int, col_range.split(':'))
                sliced = self.array[row_start:row_end, col_start:col_end]
                print(f"Sliced Array:\n{sliced}")

            elif self.array.ndim == 3:
                dim1_range = input("Enter the 1st dimension range (start:end): ").strip()
                dim2_range = input("Enter the 2nd dimension range (start:end): ").strip()
                dim3_range = input("Enter the 3rd dimension range (start:end): ").strip()
                d1_start, d1_end = map(int, dim1_range.split(':'))
                d2_start, d2_end = map(int, dim2_range.split(':'))
                d3_start, d3_end = map(int, dim3_range.split(':'))
                sliced = self.array[d1_start:d1_end, d2_start:d2_end, d3_start:d3_end]
                print(f"Sliced Array:\n{sliced}")
            else:
                print("Unsupported array dimension.")
        except Exception as e:
            print(f"Error during slicing: {e}")

    def math_operations(self):
        if self.array is None:
            print("No array available.")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter your choice: "))

        elements = list(map(int, input(f"Enter {self.array.size} elements for the second array separated by space: ").split()))
        second_array = np.array(elements).reshape(self.array.shape)

        print("Original Array:")
        print(self.array)
        print("Second Array:")
        print(second_array)

        if choice == 1:
            result = self.array + second_array
        elif choice == 2:
            result = self.array - second_array
        elif choice == 3:
            result = self.array * second_array
        elif choice == 4:
            result = self.array / second_array
        else:
            print("Invalid choice!")
            return

        print("Result of Operation:")
        print(result)

    def combine_split_arrays(self):
        if self.array is None:
            print("No array available.")
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = list(map(int, input(f"Enter {self.array.size} elements for another array: ").split()))
            second_array = np.array(elements).reshape(self.array.shape)
            combined = np.vstack((self.array, second_array))
            print("Combined Array (Vertical Stack):")
            print(combined)

        elif choice == 2:
            sections = int(input("Into how many parts do you want to split?: "))
            try:
                split_arrays = np.array_split(self.array, sections)
                print("Split Arrays:")
                for idx, arr in enumerate(split_arrays):
                    print(f"Part {idx+1}:\n{arr}")
            except Exception as e:
                print(f"Error during splitting: {e}")
        else:
            print("Invalid choice!")

    def search_sort_filter(self):
        if self.array is None:
            print("No array available.")
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter the value to search: "))
            result = np.where(self.array == val)
            print(f"Value found at indices: {result}")

        elif choice == 2:
            sorted_array = np.sort(self.array, axis=1 if self.array.ndim > 1 else 0)
            print("Sorted Array:")
            print(sorted_array)

        elif choice == 3:
            cond = int(input("Enter the value to filter greater than: "))
            filtered = self.array[self.array > cond]
            print(f"Filtered Array (elements > {cond}):")
            print(filtered)
        else:
            print("Invalid choice!")

    def aggregates_statistics(self):
        if self.array is None:
            print("No array available.")
            return

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Min and Max")
        print("7. Percentiles")
        print("8. Correlation Coefficient (for 1D arrays only)")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Sum: {np.sum(self.array)}")
        elif choice == 2:
            print(f"Mean: {np.mean(self.array)}")
        elif choice == 3:
            print(f"Median: {np.median(self.array)}")
        elif choice == 4:
            print(f"Standard Deviation: {np.std(self.array)}")
        elif choice == 5:
            print(f"Variance: {np.var(self.array)}")
        elif choice == 6:
            print(f"Minimum: {np.min(self.array)}, Maximum: {np.max(self.array)}")
        elif choice == 7:
            percentile = float(input("Enter the percentile (0-100): "))
            print(f"{percentile}th Percentile: {np.percentile(self.array, percentile)}")
        elif choice == 8:
            if self.array.ndim == 1:
                another = list(map(int, input("Enter another 1D array of same size separated by space: ").split()))
                another_array = np.array(another)
                coeff = np.corrcoef(self.array, another_array)
                print("Correlation Coefficient Matrix:")
                print(coeff)
            else:
                print("Correlation requires 1D arrays.")
        else:
            print("Invalid choice!")

    @staticmethod
    def welcome_message():
        print("Welcome to the NumPy Analyzer!")
        print("=" * 30)

    @classmethod
    def quality_message(cls):
        print('"Quality is our Motto."')

def main():
    analyzer = DataAnalytics()
    analyzer.welcome_message()
    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            analyzer.create_array()
        elif choice == 2:
            analyzer.math_operations()
        elif choice == 3:
            analyzer.combine_split_arrays()
        elif choice == 4:
            analyzer.search_sort_filter()
        elif choice == 5:
            analyzer.aggregates_statistics()
        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            analyzer.quality_message()
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()