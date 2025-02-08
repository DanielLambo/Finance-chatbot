import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
gemini_api_key = os.getenv("gemini_api_key")

# Set up the Streamlit app
st.title('Ask Me Anything About The Cozy-Corner BNB')
st.image('Flux_Dev_create_a_2d_cartoon_image_of_a_confident_and_professi_3.jpeg', width=300)
st.write('Hi, I\'m Devon, your AI business consultant. Nice to meet you! I\'m here to help you take control of your business finances, website creation and marketing. I\'ll securely manage your data and answer your questions about marketing, business strategy, and all things finance. Look below to see how your current social and financial metrics look!')

# Business information
business_info = {
    "Name": "The Cozy Corner BNB",
    "Address": "Huntsville, AL",
    "Phone": "256-555-5555",
    "number_of_rooms": 10,
    "number_of_beds": 10,
    "number_of_bathrooms": 10,
    "number_of_pets": 0,
    "nightly_rate": 150,
    "check_in_time": "10:00 AM",
    "check_out_time": "10:00 AM",
    "amenities": "TV, WiFi, AC, Kitchen",
    "total_guests_a_year": 416,
    "weekly_revenue": 1800,
    "monthly_revenue": 7800,
    "yearly_revenue": 93600,
    "average_monthly_review": 4.5,
    "maintenance_cost_yearly": 8000,
    "staffing_cost_yearly": 20000,
    "supplies": 6000,
    "insurance": 4000,
    "utilities": 10000,
    "cleaning": 8000,
    "taxes": 12000,
    "total_expenses": 68000,
    "total_revenue": 93600,
    "clicks_from_instagram": 12,
    "clicks_from_google": 6,
    "clicks_from_facebook": 8,
    "new_website_visitors": 14,
    "peak_season": "Winter",
    "net_profit": 25600,
    "annual_loss": 0,
    "annual_profit": 25600,
    "rev_par": 34.50,
    "current_business_growth": "Positive",
}

# Display key financial metrics
st.markdown("### Key Financial Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Yearly Revenue", f"${business_info['yearly_revenue']:,.2f}")
col2.metric("Total Expenses", f"${business_info['total_expenses']:,.2f}")
col3.metric("Net Profit", f"${business_info['net_profit']:,.2f}")

# Monthly revenue vs. expenses chart
st.markdown("### Monthly Revenue vs. Expenses")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_revenue = [business_info["monthly_revenue"]] * 12
monthly_expenses = [business_info["total_expenses"] / 12] * 12

df = pd.DataFrame({
    "Month": months,
    "Revenue": monthly_revenue,
    "Expenses": monthly_expenses
}).set_index("Month")

st.bar_chart(df)

# Business story
story = f"""
The Huntsville sun peeked over the mountains as I prepared The Cozy Corner BNB for another day. 

Guests would soon be stirring, eager for the aroma of freshly brewed coffee. I checked the reservations. {business_info["total_guests_a_year"]} guests graced my doorstep this past year, a testament to the charm of my little haven at {business_info["Address"]}. I smiled, remembering the day I first opened, the phone ringing off the hook at {business_info["Phone"]}.

Each of the {business_info["number_of_rooms"]} rooms was meticulously clean, the {business_info["number_of_beds"]} beds crisply made. 

The {business_info["number_of_bathrooms"]} sparkled. Thankfully, I didn't have to worry about {business_info["number_of_pets"]} pets, keeping things simpler. Guests loved the comfortable {business_info["nightly_rate"]} and the convenient {business_info["check_in_time"]} and {business_info["check_out_time"]}. The reviews raved about the {business_info["amenities"]}, especially the fast WiFi and the well-equipped kitchen. This month I have {business_info["clicks_from_facebook"]} clicks of my ad campaign from Facebook, {business_info["clicks_from_google"]} clicks from Google, and {business_info["clicks_from_instagram"]} clicks from Instagram. With a total of {business_info["new_website_visitors"]} new website visitors, the {business_info["peak_season"]} was a peak season for The Cozy Corner BNB. 

This year had been good. My {business_info["weekly_revenue"]} came in consistently each week, adding up to a healthy {business_info["monthly_revenue"]} and a satisfying {business_info["yearly_revenue"]}. My {business_info["average_monthly_review"]} was a source of pride. Of course, running a BNB wasn't without its challenges. My {business_info["maintenance_cost_yearly"]} seemed to climb every year, and my {business_info["staffing_cost_yearly"]} was a significant expense. {business_info["supplies"]}, {business_info["insurance"]}, {business_info["utilities"]}, and {business_info["cleaning"]} all added up. And then there were the unavoidable {business_info["taxes"]}. All these expenses, totaling {business_info["total_expenses"]}, had to be carefully managed.

But the numbers told a positive story. With a total revenue of {business_info["total_revenue"]}, my {business_info["net_profit"]} was a respectable sum. There was no {business_info["annual_loss"]}, only a healthy {business_info["annual_profit"]}. My {business_info["rev_par"]} was steady, a good sign. I was pleased with the {business_info["current_business_growth"]} and excited about the future of The Cozy Corner BNB. As the first guests came down for breakfast, I knew I was doing what I loved, creating a welcoming home away from home., my business has grown since i started using easybiz , they use a reply guy api to webscrape and reply under comments to promte me and their no code website solution is a great idea, this is the first time i am ever digitizing my business though, i know nothing about tech at all, so this llm is all the help i have
"""

