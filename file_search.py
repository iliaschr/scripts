# Old script
# Goal: Learning about re and os
import argparse
import os
import re


def main():
    parser = argparse.ArgumentParser(
                    prog='File Search',
                    description='Local file search tool with regex support ',
                    epilog='Thank you for using my program')
  
    parser.add_argument('-p', '--path')     
    parser.add_argument('-r', '--pattern')
     
    args = parser.parse_args()
    print(args.path, args.pattern)



    result = []
    for root, dirs, files in os.walk(args.path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, start=1): 
                        if re.search(args.pattern, line):
                            print(f"{file_path}:{i}:{line.strip()}")
            except Exception as e:
                pass 
    
    print(result)
    

if __name__ == "__main__":
    main()
