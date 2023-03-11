#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb)"
    valid_classes = ['BaseModel', 'User', 'Amenity', 'Review', 'State', 'City',
                     'Place']

    def do_create(self, arg):
        """ Creates new elements
        Usage: create <class_name> or <class_name>.create()
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            instance = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                        'City': City, 'Amenity': Amenity, 'State': State,
                        'Review': Review}
            dct_save = instance[arg]()
            print(dct_save.id)
            dct_save.save()

    def do_show(self, arg):
        """ Shows an element by id_number
        Usage: show <class_name> <id> or <class_name>.show("<id>")
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes elements in storage
        Usage: destroy <class_name> <id> or <class_name>.destroy("<id>")
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all elements in storage by class name
         Usage: all or all <class_name> or <class_name>.all()
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            instances = []
            for k, v in all_objs.items():
                ob_name = v.__class__.__name__
                if ob_name == arg[0]:
                    instances += [v.__str__()]
            print(instances)

    def do_update(self, arg):
        """ Updates info in storage
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        or <class_name>.update("<id>", "<attribute_name>", "<attribute_value>")
        """
        if not arg:
            print("** class name missing **")
            return
        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_count(self, arg):
        """ Retrieves the number of instances of a specific class
        Usage: <class_name>.count()
        """
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == arg:
                count = count + 1
        print(count)

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
