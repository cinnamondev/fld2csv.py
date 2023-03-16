"""Copyright 2023 Cinnamondev

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

# 15/03/2023: Moved to github repository.
import os
import sys
import datetime
import argparse 
import re

args = argparse.ArgumentParser(
                    prog = 'fld2csv.py',
                    description = """Helper script for parsing FLD and NI ELVISmx log files.
https://github.com/cinnamondev/fld2csv.py/""",
                    formatter_class=argparse.RawTextHelpFormatter
                  )
args.add_argument('file',
                     type=argparse.FileType('r', encoding='UTF-8'),
                     default=sys.stdin,
                     nargs="?",
                     help="Location of file to parse. Also accepts piped input.",
                     )                    
args.add_argument('-o', '--output', 
                    type=argparse.FileType('w', encoding='UTF-8'),
                    default=sys.stdout,
                    nargs="?",
                    help="""When omitted, it will guess first on input filename, failing that, it will use <type>_<timestamp>.csv .
If the output of the script is redirected, it will output results to stdout instead of a file."""
                    )
args.add_argument('-t', '--type',
                     choices=["fld","elvis"],
                     default="fld",
                     required=False,
                     help="""Default: fld.
fld: Parse as a fld file.
elvis: Parse as a log file output from an NI ELVISmx tool.""")     
args.add_argument('-n', '--quiet',
                     action='store_true',
                     required=False,
                     default=False,
                     help="Execution with --quiet will not open the csv file in its associated program. Ignored if output is redirected.")
"""args.add_argument('-v', '--verbose',
                     action='store_true',
                     required=False,
                     default=False,
                     help="Output debug messages.")"""                                          

a = args.parse_args()

# Input guard - only allow piped input or provided file. this looks ugly :(
is_stdin = a.file.name == '<stdin>'
is_stdout = a.output.name == '<stdout>'
if not ((a.file.name == '<stdin>') and not sys.stdin.isatty()) or (a.file.name != '<stdin>'): 
   print("""usage: fld2csv.py [-h] [-o OUTPUT] [-t {fld,elvis}] [-n] file
fld2csv.py: error: the following arguments are required: file""")
   exit()


if a.output.name == '<stdout>' and sys.stdout.isatty():          # handle no output file
   if a.file.name != '<stdin>':
      fileName = a.file.name.rsplit('.',1)[0] + ".csv" # Guess using input file.
   else:   
      # Create file name using ISO timestamp.
      filename = a.type +"_" + datetime.datetime.now().isoformat().replace(":","-") + ".csv"
   
   a.output = open(
      filename,
      "w",
      encoding='UTF-8')

print(a)
# Now for the actual work!
match a.type:
   case "fld":
      # Ignore line 0, 1 is already comma delim (ignore), 2 is space delim.
      a.file.readline() # Discard
      output = a.file.readline()
      for line in a.file: # read rest of file.
         output += re.sub(" +",",",line.lstrip())
      a.output.write(output)
   case "elvis":
      # write 1 and 2, 3 is tab delim, + is space delim.
      output = a.file.readline() + a.file.readline()
      output += ",".join(a.file.readline().split("""	""")) # Contains TAB ASCII.
      for line in a.file: # read rest of file.
         output += re.sub(" +",",",line.lstrip())
      a.output.write(output)
   case _:
      print("Unexpected error, unknown type")

a.output.close()
a.file.close()  

if not a.quiet and not is_stdout:
   os.startfile(a.output.name)