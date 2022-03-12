from rawStrings import *
import os

def createRustProject():
    os.system('cargo new connector')

def createMainRustFile(url):
    rawRust = getRustFileHeader() + getRustFileUrl(url) + getRestRustFile()
    file = open("connector/src/main.rs", "w")
    file.write(rawRust)

def createCargoTomlFile():
    rawToml = getRawCargoTomlFile()
    file = open("connector/Cargo.toml", "w")
    file.write(rawToml)

def createExecutable():
    os.system('cd connector && cargo build')

def moveExecutable():
    os.system('mv connector/target/debug/connector-builder .')

def deleteCargoProject():
    os.system('rm -rf connector/')

def main():

    url = '"https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=USD"'

    createRustProject()
    createMainRustFile(url)
    createCargoTomlFile()
    createExecutable()
    moveExecutable()
    deleteCargoProject()

if __name__=="__main__":
    main()