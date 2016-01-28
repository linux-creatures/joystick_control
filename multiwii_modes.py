from socket import *
import sys
import select
import struct
import pygame
import time
from joystick import *       #Import the PS3 library
from multiwii_modes import *
from numpy import interp


UDP_IP = "192.168.0.102"
UDP_PORT = 51001

address = (UDP_IP, UDP_PORT)
client_socket = socket(AF_INET, SOCK_DGRAM)

def board_arm(sleep_time):

	start_time = time.time()
	while time.time() < start_time + sleep_time:
		aux_1 = 1000
  		aux_2 = 1000
  		aux_3 = 1000
  		aux_4 = 1000

  		numOfValues = 8
  		mess=struct.pack('>' + 'd' * numOfValues, 1500, 1500, 2000, 1000, aux_1, aux_2, aux_3, aux_4)
  		client_socket.sendto(mess, address)