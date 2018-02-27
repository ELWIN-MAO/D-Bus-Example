#! /usr/bin/env python3

import dbus

bus = dbus.SystemBus()
system = bus.get_object("org.me.test_system", "/org/me/test_system")

# Get each method for the specific interface
method_message1 = system.get_dbus_method('system_bus_message1', 'org.me.test1')
method_message2 = system.get_dbus_method('system_bus_message2', 'org.me.test2')
method_message3 = system.get_dbus_method('system_bus_strings', 'org.me.test2')

# Call the methods with their specific parameters
print(method_message1())
print(method_message2())
print(method_message3("Hello", "world"))

