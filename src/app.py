import streamlit as st
from utils.api_client import N8nApiClient

# Initialize the API client
# You can change the base_url if needed, otherwise it uses the default
client = N8nApiClient()

st.set_page_config(page_title="N8n API Connector", layout="wide")

st.title("N8n API Connector Dashboard")

st.sidebar.header("Configuration")
endpoint = st.sidebar.text_input("Endpoint", value="validLink", help="The specific endpoint to call (e.g., validLink)")

st.subheader("Test API Endpoint")

# Input area for data to send
st.markdown(f"**Target URL:** `{client.base_url}/{endpoint}`")

with st.form("api_form"):
    # Example input field - you can add more based on your needs
    input_data = st.text_area("Input JSON Data (as string for demo)", value='{"test": "value"}', help="Enter data to send")
    
    submitted = st.form_submit_button("Send Request")

    if submitted:
        import json
        try:
            # Try to parse the input as JSON
            payload = json.loads(input_data)
            
            with st.spinner("Sending request to n8n..."):
                response = client.call_endpoint(endpoint, data=payload)
            
            if "error" in response:
                st.error(f"Error: {response['error']}")
            else:
                st.success("Request successful!")
                st.json(response)
                
        except json.JSONDecodeError:
            st.error("Invalid JSON format in input data.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

st.markdown("---")
st.info("Modify `src/utils/api_client.py` to add more specific methods or change the base URL.")
