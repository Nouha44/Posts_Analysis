import pandas as pd
import streamlit as st

# Load the Excel file
excel_file = "Nouha_final_data_with_engagement1.xlsx"
df = pd.read_excel(excel_file,engine='openpyxl')
st.title("Likes/Comments/Shares/viewCounts Analysis")

def load_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
selected_question = st.selectbox("Select a question:", ["top 50 Most Liked posts", "top 50 Most commented posts","top 50 Most shared posts","top 50 Most viewed videos"])

if selected_question == "top 50 Most Liked posts":
    st.subheader("Question: top 50 Most Liked posts")
    top_posts = df.nlargest(50, "likes")
    top_posts_info = top_posts[["postId","pageName", "likes", "url"]]
    table_data = []
    for index, row in top_posts_info.iterrows():
      st.write(f"PostId: {row['postId']}, Likes: {row['likes']},{row['pageName']}")
      st.write(f"URL: <a href='{row['url']}' target='_blank'>{row['url']}</a>", unsafe_allow_html=True)
      st.write("---")       
       
elif selected_question == "top 50 Most commented posts":
    st.subheader("Question: top 50 Most Commented posts")
    top_comments = df.nlargest(50, "comments")
    top_comments_info = top_comments[["postId", "pageName", "comments", "url"]]
    table_data = []
    for index, row in top_comments_info.iterrows():
      st.write(f"PostId: {row['postId']}, comments: {row['comments']}")
      st.write(f"URL: <a href='{row['url']}' target='_blank'>{row['url']}</a>", unsafe_allow_html=True)
      st.write("---")          
elif selected_question == "top 50 Most shared posts":
    st.subheader("Question: top 50 Most Shared posts")
    top_shared = df.nlargest(50, "shares")
    top_shared_info = top_shared[["postId", "pageName", "shares", "url"]]
    table_data = []
    for index, row in top_shared_info.iterrows():
      st.write(f"PostId: {row['postId']}, shares: {row['shares']}")
      st.write(f"URL: <a href='{row['url']}' target='_blank'>{row['url']}</a>", unsafe_allow_html=True)
      st.write("---")          
elif selected_question == "top 50 Most viewed videos":
    st.subheader("Question: top 50 Most viewed videos")
    top_shared = df.nlargest(50, "viewsCount")
    top_shared_info = top_shared[["postId", "pageName", "viewsCount", "url"]]
    table_data = []
    for index, row in top_shared_info.iterrows():
      st.write(f"PostId: {row['postId']},viewsCount: {row['viewsCount']}")
      st.write(f"URL: <a href='{row['url']}' target='_blank'>{row['url']}</a>", unsafe_allow_html=True)
      st.write("---")   