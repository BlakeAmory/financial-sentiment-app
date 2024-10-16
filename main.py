import subprocess
import webbrowser
import time

def run_backend():
    return subprocess.Popen(["python", "backend/manage.py", "runserver"])

def run_frontend():
    return subprocess.Popen(["python", "frontend/app.py"])

if __name__ == "__main__":
    print("Starting the Financial Sentiment Analysis Chatbot...")
    
    backend_process = run_backend()
    print("Backend server started.")
    
    time.sleep(5)  # Wait for the backend to fully start
    
    frontend_process = run_frontend()
    print("Frontend server started.")
    
    # Open the Gradio interface in the default web browser
    webbrowser.open("http://localhost:7860")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Application stopped.")
