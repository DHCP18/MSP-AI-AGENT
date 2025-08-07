import streamlit as st
import pandas as pd
import io

# Title and instructions
st.title("AI Agent: Cloudtango MSP Enrichment")
st.markdown("""
Upload your MSP listings CSV file from Cloudtango.  
Click the button below to simulate enrichment using sample ZoomInfo data.  
Once enriched, you can download the updated CSV file.
""")

# File uploader
uploaded_file = st.file_uploader("Upload Cloudtango MSP CSV", type=["csv"])

# Placeholder for enriched data
enriched_df = None

# Simulate enrichment function
def simulate_enrichment(df):
    enriched = df.copy()
    enriched["Industry"] = "Managed Services"
    enriched["Company Size"] = "51-200"
    enriched["Revenue"] = "$5M-$10M"
    enriched["Contact Name"] = "John Doe"
    enriched["Contact Title"] = "IT Director"
    enriched["Contact Email"] = "johndoe@example.com"
    enriched["Tag"] = "AI AGENT MSP SEARCH CLOUD TANGO"
    return enriched

# Process uploaded file
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Preview of Uploaded MSP Listings:")
    st.dataframe(df)

    if st.button("Simulate ZoomInfo Enrichment"):
        enriched_df = simulate_enrichment(df)
        st.success("✅ Enrichment complete!")
        st.write("📄 Preview of Enriched Data:")
        st.dataframe(enriched_df)

        # Download enriched CSV
        csv_buffer = io.StringIO()
        enriched_df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="Download Enriched CSV",
            data=csv_buffer.getvalue(),
            file_name="zoominfo_enriched_msp_listings.csv",
            mime="text/csv"
        )
