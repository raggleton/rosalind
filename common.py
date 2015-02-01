import sys


def runit(custom_fn):
    if not sys.argv[1]:
        print "Not running, need filename"
        return
    print sys.argv[1]
    with open(sys.argv[1], "r") as f:
        line = f.readline().strip()
        print line
        out = custom_fn(line)
        print out
        return out


def test(custom_fn, sample_data, sample_output):
    if sample_output != custom_fn(sample_data):
        print "YOU MUCKED UP"
        return False
    else:
        return True
