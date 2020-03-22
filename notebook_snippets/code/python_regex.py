code = [
    {
        'name' : 'Basic search for pattern anywhere in string',
        'snippet' : [
            'string = " abc def "',
            'pattern = re.compile(r"[a-z]+")',
            'result = re.search(pattern, string)',
            'if result is not None:',
            '    print("Substring \'{0}\' was found in the range {1}".format(result.group(), result.span()))',
        ],
    },
    {
        'name' : 'Basic search (match) for exact pattern at beginning of string',
        'snippet' : [
            'string = " abc def "',
            'pattern = re.compile(r".*[a-z]+")',
            'result = re.match(pattern, string)',
            'if result is not None:',
            '    print("Substring \'{0}\' was found in the range {1}".format(result.group(), result.span()))',
        ],
    },
    {
        'name' : 'Basic substitution',
        'snippet' : [
            'string = " abc def "',
            'pattern = re.compile(r"[a-z]+")',
            'new_string = re.sub(pattern, "something", string)',
            'print("New string is \'{0}\'".format(new_string))',
        ],
    },
    {
        'name' : 'Substitution with backreferences',
        'snippet' : [
            'string = "John Doe lives at 221B Baker Street."',
            'pattern = re.compile(r"""',
            '    ([a-zA-Z ]+)      # Save as many letters and spaces as possible to group 1',
            '    \\ lives\\ at\\      # Match " lives at "',
            '    (?P<address>.*)   # Save everything in between as a group named `address`',
            '    \\.                # Match the period at the end',
            '""", re.VERBOSE)',
            'new_string = re.sub(pattern, r"\\g<address> is occupied by \\1.", string)',
            'print("New string is \'{0}\'".format(new_string))',
        ],
    },
]