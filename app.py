import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Burhanettin's Place - Admin Control", page_icon="🛡️")

# --- 1. FONKSİYON: Yorumları Gruplandırma (Yapay Zeka Mantığı) ---
def classify_comment(text):
    text = text.lower()
    # Kötü sözler filtresi (Örnektir, genişletilebilir)
    bad_words = ["bad", "disgusting", "stupid", "spam"] 
    # Destek ve Kahve filtresi
    coffee_words = ["advice", "coffee", "offers", "support", "support"]
    # Tavsiye filtresi
    advice_words = ["advice", "öneri", "should", "suggest"]

    if any(word in text for word in bad_words):
        return "⚠️ Quarantine (bad words)"
    elif any(word in text for word in coffee_words):
        return "☕ Coffee & Support"
    elif any(word in text for word in advice_words):
        return "💡 Advice"
    else:
        return "✅ like"

# --- 2. VERİ SAKLAMA ---
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {"user": "Burhanettin", "content": "Growing Fast!", "category": "✅ like", "likes": 500}
    ]

# --- 3. ARAYÜZ ---
st.title("🚀 Burhanettin's Place")
st.sidebar.title("Admin Panel")
app_mode = st.sidebar.selectbox("Select Sections", ["Main Stream", "Admin's Archive"])

if app_mode == "Main Stream":
    with st.form("post_form"):
        user = st.text_input("User Name")
        content = st.text_area("Comments")
        submitted = st.form_submit_button("Share")
        
        if submitted and user and content:
            cat = classify_comment(content) # Yorumu otomatik sınıflandır
            st.session_state.posts.append({"user": user, "content": content, "category": cat, "likes": 0})
            st.success(f"Your Comments'{cat}' shared!")

    st.subheader("📱 Main Stream")
    for post in st.session_state.posts:
        if post['category'] != "⚠️ Quarantine (bad words)": # Kötüleri akışta gösterme
            st.write(f"**@{post['user']}**: {post['content']} | {post['category']}")
            st.divider()

elif app_mode == "Admin's Archive":
    st.header("📊 Comments Archive")
    
    # Kategorilere göre filtreleme
    target_cat = st.selectbox("All the Group", ["All", "⚠️ Quarantine (bad words)", "☕Coffee & Support", "💡 Advice", "✅ like"])
    
    for i, post in enumerate(st.session_state.posts):
        if target_cat == "All" or post['category'] == target_cat:
            col1, col2 = st.columns([4, 1])
            col1.write(f"**{post['user']}**: {post['content']} ({post['category']})")
            if col2.button("Delete", key=f"del_{i}"):
                st.session_state.posts.pop(i)
                st.rerun()

    if st.button("Delete All the Comments"):
        st.session_state.posts = [p for p in st.session_state.posts if p['category'] != "⚠️ Quarantine (bad words)"]
        st.success("All the comments deleted!")
