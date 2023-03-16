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
                    help="Location of file to parse.",
                    )
args.add_argument('-o', '--output', 
                    type=argparse.FileType('w', encoding='UTF-8'),
                    required=False,
                    help="When specified, the output file will be saved to this location."
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
                     help="Execution with --quiet will not open the csv file in its associated program.")                     

a = args.parse_args()
if a.output == None:                       # handle no output file
   fileName = a.file.name.rsplit('.',1)[0] + ".csv" # all cases
   a.output = open(
      fileName,
      "w",
      encoding='UTF-8')

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

if not a.quiet:
   os.startfile(a.output.name)