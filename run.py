import argparse
from pcm2mp3 import pcm_files, convert
import os

parser = argparse.ArgumentParser(description='Convert pcm files to csv files')

# add arguments
parser.add_argument('-i', type=str, help="folder path which has pcm files")
parser.add_argument('-o', type=str, help="folder path where mp3 files will be created")

args = parser.parse_args()

if __name__ == "__main__" :
    try :
        if args.i == None and args.o == None :
            input_path = './'
            pcm_files = pcm_files(input_path)
            output_path = './'
            convert(input_path, output_path, pcm_files)
        elif args.i == None and args.o != None :
            input_path = './'
            pcm_files = pcm_files(input_path)
            output_path = args.o
            convert(input_path, output_path, pcm_files)
        elif args.i != None and args.o == None :
            input_path = args.i
            pcm_files = pcm_files(input_path)
            output_path = './'
            convert(input_path, output_path, pcm_files)
        elif args.i != None and args.o != None :
            input_path = args.i
            pcm_files = pcm_files(input_path)
            output_path = args.o
            convert(input_path, output_path, pcm_files)
        
        
    
    except Exception :
        print("No folder name '" + output_path + "'.")