# Online Engagement Metrics
st.markdown("## Online Engagement Metrics")

# Create DataFrame for social media clicks
social_data = pd.DataFrame({
    "Platform": ["Instagram", "Google", "Facebook"],
    "Clicks": [
        business_info["clicks_from_instagram"],
        business_info["clicks_from_google"],
        business_info["clicks_from_facebook"]
    ]
})

# Altair chart: Social Media Clicks (Bar Chart)
social_chart = alt.Chart(social_data).mark_bar().encode(
    x=alt.X('Platform:N', title='Platform'),
    y=alt.Y('Clicks:Q', title='Clicks'),
    color=alt.Color('Platform:N', legend=None),
    tooltip=['Platform', alt.Tooltip('Clicks:Q')]
).properties(
    width=350,
    height=350,
    title="Social Media Clicks"
)

# Create DataFrame for website visitors
website_data = pd.DataFrame({
    "Metric": ["Website Visitors"],
    "Count": [business_info["new_website_visitors"]]
})

# Altair chart: Website Visitors (Bar Chart)
website_chart = alt.Chart(website_data).mark_bar(color="#2196F3").encode(
    x=alt.X('Metric:N', title=''),
    y=alt.Y('Count:Q', title='Count'),
    tooltip=['Metric', alt.Tooltip('Count:Q')]
).properties(
    width=350,
    height=350,
    title="New Website Visitors"
)
colA, colB = st.columns(2)
with colA:
    st.altair_chart(social_chart, use_container_width=True)
with colB:
    st.altair_chart(website_chart, use_container_width=True)

# Custom CSS to fix the chat bar to the bottom and avoid content overlap
st.markdown(
    """
    <style>
    .chat-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f9f9f9;
        padding: 10px;
        border-top: 1px solid #ccc;
        z-index: 100;
    }
    .chat-footer input {
        width: 80%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    .chat-footer button {
        padding: 10px 20px;
        margin-left: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
    }
    /* Ensure main content does not get hidden behind the chat footer */
    .main .block-container {
        padding-bottom: 120px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Chat interface wrapped in a fixed footer div
st.markdown('<div class="chat-footer">', unsafe_allow_html=True)
st.markdown("## Chat with Devon")
genai.configure(api_key=gemini_api_key)
prompt = st.text_input("Enter a prompt: ")
if prompt:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        "My name is hillary thompson and  " + story + "\n\n use that information to answer the prompt: -" + prompt + " Pretend your name is Davon the virtual robot business consultant, and you live on an app that helps people build no code websites called EasyBiz, where it is a drag and drop no code solution which uses shopifys exact technology, you work for our so try not to mention our competitors. You work for a local business called The Cozy Corner BNB and manage their businesses and I am your client named Hillary, answer in short concise steps and be as objective as possible, also add some interest to the response, dont make it too boring "
    )
    st.write(response.text)
st.markdown('</div>', unsafe_allow_html=True)
