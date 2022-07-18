#!/usr/bin/env python

import sys

def greetings(name):
  greet = f"Hello, {name}! How are you doing today? It's great to see you today!"
  return greet

if __name__ == "__main__":
  name = "Cool Cat"
  if len(sys.argv) > 1:
      name = sys.argv[1] 
  greetings(name)
