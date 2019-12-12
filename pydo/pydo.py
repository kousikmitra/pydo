import argparse
import sys
from os.path import dirname, abspath, join
from random import randrange
import json

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def inspire():
    inspire_file = join(dirname(dirname(abspath(__file__))), 'static', 'inspiration.json')
    with open(inspire_file, 'r') as f:
        data = json.load(f)
        print(data[randrange(len(data))])

def main():
    parser = MyParser(prog ='pydo', description ='A python command line todo app') 
  
    parser.add_argument('--say', dest='say', type=str,
                        help='Echos the sentence')
    
    parser.add_argument('--inspire', dest='inspire', action='store_true', help='Will tell you an inspiration quote')

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
  
    args = parser.parse_args() 
  
    if args.say: 
        print("Echo: ", args.say)
    elif args.inspire:
        inspire()
    elif args.save:
        print("Saving task...")
    else:
        print("What? :|")


if __name__ == "__main__":
    main()