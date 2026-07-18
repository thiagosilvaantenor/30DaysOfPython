# Dice roller for n-sided dice

import argparse,random



def get_random_rolls(dices, sides):
    try:
        # Removes 'd' and parses to a int
        dices.strip()
        i_dices = int(dices)

        sides.strip()
        i_sides = int(sides)
        
        rolls = []

        for x in range(i_dices):
            # Add a dice rool
            rolls.append(random.randrange(start=1,stop=i_sides+1))
        
        return rolls
    except Exception:
        raise(f"Oops, number of dices is not valid: {dices}")
    


def calculate_rool_avg(rolls:list):
    s_list = sum(rolls)
    return s_list / len(rolls)


def write_log(output, name_file="roll_log.txt" ):
    from pathlib import Path
    from datetime import datetime
    #"/home/thiago/projetos/estudos/30DaysOfPython/"
    script_dir = Path(__file__).parent.resolve()
    
    file_path = script_dir / f"./{name_file}"

    timestamp = datetime.now()
    msg = f'{str(timestamp)} - Log: {output}'

    with open(file_path, "a") as log_file:
        log_file.write(f'{msg}\n')



def main():
    # argparse configuration 
    parser = argparse.ArgumentParser(
        description="Dice roller for n-sided dice"
        )

    parser.add_argument(
        "dicesDsides",   
        help="Number of dices, before a 'd', after the 'd' number of sides ex 3 dices with 6 sides: 3d6"
        )

    parser.add_argument(
        "--log",
        "-l",
        help="Log file name, if it's not inform will use the default 'roll_log.txt'"
    )

    parser.add_argument(
        "--repeat",
        "-r",
        default=0,
        type=int,
        help="Specify a number of times to roll the dice set"
    )

    args = parser.parse_args()

    #split input
    dices, sides = args.dicesDsides.split('d')
    print(f'Number of Dices={dices}, sides={sides}')

        
    for i in range(args.repeat):

        # processing input
        rolls = get_random_rolls(dices, sides)
        avg = calculate_rool_avg(rolls)
        str_rolls = ", ".join(map(str,rolls))

        msg = f'Rolls: {str_rolls} - Total: {len(rolls)} - Average: {avg}'

        if args.log:
            write_log(msg, args.log)
        else:
            write_log(msg)
            
        print(msg)
    




main()


