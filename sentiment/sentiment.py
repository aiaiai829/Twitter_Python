import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def test(tf):
    text = []
    for s in tf.readlines():
            y = s .split("\t")
            text.append((y[0]))
    return text
    
def sfDict(sf):
    x = []
    for s in sf.readlines():
            y = s .split("\t")
            x.append((y[0], y[1]))
    return x

def check(text, op):
    for z in text:
        val= 0.0
        for (x,y) in op:
            if ((x + " " )  or (" " + x)) in z:
                val= val + float(y)
        #print z + "  : " + str(val)
        print str(val)
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    x = test(tweet_file)
    y = sfDict(sent_file)
    check (x,y)

if __name__ == '__main__':
    main()
