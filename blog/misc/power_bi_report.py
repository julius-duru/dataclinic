import streamlit as st
import pandas as pd

TITLE = "Storytelling with Data in Power BI Reports"
CATEGORY = "misc"
KEYWORDS = ["Power BI", "data storytelling", "data visualization", "business intelligence", "dashboard design", "executive reporting", "DAX", "analytics", "report flow", "KPIs"]


def show():
    st.title("Storytelling with Data in Power BI Reports")
    st.caption("Category: misc | Level: Beginner → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        This article is for: Aspiring analysts, Data scientists, BI developers, and Analytics leaders.
        The core themes include: visualization selection, report flow architecture, DAX measures, industry-specific dashboards, and executive storytelling.
        
        **Why This Guide Matters**
        
        - **If you are a beginner analyst:** You will learn how to choose the right chart for your data type and audience—not just what looks "cool." You'll understand how to structure a multi-page report that answers business questions.
        - **If you are an experienced data professional:** You will gain a reusable 5-page storytelling framework, a cross-industry visual mapping table, and advanced techniques like dynamic titles, decomposition trees, and key influencers.
        
        > The best Power BI dashboards are not about visuals—they are about decisions.
        
        Below, we present a complete guide to visualization selection, followed by a universal 5-step storytelling model, industry-specific visual mapping, and the core skills required at every level.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 1: Start With the Business Question
    # ============================================
    st.header("1. Start With the Business Question (Not the Chart)")
    
    st.write(
        """
        Before selecting any visual, ask three questions:
        
        1. **What question am I answering?**
        2. **What insight should the user gain?**
        3. **Who is the audience?** (Technical vs. non-technical)
        
        > **A good rule:** Every visual must answer one specific question.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 2: Match Visualization to Data Type
    # ============================================
    st.header("2. Match Visualization to Data Type")
    
    st.write("Choosing the right visual is the foundation of effective storytelling. The wrong chart can mislead users, while the right one instantly reveals insights.")
    
    viz_data = {
        "Goal": ["Compare categories", "Show trends over time", "Show proportions (part-to-whole)", "Show relationships & correlation", "Show process flow", "Show geographic analysis", "Show KPIs & key metrics", "Show detailed data"],
        "Best Visual": ["Bar chart / Column chart", "Line chart", "Pie chart (≤5-8 categories) / Treemap", "Scatter plot / Bubble chart", "Funnel chart / Waterfall chart", "Map / Filled map", "Card / KPI visual / Gauge", "Table / Matrix"],
        "Example": ["Sales by region", "Monthly revenue growth", "Market share", "Price vs. Sales", "Conversion stages", "Sales by location", "Total revenue vs. target", "Customer list"]
    }
    df_viz = pd.DataFrame(viz_data)
    st.dataframe(df_viz, use_container_width=True)
    
    st.info("**Key Insight:** Humans compare length better than angles. Bar charts outperform pie charts for precise comparisons. Avoid 3D charts—they distort perception.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION 3: Apply Key Selection Principles
    # ============================================
    st.header("3. Apply Key Selection Principles")
    
    principles_data = {
        "Principle": ["Simplicity Wins", "Readability Over Creativity", "Use Color Strategically", "Think Like the User", "Tell a Story"],
        "Guideline": [
            "Avoid clutter. Use minimal colors and labels. Focus on key insights.",
            "Avoid 3D charts and too many pie slices. Use consistent scales.",
            "Green = positive, Red = negative, Yellow = warning. Highlight insights, don't decorate.",
            "Executives → Simple KPIs & summaries. Analysts → Detailed tables + drilldowns.",
            "Show what happened → Explain why → Suggest what to do next."
        ]
    }
    df_principles = pd.DataFrame(principles_data)
    st.dataframe(df_principles, use_container_width=True)
    
    st.error("**Common Mistakes to Avoid:**")
    st.markdown(
        """
        - ❌ Using pie charts for many categories
        - ❌ Mixing unrelated data in one visual
        - ❌ Overloading dashboards with too many charts
        - ❌ Using the wrong chart type (e.g., line chart for categories)
        - ❌ Ignoring audience needs
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 4: The 5-Step Storytelling Framework
    # ============================================
    st.header("4. The 5-Step Storytelling Framework for Any Power BI Report")
    
    st.write(
        """
        Think of your Power BI report like a movie or a presentation. It needs a logical beginning, middle, and end.
        """
    )
    
    flow_data = {
        "Page": ["Page 1: Executive Summary", "Page 2: Trend Analysis", "Page 3: Breakdown Analysis", "Page 4: Deep Dive", "Page 5: Insights & Actions"],
        "Purpose": ["Snapshot of performance", "Time-based changes", "Category insights", "Root cause analysis", "Recommendations"],
        "Key Question": ["What is happening?", "When did it happen?", "Where did it happen?", "Why did it happen?", "What should we do next?"],
        "Recommended Visuals": [
            "KPI Cards, Line Chart, Bar Chart",
            "Line Chart, Area Chart",
            "Bar Chart, Treemap, Stacked Bar",
            "Decomposition Tree, Scatter Plot, Key Influencers",
            "Text Boxes, KPI Targets, Forecast"
        ]
    }
    df_flow = pd.DataFrame(flow_data)
    st.dataframe(df_flow, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 5: Power BI Visualizations vs Use Cases Across Business Verticals
    # ============================================
    st.header("5. Power BI Visualizations vs Use Cases Across Business Verticals")
    
    st.write("This table shows you exactly which visual to use for which business problem across different industries.")
    
    vertical_data = {
        "Visualization": ["Bar/Column Chart", "Line Chart", "Pie/Donut Chart", "Treemap", "Scatter Plot", "Funnel Chart", "Waterfall Chart", "Map", "Card (KPI)", "Decomposition Tree"],
        "Finance": [
            "Expense by department", "Revenue growth", "Budget allocation", "Expense hierarchy", "Risk vs. return", "Loan approval stages", "Profit & loss breakdown", "Revenue by region", "Total revenue", "Profit drivers"
        ],
        "Sales & Marketing": [
            "Sales by region/product", "Campaign performance", "Market share", "Product category contribution", "Ad spend vs. revenue", "Sales pipeline conversion", "Revenue contribution by channel", "Customer distribution", "Total sales", "Sales decline drivers"
        ],
        "Healthcare": [
            "Patient count by department", "Patient admissions trend", "Disease distribution", "Hospital department load", "Age vs. recovery rate", "Patient treatment stages", "Cost of treatment analysis", "Disease spread", "Total patients", "Patient outcome drivers"
        ],
        "Retail & E-commerce": [
            "Sales by product category", "Daily/weekly sales trend", "Payment method usage", "Product hierarchy sales", "Price vs. sales", "Checkout funnel", "Margin analysis", "Store performance by location", "Total orders", "Revenue drop causes"
        ],
        "Manufacturing": [
            "Output by production line", "Production trend", "Cost breakdown", "Component cost breakdown", "Machine efficiency vs. output", "Production stages", "Cost variance analysis", "Factory locations", "Total output", "Defect causes"
        ]
    }
    df_vertical = pd.DataFrame(vertical_data)
    st.dataframe(df_vertical, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 6: Complete Storytelling Dashboard Layout 
    # ============================================
    st.header("6. Complete Storytelling Dashboard Layout ")
    
    st.write("Here is how to map your actual dataset to the 5-page storytelling structure.")
    
    mapping_data = {
        "Page": ["Page 1: Executive Summary", "Page 2: Trend Analysis", "Page 3: Breakdown Analysis", "Page 4: Deep Dive", "Page 5: Insights & Actions"],
        "Visual": ["KPI Cards, Line Chart, Bar Chart", "Line Chart, Area Chart", "Bar Chart, Treemap, Stacked Bar", "Decomposition Tree, Scatter Plot, Key Influencers", "Text Boxes, KPI Targets, Forecast"],
        "Typical Fields": [
            "Total Sales, Total Orders, Date vs. Sales, Product vs. Sales",
            "Date vs. Sales, Date vs. Profit, Date vs. Quantity",
            "Country vs. Sales, Product Line vs. Sales, Deal Size vs. Sales",
            "Sales → Country → Product Line, Price vs. Sales, Sales drivers",
            "Key insights, Recommendations, Sales forecast"
        ]
    }
    df_mapping = pd.DataFrame(mapping_data)
    st.dataframe(df_mapping, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 7: Core DAX Measures
    # ============================================
    st.header("7. Core DAX Measures (Your Data Modeling Toolkit)")
    
    st.write("Before building visuals, you need measures. These are the essential DAX formulas for any sales dashboard.")
    
    dax_data = {
        "Measure Name": ["Total Sales", "Total Orders", "Total Quantity", "Average Order Value", "Sales Growth %"],
        "DAX Formula": [
            "`SUM(Sales[SALES])`",
            "`DISTINCTCOUNT(Sales[ORDERNUMBER])`",
            "`SUM(Sales[QUANTITYORDERED])`",
            "`DIVIDE([Total Sales], [Total Orders])`",
            "`DIVIDE([Total Sales] - CALCULATE([Total Sales], PREVIOUSMONTH(DateTable[Date])), CALCULATE([Total Sales], PREVIOUSMONTH(DateTable[Date])))`"
        ],
        "Purpose": ["Total revenue", "Number of unique transactions", "Total units sold", "Revenue per order", "Month-over-month growth"]
    }
    df_dax = pd.DataFrame(dax_data)
    st.dataframe(df_dax, use_container_width=True)
    
    st.info("**💡 Pro Tip:** Create a separate Date Table and link it to your fact table. This enables time intelligence functions like PREVIOUSMONTH, SAMEPERIODLASTYEAR, and TOTALYTD.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION 8: Real-World Example (Retail Dashboard)
    # ============================================
    st.header("8. Real-World Example: Retail Dashboard Story")
    
    st.write("Here is how the storytelling flow works for a retail company:")
    
    example_data = {
        "Step": ["1. Summary", "2. Trend", "3. Breakdown", "4. Deep Dive", "5. Action"],
        "Page": ["Executive Summary", "Trend Analysis", "Breakdown Analysis", "Deep Dive", "Insights & Actions"],
        "Finding": [
            "Total Sales = $1M (↓ 10% from last month)",
            "Decline started in the middle of the month",
            "'West' region dropped significantly",
            "Low inventory → low sales in West region (scatter plot)",
            "**Insight:** 'Restock the West region to recover sales'"
        ]
    }
    df_example = pd.DataFrame(example_data)
    st.dataframe(df_example, use_container_width=True)
    
    st.success("👉 This combination answers: What happened? When? Where? Why? And what to do next.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION 9: Pro Tips for Advanced Storytelling
    # ============================================
    st.header("9. Pro Tips for Advanced Storytelling")
    
    pro_tips_data = {
        "Technique": ["Dynamic Titles (DAX)", "Conditional Formatting", "Custom Tooltip Pages", "Navigation Buttons", "Decomposition Tree", "Key Influencers Visual"],
        "How to Implement": [
            "Create a measure: `'Sales Report for ' & SELECTEDVALUE(Sales[Region], 'All Regions')`",
            "Set rules: Red for below target, Green for above target",
            "Build a separate report page and assign as tooltip",
            "Add buttons for 'Drill through to details' and bookmarks",
            "Best for root cause analysis: Sales by Region → Product → Customer",
            "Automatically discovers drivers of sales or churn"
        ]
    }
    df_pro = pd.DataFrame(pro_tips_data)
    st.dataframe(df_pro, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 10: Core Skills Progression
    # ============================================
    st.header("10. Core Skills Progression: Beginner → Advanced")
    
    skills_data = {
        "Skill Area": ["Visualization", "Storytelling", "DAX & Data Modeling", "Interactivity", "Performance Optimization", "Tools"],
        "Beginner": [
            "Chooses bar/line/pie charts correctly",
            "Reports what happened",
            "Writes basic SUM, COUNT, DIVIDE",
            "Adds slicers and basic filters",
            "Uses default import mode",
            "Power BI Desktop + basic SQL"
        ],
        "Advanced / Lead": [
            "Uses decomposition tree, key influencers, scatter plots",
            "Predicts what will happen and recommends actions",
            "Writes time intelligence, CALCULATE, FILTER, variables",
            "Builds drill-through, custom tooltips, bookmarks, buttons",
            "Optimizes with DAX studio, aggregations, composite models",
            "Power BI + DAX Studio + Tabular Editor + DevOps"
        ]
    }
    df_skills = pd.DataFrame(skills_data)
    st.dataframe(df_skills, use_container_width=True)
    
    st.write(
        """
        **Most important universal skill:**  
        *The ability to ask "So what?" to your own analysis before anyone else does.*
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 11: Best Practices Summary Table
    # ============================================
    st.header("11. Best Practices Summary")
    
    summary_data = {
        "Best Practice": [
            "Start with the business question",
            "Match visual to data type",
            "Use the 5-page flow",
            "Keep it simple",
            "Use color strategically",
            "Enable interactivity",
            "End with actionable insights"
        ],
        "Why It Matters": [
            "Every visual must answer one specific question",
            "The wrong chart misleads; the right chart reveals insights",
            "Guides users from summary → trend → breakdown → deep dive → action",
            "Clutter confuses; focus drives decisions",
            "Green = good, Red = bad (consistent across pages)",
            "Turns passive viewers into active explorers",
            "Dashboards without recommendations are just scorecards"
        ]
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")
    
    st.write(
        """
        **For beginners:** Start with the visualization cheat sheet (Section 2). Practice the 5-page flow on any dataset. Build the core DAX measures first, then add visuals.
        
        **For advanced professionals:** Use the industry mapping table (Section 5) to benchmark your dashboards. Implement the pro tips (Section 9) to elevate your reports. Teach the storytelling framework to junior peers.
        
        > A great Power BI report is not just built—it is narrated.
        
        ---
        
        **Your winning formula:**
        
        1. Define the business question
        2. Match the data type to the appropriate visual
        3. Structure your report flow (Summary → Trend → Breakdown → Deep Dive → Action)
        4. Use color and hierarchy to guide the user
        5. End with clear, actionable insights
        
        **Next actions for you:**  
        1. Open an existing Power BI report. Does it follow the 5-page flow? If not, restructure it.
        2. Pick one visual. Does it answer one specific question? If not, replace it.
        3. Add a "Recommendations" text box to your next dashboard. That's where business value lives.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Further Reading:**
        
        - [DAX Guide](https://dax.guide/): Complete reference for DAX functions
        - [Power Query Guide](https://devinknightsql.com/category/power-query/): Blog posts and tutorials on Power Query
       
        """
    )
    
    st.markdown("---")
    st.caption("© 2026 | Storytelling with Data in Power BI Reports | For analytics professionals who want to drive decisions, not just build dashboards.")
