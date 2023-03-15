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

import argparse 
import re

args = argparse.ArgumentParser(
                    prog = 'fld2csv.py',
                    description = 'Converts a fld file (ansys) to a csv file.',
                  )
args.add_argument('file',
                    type=argparse.FileType('r', encoding='UTF-8'),
                    )
args.add_argument('-o', '--output', 
                    type=argparse.FileType('w', encoding='UTF-8'),
                    required=False,
                    )
args.add_argument('-t', '--type',
                     choices=["fld","elvis"],
                     default="fld",
                     required=False,
                     help="""Available choices:
                     - (DEFAULT) fld: process with FLD layout.
                     - elvis: process with elvismx log output layout.""")                    
a = args.parse_args()
if a.output == None:                       # handle no output file
   fileName = "".join(a.file.name.rsplit('.',1)) + ".csv" # all cases
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
