**Sales Data Analysis Report**



Analyze sales data using Python and Pandas to identify revenue, profit, customers, and sales trends.



The project successfully merged multiple CSV files and performed sales analysis using Pandas. Revenue and profit calculations provided insight into business performance.



**Dataset Information**

Total Rows: 3864

Total Columns: 45



**Data Cleaning**

Missing Values Checked using:

combined\_df.isnull().sum()



Duplicate Records Checked using:

combined\_df.duplicated().sum()



**Analysis Performed**

Revenue Formula

Revenue = Quantity Ordered × Price Each



combined\_df\["revenue"] =

combined\_df\["quantityOrdered"] \*

combined\_df\["priceEach"]



Profit Formula

Profit = (Price Each - Buy Price) × Quantity Ordered



combined\_df\["profit"] =

(combined\_df\["priceEach"]

\- combined\_df\["buyPrice"])

\* combined\_df\["quantityOrdered"]



**Results**

Metric	Value

Total Revenue	9604190.61

Total Profit	0.0





