import os
import subprocess

# Config
repository_url = "https://github.com/0xCriptik/Notes.git"
folder_to_commit = "D:/PC/Files/Notes"
commit_message = "Auto Commit, By 0xCriptik"

# Change to folder to commit to
try:
    os.chdir(folder_to_commit)
    print(f'\nDirectory changed to {folder_to_commit}')
except Exception as e:  # Corrected the exception variable name
    print(f'Error has occurred: {e}')

# Add all files in the folder to the staging area
try:
    subprocess.call(["git", "add", "."])
    print(f'\nFiles all added to staging area')
except Exception as e:  # Corrected the exception variable name
    print(f'Error has occurred: {e}')

# Commit folder with the message
try:
    subprocess.call(["git", "commit", "-m", commit_message])
    print(f'\nFolder committed with message: {commit_message}')
except Exception as e:  # Corrected the exception variable name
    print(f'Error has occurred: {e}')

# Push the project
try:
    subprocess.call(["git", "push", "origin", "master"])  # Corrected the push command
    print(f'\nPushed to project to repo: {repository_url}')
except Exception as e:  # Corrected the exception variable name
    print(f'Error has occurred: {e}')
