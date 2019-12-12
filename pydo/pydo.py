import argparse
import sys

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def main():
    parser = MyParser(prog ='pydo', description ='A python command line todo app') 
  
    parser.add_argument('--say', dest='say', type=str,
                        help='Echos the sentence') 

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
  
    args = parser.parse_args() 
  
    if args.say: 
        print("Echo: ", args.say)
    elif args.save:
        print("Saving task...")
    else:
        print("What? :|")
