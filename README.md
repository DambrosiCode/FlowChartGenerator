# FlowChartGenerator
Simple Python class for generating a flow chart line by line should the need arise to print a flowchart via terminal

Each function prints a symbol based on standard flow chart symbols. Arguments should include a text string and position integer that is based on the distance from the left of the terminal or last character (arrows require no text, diamonds require three strings to denote the choice and two options). 

Current symbols and what they symbolize include 
|box| : action being performed 
optionA--<diamond>--optionB : choice and options
(circle) : Start and Finish or flowchart
right arrow : ----->
left arrow : <-----
down arrow : \|/
                    
                    
How To Construct a Flow Chart:
Each line must be constructed individually so it's recommended to draw out how the flowchart first.
1) Begin by calling the class, ex: flow = OutLiner()
2) Print the start of the file on the first line roughly in the center of the terminal ex: flow.circle('START', 40)
3) Call a down arrow directly underneath ex: flow.down_arrow(40)
4) Continue this process until finished ex: flow.circle('FINISH', 40)
