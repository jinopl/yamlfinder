import argparse,sys
from datetime import datetime


def opfilename():
   now = datetime.now()
   return 'file' + now.strftime("%d%m%Y%H%M") + '.txt'



parser = argparse.ArgumentParser()
parser.add_argument('--ifile',type=str,dest='ifile',help="name of input file", required=True)
parser.add_argument('--ofile',type=str,dest='ofile',help="name of output file")
args = parser.parse_args()

if not args.ofile:
    ofile = opfilename()
else:
    ofile = args.ofile

ifile = args.ifile

#sys.exit(1)

# with open(ifile) as myfile:
#    content_list = myfile.readlines()


yamlfiles = []


# for f in content_list:
#    if f.strip().endswith(('.yaml','.yml')):
    # yamlfiles.append(f.strip())

# with open(ofile, 'w') as f:
    # for line in yamlfiles:
        # f.write(line)
        # f.write('\n')
