pyinstaller --onefile --add-data "streamlit_test.py;." --collect-all streamlit --hidden-import=streamlit.web.cli --hidden-import=streamlit.runtime.scriptrunner.magic_funcs --hidden-import=streamlit.runtime.credentials --hidden-import=streamlit.runtime.legacy_caching --hidden-import=streamlit.runtime.media_file_manager run_app.py
