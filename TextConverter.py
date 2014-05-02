# -*- coding: utf-8 -*-
#Cool stuff


letterCodes = {'A' : [1,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
'B' : [1,1,1,1,0,1,1,1,0,1,0,1,1,1,1],
'C' : [1,1,1,1,0,0,1,0,0,1,0,0,1,1,1],
'D' : [1,1,0,1,0,1,1,0,1,1,0,1,1,1,0],
'E' : [1,1,1,1,0,0,1,1,1,1,0,0,1,1,1],
'F' : [1,1,1,1,0,0,1,1,0,1,0,0,1,0,0],
'G' : [1,1,1,1,0,0,1,0,1,1,0,1,1,1,1],
'H' : [1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
'I' : [1,1,1,0,1,0,0,1,0,0,1,0,1,1,1],
'J' : [1,1,1,0,0,1,0,0,1,1,0,1,1,1,1],
'K' : [1,0,1,1,0,1,1,1,0,1,0,1,1,0,1],
'L' : [1,0,0,1,0,0,1,0,0,1,0,0,1,1,1],
'M' : [1,0,1,1,1,1,1,0,1,1,0,1,1,0,1],
'N' : [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
'O' : [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1],
'P' : [1,1,1,1,0,1,1,1,1,1,0,0,1,0,0],
'Q' : [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1],
'R' : [1,1,1,1,0,1,1,0,1,1,1,0,1,0,1],
'S' : [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1],
'T' : [1,1,1,0,1,0,0,1,0,0,1,0,0,1,0],
'U' : [1,0,1,1,0,1,1,0,1,1,0,1,1,1,1],
'V' : [1,0,1,1,0,1,1,0,1,1,0,1,0,1,0],
'W' : [1,0,1,1,0,1,1,0,1,1,1,1,1,0,1],
'X' : [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
'Y' : [1,0,1,1,0,1,0,1,0,0,1,0,0,1,0],
'Z' : [1,1,1,0,0,1,0,1,0,1,0,0,1,1,1],
' ' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
'!' : [0,1,0,0,1,0,0,1,0,0,0,0,0,1,0],
'?' : [1,1,1,0,0,1,0,1,0,0,0,0,0,1,0],
'.' : [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]}


textToRender = "CALCULUS"
height = 9
length = 5 * len(textToRender) + 2


#Create array of 0s where characters will be rendered
arr = []
for i in range(height):
  a = []
  for j in range(length):
    a.append(1)
  arr.append(a)
for i in range(1, height-1):
  for j in range(1, length-1):
    arr[i][j] = 0


#Add ones where letter is.
iter = 0
for i in textToRender:
  #Add ones to array in shape of letters
  for j in range(height - 4):
    for k in range(3):
      arr[j+2][5*iter + k + 2] = letterCodes[i][3*j + k]
  iter += 1  

string = ""


#TEMPORARY FOR TESTING:
for i in range(height):
  for j in range(length):
    string += str(arr[i][j])
  string += "\n"
  
#print(string)
string = ""


#Convert from 1s and 0s to symbols:
top = False
bottom = False
left = False
right = False

for i in range(1, height - 1):
  for j in range(1, length - 1):
    if arr[i][j] == 0:
      top = (arr[i-1][j] == 0)
      bottom = (arr[i+1][j] == 0)
      left = (arr[i][j-1] == 0)
      right = (arr[i][j+1] == 0)
      if top and bottom and left and right:
        string += u"╬"
      elif top and bottom and left:
        string += u"╣"
      elif top and bottom and right:
        string += u"╠"
      elif top and left and right:
        string += u"╩"
      elif bottom and left and right:
        string += u"╦"
      elif top and bottom:
        string += u"║"
      elif top and right:
        string += u"╚"
      elif left and right:
        string += u"═"
      elif bottom and left:
        string += u"╗"
      elif top and left:
        string += u"╝"
      elif bottom and right:
        string += u"╔"
      elif top:
        string += u"╨"
      elif bottom:
        string += u"╥"
      elif left:
        string += u"╡"
      elif right:
        string += u"╞"
      else:
        string += u"║"
    else:
      top = (arr[i-1][j] == 1)
      bottom = (arr[i+1][j] == 1)
      left = (arr[i][j-1] == 1)
      right = (arr[i][j+1] == 1)
      if top and bottom and left and right:
        string += u"╬"
      elif top and bottom and left:
        string += u"╣"
      elif top and bottom and right:
        string += u"╠"
      elif top and left and right:
        string += u"╩"
      elif bottom and left and right:
        string += u"╦"
      elif top and bottom:
        string += u"║"
      elif top and right:
        string += u"╚"
      elif left and right:
        string += u"═"
      elif bottom and left:
        string += u"╗"
      elif top and left:
        string += u"╝"
      elif bottom and right:
        string += u"╔"
      elif top:
        string += u"╨"
      elif bottom:
        string += u"╥"
      elif left:
        string += u"╡"
      elif right:
        string += u"╞"
      else:
        string += u"║"
  string += u"\n"
  

print(string)
