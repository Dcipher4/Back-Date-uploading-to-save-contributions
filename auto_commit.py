import os
import datetime
import time
import schedule

REPO_PATH = r"C:\Users\Admin\OneDrive\Desktop\python programs\Learning Curve\Back-Date-uploading-to-save-contributions"
COMMIT_MESSAGE = "Daily automated commit"

def git_commit_push():
    try:
        os.chdir(REPO_PATH)
        
        # Create/update commit log
        with open("commit_log.txt", "a") as f:
            f.write(f"Commit at: {datetime.datetime.now()}\n")
        
        # Git operations
        os.system('git add .')
        os.system(f'git commit -m "{COMMIT_MESSAGE}"')
        os.system('git push origin main')
        
        print(f"Successfully committed at {datetime.datetime.now()}")
    except Exception as e:
        print(f"Error: {str(e)}")
        with open("error_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {str(e)}\n")

if __name__ == "__main__":
    # Initial commit on startup
    git_commit_push()
    
    # Schedule daily commits
    schedule.every().day.at("23:55").do(git_commit_push)
    
    print("Auto-commit system active. Monitoring for changes...")
    while True:
        schedule.run_pending()
        time.sleep(60)
