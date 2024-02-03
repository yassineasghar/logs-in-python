from Logs import Logs

DEV_FILE = 'logs/dev.log'
OPS_FILE = 'logs/ops.log'
USR_FILE = 'logs/usr.log'
DEV_ROLE = 'for DEV'
OPS_ROLE = 'for OPS'
USR_ROLE = 'for USER'


class Something:
    @staticmethod
    def validate(number):
        return number


def main():
    dev_log = Logs(DEV_ROLE, DEV_FILE)
    ops_log = Logs(OPS_ROLE, OPS_FILE)
    usr_log = Logs(USR_ROLE, USR_FILE)

    first_number = Something.validate(34)
    second_number = Something.validate(43)

    dev_log.add('INFO', f'first number is : {first_number}')
    ops_log.add('ERROR', f'second number is : {second_number}')
    result = first_number + second_number
    if first_number == second_number:
        ops_log.add('WARNING', f'first number is the same as the second number: {second_number}')
    else:
        dev_log.add('WARNING', f'result of numbers is : {result}')
        usr_log.add('INFO', f'debug line only : {result}')
        dev_log.add('WARNING', f'hello i am a bad warning: {result}')
        ops_log.add('ERROR', f'you should better use me in a try catch')
        usr_log.add('CRITICAL', f'glad to be here, finally someone called me')


if __name__ == '__main__':
    main()
