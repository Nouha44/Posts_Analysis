import pandas as pd
import streamlit as st

# Load the Excel file
excel_file = "Nouha_final_data_with_engagement1.xlsx"
df = pd.read_excel(excel_file,engine='openpyxl')

# Convert the "time" column to datetime format
df['time'] = pd.to_datetime(df['time'])

# Extract the time in the format HH:MM:SS
df['extracted_time'] = df['time'].dt.strftime('%H:%M:%S')

st.title("Likes Analysis")
st.write("")

# Create a slider for selecting the range of likes
selected_likes_range = st.slider("Select a range of likes:", min_value=df['likes'].min(), max_value=df['likes'].max(), value=(df['likes'].min(), df['likes'].max()))

# Filter the DataFrame based on the selected range of likes
filtered_df = df[(df['likes'] >= selected_likes_range[0]) & (df['likes'] <= selected_likes_range[1])]

# Display the filtered DataFrame
st.subheader("Posts with Likes in the Selected Range")
#st.dataframe(filtered_df[['pageName', 'postId', 'url', 'extracted_time']])
for index, row in filtered_df.iterrows():
      st.write(f"PostId: {row['postId']},extracted_time: {row['extracted_time']}")
      st.write(f"URL: <a href='{row['url']}' target='_blank'>{row['url']}</a>", unsafe_allow_html=True)
      st.write("---") 
