# Brazil Real Estate Analysis

This Streamlit application provides an interactive analysis of the Brazilian real estate market. It combines data preprocessing, visualization, and storytelling to uncover valuable insights about property prices and trends across Brazil.

## Key Features

1. **Geographical Distribution**
   - An interactive map displays properties across Brazil, showing their locations and price ranges.

2. **Price Trends**
   - A histogram highlights the distribution of home prices, revealing a concentration of lower-priced homes and a few high-value outliers.
   - A bar chart shows the average price of homes by region, helping to identify high-value areas.

3. **Home Sizes**
   - A box plot illustrates the range of home sizes, highlighting typical property sizes and large outliers.

4. **Regional Insights**
   - Specific analysis for Rio Grande do Sul includes a scatter plot showing the relationship between home size and price.
   - Correlation analysis across southern states uncovers relationships between property size and price.

## Data Used

The analysis combines two datasets:
- `brasil-real-estate-1.csv`
- `brasil-real-estate-2.csv`

### Preprocessing Steps
1. Dropped missing values.
2. Extracted latitude and longitude for mapping.
3. Converted prices to USD for uniformity.
4. Combined both datasets into a single DataFrame for analysis.

## Visualizations

- **Interactive Map:** Shows property locations and their price ranges using Plotly's Mapbox.
- **Histograms:** Visualize the distribution of home prices.
- **Box Plot:** Displays the distribution of property sizes.
- **Bar Chart:** Shows average property prices by region.
- **Scatter Plot:** Examines the relationship between home size and price in Rio Grande do Sul.

## Insights

1. **Home Prices:**
   - Most properties are priced on the lower end, with few outliers.
   - Regional price variations are significant, with some regions being more expensive.

2. **Property Sizes:**
   - Typical homes fall within a specific size range, with some very large properties creating outliers.

3. **Regional Trends:**
   - Larger homes tend to have higher prices in Rio Grande do Sul.
   - Correlation analysis reveals varying relationships between size and price across different states in the southern region.

## How to Run

1. Clone this repository.
2. Place the `brasil-real-estate-1.csv` and `brasil-real-estate-2.csv` files in a `data` directory.
3. Install the required dependencies:
   ```bash
   pip install streamlit pandas matplotlib plotly
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Outputs

The app generates insights in both tabular and visual forms, helping users make informed decisions about the Brazilian real estate market.

## License

This project is licensed under the MIT License. Feel free to use and modify it as per your requirements.

