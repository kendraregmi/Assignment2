# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-came  l-case) as well.

def camel_to_snake(s):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in s]).lstrip('_')

def camel_to_kebab(s):
    return ''.join(['-'+c.lower() if c.isupper() else c for c in s]).lstrip('-')
result=camel_to_snake("ThisIsCamelCased")
print(result)

result=camel_to_kebab("ThisIsCamelCased")
print(result)
