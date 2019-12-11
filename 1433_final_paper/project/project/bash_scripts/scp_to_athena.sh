# Simple bash script for pushing codebase to athena server


# First, change directory to one level above project directory, if not there already
cd ~/Documents/

# Now push all the data in this directory to athena
scp -r 1433_final_paper/project/ rmsander@athena.dialup.mit.edu:~/Documents/14.33/
