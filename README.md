# AES  

## Description  
 
The algorithm follows the [official specification of AES](http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf).  

This means files will be encrypted with the Rijndael algorithm. Block length is fixed at 128 bits. Supported key lengths are 128, 192 and 256 bits.  

## Dependencies  

> code is based on Python 3.6.1  
> no additional libraries are needed  

## Usage  
    AES.py [-h] -k KEY -i INPUT [-d]  

#### Arguments  
`-h, --help` _show this help message and exit_  
`-k KEY, --key KEY` _Key in textform of length 16, 24 or 32 Symbols_  
`-i INPUT, --input INPUT` _Path to file which should be encrypted or decrypted_  
`-d` _set this flag if you want to decrypt the file_  
