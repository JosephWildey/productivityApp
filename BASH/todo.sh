# !#/bin/bash

# Let the user know what's going on and create some blank space
echo "Retrieving todo list..."
echo

# Read the latest iteration of the file in terminal 
cat ~/schedule.txt

# Ask the user if they want to change the file, and create some blank space for formatting purposes
echo
echo "Do you need to access the file?"
echo

# Store their answer as a variable
read answer

# Start the if block and check the user's answer
if [ $answer == "y" ] || [ $answer == "Y" ]
then
    echo "Backing up and then opening the scheduling file..."
    echo
    
    # back up the original version of the file before opening it in an editor
    cp ~/schedule.txt ~/schedule.bak
    emacs ~/schedule.txt
else
    # They don't need access so there's nothing to do, just terminate
    echo "Have a great day..."
    
# terminates the if block in BASH
fi

# terminates the program
exit 0
