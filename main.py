from rawStrings import *
import os
import sys

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

def putSourceCodeInOwnFolder():
    os.system('mkdir source-code')

    os.system('mv connector/src/main.rs source-code')
    os.system('mv connector/Cargo.toml source-code')

def deleteCargoProject():
    os.system('rm -rf connector/')

def main():
    url = sys.argv[1]

    createRustProject()
    createMainRustFile(url)
    createCargoTomlFile()
    createExecutable()
    moveExecutable()
    putSourceCodeInOwnFolder()
    deleteCargoProject()

if __name__=="__main__":
    main()
