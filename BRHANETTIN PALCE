import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Burhanettin's Place - Admin Control", page_icon="🛡️")

# --- 1. FONKSİYON: Yorumları Gruplandırma (Yapay Zeka Mantığı) ---
def classify_comment(text):
    text = text.lower()
    # Kötü sözler filtresi (Örnektir, genişletilebilir)
    bad_words = ["kötü", "çirkin", "aptal", "spam"] 
    # Destek ve Kahve filtresi
    coffee_words = ["kahve", "coffee", "ısmarlar", "destek", "support"]
    # Tavsiye filtresi
    advice_words = ["tavsiye", "öneri", "should", "suggest"]

    if any(word in text for word in bad_words):
        return "⚠️ Karantina (Kötü Söz)"
    elif any(word in text for word in coffee_words):
        return "☕ Kahve & Destek"
    elif any(word in text for word in advice_words):
        return "💡 Tavsiye/Öneri"
    else:
        return "✅ Genel/Beğeni"

# --- 2. VERİ SAKLAMA ---
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {"user": "Burhanettin", "content": "EVEYES 360 vizyonu ile büyüyoruz!", "category": "✅ Genel/Beğeni", "likes": 500}
    ]

# --- 3. ARAYÜZ ---
st.title("🚀 Burhanettin's Place")
st.sidebar.title("Yönetim Paneli")
app_mode = st.sidebar.selectbox("Bölüm Seçin", ["Ana Akış", "Yönetici Arşivi (1M Veri Yönetimi)"])

if app_mode == "Ana Akış":
    with st.form("post_form"):
        user = st.text_input("Kullanıcı Adı")
        content = st.text_area("Yorumunuz")
        submitted = st.form_submit_button("Paylaş")
        
        if submitted and user and content:
            cat = classify_comment(content) # Yorumu otomatik sınıflandır
            st.session_state.posts.append({"user": user, "content": content, "category": cat, "likes": 0})
            st.success(f"Yorumunuz '{cat}' olarak işaretlendi ve paylaşıldı!")

    st.subheader("📱 Canlı Akış")
    for post in st.session_state.posts:
        if post['category'] != "⚠️ Karantina (Kötü Söz)": # Kötüleri akışta gösterme
            st.write(f"**@{post['user']}**: {post['content']} | {post['category']}")
            st.divider()

elif app_mode == "Yönetici Arşivi (1M Veri Yönetimi)":
    st.header("📊 Yorum Arşivi ve Moderasyon")
    
    # Kategorilere göre filtreleme
    target_cat = st.selectbox("Görüntülenecek Grup", ["Hepsi", "⚠️ Karantina (Kötü Söz)", "☕ Kahve & Destek", "💡 Tavsiye/Öneri", "✅ Genel/Beğeni"])
    
    for i, post in enumerate(st.session_state.posts):
        if target_cat == "Hepsi" or post['category'] == target_cat:
            col1, col2 = st.columns([4, 1])
            col1.write(f"**{post['user']}**: {post['content']} ({post['category']})")
            if col2.button("Sil", key=f"del_{i}"):
                st.session_state.posts.pop(i)
                st.rerun()

    if st.button("Karantinadaki Tüm Yorumları Temizle"):
        st.session_state.posts = [p for p in st.session_state.posts if p['category'] != "⚠️ Karantina (Kötü Söz)"]
        st.success("Tüm kötü yorumlar silindi!")
