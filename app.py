import streamlit as st
import pandas as pd
from datetime import datetime

# --- 網頁設定 ---
st.set_page_config(page_title="綠色通勤認證平台", page_icon="🌿", layout="centered")

# --- 主程式區塊 ---
def main():
    # 側邊欄設計
    st.sidebar.title("🌿 綠色通勤認證")
    st.sidebar.info("歡迎企業提交綠色通勤計畫申請，共同為ESG盡一份心力。")
    st.sidebar.markdown("---")
    st.sidebar.write("系統版本: v1.0 (Demo)")

    # 主標題
    st.title("企業綠色通勤認證申請系統")
    st.markdown("請填寫以下表格並上傳相關佐證文件。")
    st.markdown("---")

    # 建立表單
    with st.form("application_form"):
        st.subheader("1. 企業基本資料")
        col1, col2 = st.columns(2)
        company_name = col1.text_input("企業名稱 (Company Name)")
        tax_id = col2.text_input("統一編號 (Tax ID)")
        contact_person = col1.text_input("聯絡人姓名")
        email = col2.text_input("聯絡人 Email")

        st.subheader("2. 綠色通勤措施")
        st.info("請勾選貴公司目前已實施的項目：")
        commute_type = st.multiselect(
            "措施項目 (可複選)：",
            ["鼓勵搭乘大眾運輸 (補貼/獎勵)", "提供單車停放區/淋浴間", "實施遠距辦公 (WFH)", "共乘制度 (Carpooling)", "提供電動車充電樁", "其他創新作法"]
        )
        
        description = st.text_area("執行成效簡述 (例如：減少了多少碳排放、參與人數等)")

        st.subheader("3. 佐證文件上傳")
        uploaded_file = st.file_uploader("請上傳相關辦法或照片 (PDF, JPG, PNG)", type=['pdf', 'jpg', 'png'])

        # 提交按鈕
        submitted = st.form_submit_button("提交申請資料")

        if submitted:
            # 檢查必填欄位
            if not company_name or not email or not uploaded_file:
                st.error("❌ 申請失敗：請確認「企業名稱」、「Email」與「佐證文件」皆已填寫與上傳。")
            else:
                # 這裡處理提交成功後的動作
                process_submission(company_name, email, uploaded_file)

def process_submission(company, email, file):
    # 顯示成功訊息
    st.success(f"✅ 提交成功！感謝 {company} 的申請。")
    st.balloons() # 放一點慶祝氣球動畫
    
    # 顯示收到的資料預覽 (讓用戶安心)
    with st.expander("查看已提交的資料詳情"):
        st.write(f"**申請時間:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        st.write(f"**聯絡信箱:** {email}")
        st.write(f"**上傳檔案名稱:** {file.name} (大小: {file.size / 1024:.2f} KB)")
        st.warning("注意：此為演示版，若伺服器重啟，暫存檔案將會清除。")

if __name__ == "__main__":
    main()
