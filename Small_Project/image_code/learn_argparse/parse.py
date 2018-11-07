# https://www.cnblogs.com/yymn/p/8056487.html

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x",type = int , help="thr base") #action="store_true"
args = parser.parse_args()
answer = args.x*2
# if args.verbosity:
#         print("verbosity turned on")
#         print(args.verbosity)
print(answer)