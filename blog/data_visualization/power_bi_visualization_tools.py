import streamlit as st
import pandas as pd

TITLE = "Advanced Insights with Power BI Visuals"
CATEGORY = "data_visualization"
KEYWORDS = [
    "Power BI", "data visualization", "decomposition tree", "key influencers", "ribbon chart",
    "scatter chart", "Q&A", "slicer", "KPI", "waterfall", "treemap", "funnel", "infographics",
    "narrative", "gauge", "card", "map", "pie chart", "donut chart", "line chart", "area chart"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Beginner → Intermediate (Report Design & Analytics)")
    st.markdown("---")

    # INTRO – conversational and motivating
    st.write(
        """
        Assume that you have loaded your data into Power BI. Now you’re staring at the Visualizations pane thinking:  
        *There are way too many icons here. Do I really need a ribbon chart? What even is a decomposition tree?*

        I get it. It’s overwhelming.

        But here’s the secret: **Every visual exists to answer a specific question.**  
        You don’t need to master all of them. You just need to know which tool to grab when your boss asks,  
        *“Why did sales drop?”* or *“Are we on track?”*

        In this guide we’ll walk through the most useful Power BI visuals – **no jargon, just real talk**.  
        You’ll learn:
        - Which visual to use for KPIs, trends, proportions, and root‑cause analysis  
        - How AI‑powered visuals (Key Influencers, Decomposition Tree) save you hours of slicing  
        - A simple cheat sheet you can keep next to your monitor  
        - Resources to go deeper (free Microsoft docs, YouTube channels, and books)

        > This is not a dry reference. You’ll leave with a clear mental model and a **checklist** for choosing the right visual every time.
        """
    )
    st.markdown("---")

    # 1. FOUNDATIONAL KPIs & REAL‑TIME MONITORING
    st.header(" Step 1 – Foundational KPIs & Real‑time Monitoring")
    st.write(
        """
        These are the visuals you’ll use in almost every report. They answer: *“What’s the number, and are we winning?”*
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Card")
        st.write("**One giant number.**")
        st.write("Total sales. Current inventory. Active users. Simple, readable from across the room.")
    with col2:
        st.subheader("KPI")
        st.write("**Number + target + trend.**")
        st.write("Monthly revenue vs. quarterly goal. Green arrow up = good. Red arrow down = meeting time.")
    with col3:
        st.subheader("Gauge")
        st.write("**Speedometer style.**")
        st.write("CPU usage (0–100%). CSAT score (0–10). Instantly shows green/yellow/red zones.")

    st.info(" **Pro tip:** Use a Card when you need one number. Use a KPI when you need context (goal + trend). Use a Gauge when you have a defined range and a danger zone.")

    st.markdown("---")

    # 2. NAVIGATION & INTERACTIVITY
    st.header("Step 2 – Navigation & Interactivity")
    st.write(
        """
        A static report is a PDF. An interactive report is a tool. These visuals put the user in the driver’s seat.
        """
    )

    with st.expander("Slicer – the TV remote for your report", expanded=False):
        st.write(
            """
            **What it does:** Filters all other visuals on the page simultaneously.  
            **Use case:** A date range slider, a dropdown for “Region”, or a list of product categories.  
            **Why it’s essential:** Without a slicer, you’d have to build a separate report for every combination of filters.  
            """
        )
        st.caption("Pro tip: Use the ‘Format’ pane to turn a slicer into a dropdown, a list, or even a tile grid.")

    with st.expander("Q&A – natural language queries for non‑technical users", expanded=False):
        st.write(
            """
            **What it does:** Lets users type a question in plain English and Power BI draws the visual automatically.  
            **Use case:** An executive types *“Show me sales for Product X in Germany last quarter”* – no training required.  
            **Why it’s powerful:** It reduces ad‑hoc report requests and empowers business users to self‑serve.  
            """
        )
        st.code("Example questions: “Total sales by month”, “Top 5 customers by profit”, “Average rating per product category”", language="text")

    with st.expander("Narrative – dynamic text that changes with filters", expanded=False):
        st.write(
            """
            **What it does:** Writes a summary sentence that updates when you slice or filter the report.  
            **Use case:** *“Total sales reached $1.2M, which is 5% above target. The best region was Europe.”*  
            Filter to Asia, and the sentence rewrites itself.  
            """
        )
        st.caption("Great for executive dashboards – they get both the visual *and* an plain‑English explanation.")

    st.markdown("---")

    # 3. DISTRIBUTION & PART‑TO‑WHOLE
    st.header("Step 3 – Showing Parts of a Whole")
    st.write(
        """
        “What percentage of total sales comes from each product?” That’s a part‑to‑whole question. Choose carefully – the wrong visual can mislead.
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pie & Donut Charts")
        st.write("**Best for 3–5 categories.**")
        st.write("Market share by competitor. Donut > Pie because you can put the total in the middle.")
        st.warning("Avoid when you have more than 5 slices – nobody can distinguish six shades of blue.")
    with col2:
        st.subheader("Treemap")
        st.write("**Many categories, nested rectangles.**")
        st.write("Portfolio of 50 stocks – the biggest rectangle is your largest holding. Drill down to see sub‑categories.")
        st.success("Extremely space‑efficient. Use it whenever a pie chart becomes a mess.")

    with st.expander("Funnel – for linear processes with drop‑off", expanded=False):
        st.write(
            """
            **What it does:** Shows sequential stages as a narrowing funnel.  
            **Use case:** Sales pipeline (Leads → Qualified → Proposal → Closed Won) or website conversion (Visits → Signups → Purchases).  
            **Why it’s insightful:** The narrowing width highlights exactly where you lose people.  
            """
        )

    st.markdown("---")

    # 4. TRENDS & TIME SERIES
    st.header("Step 4 – Trends & Time Series ")
    st.write(
        """
        Time is the most common axis in business reporting. These visuals are your go‑to tools.
        """
    )

    with st.expander("Line Chart & Area Chart – the gold standard", expanded=False):
        st.write(
            """
            **Line chart:** Stock prices, monthly revenue, daily visitors. Clean and familiar.  
            **Area chart:** Same but filled underneath. Best for cumulative totals (total users, total rainfall).  
            **When to use which:** Line for trends, area for magnitude of accumulation.  
            """
        )

    with st.expander("Ribbon Chart – tracking rank changes", expanded=False):
        st.write(
            """
            **What it does:** Shows how categories move up and down in rank over time.  
            **Use case:** Top 5 selling products each month. If Product A drops from #1 to #5, the ribbon visually flows downward.  
            **Why it’s special:** Bar charts show the value, but only ribbons show the *change in position*.  
            """
        )

    st.markdown("---")

    # 5. CORRELATION & OUTLIERS
    st.header("Step 5 – Finding Relationships & Outliers")
    st.write(
        """
        Sometimes you don’t know what you’re looking for – you just want to spot patterns or anomalies.
        """
    )

    with st.expander("Scatter Chart – X vs. Y with a third dimension", expanded=False):
        st.write(
            """
            **What it does:** Plots two numeric variables. Add a “Play axis” to see changes over time, or bubble size for a third measure.  
            **Use case:** Profit margin (X) vs. Sales volume (Y). Large, high‑profit bubbles = your golden products.  
            **Why it’s powerful:** Instantly reveals outliers – the tiny bubble in the top‑left that’s high profit but low volume.  
            """
        )
        st.code("Pro tip: Use the ‘Analytics’ pane to add a trend line, median line, or even a clustering model.", language="text")

    st.markdown("---")

    # 6. AI‑POWERED “WHY DID THAT HAPPEN?” VISUALS
    st.header("Step 6 – AI‑Powered Root Cause Analysis ")
    st.write(
        """
        This is where Power BI stops being a reporting tool and becomes an analytics assistant.  
        These visuals automatically search for patterns and explain changes.
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Decomposition Tree")
        st.write("**Automatic detective.** Click a measure, then break it down by any dimension. “Why did sales drop 20%?” → Region → Product → Salesperson → culprit found.")
        st.info("Also great for ranking: “Which segment contributed the most?”")
    with col2:
        st.subheader("Key Influencers")
        st.write("**Machine learning in one click.** “What makes customers churn?” It analyses all data and returns: *“If support tickets > 3 → 85% churn probability. If subscription < 6 months → 60% churn probability.”*")
        st.success("No separate AI service. It’s built into your Power BI license.")

    st.markdown("---")

    # 7. GEOGRAPHIC & SPECIALIZED
    st.header("Step 7 – Geographic & Specialized Visuals")
    st.write(
        """
        When your data has a “where” or a “how we got here”, these visuals shine.
        """
    )

    with st.expander("Map – location intelligence", expanded=False):
        st.write(
            """
            **Use case:** Store density by zip code, sales by state, delivery routes.  
            **Options:** Azure Maps (built‑in), ArcGIS (advanced), or Filled Map (choropleth).  
            """
        )

    with st.expander("Waterfall – financial add/subtract steps", expanded=False):
        st.write(
            """
            **What it does:** Shows how a starting value becomes an ending value through positive and negative contributions.  
            **Use case:** P&L statement (Revenue – COGS – Operating Expenses = Net Income) or inventory (Starting + Purchases – Sales = Ending).  
            **Why it’s irreplaceable:** A bar chart can’t show the step‑by‑step journey.  
            """
        )

    with st.expander("Infographics (Custom Visuals)", expanded=False):
        st.write(
            """
            **What they are:** Community‑built or custom visuals (HTML Content, Chiclet Slicer, Radar Chart, etc.).  
            **Use case:** A “thermometer” for fundraising progress, a “radar chart” for employee skills.  
            **Caution:** Custom visuals may have performance or security implications. Use from AppSource only.  
            """
        )

    st.markdown("---")

    # 8. THE 5‑SECOND CHEAT SHEET (DataFrame)
    st.header("The 5‑Second Cheat Sheet – Which Visual Should You Grab?")
    st.write(
        """
        Print this, bookmark it, or tape it to your monitor. When you’re stuck, ask yourself the question in the left column.
        """
    )

    cheat_df = pd.DataFrame({
        "You want to…": [
            "Show one big number",
            "Show progress to a goal",
            "Let users filter the report",
            "Show a simple percentage split (3‑5 parts)",
            "Show many categories by size",
            "Show a process with drop‑off",
            "Show change over time",
            "Show ranking changes over time",
            "Find outliers or relationships",
            "Answer “Why did this happen?”",
            "Find hidden causes automatically",
            "Let people ask questions in plain English",
            "Show geographic data",
            "Show financial add/subtract steps"
        ],
        "Use this visual": [
            "Card",
            "KPI or Gauge",
            "Slicer",
            "Pie / Donut",
            "Treemap",
            "Funnel",
            "Line Chart / Area Chart",
            "Ribbon Chart",
            "Scatter Chart",
            "Decomposition Tree",
            "Key Influencers",
            "Q&A",
            "Map",
            "Waterfall"
        ]
    })
    st.dataframe(cheat_df, use_container_width=True, hide_index=True)
    st.caption("When in doubt: start with a **line chart** for time, a **card** for a single number, and a **slicer** for interactivity.")

    st.markdown("---")

    # 9. CHECKLIST FOR CHOOSING THE RIGHT VISUAL
    st.header("Your Personal Checklist Before You Publish a Report")
    st.write(
        """
        Copy this into your project notebook or sticky notes app. Tick off each item before you share a report with stakeholders.
        """
    )
    checklist = """
    **Before you drag a field onto the canvas:**  
    - [ ] Have I written down the *exact question* this visual should answer?  
    - [ ] Is it a “one number” question? → Card.  
    - [ ] Is it a “trend over time” question? → Line/Area.  
    - [ ] Is it a “part of a whole” question with ≤5 parts? → Pie/Donut. With >5 parts? → Treemap.  
    - [ ] Is it a “process drop‑off” question? → Funnel.  
    - [ ] Is it a “ranking change” question? → Ribbon chart.  
    - [ ] Is it a “root cause” or “why” question? → Decomposition Tree or Key Influencers.  

    **While building the report:**  
    - [ ] Did I add a slicer so users can explore?  
    - [ ] Did I avoid using a Pie chart for 12 categories? (Seriously, don’t.)  
    - [ ] Did I label the axes clearly (especially for Scatter and Waterfall)?  

    **Before publishing:**  
    - [ ] Have I tested the report on a mobile layout?  
    - [ ] Did I add a brief narrative or tooltip for complex visuals?  
    - [ ] Would a non‑technical stakeholder understand this in 10 seconds?  
    """
    st.markdown(checklist)
    st.success("Check everything – then your report is ready for the business.")

    st.markdown("---")

    # 10. RESOURCES – BOOKS, DOCS, YOUTUBE
    st.header("Great Resources to Go Deeper")
    st.write(
        """
        You don’t need to memorise this article. Bookmark these instead – they’re free, practical, and updated regularly.
        """
    )
    st.markdown(
        """
        **Official Microsoft Documentation (always up to date)**  
        - [Create a Decomposition Tree (step by step)](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-decomposition-tree)  
        - [Use Key Influencers visual](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-influencers)  
        - [Q&A visual best practices](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-q-and-a)  
 

        **Practice Datasets (built into Power BI)**  
        - Go to **Get Data** → **Samples** → **Financial Sample** or **Retail Analysis Sample**.  
        - These are pre‑loaded and perfect for practising every visual above.  

        **Communities**  
        - [Power BI Community Forum](https://community.powerbi.com) – Microsoft’s official forum.  
        - r/PowerBI on Reddit – great for “is this visual the right choice?” discussions.  

        **Books (if you like paper)**  
        - *Power BI Cookbook* by Greg Deckler – full of recipes for specific visuals.  
        - *Storytelling with Data* by Cole Nussbaumer Knaflic – not Power BI specific, but essential for choosing the right chart.  
        """
    )
    st.markdown("---")

    # 11. FINAL ADVICE
    st.header("Keep It Simple, Then Iterate")
    st.write(
        """
        You don’t need a Decomposition Tree for everything. You don’t need to ban pie charts entirely.  

        **Start with the basics:** Card, Slicer, Line chart, Table.  
        **Add complexity only when the question demands it.**  

        Your next actions:  
        1. Open Power BI Desktop and load the **Financial Sample** dataset.  
        2. Build a Card for total sales.  
        3. Add a Slicer for year.  
        4. Add a Line chart for sales over time.  
        5. Swap the Line chart for a Ribbon chart – see how ranks change.  
        6. Throw in a Key Influencers visual and ask: *“What influences profit?”* – watch the AI work.  

        The more you experiment, the more natural it becomes.  
        And remember: the best visual is the one that answers the question *clearly* – not the one that looks coolest.
        """
    )
    st.markdown("---")
    st.caption("© 2026 | Beyond Bars and Columns – Unlocking Advanced Insights with Power BI Visuals | Choose wisely, tell better stories.")