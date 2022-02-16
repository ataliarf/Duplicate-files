
# Duplicate files

This script scans a directory to find duplicate files based on their content.
##### If the directory has files A, B, C, D, E, F and A+B+E have the same content and D+F have the same content, the expected output should be:
##### * duplicate files: A, B, E
##### * duplicate files: D, F
# 
##### MD5 is cryptographically hash function producing a 128-bit hash value.
##### The script gets a path as a input. First, I checked if the path is valid.
##### After it, I walked through all files within the folder and subfolders, mapping by size of each file to its path.
##### The second stage was to walk through the keys of this map. For each key which its files list length is greather than 1 (i.e. several files with the same length), encode each file from its files list, and put it in a map which is mapping by MD5 encode to its path.
##### In the last stage, I walked through the last map, printing duplicate files (i.e. each key that has more than 1 files in its values list).
#
The code assumes we have a read permittion to the files.

