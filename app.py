import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="債衝刺 Bond Dash", page_icon="🏃", layout="centered")

# 把 Streamlit 預設的邊框、選單藏起來，讓遊戲佔滿畫面
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 560px;}
      iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

# 讀取 Supabase 金鑰（放在 Streamlit Cloud 的 Secrets 裡）
config = {
    "url": st.secrets.get("SUPABASE_URL", ""),
    "key": st.secrets.get("SUPABASE_ANON_KEY", ""),
    # 網址帶 ?room=ABCD 時，自動幫忙填好房號
    "room": st.query_params.get("room", ""),
}

html = Path(__file__).with_name("game.html").read_text(encoding="utf-8")
html = html.replace(
    "<head>",
    "<head><script>window.BOND_DASH_CONFIG = " + json.dumps(config) + ";</script>",
    1,
)

components.html(html, height=740, scrolling=False)
