import streamlit as st
import pandas as pd

# Load your Excel file into a pandas DataFrame
excel_file = "Nouha_final_data_with_engagement222.xlsx"
df = pd.read_excel(excel_file,engine='openpyxl')

# Get unique pageNames for the dropdown
page_names = df['pageName'].unique()
selected_page = st.selectbox("Select pageName", page_names)

# Determine whether to sort by likes or comments
selected_option = st.radio("Select Option", ("Most Liked Posts", "Most Commented Posts"))

st.title(f"Top 20 {selected_option} for {selected_page}")

# Filter the DataFrame based on the selected pageName
filtered_df = df[df['pageName'] == selected_page]

# Sort the filtered DataFrame based on the selected column
sort_by_column = "likes" if selected_option == "Most Liked Posts" else "comments"
sorted_df = filtered_df.sort_values(by=sort_by_column, ascending=False)

# Display the top 20 posts for the selected pageName
count = 0
for index, row in sorted_df.iterrows():
    if count >= 20:
        break
    st.write(f"**Post ID:** {row['postId']}")
    st.write(f"**Likes:** {row['likes']}")
    st.write(f"**URL:** [{row['url']}]({row['url']})")
    st.write(f"**Comments:** {row['comments']}")
    st.write(f"**Shares:** {row['shares']}")
    st.write("---")
    count += 1