import os
import subprocess
try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')
try:
   input = raw_input
except NameError:
   pass
f_input1 = "/tmp/diff_cmd1.bk.curl"
f_input2 = "/tmp/diff_cmd2.bk.curl"
print ("Leave empty and press <Enter> to reuse input of previous run, for 1st/2nd input respectively")
if __name__ == "__main__":
    first_l = []
    second_l = []
    for cmd_i, cmd in enumerate(('1st curl: ', '2nd curl: ')):
        l = []
        input_str = input(cmd).strip()
        if cmd_i == 0:
            f_i = f_input1
        else:
            f_i = f_input2
        if input_str == '': #get from bk
            if os.path.isfile(f_i) :
                with open (f_i, 'r') as f:
                   input_str = f.read()
        else: #bk
            with open (f_i, 'w') as f:
                f.write(input_str)
        h_l = input_str.split(" -H '"); #no nid care if double quotes
        hh = []

        for x in h_l:
            if x.endswith("' "):
                hh.append(x[:-2])
            elif x.endswith("'"):
                hh.append(x[:-1])
            else:
                hh.append(x)
        h_l = hh

        url = h_l[0]
        urls = url.split("&")
        if len(urls) == 1: # == 0 doesn't make sense
            l.append("[Curl]: " + url)
        else:
            l.append("[Curl]: " + urls[0])
            urls = urls[1:]
            for u in urls:
                l.append("[1]: &" + u)
        h_l = h_l[1:]
        for i, h in enumerate(h_l):
            hs = h.split("'")
            if len(hs) == 0:
                print ("Missing quotes, something went wrong")
            elif len(hs) == 1:
                if hs[0].startswith("Cookie: "):
                    for ck in hs[0][8:].split('; '):
                        l.append("[-H Cookie]: " +  ck + "; ")
                else:
                    l.append("[-H]: " + hs[0])
            else:
                l.append("[-H]: " + hs[0])
                others = "'".join(hs[1:])
                if others.startswith(" --data '"):
                    for i, other in enumerate(others.split("&")):
                        if i == 0:
                           other = other[9:] #remove ` --data '`
                        if "'" in other:
                            other_dot = other.split("'")
                            other = other_dot[0]
                            l.append("[Other]: " + other_dot[1].strip())
                        l.append("[--data]: &" + other)
                else:
                    l.append("[Other]: " + others.strip())
        #no nid care -- or other invalid syntax(e.g. no space in `header:`), rare case for now
        if cmd_i == 0:
            first_l = l
        else:
            second_l = l
    first_l.sort()
    second_l.sort()
    print ("########### 1st ###########")
    for ll in first_l:
        print (ll)
    print ('\n')
    print ("########### 2nd ###########")
    for ll in second_l:
        print (ll)
    f1 = '/tmp/diff_url1.curl'
    f2 = '/tmp/diff_url2.curl'
    with open (f1, 'w') as f:
        f.write ("\n".join(first_l))
    with open (f2, 'w') as f:
        f.write ("\n".join(second_l))
    subprocess.Popen(["kdiff3", f1, f2], stdout=DEVNULL)


