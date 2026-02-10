import streamlit as st
from model import churn_nedeni_tahmin

st.set_page_config(
    page_title="SaaS Churn Analizi",
    page_icon="📉",
    layout="centered"
)

st.title("📉 SaaS Müşteri Kaybı Neden Analizi")
st.write("Müşterilerin neden ayrıldığını analiz edin")

st.markdown("---")

kullanici_yorumu = st.text_area(
    "📝 Müşteri Geri Bildirimi",
    placeholder="Müşteri Geri Bildirim Metni.",
    height=120
)

if st.button("🔍 Analiz Et"):
    if kullanici_yorumu.strip() == "":
        st.warning("Lütfen bir müşteri yorumu giriniz.")
    else:
        neden, guven = churn_nedeni_tahmin(kullanici_yorumu)

        st.markdown("### 📌 Tahmin Edilen Ayrılma Nedeni")
        st.success(f"**{neden}**")

        st.markdown("### 📊 Güven Oranı")
        st.progress(guven)
        st.write(f"%{int(guven * 100)} güven")

        st.markdown("### 💡 Öneri")
        if neden == "Müşteri Desteği":
            st.info("Müşteri destek süreçleri ve geri dönüş süreleri iyileştirilmeli.")
        elif neden == "Fiyatlandırma":
            st.info("Fiyatlandırma politikası gözden geçirilmeli.")
        elif neden == "Performans":
            st.info("Uygulama performansı ve sistem hataları iyileştirilmeli.")
        elif neden == "Kullanıcı Deneyimi":
            st.info("Arayüz ve kullanıcı deneyimi sadeleştirilmeli.")
        else:
            st.info("Geri bildirim detaylı şekilde analiz edilmelidir.")
