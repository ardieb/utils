from argparse import ArgumentParser
from pdfrw import PdfReader, PdfWriter
from os.path import abspath, basename, dirname


def parse_slice(s):
  a = [int(e) if e.strip() else None for e in s.split(":")]
  return slice(*a)


parser = ArgumentParser()
parser.add_argument('-file',
                    type=str,
                    action='store',
                    dest='file',
                    help='The pdf file to read')
parser.add_argument('-pages',
                    type=parse_slice,
                    action = 'store',
                    dest='pages',
                    nargs='+',
                    help='The pages to separate')

args = parser.parse_args()

path = abspath(args.file)
directory = dirname(path)
name = basename(path)

pdf = PdfReader(path)
slices = args.pages

for s in slices:
  y = PdfWriter()
  y.addpages(pdf.pages[s])
  y.write(directory + '/' + name[:-4] + str(s.start) + str(s.stop) + '.pdf')