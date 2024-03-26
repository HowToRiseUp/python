import os
import random
from datetime import datetime, timedelta

# Define the start date
start_date = datetime.now() - timedelta(days=200)

for i in range(200):
    # Generate a random date within the past 200 days
    rand = random.randint(1, 12)
    delta = timedelta(days=i)
    commit_date = start_date + delta

    # Format the date string
    commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    # Generate commit message with date
    commit_message = "Commit " + str(i+1)

    # Write to test.txt
    with open('test.txt', 'a') as file:
        file.write(commit_date_str + '\n')

    # Git commands
    os.system('git add test.txt')
    os.system(f'git commit --date="{commit_date_str}" -m "{commit_message}"')

# Push changes to origin
os.system('git push -u origin main')