import pandas as pd
import streamlit as st
import plotly.express as px

# Load the Excel file
excel_file = "Nouha_final_data_with_engagement22.xlsx"
df = pd.read_excel(excel_file,engine='openpyxl')

# Extract hashtags and their corresponding posts, likes, comments, and shares
hashtags = df["hashtags"].str.split().explode().str.lower()
hashtags_counts = hashtags.value_counts()
hashtags_info = []
for hashtag in hashtags_counts.index:
    hashtag_df = df[df["hashtags"].fillna("").str.lower().str.contains(hashtag)]
    total_likes = hashtag_df["likes"].sum()
    total_comments = hashtag_df["comments"].sum()
    total_shares = hashtag_df["shares"].sum()
    hashtags_info.append({
        "Hashtag": hashtag,
        "Total Posts": len(hashtag_df),
        "Total Likes": total_likes,
        "Total Comments": total_comments,
        "Total Shares": total_shares

    })

# Convert hashtags info to a DataFrame
hashtags_df = pd.DataFrame(hashtags_info)

# Streamlit app
st.title("Most Used Hashtags Analysis")
st.write("")

# Display the bar chart for most used hashtags
st.subheader("Bar Chart: Most Used Hashtags")
fig = px.bar(hashtags_df, x="Hashtag", y="Total Posts", title="Most Used Hashtags")
st.plotly_chart(fig, use_container_width=True)

# Display the detailed information about each hashtag
st.subheader("Detailed Information")
st.dataframe(hashtags_df)
