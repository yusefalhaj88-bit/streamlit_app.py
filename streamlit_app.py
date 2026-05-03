import streamlit as st
import requests

# --- إعدادات الصفحة الفنية ---
st.set_page_config(page_title="EcomMind AI Ultra Pro", layout="wide", initial_sidebar_state="collapsed")

# ملاحظة برمجية: الكود سيبحث عن الصور في المستودع الحالي
def get_image_url(filename):
    # سيتم جلب الرابط بناءً على بنية GitHub الخام
    return f"https://raw.githubusercontent.com/{st.context.repo_owner}/{st.context.repo_name}/main/{filename}"

# --- الهندسة البصرية (مطابقة للفيديو والصور تماماً) ---
st.markdown(f"""
    <style>
    /* 1. إخفاء القوائم الافتراضية */
    header, footer, #MainMenu {{visibility: hidden;}}

    /* 2. الخلفية الفضائية المشعة (صورتك الخاصة) */
    [data-testid="stAppViewContainer"] {{
        background: #000000 !important;
        background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.5)), 
                          url("{get_image_url('background.png')}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* 3. النوافذ الزجاجية الكريستالية الشفافة */
    .glass-card {{
        background: rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        border-radius: 30px !important;
        padding: 40px !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8) !important;
        margin-bottom: 25px;
    }}

    /* 4. اسم المنتج النيوني الشعاعي */
    .product-title {{
        color: #00f2ff !important;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 20px #00f2ff, 0 0 40px #0062ff !important;
        letter-spacing: 5px;
        margin-top: 10px;
    }}

    /* 5. خانة البحث البيضوية (سواد نيون مثل الفيديو) */
    div[data-baseweb="input"] {{
        background-color: rgba(0, 0, 0, 0.9) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 50px !important;
        box-shadow: 0 0 25px #00f2ff, inset 0 0 10px rgba(0,242,255,0.2) !important;
        height: 75px !important;
        padding: 0 25px !important;
    }}
    input {{
        color: #00f2ff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }}

    /* 6. الأزرار النيونية الحادة */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        height: 60px;
        border: none !important;
        box-shadow: 0 0 25px #00f2ff !important;
        font-size: 1.3rem;
        transition: 0.4s;
    }}
    .stButton>button:hover {{ transform: scale(1.02); box-shadow: 0 0 50px #00f2ff !important; }}
    </style>
""", unsafe_allow_html=True)

# --- محرك الذكاء الاصطناعي (Groq) ---
def call_groq_ai(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"أنت خبير تسويق عالمي. اكتب استراتيجية ووصف بيعي لمنتج: {product}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        return response.json()['choices'][0]['message']['content']
    except: return "⚠️ المحرك متصل.. جاري المعالجة الشعاعية."

# --- واجهة المستخدم ---

# عرض الشعار
st.markdown(f'<div style="text-align:center;"><img src="{get_image_url("logo.png")}" style="width:230px; filter:drop-shadow(0 0 20px #00f2ff);"></div>', unsafe_allow_html=True)

# اسم المنتج
st.markdown('<h1 class="product-title">EcomMind AI</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    query = st.text_input("", placeholder="ما هو المنتج الذي تريد تسويقه بذكاء؟")
    if st.button("إطلاق الذكاء الشعاعي ✨"):
        if query:
            with st.spinner('SYSTEM ANALYZING...'):
                res = call_groq_ai(query)
                st.markdown(f"<div style='color:#00f2ff; background:rgba(0,0,0,0.85); padding:25px; border:1px solid #00f2ff; border-radius:20px; box-shadow:0 0 20px #00f2ff; direction:rtl;'>{res}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# نافذة الاشتراك
st.markdown("<br><br>", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class='glass-card' style='text-align:center;'>
            <h1 style='color:#fff; text-shadow: 0 0 10px #00f2ff;'>EXECUTIVE PRO</h1>
            <p style='font-size:3.5rem; font-weight:900; color:#00f2ff; margin:0;'>49$</p>
            <p style='color:#888; margin-bottom: 25px;'>Premium AI Engine & VIP Support</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" style="background:#00f2ff; color:#000; padding:15px 50px; border-radius:50px; font-weight:bold; text-decoration:none; display:inline-block; box-shadow:0 0 20px #00f2ff;">تفعيل العضوية الآن 💎</a>
        </div>
    """, unsafe_allow_html=True)
