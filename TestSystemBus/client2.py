#!/usr/bin/env python3

import dbus

bus = dbus.SystemBus()
system = bus.get_object("org.me.test_system", "/org/me/test_system")

interface1 = dbus.Interface(system, "org.me.test1")
interface2 = dbus.Interface(system, "org.me.test2")

# Call the methods using the interface
print(interface1.system_bus_message1())
print(interface2.system_bus_message2())
print(interface2.system_bus_strings("Hello", "world"))
