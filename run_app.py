#!/usr/bin/env python3
"""
Simple script to run the AI Image Studio Streamlit app
"""
import subprocess
import sys
import os

def main():
    print("🎨 Starting AI Image Studio...")
    print()
    
    # Check if we're in the right directory
    if not os.path.exists("app.py"):
        print("❌ Error: app.py not found in current directory")
        print("Make sure you're running this script from the project directory")
        return
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit found")
    except ImportError:
        print("❌ Streamlit not found. Installing requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("🚀 Launching the application...")
    print("The app will open in your browser automatically")
    print("Remember to enter your Google GenAI API key in the sidebar!")
    print()
    
    # Run the streamlit app
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    main()
