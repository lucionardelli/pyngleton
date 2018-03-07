# !/usr/bin/python3
# Copyright 2017 Ignacio Vizzo. All Rights Reserved.
"""
# FIXME: ADD DOCSTRING
"""


class BonnetSingleton(object):
    '''
    # FIXME: Add docsring
    '''

    def __init__(self):
        self.registered_functions = {}
        self.registered_vars = {}
        self.cache = {}

    def __getattr__(self, item):
        """
        Using the '.' operator on the sinlgeton object will attempt to retrieve
        the function of that name
        """
        if item in self.registered_functions:
            return self.registered_functions[item]
        else:
            raise AttributeError(
                'Cannot find function or attribute %s' % (item))

    def __dir__(self):
        """
        Overloads dir operator so we can get tab completion
        """
        return self.registered_functions.keys()

    def __getitem__(self, variable):
        """
        Using the [] operator on the singleton object will attempt to determine
        and retrieve the value of that variable
        """
        if variable in self.cache:
            return self.cache[variable]
        elif variable not in self.registered_vars:
            raise Exception("Variable %s is not defined" % variable)
        else:
            return self.registered_vars[variable].calc_var()

    def __delitem__(self, key):
        """
        Remove a variable from the cache
        """
        del self.cache[key]

    def __contains__(self, item):
        """
        The 'in' operator determines whether we know about a certain variable
        """
        return item in self.cache or item in self.registered_vars

    def __setitem__(self, var, value):
        """
        Using the [] = operator will assign values to the variable cache
        """
        self.cache[var] = value

    def set_vars(self, variables, values):
        """
        Assign multiple variables to the variable cache
        """
        for var, value in zip(variables, values):
            if var not in self.cache or self.cache[var] is None:
                self[variables] = value

    def register_require_vars(self, requesting_function, vars_required):
        """
        Function called by require_vars decorator to register a
        requesting_function and its arguments
        """

        if requesting_function.__name__ in self.registered_functions:
            raise Exception('Function "%s" has been already defined' %
                            (requesting_function.__name__))
        else:
            self.registered_functions[requesting_function.__name__] =\
                Requieres(requesting_function, vars_required)

        return self.registered_functions[requesting_function.__name__]

    def register_provided_vars(self, provider_function, vars_provided):
        """
        Helper for the decorators, this ill register in the singleton object
        the provided variables
        """
        if provider_function.__name__ in self.registered_functions:
            raise Exception('Function "%s" has been already defined' %
                            (provider_function.__name__))
        else:
            self.registered_functions[provider_function.__name__] =\
                Provides(provider_function, vars_provided)

        for var in vars_provided:
            if var in self.registered_vars:
                raise Exception(
                    'Variable "%s" has been already provided' % var)
            self.registered_vars[var] =\
                self.registered_functions[provider_function.__name__]

        return self.registered_functions[provider_function.__name__]


class Requieres(object):
    '''
    # FIXME: Add docsring
    '''

    def __init__(self, function, variables):
        self.function = function
        self.variables = variables

    def __call__(self):
        for var in self.variables:
            return self.function(get_singleton_object()[var])


class Provides(object):
    '''
    # FIXME: add docstring
    '''

    def __init__(self, pyfunc, provide_vars):
        self.func = pyfunc
        self.provide_vars = provide_vars

    def calc_var(self):
        retval = self.func()
        get_singleton_object().set_vars(self.provide_vars, retval)
        return retval


# # FIXME: Public API:  Explain this
__SINGLETON = BonnetSingleton()


def get_singleton_object():
    """
    # FIXME: add docstring
    """
    return __SINGLETON


def require_vars(*vars_required):
    """
    Decorator to requiere any variable from the main program. You can call this
    from anywhere as long as you import the singleton object. The way is
    designed it won't allow to call this decorator withouth no parameters, this
    is to prevent a super-abstract design and avoid future errors

    decorator usage:
    @require_vars('vars_required')
    def requesting_function():
        new_var = do_something_with_it(vars_required)
    """
    def require_vars(requesting_function):
        __SINGLETON.register_require_vars(requesting_function,
                                          vars_required)

    if len(vars_required) > 0 and isinstance(vars_required[0], str):
        return require_vars
    else:
        raise Exception("Please specify the required variables")


def provide_vars(*vars_provided):
    """
    Decorator to provide any variable to the main program. You can call this
    from anywhere as long as you import the singleton object

    decorator usage:
    @provide_vars('vars_provided')
    def provider_function():
        vars_provided = do_stuf()
        return vars_provided
    """
    def provide_vars(provider_function):
        __SINGLETON.register_provided_vars(provider_function,
                                           vars_provided)

    return provide_vars
