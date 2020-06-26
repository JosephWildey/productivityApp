import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# model for treeview, stores event information
events = Gtk.ListStore(str, str, str, str)

# exit application
class ScheduleApplication:
    def onDestroy(self, *args):
        Gtk.main_quit()

# retrieve app window
builder = Gtk.Builder()
builder.add_from_file("windowMain.glade")

# retrieve the window objects
window = builder.get_object("wdwMain")
addEntryWindow = builder.get_object("wdwAdd")

def on_AddButton_clicked(self):
    "This function displays the popup for adding entries"
    addEntryWindow.show_all()

# retrive the addbutton and enable it to open the popup window
addButton = builder.get_object("btnAddPopup")
addButton.connect("clicked", on_AddButton_clicked)

# retrieve the TreeView Object
mainDisplay = builder.get_object("trvMain")

# connect treeview to liststore
mainDisplay.set_model(events)

window.show_all()

Gtk.main()
