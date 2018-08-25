import argparse
import collections

defaults = {
    'spam': 'default spam value',
    'eggs': 'default egg value',
}

parser = argparse.ArgumentParser()
parser.add_argument('--spam')
parser.add_argument('--eggs')

args = vars(parser.parse_args())
print(args)

filtered_args = {k: v for k, v in args.items() if v}
print(filtered_args)

combined = collections.ChainMap(filtered_args, defaults)
print(combined['spam'])
print(combined['eggs'])
print(combined)
print()