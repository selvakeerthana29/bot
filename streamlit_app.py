import os
import streamlit as st


st.title('Aruba Company FAQ')


aruba_faq = {
    "What is Aruba?": "Aruba is a leading global provider of enterprise network solutions, specializing in cloud-managed networking and security solutions.",
    "Where is Aruba located?": "Aruba is headquartered in Chennai, India.",
    "What products does Aruba offer?": "Aruba offers networking hardware, including Wi-Fi access points, routers, switches, and network security solutions.",
    "What services does Aruba provide?": "Aruba provides cloud-managed networking solutions, enterprise-level IT infrastructure, and cybersecurity services.",
    "What is Aruba's mission?": "Aruba's mission is to help businesses improve their digital transformation and network efficiency through innovative, secure, and scalable IT solutions.",
    "How can I contact Aruba customer support?": "You can contact Aruba support through their official website or by calling their support hotline. You can also reach them via email for product inquiries.",
    "What is the warranty on Aruba products?": "Aruba offers a standard 1-year warranty on most of its products, with extended warranty options available."
}

input_question = st.text_input("Ask a question about Aruba:")

if input_question:

    answer = aruba_faq.get(input_question, "Sorry, I don't have an answer to that question. Please check Aruba's official website or contact support.")
    
    
    st.write(f"Answer: {answer}")
