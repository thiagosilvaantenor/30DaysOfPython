#3. Below you'll find an itemgetter function that takes in a collection, 
# and either a key or index. Catch any instances of KeyError or IndexError, 
# and write the exception to a file called log.txt, along with the arguments 
# that caused this issue. Once you have written to the log file, reraise the original exception.

import datetime


def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except LookupError as e_lk:
        write_log(e_lk, collection, identifier)
        raise LookupError(f"Oops, key or index not found, check the log file")
    
    

def write_log(exception, arg1, arg2):
    from pathlib import Path
    #"/home/thiago/projetos/estudos/30DaysOfPython/"
    script_dir = Path(__file__).parent.resolve()
    file_path = script_dir / "./logs.txt"

    timestamp = datetime.datetime.now()
    msg = f'{str(timestamp)},Error: {exception}, collection: {arg1}, identifier: {arg2}'

    with open(file_path, "a") as log_file:
        log_file.write(f'\n{msg}')


print(itemgetter(['1','2','3'], 3))
