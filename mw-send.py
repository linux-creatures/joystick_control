
from socket import *
import sys
import select
import struct
import pygame
import time
from joystick import *       #Import the PS3 library
from multiwii_modes import *
from numpy import interp


UDP_IP = "192.168.0.105"
UDP_PORT = 51001

address = (UDP_IP, UDP_PORT)
client_socket = socket(AF_INET, SOCK_DGRAM)


p=ps3()             #Create a PS3 object
print "Done Initializing."

##board_arm(5)


while True:

  p.update()      #Read the ps3 values



  yaw = int(interp(p.a_joystick_left_x,[-1,1],[1000,2000]))
  throttle = int(interp(p.a_joystick_left_y,[-1,1],[2000,1000]))
  roll = int(interp(p.a_joystick_right_x,[-1,1],[2000,1000]))
  pitch = int(interp(p.a_joystick_right_y,[-1,1],[1000,2000]))

  aux_1 = 1000
  aux_2 = 1000
  aux_3 = 1000
  aux_4 = 1000

  numOfValues = 8
  if yaw==1999:
      yaw = 2000

  mess=struct.pack('>' + 'd' * numOfValues, roll, pitch, yaw, throttle, aux_1, aux_2, aux_3, aux_4)
  client_socket.sendto(mess, address)
  #print throttle
  #print pitch
  #print "roll"
  #print roll
  print yaw
