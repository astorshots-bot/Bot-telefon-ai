import streamlit as st
import requests

st.set_page_config(page_title="Shopify Enterprise Spy", layout="wide")

st.title("🛡️ Enterprise E-commerce Intelligence Suite")
st.write("Profesjonalna platforma analityczna do zaawansowanego szpiegowania sklepów Shopify.")

store_domain = st.text_input("Wpisz domenę sklepu konkurencji (np. sklep.pl):", "")

if st.button("Uruchom Głęboki Skan"):
    if store_domain:
        clean_domain = store_domain.strip().replace("https://", "").replace("http://", "").split("/")[0]
        url = f"https://{clean_domain}/products.json"
        
        with st.spinner("Trwa zaawansowana analiza struktury i technologii..."):
            try:
                res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
                if res.status_code == 200:
                    products = res.json().get("products", [])
                    st.success(f"Sukces! Znaleziono {len(products)} produktów w bazie sklepu.")
                    
                    st.subheader("Analiza Top Produktów:")
                    for p in products[:10]:
                        title = p.get("title")
                        ptype = p.get("product_type", "Inne")
                        variants = p.get("variants", [{}])
                        price = variants[0].get("price", "Brak") if variants else "Brak"
                        st.markdown(f"- **{title}** | Typ: `{ptype}` | Cena: `{price}`")
                else:
                    st.error("Sklep nie udostępnia publicznych danych lub nie korzysta z platformy Shopify.")
            except Exception as e:
                st.error(f"Błąd krytyczny skanera: {e}")
    else:
        st.warning("Najpierw wpisz poprawny adres URL.")

st.divider()
st.subheader("Odblokuj pełny zestaw analityczny (Wersja PRO)")
st.write("Uzyskaj dostęp do wykrywania wtyczek, predykcji obrotów i automatycznych audytów AI.")
st.link_button("Kup subskrypcję PRO (29 € / miesiąc)", "https://buy.stripe.com/twoj_link_plnosci")
