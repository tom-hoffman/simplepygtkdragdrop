# Simplest Python GTK Drag and Drop Example

# Tom Hoffman
# Computer Science Teacher
# Providence Career and Technical Academy

# In the course of figuring out how to implement drag and drop
# in a GTK+ application I'm working on, I found I needed an even
# simpler example than the ones I found on the web.

# The really hard part with this is the lack of error messages if
# you haven't wired up things properly.  One missing piece and
# nothing happens (silently).

# So I wrote this.  Bear in mind that I'm not an expert but I'm
# taking a little extra time to make this a straightforward
# and clean example.  

# Basically you have a Drag button and a Drop button.
# You drag the Drag button onto the Drop button and get some
# signals printing info to the console hopefully illuminating
# what is happening.  That's it.

# You may not need all these signals to
# get started in your app, I've included a few extras which may
# be helpful in getting started and debugging your code.

# This example will ONLY pass text; i.e., strings.  You can also
# pass URI's, Pixbufs or Gdk.Atom's but that's outside my needs
# or understanding at this point.  Limiting yourself to text
# simplifies the process a lot.

# You need this special import boilerplate for GTK 3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkX11

# Handler functions to be connected to signals

# Drag source signals
# To get deeper with signals see:
# https://developer.gnome.org/gtk3/stable/GtkWidget.html#GtkWidget-drag-drop

def drag_begin(widget: Gtk.Widget,
               context: GdkX11.X11DragContext):
    # Called when the user starts a drag.  Useful for debugging.
    print(f'Beginning drag from {widget}.')
    
def drag_data_get(sending_widget: Gtk.Widget,
                  context: GdkX11.X11DragContext,
                  data: Gtk.SelectionData,
                  info: int,
                  time: int):
    # Called when drag data is requested by the destination.
    # This is actually when the drop happens, not when the drag starts.
    # The data to be transfered needs to be set in the
    # Gtk.SelectionData object which starts as the data parameter.
    # We're using text (string) data.
    print(f"data into drag_data_get(): {data.get_text()}")
    # .set_text takes the string as its first parameter and
    # the length of the string as the second.  Or just use -1
    # and your computer will figure it out.
    data.set_text("Hello, world!", -1)
    print(f"data after drag_data_get(): {data.get_text()}")

def drag_motion(receiving_widget: Gtk.Widget,
                context: GdkX11.X11DragContext,
                x: int,
                y: int,
                time: int):
    # Called when you drag over a drop area.
    # Handy for debugging whether your drop area is configured correctly.
    print(f"Over the drop area at ({x}, {y}).")

def drag_data_received(receiving_widget: Gtk.Widget,
                       drag_context: GdkX11.X11DragContext,
                       x: int,
                       y: int,
                       data: Gtk.SelectionData,
                       info: int,
                       time: int):
    # This is the signal called if everything worked up to this point
    # and you're ready to read the data from your source,
    # which is in the data parameter as a Gtk.SelectionData object.
    print("Received data from drag: %s" % data.get_text())

# Setting up a simple window with two buttons.
win = Gtk.Window()
win.title = "Drop Test."
hbox = Gtk.Box(spacing=6)
win.add(hbox)

dragButton = Gtk.Button.new_with_label("Drag")
hbox.pack_start(dragButton, True, True, 0)
dropButton = Gtk.Button.new_with_label("Drop")
hbox.pack_start(dropButton, True, True, 0)

# Setting the buttons as drag and dest sources.
# The first parameter indicatyes you're dragging with the left mouse button.
# The second parameter is the target list.  Easiest to start with this empty.
# The third parameter is the action: COPY or MOVE being the main options here.
dragButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK,
                           [],
                           Gdk.DragAction.COPY)

# Dest is similar, but we can just try the default behavior for the drop action.
dropButton.drag_dest_set(Gtk.DestDefaults.ALL,
                         [],
                         Gdk.DragAction.COPY)

# Note that if you are dragging and dropping from a more complex widget
# based on a data model, such as a TreeView, you'll use a different method.

# ------------

# Targets are probably the most confusing part of all this.
# A "target" is really more of a data type than a location.
# This can also get into Gdk.Atoms quickly, which you might want to avoid
# if you aren't already using this concept in your application.

# You do have to specify targets for the source and destination, or nothing
# will happen.  For our purposes, we can just use these commands to indicate
# we're transferring textual data (strings).
# There are similar convenience functions for URI's and pixbuf images.

dragButton.drag_source_add_text_targets()
dropButton.drag_dest_add_text_targets()

# Connect our signal handling functions.

dragButton.connect("drag-begin", drag_begin)
dragButton.connect("drag-data-get", drag_data_get)

dropButton.connect("drag-data-received", drag_data_received)
dropButton.connect("drag-motion", drag_motion)

# Display the window and run the main loop.

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
