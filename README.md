## Installation
1. Clone the repository with `git clone`.
2. Install with pip: `pip3 install /path/to/hash-cli-generator`

## What the tool does
I was tired of having to use workarounds to get a string hash on Linux, such as `md5sum <<< somestring` or `echo -n somestring | md5sum | awk '{print $1}'` so I created this small python CLI which is based on hashlib. 
The hashes are computed by python's built-in libraries.

## Usage
1. Basic usage: `hash-generator [string or path to a file] [type of hash]`
<br>*Examples:* 
- `hash-generator hello sha1`
- `hash-generator /path/to/file md5`
2. To get more information on how to use this tool: `hash-generator -h`
Usable algorithms depend on your system but these algorithms are always available:
* md5
* blake2b, blake2s
* sha384, sha3_384, sha3_224, sha3_256, sha224, sha1, sha256, sha3_512, sha512
* shake_128, shake_256
3. If you want to run the tests, just use `python -m unittest` in the tests directory.


## License
This tool is licensed under MIT license. You can basically do whatever you want with it !
