# 🎨 AI Image Studio

A complete Streamlit application for AI-powered image generation, editing, and understanding using Google's Gemini 2.5 Flash model.

## Features

### 🖼️ Image Generation
- Generate images from text descriptions
- High-quality AI-generated artwork
- Download generated images as PNG files

### ✂️ Image Editing
- Upload existing images and modify them with AI
- Natural language editing instructions
- Before/after comparison view

### 🔎 Image Understanding
- Ask questions about uploaded images
- Get detailed descriptions and analysis
- Perfect for accessibility and content understanding

## Setup and Installation

### Option 1: Quick Setup (Recommended)
1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/ai-image-studio.git
   cd ai-image-studio
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   - Copy `.env.example` to `.env`
   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Edit `.env` and replace `your_google_genai_api_key_here` with your actual key

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```
   Or use the provided scripts:
   - Windows: Double-click `run_app.bat`
   - Any platform: `python run_app.py`

### Option 2: Manual API Key Entry
1. **Follow steps 1-2 above**
2. **Run the application without setting up .env**
3. **Enter your API key in the sidebar when the app opens**

## Usage

### Image Generation
1. Navigate to the "🖼️ Image Generation" tab
2. Enter a detailed description of the image you want to create
3. Click "✨ Generate Image"
4. Download the result when satisfied

### Image Editing
1. Navigate to the "✂️ Image Editing" tab
2. Upload an image (PNG/JPG)
3. Describe the changes you want to make
4. Click "🎨 Edit Image"
5. Compare the original and edited versions

### Image Understanding
1. Navigate to the "🔎 Image Understanding" tab
2. Upload an image for analysis
3. Ask a question about the image
4. Click "🔍 Get Answer"
5. Read the AI's response

## Privacy and Security

- Your API key is only stored for the current session
- Images are processed through Google's secure API
- No data is permanently stored by this application
- All processing happens in real-time

## Technical Details

- **Frontend:** Streamlit
- **AI Model:** Google Gemini 2.5 Flash with image preview
- **Image Processing:** PIL (Python Imaging Library)
- **API:** Google GenAI SDK

## Requirements

- Python 3.7+
- Google GenAI API key
- Internet connection for API calls

## Troubleshooting

**API Key Issues:**
- Ensure your API key is correct and active
- Check that you have remaining quota
- Verify your Google account has access to GenAI

**Image Upload Issues:**
- Supported formats: PNG, JPG, JPEG
- Try reducing image size if upload fails
- Ensure good internet connection

**Generation/Editing Issues:**
- Try more specific prompts
- Check if the model supports your request type
- Retry if temporary API issues occur

## License

This project is open source. Please respect Google's API terms of service when using the GenAI API.
