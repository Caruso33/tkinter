create_executable:
	@pyinstaller --onefile --icon=app/favicon.ico --windowed main.py

create_executable_debug:
	@pyinstaller --onefile --icon=app/favicon.ico --debug=all main.py