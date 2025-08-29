import streamlit as st
from PIL import Image
from io import BytesIO
import core

st.set_page_config(page_title="🎨 AI Image Studio", layout="wide")

# ------------------- Custom CSS -------------------
st.markdown("""
    <style>
        /* Dark theme with black background for image work */
        .stApp {
            background-color: #000000;
            color: #ffffff;
        }
        
        /* Main container */
        .main .block-container {
            background-color: #000000;
            color: #ffffff;
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #1a1a1a;
        }
        
        .stTabs [data-baseweb="tab-list"] button {
            background-color: #1a1a1a;
            color: #ffffff !important;
        }
        
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
            background-color: #333333;
            color: #ffffff !important;
        }
        
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.2rem;
            font-weight: bold;
            color: #ffffff !important;
        }
        
        /* Main header styling */
        .main-header {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            color: #4CAF50 !important;
            margin-bottom: 20px;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: #4CAF50 !important;
            color: #ffffff !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #45a049 !important;
            transform: scale(1.02);
            transition: all 0.2s ease-in-out;
        }
        
        /* Text areas and inputs */
        .stTextArea textarea {
            background-color: #1a1a1a !important;
            color: #ffffff !important;
            border: 2px solid #333333 !important;
        }
        
        .stTextInput input {
            background-color: #1a1a1a !important;
            color: #ffffff !important;
            border: 2px solid #333333 !important;
        }
        
        /* Text elements */
        p, div, span, label {
            color: #ffffff !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }
        
        /* Subheader styling */
        .stMarkdown h3 {
            color: #4CAF50 !important;
            font-weight: bold;
        }
        
        /* Info boxes with dark theme */
        .stInfo {
            background-color: #1a3a5c !important;
            color: #87ceeb !important;
            border: 1px solid #4a90e2 !important;
        }
        
        .stWarning {
            background-color: #5c4a1a !important;
            color: #ffd700 !important;
            border: 1px solid #ffb347 !important;
        }
        
        .stSuccess {
            background-color: #1a5c1a !important;
            color: #90ee90 !important;
            border: 1px solid #4CAF50 !important;
        }
        
        .stError {
            background-color: #5c1a1a !important;
            color: #ff6b6b !important;
            border: 1px solid #e74c3c !important;
        }
        
        /* File uploader */
        .stFileUploader {
            background-color: #1a1a1a !important;
            border: 2px solid #333333 !important;
            border-radius: 8px;
            padding: 1rem;
        }
        
        .stFileUploader label {
            color: #ffffff !important;
            font-weight: bold;
        }
        
        /* Sidebar dark theme */
        section[data-testid="stSidebar"] {
            background-color: #1a1a1a !important;
        }
        
        section[data-testid="stSidebar"] .element-container {
            color: #ffffff !important;
        }
        
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3 {
            color: #ffffff !important;
        }
        
        section[data-testid="stSidebar"] p, 
        section[data-testid="stSidebar"] li {
            color: #ffffff !important;
        }
        
        /* API key input in sidebar */
        section[data-testid="stSidebar"] .stTextInput input {
            background-color: #333333 !important;
            color: #ffffff !important;
            border: 2px solid #666666 !important;
        }
        
        /* API key info box */
        .api-key-info {
            background-color: #1a3a1a !important;
            color: #ffffff !important;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #4CAF50;
            margin: 1rem 0;
        }
        
        .api-key-info h3 {
            color: #4CAF50 !important;
        }
        
        .api-key-info p, .api-key-info li {
            color: #ffffff !important;
        }
        
        .api-key-info a {
            color: #87ceeb !important;
        }
        
        /* Download button styling */
        .stDownloadButton button {
            background-color: #2196F3 !important;
            color: #ffffff !important;
        }
        
        /* Image captions */
        .caption {
            color: #cccccc !important;
            font-style: italic;
        }
        
        /* Markdown styling */
        .stMarkdown {
            color: #ffffff !important;
        }
        
        /* Response box styling */
        .response-box {
            background-color: #1a1a1a !important;
            color: #ffffff !important;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #4CAF50;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🎨 AI Image Studio</h1>", unsafe_allow_html=True)

# ------------------- API Key Configuration -------------------
st.sidebar.header("🔑 Configuration")

# Get default API key from environment
default_api_key = core.get_default_api_key()

api_key = st.sidebar.text_input(
    "Enter your Google GenAI API Key:",
    value=default_api_key,
    type="password",
    help="Get your API key from Google AI Studio: https://aistudio.google.com/app/apikey"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📱 About This App")
st.sidebar.markdown("""
**This AI Image Studio provides three main features:**

- **🖼️ Image Generation**: Create images from text descriptions
- **✂️ Image Editing**: Modify existing images with AI  
- **🔎 Image Understanding**: Ask questions about images

**Powered by Google's Gemini 2.5 Flash**
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔒 Privacy & Security")
st.sidebar.markdown("""
- Your API key is stored only for this session
- Images are processed through Google's API
- No data is permanently stored by this app
""")

if not api_key:
    st.warning("⚠️ Please enter your Google GenAI API key in the sidebar to use the application.")
    st.markdown("""
    <div class="api-key-info">
    <h3>🔑 How to get your API key:</h3>
    <ol style="color: #ffffff;">
    <li>Go to <a href="https://aistudio.google.com/app/apikey" target="_blank" style="color: #87ceeb;">Google AI Studio</a></li>
    <li>Sign in with your Google account</li>
    <li>Click "Create API Key"</li>
    <li>Copy the key and paste it in the sidebar</li>
    </ol>
    <p style="color: #ffffff;"><strong>Note:</strong> The API key is free to get and includes generous usage limits.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Add a success indicator when API key is provided
st.sidebar.success("✅ API Key configured successfully!")

# ------------------- Tabs -------------------
tab1, tab2, tab3 = st.tabs(["🖼️ Image Generation", "✂️ Image Editing", "🔎 Image Understanding"])

# ------------------- TAB 1: IMAGE GENERATION -------------------
with tab1:
    st.subheader("Generate a new AI image from text")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 📝 Enter your prompt below")
        prompt = st.text_area(
            "Describe the image you want to create:",
            "A 3D rendered pig with wings and a top hat flying over a futuristic city.",
            height=150,
            help="Be descriptive! Mention style, setting, and subject for better results."
        )
        st.markdown("**Tip:** Be descriptive! Mention style, setting, and subject for better results.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✨ Generate Image"):
            with st.spinner("Generating image..."):
                result = core.generate_image(prompt, api_key)
                if result["status"] == "success":
                    st.success("Image generated successfully!")
                    st.session_state.gen_result = result
                else:
                    st.error(result["message"])
                    st.session_state.gen_result = None

    with col2:
        if "gen_result" in st.session_state and st.session_state.gen_result is not None:
            st.image(st.session_state.gen_result["image"], caption="Generated Image", width='stretch')

            d_col1, d_col2, d_col3 = st.columns([1, 1, 1])
            with d_col2:
                img_bytes = BytesIO()
                st.session_state.gen_result["image"].save(img_bytes, format="PNG")
                st.download_button(
                    label="⬇️ Download Image",
                    data=img_bytes.getvalue(),
                    file_name="gemini_generated.png",
                    mime="image/png"
                )
            if st.session_state.gen_result["text"]:
                st.markdown("---")
                st.markdown("### 📝 Model Notes:")
                st.markdown(f"_{st.session_state.gen_result['text']}_")

# ------------------- TAB 2: IMAGE EDITING -------------------
with tab2:
    st.subheader("Edit an existing image with AI")
    col1, col2 = st.columns([1, 2])

    with col1:
        uploaded_file = st.file_uploader("📁 Upload an image (PNG/JPG)", type=["png", "jpg", "jpeg"])

        st.markdown("### ✏️ Enter your edit instruction")
        edit_prompt = st.text_area(
            "Describe the change you want to make:",
            "Add a llama next to me",
            height=100,
            help="The model works best with clear, specific instructions."
        )
        st.markdown("**Tip:** The model works best with clear, specific instructions.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🎨 Edit Image"):
            if uploaded_file is None:
                st.warning("Please upload an image before editing.")
            else:
                input_image = Image.open(uploaded_file)
                with st.spinner("Editing image..."):
                    result = core.edit_image(edit_prompt, input_image, api_key)
                    if result["status"] == "success":
                        st.success("Image edited successfully!")
                        st.session_state.edit_result = result
                    else:
                        st.error(result["message"])
                        st.session_state.edit_result = None

    with col2:
        if uploaded_file is not None:
            input_image = Image.open(uploaded_file)
            st.image(input_image, caption="Uploaded Image", width='stretch')

        st.markdown("---")

        if "edit_result" in st.session_state and st.session_state.edit_result is not None:
            st.image(st.session_state.edit_result["image"], caption="Edited Image", width='stretch')
            d_col1, d_col2, d_col3 = st.columns([1, 1, 1])
            with d_col2:
                img_bytes = BytesIO()
                st.session_state.edit_result["image"].save(img_bytes, format="PNG")
                st.download_button(
                    label="⬇️ Download Edited Image",
                    data=img_bytes.getvalue(),
                    file_name="gemini_edited.png",
                    mime="image/png"
                )
            if st.session_state.edit_result["text"]:
                st.markdown("---")
                st.markdown("### 📝 Model Notes:")
                st.markdown(f"_{st.session_state.edit_result['text']}_")

# ------------------- TAB 3: IMAGE Q&A -------------------
with tab3:
    st.subheader("Ask questions about an image")
    col1, col2 = st.columns([1, 2])

    with col1:
        qna_file = st.file_uploader("📁 Upload an image for Q&A (PNG/JPG)", type=["png", "jpg", "jpeg"], key="qna_uploader")
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### 🤔 Enter your question")
        query = st.text_input("What would you like to know about this image?", "Caption this image.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 Get Answer"):
            if qna_file and query:
                with st.spinner("Analyzing image..."):
                    image_bytes = qna_file.read()
                    result = core.understand_image(query, image_bytes, api_key)
                    if result["status"] == "success":
                        st.session_state.qna_result = result
                        st.success("Analysis complete!")
                    else:
                        st.error(result["message"])
                        st.session_state.qna_result = None
            else:
                st.warning("Please upload an image and enter a query.")

    with col2:
        if qna_file is not None:
            st.image(qna_file, caption="Uploaded Image", width='stretch')

        st.markdown("---")

        if "qna_result" in st.session_state and st.session_state.qna_result is not None:
            st.markdown("### 💬 AI Response:")
            st.markdown(f"""
            <div class="response-box">
                {st.session_state.qna_result["text"]}
            </div>
            """, unsafe_allow_html=True)