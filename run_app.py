import subprocess
import sys
import os

def run_streamlit():
    # Get the directory of the executable
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        script_dir = os.path.dirname(sys.executable)
    else:
        # Running as script
        script_dir = os.path.dirname(os.path.abspath(__file__))

    streamlit_script = os.path.join(script_dir, "streamlit_test.py")
    
    # Run Streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", streamlit_script])

if __name__ == "__main__":
    run_streamlit()
