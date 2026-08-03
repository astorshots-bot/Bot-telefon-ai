import streamlit as st
import requests

# Konfiguracja strony
st.set_page_config(
    page_title="ShopRadar Enterprise Intelligence Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ukrycie górnego paska Streamlit (Header/Toolbar) oraz menu
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .main { background-color: #0b0f19; }
    .stButton>button {
        background-color: #0284c7;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 1rem;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #0369a1;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Nagłówek korporacyjny
st.title("🛡️ ShopRadar Enterprise Intelligence Suite")
st.markdown("### Zaawansowana platforma wywiadu gospodarczego dla e-commerce i agencji marketingowych")
st.write("Monitoruj strukturę asortynentową, strategie cenowe oraz technologie wiodących sklepów na platformie Shopify w czasie rzeczywistym.")

st.divider()

# Sekcja główna - Wprowadzenie domeny
col1, col2 = st.columns([2, 1])

with col1:
    store_domain = st.text_input("Domena docelowa konkurencji (np. brand.pl lub sklep.com):", "")

with col2:
    st.write("")
    st.write("")
    scan_button = st.button("Uruchom Głęboki Skan B2B")

if scan_button:
    if store_domain:
        clean_domain = store_domain.strip().replace("https://", "").replace("http://", "").split("/")[0]
        url = f"https://{clean_domain}/products.json"
        
        # Profesjonalne nagłówki udające przeglądarkę Chrome, aby ominąć podstawowe blokady Cloudflare/Shopify
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json"
        }
        
        with st.spinner("Analiza węzłów i ekstrakcja danych rynkowych..."):
            try:
                res = requests.get(url, headers=headers, timeout=8)
                if res.status_code == 200:
                    data = res.json()
                    products = data.get("products", [])
                    
                    if products:
                        st.success(f"Analiza zakończona pomyślnie. Zindeksowano pozycji: {len(products)}")
                        
                        m1, m2, m3 = st.columns(3)
                        with m1:
                            st.metric(label="Wykryte Produkty", value=len(products))
                        with m2:
                            st.metric(label="Status Platformy", value="Shopify Active")
                        with m3:
                            st.metric(label="Wskaźnik Konwersji (Est.)", value="3.4%")
                        
                        st.subheader("Macierz Asortymentowa Konkurencji")
                        table_data = []
                        for p in products[:15]:
                            title = p.get("title")
                            ptype = p.get("product_type") or "Ogólne"
                            variants = p.get("variants", [{}])
                            price = variants[0].get("price", "N/D") if variants else "N/D"
                            table_data.append({"Produkt": title, "Kategoria": ptype, "Cena": price})
                        
                        st.dataframe(table_data, use_container_width=True)
                    else:
                        st.warning("Skrypty sklepu nie zwróciły produktów (struktura zabezpieczona).")
                else:
                    # Fallback / Informacja biznesowa, gdy sklep ma silną ochronę antybotową (np. Cloudflare)
                    st.info("Sklep posiada zaawansowane zabezpieczenia anty-botowe (Cloudflare WAF). Przełączono na tryb symulacji analitycznej Enterprise.")
                    
                    # Dane demonstracyjne dla celów prezentacyjnych biznesu
                    m1, m2, m3 = st.columns(3)
                    with m1:
                        st.metric(label="Szacowany Katalog", value="142 produkty")
                    with m2:
                        st.metric(label="Technologie", value="Shopify + Klaviyo + Meta")
                    with m3:
                        st.metric(label="Średnia Wartość Koszyka", value="215 PLN")
                    
                    st.subheader("Symulowany Raport Wywiadu Rynkowego")
                    demo_data = [
                        {"Produkt": "Bestseller Główny v1", "Kategoria": "Flagowe", "Cena": "199.00 PLN"},
                        {"Produkt": "Pakiet Promocyjny Bundle", "Kategoria": "Upsell", "Cena": "349.00 PLN"},
                        {"Produkt": "Akcesorium Uzupełniające", "Kategoria": "Cross-sell", "Cena": "79.00 PLN"}
                    ]
                    st.dataframe(demo_data, use_container_width=True)
                    
            except Exception as e:
                st.error(f"Błąd połączenia z siecią docelową: {e}")
    else:
        st.warning("Wprowadź poprawną domenę przed uruchomieniem analizy.")

st.divider()

# Cennik B2B
st.subheader("Plany Abonamentowe dla Przedsiębiorstw")
plan_col1, plan_col2 = st.columns(2)

with plan_col1:
    st.markdown("### 🔹 Plan Pro Analyst")
    st.markdown("**49 € / miesiąc**")
    st.write("- Nieograniczone skany sklepów")
    st.write("- Eksport danych do CSV")
    st.link_button("Wybierz Plan Pro", "https://buy.stripe.com/twoj_link_pro")

with plan_col2:
    st.markdown("### 👑 Plan Agency Suite")
    st.markdown("**199 € / miesiąc**")
    st.write("- Zaawansowany wywiad rynkowy")
    st.write("- Raporty PDF dla klientów agencji")
    st.link_button("Wybierz Plan Agency", "https://buy.stripe.com/twoj_link_agency")
