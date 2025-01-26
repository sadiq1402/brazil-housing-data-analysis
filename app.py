import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Brazil Real Estate Analysis")

# Load datasets
df1 = pd.read_csv("data/brasil-real-estate-1.csv")
df2 = pd.read_csv("data/brasil-real-estate-2.csv")

# Preprocess df1
df1 = df1.dropna()
df1["lat"] = df1["lat-lon"].apply(lambda x: x.split(",")[0]).astype("float")
df1["lon"] = df1["lat-lon"].apply(lambda x: x.split(",")[1]).astype("float")
df1["state"] = df1["place_with_parent_names"].apply(lambda x: x.split("|")[2])
df1["price_usd"] = (
    df1["price_usd"].str.replace("$", "").str.replace(",", "").astype("float")
)
df1 = df1.drop(columns=["lat-lon", "place_with_parent_names"])

# Preprocess df2
df2["price_usd"] = df2["price_brl"] / 3.19
df2 = df2.drop(columns=["price_brl"])
df2 = df2.dropna()

# Combine datasets
df = pd.concat([df1, df2])

st.subheader("Combined Dataset Info")
st.write(df.info())

# Storytelling
st.subheader("Storytelling: Insights from the Data")
st.markdown(
    """
The Brazilian real estate market offers a diverse range of opportunities, and this analysis reveals key trends:

1. **Geographical Distribution:**
   Homes are distributed across Brazil, with prices varying significantly by location. The interactive map highlights the concentration of properties and their respective price ranges.

2. **Price Trends:**
   - The histogram of home prices shows a skewed distribution, indicating a majority of properties are priced in the lower range, with a few high-value outliers.
   - The mean price of homes varies by region, with some regions being significantly more expensive than others, as shown in the bar chart.

3. **Home Sizes:**
   The box plot reveals the distribution of home sizes, with most properties falling within a specific range, but some significantly larger homes creating outliers.

4. **Regional Insights:**
   - In Rio Grande do Sul, a scatter plot shows a positive correlation between home size and price, confirming the general trend that larger homes tend to cost more.
   - Correlation analysis for the southern states provides deeper insights into how price and size relate across different areas.

These findings help stakeholders make informed decisions about investments, highlighting regions of interest and price trends.
"""
)

# Map visualization
st.subheader("Real Estate Map")
fig_map = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    center={"lat": -14.2, "lon": -51.9},
    hover_data=["price_usd"],
    width=600,
    height=600,
)
fig_map.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig_map)

# Summary statistics
st.subheader("Summary Statistics")
summary_stats = df.describe()[["area_m2", "price_usd"]]
st.write(summary_stats)

# Histogram of home prices
st.subheader("Distribution of Home Prices")
plt.figure(figsize=(10, 5))
plt.hist(x=df["price_usd"], bins=30, color="blue", edgecolor="black")
plt.xlabel("Price [USD]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices")
st.pyplot(plt)

# Box plot of home sizes
st.subheader("Distribution of Home Sizes")
plt.figure(figsize=(10, 5))
plt.boxplot(df["area_m2"], vert=False)
plt.xlabel("Area [sq meters]")
plt.title("Distribution of Home Sizes")
st.pyplot(plt)

# Bar chart: Mean price by region
st.subheader("Mean Home Price by Region")
mean_price_by_region = df.groupby("region")["price_usd"].mean()
mean_price_by_region.plot(kind="bar", title="Mean Home Price by Region", color="orange")
plt.xlabel("Region")
plt.ylabel("Mean Price [USD]")
st.pyplot(plt)

# Scatter plot: Rio Grande do Sul
st.subheader("Rio Grande do Sul: Price vs. Area")
df_south_rgs = df[df["state"] == "Rio Grande do Sul"]
plt.figure(figsize=(10, 5))
plt.scatter(
    df_south_rgs["area_m2"], df_south_rgs["price_usd"], alpha=0.6, color="green"
)
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title("Rio Grande do Sul: Price vs. Area")
st.pyplot(plt)

# Correlation analysis
st.subheader("Correlation: South Region States")
df_south = df[df["region"] == "South"]
south_states_corr = {
    state: state_data["area_m2"].corr(state_data["price_usd"])
    for state, state_data in df_south.groupby("state")
}
st.write(south_states_corr)
