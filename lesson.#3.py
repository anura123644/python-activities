def shutdown():
    import os
    if os.name == 'nt':  # Check if the operating system is Windows
        os.system('shutdown /s /t 1')  # Shutdown command for Windows
    else:
        os.system('sudo shutdown -h now') 

# Call the shutdown function
shutdown()
