import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide", initial_sidebar_state="collapsed")

# --- الهندسة البصرية المتقدمة (استهداف حسابك الجديد) ---
# ملاحظة: تأكد من تسمية الخلفية background.png واللوجو logo.png في GitHub
user_repo = "solofinjthefinj-max/Python" # مسار حسابك الجديد

st.markdown(f"""
    <style>
    header, footer, #MainMenu {{visibility: hidden;}}

    /* تحميل صورتك الفضائية كخلفية */
    [data-testid="stAppViewContainer"] {{
        background: #000000 !important;
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.6)), 
                          url("https://raw.githubusercontent.com/{user_repo}/main/background.png") !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* زجاج شفاف للنوافذ */
    .glass-card {{
        background: rgba(0, 0, 0, 0.7) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        border-radius: 30px !important;
        padding: 40px !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.9) !important;
        margin-bottom: 25px;
    }}

    .neon-title {{
        color: #00f2ff !important;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 20px #00f2ff, 0 0 40px #0062ff !important;
        letter-spacing: 3px;
    }}

    /* خانة البحث البيضوية المتوهجة */
    div[data-baseweb="input"] {{
        background-color: rgba(0, 0, 0, 0.9) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 50px !important;
        box-shadow: 0 0 25px #00f2ff !important;
        height: 75px !important;
    }}
    input {{
        color: #00f2ff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }}

    /* الأزرار النيونية */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        height: 60px;
        box-shadow: 0 0 25px #00f2ff !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- المحرك البرمجي ---
def run_ai(query):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {{"Authorization": f"Bearer {{api_key}}"}}
    payload = {{
        "model": "llama-3.1-8b-instant",
        "messages": [{{ "role": "user", "content": f"اكتب وصف بيعي لمنتج: {{query}}" }}]
    }}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        return response.json()['choices'][0]['message']['content']
    except: return "⚠️ النظام متصل.. جاري المعالجة"

# --- الواجهة ---
st.markdown(f'<div style="text-align:center;"><img src="https://raw.githubusercontent.com/{user_repo}/main/logo.png" style="width:230px; filter:drop-shadow(0 0 20px #00f2ff);"></div>', unsafe_allow_html=True)
st.markdown('<h1 class="neon-title">EcomMind AI</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    p_name = st.text_input("", placeholder="ما هو منتجك القادم؟")
    if st.button("إطلاق الذكاء الشعاعي ✨"):
        if p_name:
            with st.spinner('ANALYZING...'):
                res = run_ai(p_name)
                st.markdown(f"<div style='color:#00f2ff; background:rgba(0,0,0,0.8); padding:25px; border:2px solid #00f2ff; border-radius:20px;'>{{res}}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# نافذة الاشتراك
st.markdown("<br>", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class='glass-card' style='text-align:center;'>
            <h1 style='color:#fff;'>EXECUTIVE PRO</h1>
            <p style='font-size:3.5rem; font-weight:900; color:#00f2ff;'>49$</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" style="background:#00f2ff; color:#000; padding:15px 40px; border-radius:50px; font-weight:bold; text-decoration:none; display:inline-block; box-shadow:0 0 20px #00f2ff;">تفعيل العضوية الآن 💎</a>
        </div>
    """, unsafe_allow_html=True)
