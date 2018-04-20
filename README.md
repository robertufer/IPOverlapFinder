# IPOverlapFinder
Tool that searches two groups of IP ranges for overlaps



This tool takes 2 files of IP addresses + mask and will use an interval tree search to find where the IPs from file A overlap with B. 

I provided an example data set, inputaddressesA and B.txt. 

indexer.py converts the lists to a format the elementtree module can use

treecomapre.py compares entries in list A to B and returns whether or not the range overlaps and what the first and last IP are.
