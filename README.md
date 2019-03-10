# FlowChartGenerator
Simple Python class for generating a flow chart line by line should the need arise to print a flowchart via terminal

Each function prints a symbol based on standard flow chart symbols. Arguments should include a text string and position integer that is based on the distance from the left of the terminal or last character (arrows require no text, diamonds require three strings to denote the choice and two options). To place more than one object on the same line everything must be done in a print() function.

Current symbols and what they symbolize include 

|box| : action being performed 

optionA--<diamond>--optionB : choice and options

(circle) : Start and Finish or flowchart

right arrow : |----->

left arrow : <-----|

down arrow : \\/
                    
                    
How To Construct a Flow Chart:
Each line must be constructed individually so it's recommended to draw out how the flowchart first.
1) Begin by calling the class, ex: flow = OutLiner()
2) Print the start of the file on the first line roughly in the center of the terminal ex: print(flow.circle('START', 40))
3) Call a down arrow directly underneath ex: print(flow.down_arrow(40))
4) For more than one symbol on the same line simply concatenate in the print() function ex: print(flow.box('this is on', 10) + flow.trap('the same line', 10))
5) Continue this process until finished ex: print(flow.circle('FINISH', 40))

Here is what the included Example.py output should generate:
<pre>
                                        (START)
                                           \/
                             BAM------BAM or fastq-----fastq
                              \/                         \/
          Yes----<Is the bam Clean?>----No               \/
           \/                           \/               \/
      /clean bam/<-----\/              /bam/             \/
           \/          \/               \/               \/
      |Merge bam|      \/           |sam2fastq|          \/
           \/          \/               \/               \/
      /merged bam/     \/            /fastq/<------------\/
           \/          \/               \/
        (FINISH)       \/               \/
                       \/             |trim|
                       \/               \/
                       \/         /clean fastq/
                       \/               \/
                       \/            |Merge|
                       \/               \/
                       \/         /merged fastq/
                       \/<--------------\/
</pre?
