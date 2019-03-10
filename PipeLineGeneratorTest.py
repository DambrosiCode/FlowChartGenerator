# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:13:30 2019

@author: Matt
"""
import shutil


class OutLiner(object):
    def box(self,text, pos): 
        '''
        Outputs |box| for flowchart elements depictings a process
        Arguments:
            text(string): text
            pos(int): position
        Returns:
            string: |text|
        '''
        
        self.text = text            

        space_len = (len(self.text) - len(self.text))
        box = ('|' + self.text + ' '*space_len +'|')
        
        return(box[i].rjust(pos + int(len(box)/2)))
        
    def diamond(self,text, pos, optionA, optionB): 
        '''
        Outputs <diamond> and 2 options for flowchart elements depictings a conditional
        Arguments:
            text(string): text
            pos(int): position
        Returns:
            string: optionA----<text>----optionB
        '''
        
        self.text = text

        self.optionA = optionA
        self.optionB = optionB
        
        space_len = (len(self.text) - len(self.text))
        trap = (self.optionA + '----' +'<' + self.text + ' '*space_len +'>' +'----' + self.optionB)
        
        return(trap.rjust(pos + int(len(trap)/2)))
            
    def trap(self,text,pos): 
        '''
        Outputs /trapezoid/ andfor flowchart elements depictings an input or output
        Arguments:
            text(string): text
            pos(int): position
        Returns:
            string: /text/
        '''
        
        self.text = text
        space_len = (len(self.text) - len(self.text))
        trap = ('/' + self.text + ' '*space_len +'/')
        
        
        return(trap.rjust(pos+int(len(trap)/2)))
        
    def circle(self,text, pos):
        '''
        Outputs (circle) and for flowchart elements depictings start and finish 
        Arguments:
            text(string): text
            pos(int): position
        Returns:
            string: (text)
        '''
        
        self.text = text
        circ = ('(' + self.text +')')
            
        return(circ.rjust(pos + int(len(circ)/2)))
    
    def down_arrow(self, pos):
        '''
        Outputs down arrow to signify next flow chart element
        Arguments:
            pos(int): position
        Returns:
            string: \/
        '''
        
        #pos = int(len(text)/2)
        return('\/'.rjust(pos))
        
    def left_arrow(self, length):
        '''
        Outputs down arrow to signify next flow chart element
        Arguments:
            length(int): how long the arrow should be
        Returns:
            string: <-|
        '''
        
        left = ('<'+'-'*length + '|')
        return(left)
        
    def right_arrow(self, length):
        '''
        Outputs down arrow to signify next flow chart element
        Arguments:
            length(int): how long the arrow should be
        Returns:
            string: |->
        '''
        
        right = ('|' + '-'*length + '>')
        return(right)
