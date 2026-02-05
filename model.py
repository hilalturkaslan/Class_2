def churn_nedeni_tahmin(text):
    text = text.lower()

    if "fiyat" in text or "pahalı" in text or "ücret" in text:
        return "Fiyatlandırma", 0.85
    elif "destek" in text or "cevap" in text or "müşteri hizmetleri" in text:
        return "Müşteri Desteği", 0.82
    elif "yavaş" in text or "hata" in text or "çöküyor" in text:
        return "Performans", 0.78
    elif "karışık" in text or "zor" in text or "anlaşılmıyor" in text:
        return "Kullanıcı Deneyimi", 0.75
    else:
        return "Diğer", 0.60
