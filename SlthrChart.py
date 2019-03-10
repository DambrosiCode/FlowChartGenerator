# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:13:30 2019

@author: Matt
"""
import shutil


class OutLiner(object):    
    def __init__(self):
        self.center = int(shutil.get_terminal_size().columns/2)


    def box(self,text, pos,): 
        self.text = text            

        space_len = (len(self.text) - len(self.text))
        box = ('|' + self.text + ' '*space_len +'|')
        
        return(box.rjust(pos + int(len(box)/2)))
        
    def diamond(self,text, pos, optionA, optionB): 
        self.text = text

        self.optionA = optionA
        self.optionB = optionB
        
        space_len = (len(self.text) - len(self.text))
        trap = (self.optionA + '----' +'<' + self.text + ' '*space_len +'>' +'----' + self.optionB)
        
        return(trap.rjust(pos + int(len(trap)/2)))
            
    def trap(self,text,pos): 
        self.text = text
        space_len = (len(self.text) - len(self.text))
        trap = ('/' + self.text + ' '*space_len +'/')
        
        
        return(trap.rjust(pos+int(len(trap)/2)))
        
    def circle(self,text, pos):
        self.text = text
        circ = ('(' + self.text +')')
            
        return(circ.rjust(pos + int(len(circ)/2)))
    
    def down_arrow(self, pos):
        #pos = int(len(text)/2)
        return('\/'.rjust(pos + 1))
        
    def left_arrow(self, length):
        left = ('<'+'-'*length + '\/')
        return(left)
        
    def right_arrow(self, length):
        right = ('\/' + '-'*length + '>')
        return(right)
