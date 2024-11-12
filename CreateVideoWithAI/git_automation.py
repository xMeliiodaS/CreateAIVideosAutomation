import os
import subprocess
import logging


PROMPTS_DIR = 'src/prompts/automation_prompts'  # Update this path if needed


def pull_prompts_repo():
    try:
        # Navigate to the prompts directory
        os.chdir(PROMPTS_DIR)

        # Pull the latest changes
        logging.info("Pulling latest updates from the remote repository...")
        result = subprocess.run(['git', 'pull'], capture_output=True, text=True)

        if 'Already up to date' in result.stdout:
            logging.info("Prompts are already up to date.")
        else:
            logging.info("Prompts repository updated successfully.")

    except Exception as e:
        logging.error(f"Failed to pull updates: {e}")
    finally:
        # Navigate back to the original directory
        os.chdir('')
