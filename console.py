#!/usr/bin/env python3
"""entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb)"
    
    def do_quit(self, line):
        """exit command interpreter"""
        return True

    def do_EOF(self, line):
        """Exit the command interpreter"""
        return True

    def help_help(self):
        """ Prints help command description """
        print("Describes a given command")

    def emptyline(self):
        """ do nothing if line is empty"""
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
