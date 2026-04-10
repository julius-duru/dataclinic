import streamlit as st
import pandas as pd

TITLE = "Power BI Visualization and Reporting"
CATEGORY = "data_visualization"
KEYWORDS = [
    "power bi", "power query", "data cleaning", "data modeling", "DAX",
    "visualization", "dashboard design", "KPI", "row level security",
    "gateway","snowflakes schema", "star schema", "ETL", "business intelligence"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Beginner → Advanced")
    st.markdown("---")

    # INTRO
    st.write(
        """
        Assume that you are Alex, a data analyst at NorthStar Retail shop. You are tasked with building a production-ready **Sales Performance Dashboard** from scratch.  
        The project requires mastering Power Query, data cleaning methodologies, star schema modeling, DAX calculations (basic to complex), dashboard planning with KPIs, 
        and report sharing across the enterprise.

        **This is a tailored end-to-end Power BI workflow to design a professional dashboard,and share same with all stakeholders**  
        - **Reproducibility** – Every transformation step is documented and automated.  
        - **Performance** – A star schema and optimized DAX return sub-second queries.  
        - **Governance** – Row-Level Security and gateways ensure safe, scheduled refreshes.

        > A structured architecture turns a chaotic Excel report into a trusted, company-wide analytics asset.
        """
    )
    st.markdown("---")

    # POWER BI DESKTOP 
    st.header("Power Query – Connecting to Disparate Data Sources")
    st.write(
        """
        Assume that Alex's data live in three data sources:
        - **SQL Server** (on-premises) – transactional sales from physical stores  
        - **Google Sheets** (cloud) – daily online sales from Shopify  
        - **SharePoint Excel file** – regional sales targets from finance  

        Power Query from POWER BI desktop would be the ETL engine that connects to all of them simultaneously.
        """
    )
    st.subheader("Step 1: Connect to sources")
    st.code(
        """
# In Power BI Desktop: Get Data → SQL Server → Select FactSales
# Get Data → Web → Paste Google Sheets public link
# Get Data → SharePoint folder → Select Targets file

# After loading, Alex has three queries: SQL_Sales, Online_Sales, Targets
        """,
        language="text"
    )
    st.subheader("Step 2: Append online and offline sales")
    st.code(
        """
# Home → Append Queries → Stack SQL_Sales + Online_Sales → New table "All_Sales"
        """,
        language="text"
    )
    st.subheader("Step 3: Merge targets (Advanced: Query Folding)")
    st.code(
        """
# Merge All_Sales with Targets on YearMonth and Region (Left Outer Join)
# Check query folding: Right-click last step → View Native Query
# If grayed out, reorder steps to push filters back to source database
        """,
        language="text"
    )
    st.info(" **Beginner tip**: Every click in Power Query (remove column, filter rows) becomes a step. You rarely need to write M code manually. **Advanced tip**: Query folding pushes transformations to the source database – critical for performance on large datasets.")
    st.markdown("---")

    # DATA CLEANING
    st.header(" Data Cleaning – Methodology by Use Case")
    st.write(
        """
        Raw data is never clean. Alex applies different cleaning strategies depending on the problem.
        """
    )
    
    cleaning_cases = pd.DataFrame({
        "Use Case": [
            "Duplicate transactions (online)",
            "Missing store names (SQL)",
            "Outlier amounts (manual entry)",
            "Inconsistent date formats"
        ],
        "Issue": [
            "Webhook retry created duplicate rows",
            "NULL or 0 values for online orders",
            "Test entries with 999,999",
            "MM/DD/YYYY vs DD/MM/YYYY"
        ],
        "Methodology": [
            "Remove duplicates by TransactionID, keep earliest timestamp",
            "Replace NULL/0 with 'Online', create flag column",
            "IQR method: flag outliers, exclude from KPIs (don't delete)",
            "Date.FromText with locale ('en-US' / 'fr-CA')"
        ],
        "Power Query step": [
            "Select column → Remove Duplicates",
            "Replace Values → 'Online' → Add conditional column",
            "Add column → Custom column with IQR formula",
            "Change data type → Using locale"
        ]
    })
    st.dataframe(cleaning_cases, use_container_width=True)
    
    st.code(
        """
# IQR outlier detection example (Power Query M code)
let
    Q1 = List.Percentile(Table.Column(#"Previous Step", "Amount"), 0.25),
    Q3 = List.Percentile(Table.Column(#"Previous Step", "Amount"), 0.75),
    IQR = Q3 - Q1,
    Lower = Q1 - 1.5 * IQR,
    Upper = Q3 + 1.5 * IQR,
    #"Flag Outliers" = Table.AddColumn(#"Previous Step", "IsOutlier", each [Amount] < Lower or [Amount] > Upper)
in
    #"Flag Outliers"
        """,
        language="text"
    )
    st.success(" **Golden rule**: Never delete outliers – flag them. Business users may want to include or exclude them differently.")
    st.markdown("---")

    # DATA MODELING
    st.header("Modeling – The Star Schema Backbone")
    st.write(
        """
        A flat table is slow and confusing. Alex transforms the data into a **star schema**: one fact table connected to multiple dimension tables.
        """
    )
    st.subheader("Fact table (narrow, long)")
    st.code(
        """
All_Sales: DateKey, ProductKey, StoreKey, Amount, Quantity (10M rows)
        """,
        language="text"
    )
    st.subheader("Dimension tables (wide, short)")
    st.code(
        """
DimDate:     DateKey, Year, Month, Quarter, Weekday, IsWeekend (365 rows)
DimProduct:  ProductKey, ProductName, Category, UnitCost (1K rows)
DimStore:    StoreKey, StoreName, City, Region (50 rows)
        """,
        language="text"
    )
    st.subheader("Relationships (Model view)")
    st.code(
        """
DimDate[DateKey]    → All_Sales[DateKey]      (one-to-many, single direction)
DimProduct[ProductKey] → All_Sales[ProductKey] (one-to-many)
DimStore[StoreKey]  → All_Sales[StoreKey]      (one-to-many)

# Inactive relationship for ship date analysis
DimDate[DateKey]    → All_Sales[ShipDateKey]   (inactive, will use USERELATIONSHIP in DAX)
        """,
        language="text"
    )
    st.info(" **Beginner rule**: Never create direct relationships between two fact tables. Always connect them through shared dimensions. **Advanced pattern**: Use inactive relationships for role‑playing dimensions (order date, ship date, delivery date).")
    st.markdown("---")

    # CALCULATIONS with Data Analysis Expressions (DAX)
    st.header("Data Analysis Expressions (DAX) – Measures that Drive Insights")
    st.write(
        """
        DAX (Data Analysis Expressions) calculates measures *on the fly* – no storage overhead, always fresh.
        """
    )
    
    st.subheader("Beginner: Basic KPIs")
    st.code(
        """
Total Sales = SUM(All_Sales[Amount])

Total Quantity = SUM(All_Sales[Quantity])

Average Order Value = DIVIDE([Total Sales], COUNTROWS(All_Sales))

Sales vs Target % = 
VAR Actual = [Total Sales]
VAR Target = SUM(Targets[MonthlyTarget])
RETURN DIVIDE(Actual - Target, Target)
        """,
        language="text"
    )
    
    st.subheader("Intermediate: Time Intelligence")
    st.code(
        """
Sales PY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(DimDate[Date]))

YoY Growth % = DIVIDE([Total Sales] - [Sales PY], [Sales PY])

Sales by Ship Date = 
CALCULATE([Total Sales], USERELATIONSHIP(All_Sales[ShipDateKey], DimDate[DateKey]))
        """,
        language="text"
    )
    
    st.subheader("Advanced: Dynamic Segmentation (ABC Analysis)")
    st.code(
        """
Product Class = 
VAR TotalSalesAll = [Total Sales]
VAR ProductRank = RANKX(ALL(DimProduct[ProductID]), [Total Sales])
VAR TotalProducts = COUNTROWS(ALL(DimProduct))
VAR PercentRank = ProductRank / TotalProducts
RETURN
SWITCH(TRUE(),
    PercentRank <= 0.2, "A (Top 20%)",
    PercentRank <= 0.5, "B (Middle 30%)",
    "C (Bottom 50%)"
)
        """,
        language="text"
    )
    
    st.subheader("Advanced: What-If Parameter (Dynamic Analysis)")
    st.code(
        """
# Create What-If parameter via Modeling tab → New Parameter
# Generates a slicer and measure 'Parameter Value'

Projected Sales = [Total Sales] * (1 + [Parameter Value] / 100)
        """,
        language="text"
    )
    st.warning(" **Performance rule**: Prefer measures over calculated columns. Measures evaluate only when needed; calculated columns consume RAM permanently. Use `VAR` for readability and to avoid recalculations.")
    st.markdown("---")

    # VISUALIZATION
    st.header("Visualization – Dashboard Planning with KPIs")
    st.write(
        """
        Before dragging a single visual, Alex plans the dashboard on paper.
        """
    )
    
    st.subheader("Executive Sales Dashboard Layout")
    dashboard_layout = pd.DataFrame({
        "Zone": ["Top row", "Left column", "Middle", "Right column", "Bottom"],
        "Content": [
            "KPI cards: Total Sales, YoY Growth %, Sales vs Target %",
            "Line chart: Sales by Month + Year slicer",
            "Filled map: Sales by Region",
            "Bar chart: Top 10 Products with ABC legend",
            "Table: Detailed sales (store, product, amount) with drill-through"
        ],
        "Visual type": ["Card / Gauge", "Line chart", "Map", "Bar chart", "Table + Drill-through"]
    })
    st.dataframe(dashboard_layout, use_container_width=True)
    
    st.subheader("Alex's Implementation Steps")
    st.code(
        """
# 1. Line chart: DimDate[Date] on axis, [Total Sales] + [Sales PY] on values
# 2. Map: DimStore[Region] as location, [Total Sales] as bubble size
# 3. Bar chart: DimProduct[ProductName] on axis, [Total Sales] as value, [Product Class] as legend
# 4. Slicers: Year, Quarter, Region (affect all visuals via model relationships)
# 5. Drill-through page: Create "Order Details" page → Right-click any visual → Drill through
# 6. Bookmarks: "Daily View" vs "Monthly View" (group dates in axis)
# 7. Tooltips: Hover on map region → show top 3 products
        """,
        language="text"
    )
    
    st.subheader("Field Parameter (User-Selectable Measure)")
    st.code(
        """
# Create parameter table (Enter Data): Measure Name = "Revenue", "Quantity", "Profit"
# Then create measure:

Selected Measure = 
SWITCH(SELECTEDVALUE('Measure Selection'[Measure]),
    "Revenue", [Total Sales],
    "Quantity", [Total Quantity],
    "Profit", [Total Profit]
)

# Use 'Selected Measure' in any visual → users can dynamically change what they see
        """,
        language="text"
    )
    st.info("**Beginner tip**: Start with Microsoft's built‑in templates and themes. **Advanced tip**: Field parameters turn static dashboards into interactive exploration tools.")
    st.markdown("---")

    # SHARING REPORTS WITH POWER BI SERVICE
    st.header("Sharing Reports with Power BI Service")
    st.write(
        """
        The report works beautifully. Now Alex must deliver it to sales managers securely and keep it updated automatically.
        """
    )
    
    st.subheader("Step 1: Publish to Power BI Service")
    st.code(
        """
# Power BI Desktop → Publish → Select workspace "NorthStar Sales – Production"
        """,
        language="text"
    )
    
    st.subheader("Step 2: Configure Gateway for On-Premises SQL Server")
    st.code(
        """
# Download and install On-premises data gateway on a shared server
# Power BI Service → Dataset settings → Gateway connection → Select gateway
# Set refresh schedule: Daily at 6 AM (after nightly ETL)
        """,
        language="text"
    )
    
    st.subheader("Step 3: Row-Level Security (RLS)")
    st.code(
        """
# Create mapping table: UserEmail → Region
# Define RLS role in Power BI Desktop:

[Region] = LOOKUPVALUE(Mapping[Region], Mapping[UserEmail], USERNAME())

# Publish → Go to dataset security → Assign users to roles → Test with "View as role"
        """,
        language="text"
    )
    
    st.subheader("Step 4: Deploy as App")
    st.code(
        """
# Workspace → Create app → Add report and pinned dashboard
# Set audience: "Sales Managers" (eg Azure AD group)
# Share app link → Users install from https://app.powerbi.com
        """,
        language="text"
    )
    
    st.subheader("Licensing Quick Reference")
    license_table = pd.DataFrame({
        "User need": [
            "View shared dashboard (Pro sharer + Premium workspace)",
            "Create and share content",
            ">1 GB model, >8 refreshes/day, distribute to free users"
        ],
        "License required": ["Free", "Pro per user", "Premium Per User (PPU) or Premium Capacity"]
    })
    st.dataframe(license_table, use_container_width=True)
    
    st.success("**Advanced pattern**: Use Deployment Pipelines to move content automatically from Development → Test → Production with Azure DevOps integration.")
    st.markdown("---")

    # CONCLUSION
    st.header("Conclusion: The Report")
    st.write(
        """
        The report works beautifully and automatically updates as daily data is fed into it. Now Alex must deliver it to sales managers securely and keep it updated automatically.

        **Key takeaways for every Power BI project:**
        1. **Power Query** – Connect to all sources, append/merge, and check query folding.
        2. **Data cleaning** – Deduplicate (use unique IDs), impute missing (with context), flag outliers (don't delete).
        3. **Modeling** – Star schema: one fact, multiple dimensions. Hide columns. Set sort order.
        4. **DAX** – Basic measures first (SUM, DIVIDE). Then time intelligence (SAMEPERIODLASTYEAR). Finally dynamic segmentation (RANKX).
        5. **Visualization** – Plan KPI layout. Use drill-through, bookmarks, tooltips, field parameters.
        6. **Sharing** – Publish to workspace. Gateway for on-prem. RLS with mapping table. Deploy as app. Monitor usage.

        **Practice Exercise:**
        - Open Power BI Desktop → Get Data → choose an Excel file with messy data.
        - Clean it using Power Query (remove duplicates, replace nulls, fix dates).
        - Build a star schema (one fact, two dimensions minimum).
        - Write three DAX measures: SUM, DIVIDE, and one CALCULATE with time intelligence.
        - Design a dashboard with 3 KPIs, one chart, and one slicer.
        - Publish to the free Power BI Service and share with a colleague.

        > A clean architecture turns data into a trusted, company-wide analytics asset.
        """
    )
    st.markdown("---")

    # RESOURCES
    st.header("Resources for Mastering Power BI")
    st.markdown(
        """
        **Power Query & M Language**  
        - [Power Query documentation (Microsoft)](https://docs.microsoft.com/en-us/power-query/)  
        - [Query folding explained](https://docs.microsoft.com/en-us/power-query/power-query-folding)  

        **Data Modeling & Star Schema**  
        - [Star schema guidance (Microsoft)](https://docs.microsoft.com/en-us/power-bi/guidance/star-schema)  
        - [Relationship management in Power BI](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships)  

        **DAX (Data Analysis Expressions)**  
        - [DAX reference (Microsoft)](https://docs.microsoft.com/en-us/dax/)  
        - [SQLBI – Advanced DAX patterns](https://www.sqlbi.com/articles/)  
        - [DAX Studio (free tool for writing and optimizing DAX)](https://daxstudio.org/)  

        **Visualization & Dashboard Design**  
        - [Power BI visualization types](https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)  
        
        **Sharing, Gateway & RLS**  
        - [On-premises data gateway](https://docs.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem)  
        - [Row-Level Security (RLS) guide](https://docs.microsoft.com/en-us/power-bi/admin/service-admin-rls)  
        - [Power BI licensing](https://docs.microsoft.com/en-us/power-bi/fundamentals/service-features-license-type)  

        **Community & Learning**  
        - [Power BI Community Forum](https://community.powerbi.com/)  
        
        """
    )
    st.markdown("---")
    st.caption("© 2026 | Power BI Architecture | Build reports that are fast, trustworthy, and scalable – from first query to executive dashboard.")