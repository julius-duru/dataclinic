import streamlit as st
import pandas as pd

TITLE = "Mastering Dashboard & KPI Design"
CATEGORY = "misc"
KEYWORDS = ["dashboard design", "KPI design", "data visualization", "Power BI", "Tableau", "business intelligence", "data storytelling", "data analytics", "performance metrics", "BI dashboard"]


def show():

    st.title("Mastering Dashboard & KPI Design")
    st.caption("Category: misc | Level: Beginner → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        Designing dashboards and Key Performance Indicators (KPIs) is a core competency that bridges the gap 
        between raw data and business impact. Whether you are just starting your career or looking to lead 
        complex analytics initiatives, mastering this craft will make you indispensable.
        
        A well-designed dashboard doesn't just display data—it tells a story, highlights priorities, and guides action.
        
        **Why Dashboard & KPI Design Matters:**
        - **Drives Decision-Making:** Transforms raw data into actionable business insights
        - **Aligns Teams:** Ensures everyone is measuring success against the same objectives
        - **Reveals Patterns:** Makes trends and anomalies visible at a glance
        - **Accelerates Action:** Reduces time from data to decision
        """
    )
    
    # ============================================
    # SECTION 0: Understanding KPIs
    # ============================================
    st.header("Understanding Key Performance Indicators (KPIs)")
    
    st.write(
        """
        A **Key Performance Indicator (KPI)** is a quantifiable measure used to evaluate the success of an 
        organization, employee, or process in meeting objectives.
        """
    )
    
    # SMART Framework
    st.subheader("The SMART Framework (For Beginners)")
    st.write(
        """
        If you are new to KPI design, start by ensuring every KPI meets the **SMART** criteria:
        """
    )
    
    smart_data = {
        "Criteria": ["Specific", "Measurable", "Achievable", "Relevant", "Time-bound"],
        "Description": [
            "Clearly defined and focused on a single objective",
            "Can be quantified using available data",
            "Realistic and attainable given current resources",
            "Aligned with core business goals",
            "Tied to a specific timeframe (e.g., quarterly, monthly)"
        ],
        "Example": [
            "Increase customer retention",
            "Retention rate = (customers at end - new customers) / customers at start",
            "Target 5% increase, not 50%",
            "Retention impacts profitability more than acquisition",
            "Measure quarterly, report by end of Q3"
        ]
    }
    df_smart = pd.DataFrame(smart_data)
    st.dataframe(df_smart, use_container_width=True)
    
    st.write(
        """
        **For beginners:** Master SMART first—it's the foundation of credible KPI design.  
        **For advanced readers:** Move beyond SMART to consider **KPI hierarchies** and **causal logic**. 
        Identify your **North Star Metric** (the single metric that predicts long-term success) and map the 
        **leading indicators** that drive it.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 1: Types of KPIs
    # ============================================
    st.header("1. Types of KPIs")
    
    kpi_types_data = {
        "Type": ["Strategic KPIs", "Operational KPIs", "Analytical KPIs", "Leading KPIs", "Lagging KPIs"],
        "Audience": ["Executives", "Managers", "Analysts", "All levels", "All levels"],
        "Focus": ["Long-term goals", "Daily/weekly processes", "Trend exploration", "Future performance", "Past results"],
        "Example": ["Revenue growth, market share", "Daily sales, system uptime", "Customer segmentation", "Website traffic", "Total revenue"]
    }
    df_kpi_types = pd.DataFrame(kpi_types_data)
    st.dataframe(df_kpi_types, use_container_width=True)
    
    st.write(
        """
        **For beginners:** Focus on understanding the difference between Leading (predictive) and Lagging (outcome) KPIs.  
        **For advanced readers:** Build **causal chains** that connect leading indicators to lagging outcomes. 
        Use techniques like correlation analysis and A/B testing to validate these relationships.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 2: KPI Design Process
    # ============================================
    st.header("2. KPI Design Process")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("For Beginners: The Execution Path")
        st.write(
            """
            1. **Understand the Objective:** Ask, "What decision will this data help you make?"
            2. **Define the Metric:** Clearly define success (e.g., "Increase conversion from 2% to 2.5%")
            3. **Identify the Source:** Locate data (CRM, SQL Database, Google Analytics)
            4. **Calculate:** Document the exact formula
            5. **Set Targets:** Establish benchmarks (green > 2.5%, red < 2.0%)
            """
        )
    
    with col2:
        st.subheader("For Advanced: The Architecture Path")
        st.write(
            """
            1. **Build a Semantic Layer:** Define KPIs in code (dbt, LookML) for consistency
            2. **Version Control:** Track KPI logic with Git; peer-review formulas
            3. **Statistical Validation:** Use control charts and anomaly detection for thresholds
            4. **Row-Level Security:** Implement so managers only see their own teams' data
            5. **Automate Alerts:** Send notifications via Slack/Teams for outliers
            """
        )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 3: Dashboard Design Principles
    # ============================================
    st.header("3. Dashboard Design Principles")
    
    st.write(
        """
        A dashboard is the interface for your KPIs. A poorly designed dashboard can undermine even the most accurate data.
        """
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("For Beginners: Fundamentals")
        st.write(
            """
            - **Clarity over Complexity:** If a chart requires a paragraph to explain, remove it
            - **Visual Hierarchy:** Place the most critical KPI at the top-left (where eyes naturally start)
            - **Consistency:** Use one color palette (green for good, red for bad) and consistent fonts
            - **Context Matters:** Never show a number in isolation—always include a comparison (e.g., 100k vs 90k last month)
            """
        )
    
    with col2:
        st.subheader("For Advanced: Storytelling & Performance")
        st.write(
            """
            - **Storytelling with Data:** Structure dashboards as a narrative:
                - *Overview:* The headline KPI (The Result)
                - *Diagnosis:* Breakdowns by segment (The Why)
                - *Action:* Filters for next steps (The How)
            - **Performance Optimization:** Use extracts, scheduled refreshes, and optimized SQL
            - **Mobile Optimization:** Ensure dashboards are usable on mobile devices
            """
        )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 4: Common Dashboard Types
    # ============================================
    st.header("4. Common Dashboard Types")
    
    dashboard_types_data = {
        "Type": ["Executive Dashboard", "Operational Dashboard", "Analytical Dashboard"],
        "Beginner Focus": [
            "High-level overview; strategic KPIs; clean layout",
            "Real-time monitoring; simple alerts",
            "Trend analysis; filtering by dimensions"
        ],
        "Advanced Application": [
            "Mobile-optimized views; automated commentary (NLG)",
            "Anomaly detection; automated alerts via Slack/Teams",
            "What-If parameters; integration with predictive models"
        ]
    }
    df_dashboards = pd.DataFrame(dashboard_types_data)
    st.dataframe(df_dashboards, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 5: Data Visualization Best Practices
    # ============================================
    st.header("5. Data Visualization Best Practices")
    
    viz_data = {
        "Chart Type": ["Bar Charts", "Line Charts", "Pie Charts", "Scatter Plots", "Heatmaps", "Tables"],
        "Best Used For": [
            "Comparisons across categories",
            "Trends over time",
            "Parts of a whole (use sparingly, max 3-4 slices)",
            "Correlations between two variables",
            "Intensity or density patterns",
            "Detailed data lookup"
        ],
        "Do's": [
            "Sort bars descending for quick insights",
            "Show trend lines; label key points",
            "Use horizontal bars if categories have long names",
            "Add trend lines; color by third dimension",
            "Use divergent color palettes for positive/negative",
            "Allow sorting and searching"
        ],
        "Don'ts": [
            "Don't start axes above zero for bar charts",
            "Don't use for categorical data",
            "Don't use 3D pie charts",
            "Don't overplot with too many points",
            "Don't use red-green for colorblind users",
            "Don't use when a chart would convey insight faster"
        ]
    }
    df_viz = pd.DataFrame(viz_data)
    st.dataframe(df_viz, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 6: Tools for Dashboard Design
    # ============================================
    st.header("6. Tools for Dashboard Design")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("For Beginners")
        st.write(
            """
            - **Microsoft Excel / Google Sheets:** Ideal for learning KPI logic and basic charting
            - **Google Looker Studio:** Free, cloud-based, connects to many sources
            - **Power BI Desktop:** Free for development; extensive learning resources
            """
        )
    
    with col2:
        st.subheader("For Advanced Practitioners")
        st.write(
            """
            - **Microsoft Power BI:** Master DAX for complex calculations; implement Row-Level Security
            - **Tableau:** Master Level of Detail (LOD) expressions; create guided analytics experiences
            - **Semantic Layer Tools:** dbt, LookML—define KPIs in code for consistency across the organization
            """
        )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 7: Common Mistakes to Avoid
    # ============================================
    st.header("7. Common Mistakes to Avoid")
    
    mistakes_data = {
        "Mistake": [
            "Too many KPIs on one dashboard",
            "Using irrelevant metrics",
            "Poor labeling and unclear visuals",
            "Ignoring user needs",
            "Lack of data validation",
            "Misleading axes"
        ],
        "Why It's a Problem": [
            "Creates cognitive overload; users can't find what matters",
            "Wastes attention; undermines trust",
            "Users can't interpret what they're seeing",
            "Dashboard goes unused",
            "Undermines credibility; leads to bad decisions",
            "Exaggerates or hides trends"
        ],
        "How to Fix": [
            "Limit to 5-7 core metrics per page; use tabs for deeper dives",
            "Align every metric with a specific business decision",
            "Use clear titles, axis labels, and legends; add annotations",
            "Shadow users; prototype and iterate based on feedback",
            "Cross-check totals against source of truth before publishing",
            "Start bar/line charts at zero unless you have a specific reason"
        ]
    }
    df_mistakes = pd.DataFrame(mistakes_data)
    st.dataframe(df_mistakes, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 8: Real-World Example
    # ============================================
    st.header("8. Real-World Example: Sales Dashboard")
    
    st.write(
        """
        Consider how a beginner vs. an advanced practitioner would approach a sales dashboard.
        """
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("The Beginner Approach")
        st.write(
            """
            **KPIs:** Total Revenue, Sales Growth %, Customer Acquisition Cost (CAC), Conversion Rate
            
            **Layout:** Single page with four large numbers at the top (the KPIs) and a few bar charts below.
            
            **Functionality:** Static filters (e.g., dropdown for region).
            
            **Insight:** "Sales in the West region are down."
            """
        )
    
    with col2:
        st.subheader("The Advanced Approach")
        st.write(
            """
            **KPIs:** Same core KPIs, but with:
            - Sparklines showing trends
            - Conditional formatting (red/amber/green)
            - CAC vs. Conversion Rate scatter plot to identify efficient reps
            - What-If parameter tool for discount scenarios
            
            **Layout:** 3-page story:
            1. **Summary:** KPIs with sparklines and context
            2. **Diagnosis:** Efficiency analysis by rep
            3. **Action:** What-If tool for strategic planning
            
            **Functionality:** Drill-through from region to detailed deal list.
            
            **Insight:** "West region sales are down due to 20% CAC increase. Targeting mid-market could restore profitability."
            """
        )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 9: Best Practices and Decision Framework
    # ============================================
    st.header("9. Best Practices and Decision Framework")
    
    tab1, tab2 = st.tabs(["For Beginners", "For Advanced Practitioners"])
    
    with tab1:
        st.write(
            """
            ### A Simple Workflow
            
            1. **Start with SMART:** Ensure every KPI meets the SMART criteria
            2. **Choose dashboard type:** Executive, Operational, or Analytical based on audience
            3. **Apply fundamentals:** Visual hierarchy, clarity, context (comparisons)
            4. **Pick your tool:** Start with Excel or Looker Studio
            5. **Validate:** Always double-check numbers against source data
            6. **Iterate:** Get feedback from users and refine
            """
        )
    
    with tab2:
        st.write(
            """
            ### A Refined Approach
            
            1. **Build a semantic layer:** Define KPIs in dbt or LookML for consistency across the org
            2. **Characterize user needs:** Conduct user research; shadow stakeholders
            3. **Design for performance:** Optimize data models; use extracts; implement RLS
            4. **Tell a story:** Structure dashboards as narrative flows, not just collections of charts
            5. **Add advanced features:** What-If parameters, drill-through, anomaly detection
            6. **Implement governance:** Version control KPI logic; document calculations; set SLAs for data freshness
            """
        )
    
    st.markdown("---")
    
    # ============================================
    # SUMMARY TABLE
    # ============================================
    st.header("Summary Table: Methods at a Glance")
    
    summary_data = {
        "Skill Area": [
            "KPI Definition", "KPI Types", "Dashboard Layout", 
            "Visualization", "Interactivity", "Tools", 
            "Performance", "Governance"
        ],
        "Beginner Focus": [
            "SMART framework", "Leading vs Lagging", "Clarity, hierarchy, consistency",
            "Bar, line, tables", "Filters, basic drill-down", "Excel, Looker Studio, Power BI Desktop",
            "N/A", "Manual documentation"
        ],
        "Advanced Focus": [
            "Causal chains, North Star Metric", "KPI hierarchies, validation", "Storytelling, narrative structure",
            "Advanced LOD, statistical charts", "Drill-through, What-If, parameters", "dbt, LookML, Tableau LOD, DAX",
            "Extracts, row-level security, optimized SQL", "Version control, semantic layer, automated alerts"
        ]
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header(" Conclusion")
    
    st.write(
        """
        Dashboard and KPI design is the intersection of **technical execution** and **business strategy**.
        
        **For beginners:** Focus on **accuracy and clarity**. Your goal is to become the go-to person for reliable 
        reporting. Master one tool deeply and always validate your numbers. Start with the SMART framework and 
        fundamental design principles.
        
        **For advanced practitioners:** Focus on **automation, governance, and decision velocity**. Your goal is 
        to build systems that allow the business to self-serve accurate data while you focus on predictive 
        analytics and complex problem-solving. Build semantic layers, implement row-level security, and design 
        dashboards that tell a story.
        
        If you can design dashboards that executives trust to run their business, you transition from being a 
        data analyst to being a **strategic business partner**.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Learning Resources:**
        - [Power BI Learning Path (Microsoft Learn)](https://learn.microsoft.com/en-us/power-bi/)
        - [Tableau Free Training Videos](https://www.tableau.com/learn/training)
        
        **Python Libraries:**
        - [Plotly Express](https://plotly.com/python/plotly-express/): Interactive visualizations
        - [Altair](https://altair-viz.github.io/): Declarative visualization in Python
       
        **Design Inspiration:**
        - [Data Viz Project](https://datavizproject.com/): Gallery of chart types
        - [Makeover Monday](https://makeovermonday.co.uk/): Community challenge to improve visualizations
        """
    )