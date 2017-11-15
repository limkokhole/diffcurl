Diff 2 curl commands

Prerequisites to use this script:

- Linux #you may modify the 4 /tmp/ paths if you want to make it run in Windows
- Firefox or Chrome to copy curl output
- kdiff3 tool #you can modify "kdiff3" to other diff tool in line subprocess.Popen(["kdiff3", f1, f2], stdout=DEVNULL)
- python interpreter

How to use:

[1] Inspect element in firefox, in network tab, right click to copy the link as curl  

[2] Then paste the links you want to compare into [1] and [2] prompts in python script, which run as `python diff_curl.py`  

[3] You can omit the input for [1] or [2], which will reuse previous input if exist.  


How it works:

It simply split the curl commands you've pasted into prompts to various parts, then sort them and save to files, then let kdiff3 to diff the files.

I don't bother to split --2.0 out of url's [1] field, it make code complicated without significant benefit.   
- [UPDATE] Bug report at https://bugzilla.mozilla.org/show_bug.cgi?id=1253487  shows that --2.0 has been fixed and removed in Firefox 58.  

And I lazy to make it support 3 prompts.

Kindly create a pull request if you wish to :)  

Demonstration video (Click image to play at YouTube):  

[![watch in youtube](http://img.youtube.com/vi/S4VcnRe0oAo/0.jpg)](http://www.youtube.com/watch?v=S4VcnRe0oAo "diff curl")
