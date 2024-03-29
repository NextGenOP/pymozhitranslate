#! /usr/bin/env python

from pymozhitranslate.arg import ArgumentParser
from pymozhitranslate import Translator

desc = """
Simple translator tool.
"""
def translate():
    arg = ArgumentParser(description=desc, allow_abbrev=False, add_help=False)
    arg.add_argument("-h", "--help", action="help", help="Display this message")
    arg.add_argument("-e", "--engine", type=str, help="Engine to use")
    arg.add_argument("-s", "--source", type=str, help="Source Language to translate")
    arg.add_argument("-t", "--target", type=str, help="Target Language to translate")
    arg.add_argument("-txt", "--text", type=str, help="Text to translate")
    arg.add_argument("-ll", "--list-languages",  help="List Languages support", action="store_true")
    arg.add_argument("-f", "--file",  help="Path file .txt to translate")
    arg.add_argument("-o", "--output",  help="Output file translation result")
    args = arg.parse_args()

    if args.text == None:
        print("Text is empty")
        arg.print_help()
        exit()
    if args.engine:
        translate = Translator(engine=args.engine)
    else:
        translate = Translator()
    if args.list_languages:
        lang = translate.languages()
        print("{:<25} {:<25}".format('Name', 'Code'))
        for key, value in lang.items():
            x = key
            y = value
            print("{:<25} {:<25}".format(x, y))
    elif args.file != None and args.output == None:
        with open(args.file, "r") as f:
            t = f.read()
        result = translate.translate(args.source, args.target, t)
        print(result)
    elif args.output != None and args.file == None:
        result = translate.translate(args.source, args.target, args.text)
        with open(args.output, "w") as o:
            o.write(result)
        print("Translation result saved in", args.output)
    elif args.file != None and args.output != None:
        with open(args.file, "r") as f:
            t = f.read()
        result = translate.translate(args.source, args.target, t)
        with open(args.output, "w") as o:
            o.write(result)
        print("Translation result saved in", args.output)
    else:
        result = translate.translate(args.source, args.target, args.text)
        print(result)
