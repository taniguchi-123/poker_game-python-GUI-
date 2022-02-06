# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:51:54 2021
@author: taniguchi
"""

################################################################
#check if there is any prize
################################################################
global message_list   #used inside of other method 
message_list = ["Loyal straight flash",  #message0
                "straight flash",        #message1
                "straight",              #message2
                "flash",                 #message3
                "fullhouse",             #message4
                "4 cards",               #message5
                "3 cards",               #message6
                "2 pair",                #message7
                "",
                "",
                ]

class CardCheck(list):
    

    def card_check(self,data):
        global message
        message = ''

        #sort sample card 
        number = (sorted(data, key=lambda x: x[1]))  #sort sample card by number
        #mark = (sorted(data, key=lambda x: x[0]))  #sort sample card by mark
        
        #loyal straight flash
        if data[0][0]==data[1][0]==data[2][0]==data[3][0]==data[4][0] and \
            number[0][1] == 1 and number[1][1] == 10 and number[2][1] == 11 and \
            number[3][1] == 12 and number[4][1] == 13 :
            #print('Loyal straight flash')
            message = str(message_list[0])
    
        #straight flash
        elif data[0][0]==data[1][0]==data[2][0]==data[3][0]==data[4][0] and \
            number[0][1]+1 == number[1][1] and number[0][1] + 2 == number[2][1] \
            and number[0][1] + 3 ==number[3][1] and number[0][1] + 4 == number[4][1] :
            #print('straight flash')
            message = str(message_list[1])
    
        #straight
        elif ((number[0][1]+1 == number[1][1] and number[0][1] + 2 == number[2][1] \
              and number[0][1] + 3 ==number[3][1] and number[0][1] + 4 == number[4][1]) or \
            (number[0][1] == 1 and number[1][1] == 10 and number[2][1] == 11 and \
             number[3][1] == 12 and number[4][1] == 13)):
                #print('straight')
                message = str(message_list[2])
    
        #flash 
        elif data[0][0]==data[1][0]==data[2][0]==data[3][0]==data[4][0] :
            #print('flash')
            message = str(message_list[3])
    
    
        #fullhouse
        elif (number[0][1] == number[1][1] == number[2][1] and number[3][1] == number[4][1] and number[2][1] != number[3][1]) or (number[0][1] == number[1][1]  and number[2][1] == number[3][1] == number[4][1] and number[1][1] != number[2][1]) :
            #print('fullhouse')
            message = str(message_list[4])
    
        else:
            
        #4 cards
            for i in range(2):
                if (number[i][1] == number[i+1][1]) and (number[i+1][1] == number[i+2][1] and number[i+2][1] == number[i+3][1]):
                    #print('4 cards')
                    message = str(message_list[5])
                    break
        #3 cards
                else:
                    for j in range(3):
                        if number[j][1] == number[j+1][1] and number[j+1][1] == number[j+2][1]:
                            #print('3 cards')
                            message = str(message_list[6])
                            break
                        else:
                
        #2 pair
                            pair = 0 #initialise 2 pair
                            for k in range(4):
                                if number[k][1] == number[k+1][1] :
                                    pair += 1
                                    if pair == 2:
                                        message = str(message_list[7])
                                    else:
                                        message = ''
        return message


if __name__  == '__main__':

    
    check = CardCheck()        # create CardCheck object
    #print(check.card_check(data))  
        