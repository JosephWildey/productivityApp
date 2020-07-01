import gi
import csv

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ScheduleApplication:
# exit application
    def onDestroy(self, *args):
        Gtk.main_quit()

# create the liststore
events = Gtk.ListStore(str, str, str, str)

# create a list to move to liststore
eventsData = []

# fill eventsData before it is attached to the treeview
with open('schedule.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        eventsData.append(row)

# move contents in eventsData to events liststore
for i in range(len(eventsData)):
    events.append(eventsData[i])

# retrieve app window
builder = Gtk.Builder()
builder.add_from_file("windowMain.glade")

# retrieve the window object
window = builder.get_object("wdwMain")
addEntryWindow = builder.get_object("wdwAdd")

#retrive the buttons
addButton = builder.get_object("btnAddPopup")
addCloseWindow = builder.get_object("btnAddWindowClose")

def on_AddButton_clicked(self):
    "This will display the popup when the add button is clicked"
    addEntryWindow.show_all()

def on_CloseButton_clicked(self):
    "This will close the add entry popup when clicked"
    addEntryWindow.destroy()

# connect the buttons to actions
addButton.connect("clicked", on_AddButton_clicked)
addCloseWindow.connect("clicked", on_CloseButton_clicked)

# retrieve the TreeView Object
mainDisplay = builder.get_object("trvMain")

# create columns for the treeiew and attach them to renderers
for i, column_title in enumerate(["Date", "Time", "Type", "Details"]):
    renderer = Gtk.CellRendererText()
    column = Gtk.TreeViewColumn(column_title, renderer, text=i)
    mainDisplay.append_column(column)

# connect treeview to liststore
mainDisplay.set_model(events)

window.show_all()

Gtk.main()
