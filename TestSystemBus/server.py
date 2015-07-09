#! /usr/bin/env python3

# D-Bus Server -- Server Bus

from gi.repository import Gtk
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

class Session_DBus(dbus.service.Object):

	def __init__(self):
		bus_name = dbus.service.BusName('org.me.test_system', bus=dbus.SystemBus())
		dbus.service.Object.__init__(self, bus_name, '/org/me/test_system')

	# Interface and Method
	@dbus.service.method('org.me.test1')
	def system_bus_message1(self):
		return "Server Bus 1"


	# Different Interface and different Method
	# The method must not have not the same name as the first 
	@dbus.service.method('org.me.test2')
	def system_bus_message2(self):
		return "Server Bus 2"


	# Method with arguments
	@dbus.service.method('org.me.test2')
	def system_bus_strings(self, string1, string2):
		return string1 + " " + string2


DBusGMainLoop(set_as_default=True)
dbus_service = Session_DBus()
Gtk.main()
