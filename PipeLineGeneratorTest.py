# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:44:51 2019

@author: Matt
"""

from SlthrChart import OutLiner

o = OutLiner()
print(o.circle('START', 44))
print(o.down_arrow(44))
print(o.diamond('BAM or fastq', 44, 'BAM','fastq'))
print(o.down_arrow(31) + o.down_arrow(26))
print(o.diamond('Is the bam Clean?', 26, 'Yes','No') + o.down_arrow(16))
print(o.down_arrow(12) + o.down_arrow(28) + o.down_arrow(16))
print(o.trap('clean bam', 12) + o.left_arrow(5) + o.trap('bam', 17) + o.down_arrow(14))
print(o.down_arrow(12) + o.down_arrow(11) + o.down_arrow(16) + o.down_arrow(16))
print(o.box('Merge bam', 12) + o.down_arrow(7) + o.box('sam2fastq', 17) + o.down_arrow(11))
print(o.down_arrow(12) + o.down_arrow(11) + o.down_arrow(16) + o.down_arrow(16))
print(o.trap('merged bam', 12) + o.down_arrow(6) + o.trap('fastq', 16) + o.left_arrow(12))
print(o.down_arrow(12) + o.down_arrow(11) + o.down_arrow(16))
print(o.circle('FINISH', 12), o.down_arrow(7) + o.down_arrow(16))
print(o.down_arrow(24) + o.box('trim',16))
print(o.down_arrow(24) + o.down_arrow(16))
print(o.down_arrow(24) + o.trap('clean fastq',16))
print(o.down_arrow(24) + o.down_arrow(16))
print(o.down_arrow(24) + o.box('Merge',16))
print(o.down_arrow(24) + o.down_arrow(16))
print(o.down_arrow(24) + o.trap('merged fastq', 16))
print(o.down_arrow(24) + o.left_arrow(14))
