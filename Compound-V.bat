powershell -Command "Start-Process 'python' -Verb runAs -ArgumentList 'main.py'"
@if NOT ["%errorlevel%"]==["0"] pause
