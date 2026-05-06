import streamlit as st
import requests
import json

# --- 1. الإعدادات التقنية للنظام ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide", initial_sidebar_state="collapsed")

# متغيرات الحساب (تأكد من وجود الصور في مستودعك بنفس الأسماء)
USER_REPO = "yusefalhaj88-bit/Python"
BG_URL = f"https://raw.githubusercontent.com/{USER_REPO}/main/background.png"
LOGO_URL = f"https://raw.githubusercontent.com/{USER_REPO}/main/logo.png"

# --- 2. الهندسة البصرية المتقدمة (CSS) ---
st.markdown(f"""
<style>
    /* إخفاء القوائم والزخارف الافتراضية */
    header, footer, #MainMenu {{visibility: hidden;}}
    
    /* الفضاء النيوني الحقيقي */
    .stApp {{
        background: #000000 !important;
        background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.5)), url("{BG_URL}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: #ffffff;
    }}

    /* تصميم الزجاج الكريستالي (Glassmorphism) */
    .glass-container {{
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 30px;
        padding: 40px;
        margin: 20px auto;
        max-width: 850px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    }}

    /* اسم المنتج (إشعاع ليزري) */
    .hero-title {{
        color: #00f2ff;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 900;
        text-shadow: 0 0 15px #00f2ff, 0 0 30px #0062ff;
        margin-top: 10px;
        letter-spacing: 2px;
    }}

    /* خانة البحث البيضوية (سوداء من الداخل) */
    div[data-baseweb="input"] {{
        background-color: #000000 !important;
        border: 2px solid #00f2ff !important;
        border-radius: 50px !important;
        box-shadow: 0 0 20px #00f2ff, inset 0 0 10px rgba(0,242,255,0.2) !important;
        height: 70px !important;
        padding: 0 25px !important;
    }}
    input {{
        color: #00f2ff !important;
        background-color: transparent !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }}

    /* زر التوليد النيوني الحاد */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        height: 60px;
        border: none !important;
        box-shadow: 0 0 25px #00f2ff !important;
        font-size: 1.2rem;
        margin-top: 20px;
    }}

    /* صندوق النتائج الذكي */
    .res-box {{
        background: rgba(0, 10, 25, 0.95);
        border: 2px solid #00f2ff;
        border-radius: 20px;
        padding: 25px;
        margin-top: 30px;
        color: #00f2ff;
        direction: rtl;
        line-height: 1.8;
        box-shadow: 0 0 30px rgba(0,242,255,0.2);
    }}

    /* زر الدفع الفخم */
    .checkout-btn {{
        background: linear-gradient(135deg, #00f2ff, #0062ff);
        color: #000 !important;
        padding: 18px 50px;
        border-radius: 50px;
        font-weight: 900;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 30px #00f2ff;
        margin-top: 25px;
        font-size: 1.3rem;
    }}
</style>
""", unsafe_allow_html=True)

# --- 3. منطق محرك الذكاء الاصطناعي (Groq) ---
def call_ai_engine(query):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "أنت خبير تسويق في منصة EcomMind AI. اكتب استراتيجية مبيعات لمنتج العميل."},
            {"role": "user", "content": query}
        ],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"⚠️ المحرك يستعد.. يرجى الضغط مجدداً (كود {response.status_code})"
    except:
        return "⚠️ فشل في الاتصال الشعاعي.. تأكد من الإنترنت."

# --- 4. واجهة المستخدم النهائية ---

# الشعار
st.markdown(f'<div style="text-align:center; margin-bottom:10px;"><img src="{LOGO_URL}" style="width:230px; filter:drop-shadow(0 0 20px #00f2ff);"></div>', unsafe_allow_html=True)

# اسم المنتج
st.markdown('<h1 class="hero-title">EcomMind AI</h1>', unsafe_allow_html=True)

# الوحدة الرئيسية
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.markdown("<div class='glass-container'>", unsafe_allow_html=True)
    p_name = st.text_input("", placeholder="أدخل اسم المنتج لبدء السحر الرقمي...")
    if st.button("إطلاق المعالجة الشعاعية ⚡"):
        if p_name:
            with st.spinner('SYSTEM ANALYZING...'):
                res = call_ai_engine(p_name)
                st.markdown(f"<div class='res-box'>{res}</div>", unsafe_allow_html=True)
        else:
            st.warning("يرجى كتابة اسم المنتج")
    st.markdown("</div>", unsafe_allow_html=True)

# نافذة الاشتراك النخبوية
st.markdown("<br><br>", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class='glass-container' style='text-align:center;'>
            <h2 style='color:#fff; text-shadow: 0 0 10px #00f2ff;'>EXECUTIVE PRO MEMBERSHIP</h2>
            <p style='font-size:3.5rem; font-weight:900; color:#00f2ff; margin:0;'>49$</p>
            <p style='color:#888;'>أولوية المعالجة ودعم فني VIP 24/7</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=PRO" class="checkout-btn">تفعيل العضوية الآن 💎</a>
            <p style='color:#222; font-size:0.5rem; margin-top:20px;'>SADAM AL-HAJ AI LABS v14.0</p>
        </div>
    """, unsafe_allow_html=True)
