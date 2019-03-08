# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:13:30 2019

@author: Matt
"""

import textwrap
import shutil


class OutLiner(object):    
    def __init__(self):
        self.center = int(shutil.get_terminal_size().columns/2)
        
    def __str__(self):
        pass

    def text_block(self, text):    
        """turns long strings of text into blocks. 
        Also counts the length of the first line to properly align any boarders"""
        self.text = text                                        #this is the text
        self.block = textwrap.fill(self.text, 20)               #this wraps the text into a neat little text box
        self.first_line_len = len(self.block.splitlines()[0])   #this gets the length of the first line 
        
    def box(self,text, pos,): 
        self.text = text            
        self.text_block(self.text) #here the text_block() gets the string field from self.text to mainpulate

        #lid = '+' + '-'*(self.first_line_len) + '+'
        
        #self.down_arrow(text)
        box = []
        
        for i in range(0, self.block.count('\n')+1):
            space_len = (len(self.block.splitlines()[0]) - len(self.block.splitlines()[i]))
            box = ('|' + self.block.splitlines()[i] + ' '*space_len +'|')
        
        return(box[i].rjust(pos + int(len(box)/2)))
        
    def diamond(self,text, pos, optionA, optionB, hA = True): 
        ###TODO: set default value to make hor lines but switch to vert if want
        self.text = text
        self.text_block(self.text)

        self.optionA = optionA
        
        #this should switch between a vertical or horizontal arrow
        if(hA):
            dirA = optionA+'----'
        else:
            dirA = optionA

                
        dirB = '----'+optionB
        

        for i in range(0, self.block.count('\n')+1):
            space_len = (len(self.block.splitlines()[0]) - len(self.block.splitlines()[i]))
            trap = (dirA + '<' + self.block.splitlines()[i] + ' '*space_len +'>'+dirB)
        
        #self.down_arrow(' '*int(len(trap)+self.columns))
        return(trap.rjust(pos + int(len(trap)/2)))
            
    def trap(self,text,pos): 
        self.text = text
        self.text_block(self.text)


        #lid = ' ' + '-'*(self.first_line_len) + ' '
        for i in range(0, self.block.count('\n')+1):
            space_len = (len(self.block.splitlines()[0]) - len(self.block.splitlines()[i]))
            trap = ('/' + self.block.splitlines()[i] + ' '*space_len +'/')
        
        
        return(trap.rjust(pos+int(len(trap)/2)))
        
    def circle(self,text, pos):
        self.text = text
        self.text_block(self.text)
        
        for i in range(0, self.block.count('\n')+1):
            circ = ('(' + self.block.splitlines()[i] +')')
            
        return(circ.rjust(pos + int(len(circ)/2)))
    
    def down_arrow(self, pos):
        #pos = int(len(text)/2)
        return(' | '.rjust(pos + 1))
        
    def left_arrow(self, length):
        left = ('<'+'-'*length + '|')
        return(left)

      
o = OutLiner()