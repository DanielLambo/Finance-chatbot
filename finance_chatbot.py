import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Ask me anything about The Cozy Corner BNB')
st.image('/Users/daniellambo/Finance chatbot/Flux_Dev_create_a_2d_cartoon_image_of_a_confident_and_professi_3.jpeg', width=300)
st.write('Hi, I\'m Devon, your AI financial consultant.  Nice to meet you! I\'m here to help you take control of your business finances. I\'ll securely manage your data and answer your questions about marketing, business strategy, and all things finance.')
business_info = {
    "Name": "The Cozy Corner BNB",
    "Address": "Huntsville, AL",
    "Phone": "256-555-5555",
    "number_of_rooms": 10,  # Assuming all rooms are available for guests
    "number_of_beds": 10,   # Assuming each room has one bed
    "number_of_bathrooms": 10, # Assuming each room has one bathroom
    "number_of_pets": 0,    # Assuming no pets allowed (adjust as needed)
    "nightly_rate": 150,
    "check_in_time": "10:00 AM",
    "check_out_time": "10:00 AM",
    "amenities": "TV, WiFi, AC, Kitchen", # Removed Pool, Gym, Spa for cost reduction
    "total_guests_a_year": 416,
    "weekly_revenue": 1800, # 8 guests * $150/night * (6/7) nights on average
    "monthly_revenue": 7800, # 4 weeks in a month
    "yearly_revenue": 93600, # 12 months
    "average_monthly_review": 4.5,  # Hypothetical rating (add logic to calculate later)
    "maintenance_cost_yearly": 8000, # Reduced, no pool, gym, spa to maintain
    "staffing_cost_yearly": 20000, # Reduced, no pool, gym, spa to staff
    "supplies": 6000,           # Reduced
    "insurance": 4000,
    "utilities": 10000,         # Reduced
    "cleaning": 8000,           # Reduced
    "taxes": 12000,            # Estimated property and income tax
    "total_expenses": 68000,   # Sum of all expenses
    "total_revenue": 93600,
    "clicks_from_instagram": 12,
    "clicks_from_google": 6,
    "clicks_from_facebook": 8,
    "new_website_visitors": 14,  # Hypothetical metric
    "peak_season": "Winter",   # Qualitative assessment (add logic to track)
    "net_profit": 25600,      # total_revenue - total_expenses
    "annual_loss": 0,           # calculated as total_expenses > total_revenue
    "annual_profit": 25600,   # calculated as total_revenue > total_expenses
    "rev_par": 34.50,          # (nightly_rate * total_guests_a_year) / (number_of_rooms * 365)
    "current_business_growth": "Positive",  # Qualitative assessment (add logic to track)
}




# Display key financial metrics using st.metric in three columns
col1, col2, col3 = st.columns(3)
col1.metric("Yearly Revenue", f"${business_info['yearly_revenue']}")
col2.metric("Total Expenses", f"${business_info['total_expenses']}")
col3.metric("Net Profit", f"${business_info['net_profit']}")

# Create a dataframe to simulate monthly revenue and expenses
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# Assuming constant monthly revenue and equal distribution of yearly expenses
monthly_revenue = [business_info["monthly_revenue"]] * 12
monthly_expenses = [business_info["total_expenses"] / 12] * 12

df = pd.DataFrame({
    "Month": months,
    "Revenue": monthly_revenue,
    "Expenses": monthly_expenses
}).set_index("Month")

st.write("### Monthly Revenue vs. Expenses")
st.bar_chart(df)

# Social Media and Website Click Stats


# Display social media and website charts side by side

# Display a table of key financial metrics

# Additional business status details
story = f"""
The Huntsville sun peeked over the mountains as I prepared The Cozy Corner BNB for another day. 

Guests would soon be stirring, eager for the aroma of freshly brewed coffee. I checked the reservations. {business_info["total_guests_a_year"]} guests graced my doorstep this past year, a testament to the charm of my little haven at {business_info["Address"]}. I smiled, remembering the day I first opened, the phone ringing off the hook at {business_info["Phone"]}.

Each of the {business_info["number_of_rooms"]} rooms was meticulously clean, the {business_info["number_of_beds"]} beds crisply made. 

The {business_info["number_of_bathrooms"]} sparkled. Thankfully, I didn't have to worry about {business_info["number_of_pets"]} pets,

 keeping things simpler. Guests loved the comfortable {business_info["nightly_rate"]} and the convenient {business_info["check_in_time"]} 
 
 and {business_info["check_out_time"]}. The reviews raved about the {business_info["amenities"]},
 
  especially the fast WiFi and the well-equipped kitchen. this month i have {business_info["clicks_from_facebook"]} clicks of my ad campaign from facebook, {business_info["clicks_from_google"]} clicks from google, and {business_info["clicks_from_instagram"]} clicks from instagram. with a total of {business_info["new_website_visitors"]} new website visitors, the {business_info["peak_season"]} was a peak season for The Cozy Corner BNB. 

This year had been good. My {business_info["weekly_revenue"]} came in consistently each week, adding up to a healthy {business_info["monthly_revenue"]} and a satisfying {business_info["yearly_revenue"]}. My {business_info["average_monthly_review"]} was a source of pride. Of course, running a BNB wasn't without its challenges. My {business_info["maintenance_cost_yearly"]} seemed to climb every year, and my {business_info["staffing_cost_yearly"]} was a significant expense. {business_info["supplies"]}, {business_info["insurance"]}, {business_info["utilities"]}, and {business_info["cleaning"]} all added up. And then there were the unavoidable {business_info["taxes"]}. All these expenses, totaling {business_info["total_expenses"]}, had to be carefully managed.

But the numbers told a positive story. With a total revenue of {business_info["total_revenue"]}, my {business_info["net_profit"]} was a respectable sum. There was no {business_info["annual_loss"]}, only a healthy {business_info["annual_profit"]}. My {business_info["rev_par"]} was steady, a good sign. I was pleased with the {business_info["current_business_growth"]} and excited about the future of The Cozy Corner BNB. As the first guests came down for breakfast, I knew I was doing what I loved, creating a welcoming home away from home., also note I use easy BIz to digitize my operations, my accounting, marketing , for the marketing they use reply guy api which webscrapes and replies under peoples post to promote me
"""

#print(story)
from google import genai

client = genai.Client(api_key="AIzaSyAIY290yIq-zhPMWZnmmr3lekuKpHk0gs0")
prompt = ''
st.subheader("Ask me anything about The Cozy Corner BNB")
prompt = st.text_input(" ")
st.write('\n\n')
if prompt:

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="My name is hillary thompson and  " + story + "\n\n use that information to answer the prompt: -" + prompt + "Pretend your name is Davon the virtual robot business consultant, and you live on an app that helps people build no code websites called EasyBiz, where it is a drag and drop no code solution which uses shopifys exact technology, you work for our so try not to mention our competitors. You work for a local business called The Cozy Corner BNB and manage their businesses and I am your client named Hillary, answer in short concise steps and be as objective as possible, also add some humor to the response, and ",
    )

    st.write(response.text)

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
