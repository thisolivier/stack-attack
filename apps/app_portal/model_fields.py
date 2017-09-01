from django.db import models

def parse_word(password_string):
    # Takes a unencrypted password and encrypts it.
    return 


class PasswordField(models.Field):
    description = "An encrypted password"
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 1000
        super(PasswordField, self).__init__(*args, **kwargs)
    
    def deconstruct(self):
        """
        Deconstruct turns a field into serialised data, and stores exta arguments to pass to init when reconstructing it.
        
        The form of serialisation is proprietary to Django, and has to do with turning the field object into a generic object and back again. This is *not the same* as changing the value of the field when it's queried, save to, or deleted from the database- that happens with the to_python and from_db functions. 
        
        If we've allowed the field to accept extra arguments in init (like being passed a field category), we need to add them to kwargs, since when init is called again during reconstruction, it won't have that value by default. 
        
        If we've set a default directly in init, we should strip it out of keyword args, since it doesn't need to be passed to init at all- init will add it anyway.
        """
        name, path, args, kwargs = super(PasswordField, self).deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs
    
    """
    Since we want to just return encoded strings, we don't need this
    def from_db_value(self, value, expression, connection, context):
        # Used when the value is queried from the database
        if value is None:
            return value
        return parse_hand(value)
    """

    def to_python(self, value):
        # Used in forms, when a field is initialised we need
        # To parse the input. 
        # In our case we want to encrypt it.
        if value is None:
            return value

        return parse_word(value)