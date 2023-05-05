import streamlit as st
import re


def extract_mac_addresses(text):
    mac_regex = r"(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})"
    mac_addresses = re.findall(mac_regex, text)
    return mac_addresses


st.title("MAC Address Extractor")

uploaded_file = st.file_uploader("Upload a text file", type="txt")

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    text = text.readline()
    mac_addresses = extract_mac_addresses(text)

    if len(mac_addresses) == 0:
        st.warning("No MAC addresses found in file")
    else:
        st.success(f"Found {len(mac_addresses)} MAC addresses:")
        for mac_address in mac_addresses:
            st.write(mac_address)
