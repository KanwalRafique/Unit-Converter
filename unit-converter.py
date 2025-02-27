import streamlit as st
from pint import UnitRegistry

def convert_units(value, from_unit, to_unit):
    ureg = UnitRegistry()
    try:
        result = ureg.Quantity(value, from_unit).to(to_unit)
        return f"{result:.4g} {to_unit}"
    except Exception as e:
        return f"Error: {e}"

def main():
    st.set_page_config(page_title="Google-like Unit Converter", page_icon="🔄")
    
    st.markdown("""
        <style>
            .stButton > button {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
            .stTextInput, .stNumberInput, .stSelectbox {
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🔄 Google-like Unit Converter")
    st.markdown("Convert units instantly with ease! 🌍📏⚖️🌡️")
    
    unit_categories = {
        "📏 Length": ["meter", "kilometer", "mile", "foot", "inch", "centimeter"],
        "⚖️ Weight": ["gram", "kilogram", "pound", "ounce"],
        "🌡️ Temperature": ["celsius", "fahrenheit", "kelvin"],
    }

    category = st.selectbox("📂 Select a category", list(unit_categories.keys()))
    from_unit = st.selectbox("🔄 Convert from", unit_categories[category])
    to_unit = st.selectbox("➡️ Convert to", unit_categories[category])
    value = st.number_input("✍️ Enter value", min_value=0.0, format="%.4f")
    
    if st.button("🚀 Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"✅ Result: {result}")

if __name__ == "__main__":
    main()
