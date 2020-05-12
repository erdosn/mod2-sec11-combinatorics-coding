import custom_functions.combinatorics as c
import custom_functions.plotting_functions as pf

if __name__ == "__main__":
    data = c.generate_data(100)
    print(data)
    pf.plot_histogram(data)
