#!/usr/bin/python
# -*- coding: utf-8 -*-


cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_driven = drivers
cars_not_driven = cars - drivers
carpool_capacity = cars * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "car available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."