import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(page_title="Burhanettin's Place & AI Lab", page_icon="🚀", layout="wide")

# --- 1. AI EĞİTİM MANTIĞI (Case Study Fonksiyonu) ---
def classify_comment(text):
    text = text.lower()
    bad_words = ["kötü", "spam", "hakaret"] 
    coffee_words = ["kahve", "coffee", "support", "destek"]
    advice_words = ["tavsiye", "öneri", "suggest", "improve"]

    if any(word in text for word in bad_words):
        return "⚠️ Quarantine (bad words)"
    elif any(word in text for word in coffee_words):
        return "☕ Coffee & Support"
    elif any(word in text for word in advice_words):
        return "💡 Advice/Suggestion"
    else:
        return "✅ General/Like"

# --- 2. VERİ SAKLAMA (Session State) ---
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {"user": "Burhanettin", "content": "EVEYES 360: Bilim ve sanatın buluşma noktası.", "category": "✅ General/Like", "likes": 500}
    ]

# --- 3. YAN MENÜ (Navigation) ---
st.sidebar.title("💎 EVEYES 360 Ecosystem")
app_mode = st.sidebar.selectbox("Bölüm Seçiniz", ["📱 Burhanettin's Place (Feed)", "🛡️ Admin & Archive (1M Control)", "🧪 AI Training Lab (Case Study)"])
dil = st.sidebar.selectbox("Language", ["English", "Turkish", "Yoruba", "Spanish", "French"])

# --- BÖLÜM 1: SOSYAL AKIŞ ---
if app_mode == "📱 Burhanettin's Place (Feed)":
    st.title("🚀 Burhanettin's Place")
    with st.form("post_form"):
        user = st.text_input("User Name")
        content = st.text_area("What's on your mind?")
        submitted = st.form_submit_button("Share")
        if submitted and user and content:
            cat = classify_comment(content)
            st.session_state.posts.append({"user": user, "content": content, "category": cat, "likes": 0})
            st.success("Shared successfully!")

    st.subheader("📱 Main Stream")
    for i, post in enumerate(reversed(st.session_state.posts)):
        if post['category'] != "⚠️ Quarantine (bad words)":
            with st.container():
                st.write(f"### 👤 @{post['user']}")
                st.write(post['content'])
                st.caption(f"Category: {post['category']}")
                if st.button(f"❤️ {post['likes']}", key=f"like_{i}"):
                    post['likes'] += 1
                    st.rerun()
                st.divider()

# --- BÖLÜM 2: YÖNETİCİ PANELİ ---
elif app_mode == "🛡️ Admin & Archive (1M Control)":
    st.title("📊 Big Data Management")
    st.info("Bu panel 1 milyon yorumu yönetmek ve filtrelemek için tasarlanmıştır.")
    target_cat = st.selectbox("Grup Seçin", ["All", "⚠️ Quarantine (bad words)", "☕ Coffee & Support", "💡 Advice/Suggestion", "✅ General/Like"])
    
    for i, post in enumerate(st.session_state.posts):
        if target_cat == "All" or post['category'] == target_cat:
            col1, col2 = st.columns([4, 1])
            col1.write(f"**{post['user']}**: {post['content']} ({post['category']})")
            if col2.button("Delete", key=f"del_{i}"):
                st.session_state.posts.pop(i)
                st.rerun()

# --- BÖLÜM 3: AI LABORATUVARI (Yeni Eklenen Case Study) ---
elif app_mode == "🧪 AI Training Lab (Case Study)":
    st.title("🧪 Health Sciences AI Training Lab")
    st.write("Bu bölüm, sağlık verilerini AI modellerine öğretmek için kullanılan 'Metacognitive' denetim alanıdır.")
    
    test_topic = st.text_input("Eğitilecek Konu (Örn: Biosonology - 528Hz):", "DNA Repair & Sound Frequencies")
    
    if st.button("AI Akıl Yürütme Sürecini Çalıştır"):
        with st.status("Veriler İşleniyor...", expanded=True) as status:
            st.write("🔍 Biosonoloji veritabanı taranıyor...")
            time.sleep(1)
            st.write("📚 Selçuklu Tıbbı ve Makam Terapi kayıtları karşılaştırılıyor...")
            time.sleep(1)
            st.write("🧠 AI Akıl Yürütme (Reasoning) yolu oluşturuluyor...")
            status.update(label="Analiz Tamamlandı!", state="complete")
        
        st.subheader("🤖 AI Trainer Denetim Raporu:")
        st.success(f"""
        **Konu:** {test_topic}
        \n**Denetim Notu:** AI modeline bu veriyi işlerken hem modern 'Biosonology' 
        hem de 'Seljuk Medicine' verilerini birleştirmesi talimatı verildi. 
        Spekülatif bilgiler 'Karantina' algoritmasıyla filtrelendi.
        """)
