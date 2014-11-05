#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import webbrowser

class NetbookSupport:
    # Create a Button Box with the specified parameters
    def create_bbox(self,horizontal,title, spacing, layout):
        frame = gtk.Frame(title)
       
        bbox = gtk.HButtonBox()

        bbox.set_border_width(3)
        frame.add(bbox)

        # Set the appearance of the Button Box
        bbox.set_layout(layout)
        bbox.set_spacing(spacing)

        #button = gtk.Button(stock=gtk.STOCK_OK)
       
        image = gtk.Image()
        image.set_from_file("abt_logo.png")
        image.show()
        # a button to contain the image widget
        button = gtk.Button()
        button.add(image)
        bbox.add(button)
        if (horizontal == "1"):
		button.connect("clicked", self.button_clicked, "1")
		
	elif(horizontal == "2"):
		button.connect("clicked", self.button_clicked, "2")
	else:
		
        	button.connect("clicked", self.button_clicked, "3")
        
        # button.show()
	
        return frame
        
    def button_clicked(self, widget, data=None):
      
	if (data == "1"):

		url = 'http://netbook-support.fossee.in/apps'
		webbrowser.open(url)
		
	elif(data == "2"):
		url = 'http://netbook-support.fossee.in/index/'
		webbrowser.open(url)
	else:
		url = 'http://netbook-support.fossee.in'
		webbrowser.open(url)

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Welcome to Netbook Suppport")

        window.connect("destroy", lambda x: gtk.main_quit())

        window.set_border_width(10)

        main_vbox = gtk.VBox(False, 0)
        window.add(main_vbox)

      
	
        frame_vert = gtk.Frame("Netbook Support")
        main_vbox.pack_start(frame_vert, True, True, 0)

        hbox = gtk.HBox(False, 0)
        hbox.set_border_width(13)
        frame_vert.add(hbox)

        hbox.pack_start(self.create_bbox("1","More apps",
                                         5, gtk.BUTTONBOX_SPREAD),
                        True, True, 10)

        hbox.pack_start(self.create_bbox("2","Ask a Question",
                                         5, gtk.BUTTONBOX_SPREAD),
                        True, True, 10)

        hbox.pack_start(self.create_bbox("3","Discussions",
                                         5, gtk.BUTTONBOX_SPREAD),
                        True, True, 10)
	
        window.show_all()

def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    NetbookSupport()
    main()
    
 
