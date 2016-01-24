
from socket import *
import sys
import select
import struct
import serial
import pygame
import time
from joystick import *       #Import the PS3 library
from numpy import interp


UDP_IP = "localhost"
UDP_PORT = 51001

address = (UDP_IP, UDP_PORT)
client_socket = socket(AF_INET, SOCK_DGRAM)


p=ps3()             #Create a PS3 object
print "Done Initializing."

while True:

  p.update()      #Read the ps3 values

               

  yaw = int(interp(p.a_joystick_left_x,[-1,1],[1000,2000]))
  throttle = int(interp(p.a_joystick_left_y,[-1,1],[1000,2000])) 
  roll = int(interp(p.a_joystick_right_x,[-1,1],[1000,2000]))
  pitch = int(interp(p.a_joystick_right_y,[-1,1],[1000,2000]))
  
  aux_1 = 1000
  aux_2 = 1000
  aux_3 = 1000
  aux_4 = 1000


  numOfValues = 8
  mess=struct.pack('>' + 'd' * numOfValues, throttle, yaw, roll, pitch, aux_1, aux_2, aux_3, aux_4)
  client_socket.sendto(mess, address)
  print throttle
  print pitch 
  print roll
  print yaw