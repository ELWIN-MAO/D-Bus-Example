#! /usr/bin/env python3

import dbus

bus = dbus.SessionBus()
session = bus.get_object("org.me.test_session", "/org/me/test_session")

interface1 = dbus.Interface(session, "org.me.test1")
interface2 = dbus.Interface(session, "org.me.test2")

# Call the methods using the interface
print(interface1.session_bus_message1())
print(interface2.session_bus_message2())
print(interface2.session_bus_strings("Hello", "world"))
