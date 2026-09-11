# Brazilian E-Commerce Sales, Customer & Delivery Analysis

## 1. Project Overview

This project analyzes the Brazilian E-Commerce Public Dataset by Olist to identify business opportunities and performance gaps related to sales, product categories, regional performance, delivery reliability, customer satisfaction, payments, and customer retention.

The analysis was prepared as a Data Analyst assessment project using Python and Pandas.

## 2. Business Problem

Management wants to understand:

- Which product categories and regions drive the most revenue?
- How does delivery performance relate to customer satisfaction?
- Which payment methods are most important?
- How strong is customer repeat purchasing?
- What actions can improve customer experience and sustainable growth?

## 3. Dataset

**Dataset:** Brazilian E-Commerce Public Dataset by Olist  
**Source:** Kaggle / Olist  
**Source URL:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The project uses nine related CSV files covering orders, order items, customers, products, sellers, payments, reviews, geolocation and product-category translation.

## 4. Key Analysis Approach

1. Loaded the raw CSV files using Pandas.
2. Converted order date fields to datetime.
3. Joined product information with product-category translation.
4. Aggregated order-item, payment and review tables before joining them to the order-level table.
5. Created business metrics including:
   - Revenue
   - Freight cost
   - Freight percentage
   - Delivery days
   - Difference from estimated delivery date
   - On-time delivery flag
   - Repeat-customer flag
   - Monthly order period
6. Restricted delivery-performance analysis to delivered orders where appropriate.
7. Created summary tables for categories, states, payments and delivery/review performance.

## 5. Key Findings

- Health & beauty is the highest-revenue product category in the analysis.
- São Paulo (SP) is the largest customer-state revenue contributor.
- Credit card is the dominant payment method.
- Repeat purchasing represents a relatively small share of unique customers.
- Delivery timing is strongly associated with review scores: late orders receive substantially lower average ratings than on-time/early orders.

## 6. Dashboard

The Looker Studio dashboard is designed for business management rather than technical users.

### Executive KPIs

- Delivered Orders
- Revenue
- Average Order Value
- Average Review Score
- On-Time Delivery Rate
- Repeat Customer Rate

### Main Visuals

1. Monthly Revenue & Orders Trend — line chart
2. Top 10 Product Categories by Revenue — horizontal bar chart
3. Revenue by Customer State — horizontal bar chart
4. Review Score by Delivery Performance — column/bar chart
5. Payment Method Usage — bar chart
6. Revenue vs Freight — scatter chart
7. Top categories table with Revenue, Orders and Average Item Price

### Filters

- Purchase Date / Month
- Customer State
- Product Category
- Payment Type
- Order Status
- Repeat Customer

## 7. Recommendations

### 1. Improve delivery reliability
Investigate late-order bottlenecks and prioritize operational improvements.

**Success metrics:** On-time delivery rate, late-order rate, average review score.

### 2. Increase customer retention
Use post-purchase communication, personalized offers and loyalty initiatives.

**Success metrics:** Repeat purchase rate, revenue per customer, repeat-customer revenue.

### 3. Expand high-performing categories while diversifying regional growth
Protect inventory in strong categories while developing demand outside the largest revenue region.

**Success metrics:** Category revenue growth, state-level revenue growth and average order value.

## 8. Limitations

- The dataset represents historical activity from 2016–2018.
- The analysis is observational and does not prove causality.
- Marketing spend, detailed inventory information, profit/margin and complete carrier-level operational data are not available.
- Delivery and review analyses should therefore be interpreted as business associations rather than causal conclusions.

## 9. Repository Structure

```text
olist-ecommerce-data-analyst-assessment/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── olist_orders_dataset.csv
│   │   ├── olist_order_items_dataset.csv
│   │   ├── olist_customers_dataset.csv
│   │   ├── olist_products_dataset.csv
│   │   ├── olist_sellers_dataset.csv
│   │   ├── olist_order_payments_dataset.csv
│   │   ├── olist_order_reviews_dataset.csv
│   │   ├── olist_geolocation_dataset.csv
│   │   └── product_category_name_translation.csv
│   │
│   └── processed/
│       └── olist_processed_data.csv
│
├── notebooks/
│   └── olist_analysis.ipynb
│
├── scripts/
│   └── olist_analysis.py
│
├── dashboard/
│   ├── dashboard_screenshot.png
│   └── looker_studio_link.txt
│
├── presentation/
│   └── Olist_Management_Presentation.pptx
│
└── assessment/
    └── Q1-Q10_Assessment.xlsx
```

## 10. Tools

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Jupyter Notebook / Google Colab
- Google Sheets
- Looker Studio
- GitHub

## 11. Dashboard KPI Definitions

| KPI | Definition |
|---|---|
| Revenue | Sum of item price for delivered orders |
| Delivered Orders | Distinct delivered order IDs |
| Average Order Value | Revenue / delivered orders |
| Average Review Score | Average customer review score for delivered orders |
| On-Time Delivery Rate | Delivered orders with actual delivery on or before estimated date / delivered orders with valid delivery dates |
| Repeat Customer Rate | Unique customers with more than one order / all unique customers |

## 12. Important Note

Before submission, verify all calculated values against the final Google Sheet and dashboard. The dashboard should use the same processed dataset and metric definitions as the analysis.

