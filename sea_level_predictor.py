import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
  df.plot(kind="scatter", x="Year", y="CSIRO Adjusted Sea Level")


    # Create first line of best fit
  from scipy.stats import linregress
  m = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
  t = [m.slope * i + m.intercept for i in df["Year"]]
  df["trend"] = t
  ax = df.plot.scatter(x='Year',
                       y='CSIRO Adjusted Sea Level')
  df.plot.line(x='Year',
               y='trend', 
               color='red', 
               ax=ax, 
               figsize = (16,8))
  ar = np.arange(2014,2051).tolist()

  df1 = pd.DataFrame({"Year" : ar})

  df = pd.read_csv("epa-sea-level.csv")

  df2 = df.append(df1, ignore_index=True)

  t = [m.slope*i + m.intercept for i in df2["Year"]]

  df2["trend"] = t

  ax = df.plot.scatter(x='Year',
                       y='CSIRO Adjusted Sea Level')
  df2.plot.line(x='Year',
               y='trend', 
               color='red', 
               ax=ax, 
               figsize = (16,8))


    # Create second line of best fit
  m1 = linregress(df3["Year"], df3["CSIRO Adjusted Sea Level"])
  df4 = df3.append(df1, ignore_index=True)
  t = [m.slope*i + m.intercept for i in df4["Year"]]
  df4["trend"] = t
  ax = df3.plot.scatter(x='Year',
                       y='CSIRO Adjusted Sea Level')
  df4.plot.line(x='Year',
               y='trend', 
               color='red', 
               ax=ax, 
               figsize = (16,8))


    # Add labels and title
  ax = df3.plot.scatter(x='Year',
                       y='CSIRO Adjusted Sea Level')
  ax.set_xlabel("Year")
  ax.set_ylabel("Sea Level (inches)")
  ax.set_title("Rise in Sea Level")
  df4.plot.line(x='Year',
               y='trend', 
               color='red', 
               ax=ax, 
               figsize = (16,8))

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()