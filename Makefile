create_executable:
	@pyinstaller --onefile --icon=app/favicon.ico --windowed app.py

create_executable_debug:
	@pyinstaller --onefile --icon=app/favicon.ico --debug=all app.py