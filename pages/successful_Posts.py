import streamlit as st
import pandas as pd

# Load your data from Excel
df = pd.read_excel("Nouha_final_data_with_engagement1.xlsx",engine='openpyxl')

# Create a filtered DataFrame containing only successful posts
successful_posts = df[df["validPost"] == 1]

# Display the Streamlit app
st.title("List of Successful Posts")

if successful_posts.empty:
    st.write("No successful posts found.")
else:
    for index, row in successful_posts.iterrows():
        st.write(f"the Page Name: {row['pageName']}")
        st.write(f"Number of Flollowers: {row['number of likes']}")
        st.write(f"The number of Likes: {row['likes']}")
        st.write(f"The number of Comments: {row['comments']}")
        st.write(f"The number of Shares: {row['shares']}")
        st.markdown(f"URL: [{row['url']}]({row['url']})")
        st.write("---")
