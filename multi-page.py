import streamlit as st
import pandas as pd

def load_data():
    manufacturers = pd.DataFrame({
        'Name': ['Gar Labs', 'Lily\'s', 'Beauty Private Label', 'Federal Packaging', 'Twincraft', 
                 'Coughlin Companies', 'Sinoscan', 'KKT', 'Goodkind Co'],
        'MOQ': [5000, 10000, 3000, 5000, 15000, 5000, 10000, 5000, 10000],
        'Time': [14, 16, 12, 15, 20, 14, 16, 15, 17], # dummy data for illustration
        'Price_per_unit': [2.00, 5.50, 4.50, 5.00, 2.50, 4.50, 3.50, 5.00, 3.00],
        'Email': ['tom@garlabs.com', 'hello@moesgroup.org', 'Sales@bqgmanufacturing.com', 'info@federalpackage.com', 
                  'jackson.berman@twincraft.com', 'info@contactcoghlin.com', 'info@sinoscan.com', 'krupa@kktconsultants.com', 
                  'info@nutracapusa.com']
    })
    return manufacturers

def home_page():
    st.title('Welcome to CPG Brand - Manufacturer Matching App')
    st.write('This app helps CPG brands find the perfect contract manufacturer.')
    if st.button('Next'):
        st.session_state.page += 1

def input_company_info():
    st.title('Enter Your Company Information')
    # Note: In a real-world scenario, you should consider storing these inputs somewhere to use later.
    # For simplicity, we're just using text inputs here and not doing anything with them.
    company_name = st.text_input('Company Name')
    product_type = st.text_input('Product Type')
    segment = st.text_input('Segment')
    annual_units = st.number_input('Annual Units')
    website_url = st.text_input('Website URL')
    revenue_last_year = st.number_input('Revenue in the last 12 months ($)')
    price_per_unit = st.number_input('Price Per Unit ($)')
    projected_revenue = st.number_input('Projected Revenue for the next 12 months ($)')
    ideal_monthly_units = st.number_input('Ideal Monthly Units')
    differentiation = st.text_input('Company Differentiation')
    monthly_revenue = st.number_input('Average Monthly Revenue ($)')
    monthly_expense = st.number_input('Average Monthly Expense ($)')
    if st.button('Next'):
        st.session_state.page += 1

def choose_criteria():
    st.title('Choose Your Main Criteria for Manufacturer Selection')
    criteria = st.selectbox('Choose your main criteria', ['MOQ', 'Time', 'Price_per_unit'])
    # Store the selected criteria in Streamlit's session state so it can be accessed later
    st.session_state.criteria = criteria
    if st.button('Next'):
        st.session_state.page += 1


def best_match():
    st.title('Your Best Manufacturer Matches')
    manufacturers = load_data()
    criteria = st.session_state.criteria  # Get the selected criteria from the session state
    best_manufacturer = manufacturers.loc[manufacturers[criteria].idxmin()]
    st.subheader(f'1. {best_manufacturer["Name"]}')
    st.write(f"The best manufacturer based on {criteria} criteria. It has {best_manufacturer[criteria]} {criteria}. You can contact them at {best_manufacturer['Email']}.")
    if st.button('Next'):
        st.session_state.page += 1

def manufacturers_list():
    st.title('Manufacturers List')
    manufacturers = load_data()
    st.write(manufacturers)
    if st.button('Back to Home'):
        st.session_state.page = 0

PAGES = [home_page, input_company_info, choose_criteria, best_match, manufacturers_list]

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 0
    PAGES[st.session_state.page]()

if __name__ == "__main__":
    main()
