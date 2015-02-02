import sys


def runit(custom_fn):
    if len(sys.argv) == 1:
        print "Not running, need filename"
        return
    print sys.argv[1]
    with open(sys.argv[1], "r") as f:
        line = f.readline().strip()
        print "IN: "
        print line
        out = custom_fn(line)
        print "OUT: "
        print out
        return out


def test(custom_fn, sample_data, sample_output):
    print sample_data
    if sample_output != custom_fn(sample_data):
        print "YOU MUCKED UP"
        return False
    else:
        print "Wahey, it workd"
        return True
