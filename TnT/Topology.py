import os
import turtle
from labenv2 import devices
import time
import json
from pprint import pprint



def test():
    angle = 0
    for device in devices:
        for connection in device['connections']:
            inverted_connections = dict(map(reversed, connection.items()))
            for device in devices:
                hostname = device['name']  
             


# test()

def test2():
    start_angle = 180
    for device in devices:
        turn_angle = 35
        path = turtle.Turtle()
        path.left(start_angle)
        path.forward(100)
        path.backward(100)
        for connection in device['connections']:
            path = turtle.Turtle()
            path.left(start_angle)
            path.forward(100)
            path.left(turn_angle)
            path.forward(100)
            turn_angle = turn_angle + 15
        start_angle = start_angle + 45
    turtle.done()

# test2()

def test3():
    parsed_connections_list = []
    parsed_connections_dictionary = {}
    counter = 0
    for device in devices:
        device_name = device['name']
        connections = device['connections']
        for connection in connections:
            inverted_connections = dict(map(reversed, connection.items()))
            for inverted_connection in inverted_connections:
                for device in devices:
                    if inverted_connections in device['connections']:
                        connected_device = device['name']
                        # print(f"{device_name} is connected to {connected_device}")
                        parsed_connections_list.append([device_name, connected_device])
                break
    # pprint(parsed_connections_list)
    return parsed_connections_list

# list_of_connections = test3()
# pprint(list_of_connections)

def devices_list():
    list_of_devices = []
    for device in devices:
        list_of_devices.append(device['name'])
    return list_of_devices

def draw_router(circum, xpos, ypos):
    path = turtle.Turtle()
    path.penup()
    path.goto(xpos, ypos)
    path.pendown()
    path.circle(circum)
    path.penup()
    path.goto(0, 0)



def draw_switch(x, y, xpos, ypos):
    path = turtle.Turtle()
    path.goto(xpos, ypos)
    path.left(0)
    path.forward(x/2)
    path.left(90)
    path.forward(y)
    path.left(90)
    path.forward(x)
    path.left(90)
    path.forward(y)
    path.left(90)
    path.forward(x/2) 

def test4():
    list_of_devices = devices_list()
    list_of_connections = test3()
    angle = 160
    length = 120
    start_x = 0
    start_y = 0
    for device in devices:
        if device['ports'][0][0:4:1] == 'ssss':
            draw_switch(50, 20, start_x, start_y)
            start_x = start_x +30
            start_y = start_y +30

        if device['ports'][0][0:4:1] == 'rrrr':
            draw_router(20, start_x, start_y)
            start_x = start_x +50
            start_y = start_y 

        # path = turtle.Turtle()
        # path.penup()
        # path.left(angle)
        # path.goto(start_x, start_y)
        # path.pendown()
        # path.circle(20)
        # start_x = start_x + 40
        # start_y = start_y + 40


    turtle.done()
            

test4()