"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
        'name': {
            'Jill': {
                'age':{26},
                'job':{'biologist'},
                'relationship':{
                    'friend': ['Zalika'],
                    'partner': ['John']
                    },
                },
            'Zalika': {
                'age':{28},
                'job':{'artist'},
                'relationship':{
                    'friend': ['Jill']
                    },
                },
            'John':{
                'age':{27},
                'job':{'writer'},
                'relationship':{
                    'partner':['Jill']
                    },
                },
            'Nash':{
                'age':{34},
                'job':{'chef'},
                'relationship':{
                    'cousin':['John'],
                    'lanlord':['Zalika']
                },
            }
        }
    }
