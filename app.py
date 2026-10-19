import streamlit as st
import urllib.parse

st.set_page_config(page_title="EximSaif AI Global", page_icon="🌾")

lang = st.selectbox("🌐 Language / Bhasha / اللغة", ["English", "Hindi", "Arabic", "Bhojpuri"])

if lang == "Hindi":
    title = "🌾 EximSaif AI - Chapra Se Dubai Tak"
    btn_wp = "💬 WhatsApp Pe Baat Karo"
    btn_email = "📧 Email Se Sampark Karo"
    paste_label = "Buyer ka reply yaha paste karo"
    gen_btn = "🤖 Auto Reply Banao"
elif lang == "Arabic":
    title = "🌾 EximSaif AI - من شابرا إلى دبي"
    btn_wp = "💬 اتصل عبر واتساب"
    btn_email = "📧 اتصل عبر البريد الإلكتروني"
    paste_label = "الصق رد المشتري هنا"
    gen_btn = "🤖 إنشاء رد تلقائي"
elif lang == "Bhojpuri":
    title = "🌾 EximSaif AI - Chhapra Se Dubai"
    btn_wp = "💬 WhatsApp Par Baat Kari"
    btn_email = "📧 Email Kari"
    paste_label = "Buyer ke reply ke paste kari"
    gen_btn = "🤖 Reply Banayi"
else:
    title = "🌾 EximSaif AI - Chhapra To Dubai"
    btn_wp = "💬 Contact via WhatsApp"
    btn_email = "📧 Contact via Email"
    paste_label = "Paste Buyer Reply Here"
    gen_btn = "🤖 Generate Auto Reply"

st.title(title)
st.success("Saif | +91 7492013591 | Chhapra, Bihar | Verified")
st.divider()

col1, col2 = st.columns(2)
with col1:
    wp_link = f"https://wa.me/917492013591?text={urllib.parse.quote('Hello Saif, Rice Export Inquiry')}"
    st.link_button(btn_wp, wp_link, type="primary", use_container_width=True)
with col2:
    st.link_button(btn_email, f"mailto:saif@eximsaif.com", use_container_width=True)

st.divider()
st.subheader(paste_label)
buyer_reply = st.text_area("", height=150, placeholder="Ticket ID 3254560...")

if st.button(gen_btn, type="primary"):
    low = buyer_reply.lower() if buyer_reply else ""
    if "ticket" in low or "3254560" in low or low == "":
        body = "Dear Lulu Team,\n\nThank you for Ticket ID 3254560.\n\nI am from Chhapra, Bihar - Ready to supply 1121 Basmati Rice.\n\nPrice: $1150/MT FOB, MOQ: 24 MT, Docs: IEC, APEDA Ready.\n\nWhatsApp: +91 7492013591\n\nPlease guide for vendor registration.\n\nRegards,\nSaif Ali Khan\nEximSaif AI"
        subject = "Re: Ticket ID 3254560 - Basmati Supply - Chhapra"
    else:
        body = f"Thanks for reply: {buyer_reply[:100]}\n\nPrice $1150/MT Ready.\n\nRegards Saif +91 7492013591"
        subject = "Re: EximSaif AI - Quotation"

    to = "headoffice@ae.lulumea.com"
    gmail_link = f"https://mail.google.com/mail/?view=cm&to={to}&su={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
    st.success("✅ Auto Reply Ready BOSS!")
    st.text_area("Final Reply:", body, height=200)
    st.link_button("📧 1 CLICK GMAIL SE BHEJO", gmail_link, type="primary")

st.caption("Made in Chhapra | Chrome App Ready | Add New Function Anytime!")
