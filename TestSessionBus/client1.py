#! /usr/bin/env python3

import dbus

bus = dbus.SessionBus()
session = bus.get_object("org.me.test_session", "/org/me/test_session")

# Get each method for the specific interface
method_message1 = session.get_dbus_method('session_bus_message1', 'org.me.test1')
method_message2 = session.get_dbus_method('session_bus_message2', 'org.me.test2')
method_message3 = session.get_dbus_method('session_bus_strings', 'org.me.test2')

# Call the methods with their specific parameters
print(method_message1())
print(method_message2())
print(method_message3("Hello", "world"))

