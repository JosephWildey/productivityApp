# productivityApp
An app I'm building to boost productivity, improve my understandings of GUIs, and Python/GTK. It initially started out as a
BAsH script and is evolving into something a bit more feature rich. It will likely evolve further over the years as pretty much the only app I intend to focus on while finishing my bachelor's at GVSU in Applied Data Analytics.

# todo.sh
This is the initial BASH script I wrote for this program. It accesses a file, outputs its contents, and asks if you need to update the file. Upon confirmation it opens up emacs, though you can open it in any editor you choose. Once you are done close the editor and the script terminates.

# Installing todo.sh
If you wish to install todo.sh, here are the steps.
1) Copy the code from the todo.sh page.
2) Open your favorite editor - nano is fine - and paste. Save file with a ".sh" extension.
3) Use chmod +x script.sh to make it executable

You should be all set and able to execute the script provided terminal is in the same directory as the script. Unless I'm forgetting something, which is possible.

# schedule.py (WIP)
The planned GUI version of the current file and script form of this idea. It will feature a list widget and buttons. Eventually it will allow updates in the widget, read from a file, and write to the file. All from a pretty GUI instead of editors and terminal. It will also work on any platform provided GTK is installed.
