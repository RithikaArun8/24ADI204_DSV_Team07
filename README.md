# Black Friday Logistics Nightmare
## Project Overview

Black Friday Logistics Nightmare is a data analysis and visualization project that investigates delivery delays and logistics challenges in e-commerce during periods of high demand.

The project uses the Brazilian E-Commerce Public Dataset by Olist to analyze shipping and delivery performance. The study focuses on identifying factors that contribute to delivery delays and discovering potential bottlenecks in the e-commerce supply chain.

## Objectives

The main objectives of this project are to:

* Analyze e-commerce delivery performance.
* Identify patterns in shipping and delivery delays.
* Study the relationship between delivery time and estimated delivery time.
* Investigate the effect of product and seller-related factors on delivery.
* Analyze geographical patterns in delivery performance.
* Identify potential logistics bottlenecks.
* Generate insights that can help improve delivery efficiency and customer satisfaction.

## Dataset

This project uses the Brazilian E-Commerce Public Dataset by Olist.

The dataset contains information about orders placed through the Olist e-commerce platform in Brazil, including:

* Orders
* Customers
* Sellers
* Products
* Payments
* Reviews
* Order items
* Delivery information
* Product characteristics
* Customer and seller locations

The different datasets are connected using common identifiers such as order IDs, customer IDs, seller IDs, and product IDs.

## Key Factors Analyzed

The project investigates several factors that may influence delivery performance:

### Delivery Time

Analysis of the actual delivery time compared with the estimated delivery date.

### Product Weight

Investigation of whether heavier products are associated with longer delivery times.

### Seller Location

Analysis of seller locations and their relationship with delivery performance.

### Delivery Distance

Study of geographical distance between sellers and customers to identify its effect on shipping time.

### Estimated Delivery Time

Comparison between the estimated delivery date and the actual delivery date.

### Geographical Patterns

Identification of regions and locations where delivery delays occur more frequently.

## Data Analysis & Visualization

Various data analysis and visualization techniques are used to identify meaningful patterns in the dataset.

The project includes visualizations such as:

* Delivery time distribution
* Estimated vs. actual delivery time
* Delivery delays by seller location
* Delivery delays by customer location
* Product weight vs. delivery time
* Delivery distance vs. delivery time
* Shipping performance by region
* Order volume analysis
* Delayed vs. on-time deliveries
* Correlation analysis
* Geographical distribution of orders and sellers

## Key Questions

The analysis aims to answer questions such as:

1. What percentage of orders are delivered late?
2. Which factors contribute most to delivery delays?
3. Does product weight affect delivery time?
4. Does delivery distance affect shipping performance?
5. Which seller locations experience more delays?
6. Which customer regions receive more delayed orders?
7. How accurate are the estimated delivery dates?
8. Are certain product categories more likely to experience delays?
9. Are there geographical logistics bottlenecks?
10. How does high order volume affect delivery performance?

## Technologies Used

Python 3.x
Pandas – Data manipulation and analysis
NumPy – Numerical operations
Matplotlib – Data visualization
Seaborn– Statistical visualization
Scikit-learn – Data analysis and machine learning techniques
Jupyter Notebook / Google Colab – Development and analysis
GitHub– Version control and project documentation

## Project Workflow

Dataset Collection
        ↓
Data Cleaning
        ↓
Data Integration
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Statistical Analysis
        ↓
Data Visualization
        ↓
Identify Delivery Bottlenecks
        ↓
Generate Logistics Insights

## Data Preprocessing

The dataset is prepared for analysis through several preprocessing steps:

* Handling missing values
* Removing duplicate records
* Converting date columns into appropriate datetime formats
* Merging relevant Olist datasets
* Creating delivery-time features
* Calculating delivery delays
* Calculating geographical distance
* Handling inconsistent or invalid values
* Preparing categorical and numerical variables for analysis

## Important Derived Features

Additional features are created from the original dataset to support the analysis.

### Delivery Time

Delivery Time = Actual Delivery Date - Order Purchase Date

### Delivery Delay

Delivery Delay = Actual Delivery Date - Estimated Delivery Date

A positive delay indicates that an order was delivered after the estimated date.

### Delivery Distance

The geographical coordinates of customers and sellers can be used to estimate the distance between the two locations.

## Expected Insights

The analysis is expected to reveal:

* Major factors responsible for delivery delays.
* Regions with relatively poor delivery performance.
* The relationship between shipping distance and delivery time.
* The effect of product characteristics on logistics.
* Differences in delivery performance among sellers.
* Potential supply-chain bottlenecks.
* Areas where logistics planning can be improved.

## Recommendations

Based on the analysis, possible logistics improvements may include:

* Better demand forecasting during peak shopping periods.
* Strategic placement of warehouses and fulfillment centers.
* Improved seller and carrier coordination.
* More accurate delivery-time estimation.
* Regional logistics optimization.
* Better inventory planning.
* Early identification of high-risk delayed orders.

## Results

The project uses exploratory data analysis and visualization to identify patterns in e-commerce logistics and delivery delays.

The final results will highlight the major factors associated with delayed deliveries and identify geographical and operational areas that may require logistics improvements.

## Future Scope

The project can be extended by:

* Building a machine learning model to predict delivery delays.
* Developing a real-time logistics dashboard.
* Predicting high-risk orders before shipment.
* Applying route optimization techniques.
* Incorporating real-time weather and traffic information.
* Comparing logistics performance across different periods.
* Developing an automated delivery-risk scoring system.

## Dataset

The datasets used in this project are:

- **DataCoSupplyChainDataset**
- **tokenized_access_logs**
- **DescriptionDataCoSupplyChain**
Due to GitHub file-size limitations, the datasets are stored separately.

### Dataset Source

https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis

## Conclusion

Black Friday Logistics Nightmare demonstrates how data analysis can be used to understand complex e-commerce logistics problems.

By analyzing delivery times, shipping distances, seller locations, product characteristics, and estimated delivery dates, the project aims to identify delivery bottlenecks and provide data-driven insights for improving logistics efficiency and customer satisfaction.
