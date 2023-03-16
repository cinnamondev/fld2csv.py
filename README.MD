# fld2csv.py

Parser for FLD files to CSV format.


## Usage
```
usage: fld2csv.py [-h] [-o [OUTPUT]] [-t {fld,elvis}] [-n] [file]

Helper script for parsing FLD and NI ELVISmx log files.
https://github.com/cinnamondev/fld2csv.py/

positional arguments:
  file                  Location of file to parse. Also accepts piped input.

options:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
                        When omitted, it will guess first on input filename, failing that, it will use <type>_<timestamp>.csv .
                        If the output of the script is redirected, it will output results to stdout instead of a file.
  -t {fld,elvis}, --type {fld,elvis}
                        Default: fld.
                        fld: Parse as a fld file.
                        elvis: Parse as a log file output from an NI ELVISmx tool.
  -n, --quiet           Execution with --quiet will not open the csv file in its associated program. Ignored if output is redirected.
```
Example:
```.\fld2csv.py elvis.txt -n -t elvis -o output.csv```
Creates a file `output.csv`, using `elvis.txt`as input in elvis file mode, without opening Excel.


### Scripting usage
The script can detect interactive I/O and will accept/output to redirected I/O.
Piped input will not require an input file. Piped output will bypass saving to a file.
Example:
```cat file.fld > .\fld2csv.py > file.csv```    

## Additional formats


## Licensing

Copyright 2023 Cinnamondev

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.