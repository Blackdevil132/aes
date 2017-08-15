# AES  

## Description  

The Goal of this project is to provide an easy-to-use tool for encrypting and decrypting files using the AES-Algorithm.  
specification see: http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf  

This means files will be encrypted with the Rijndael algorithm, a symmetric block cipher. Block length is 128 bits. Supported key lengths are 128, 192 and 256 bits.  

Further goals are to translate the algorithm into Java and ultimately to create an Android application.  

## Dependencies  

code is based on Python 3.6.1  
no additional libraries are needed  

## Usage  
    AES.py [-h] -k KEY -i INPUT [-d]  

arguments:  
    -h, --help            show this help message and exit  
    -k KEY, --key KEY     Key in textform of length 16, 24 or 32 Symbols  
    -i INPUT, --input INPUT  
                        Path to file which should be encrypted or decrypted  
    -d                    set this flag if you want to decrypt the file  
