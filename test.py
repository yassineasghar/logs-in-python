from Logs import Logs

LOG_CONFIG = {
    'DEV': {'ROLE': 'for DEV', 'FILE': 'logs/dev.log'},
    'OPS': {'ROLE': 'for OPS', 'FILE': 'logs/ops.log'},
    'USR': {'ROLE': 'for USER', 'FILE': 'logs/usr.log'},
    'TST': {'ROLE': 'for test', 'FILE': 'logs/test.log'},
    'ROT': {'ROLE': 'for rotation', 'FILE': 'logs/rotated/0.log'},
}


class Something:
    @staticmethod
    def validate(number):
        return number


def initiate_logs(configs):
    return {role: Logs(config['ROLE'], config['FILE']) for role, config in configs.items()}


def test_logs():
    logs = initiate_logs(LOG_CONFIG)
    first_number = Something.validate(34)
    second_number = Something.validate(43)
    logs['DEV'].add('ERROR', f'first number is : {first_number}')
    logs['OPS'].add('ERROR', f'second number is : {second_number}')
    result = first_number + second_number
    if first_number == second_number:
        logs['OPS'].add('WARNING', f'first number is the same as the second number: {second_number}')
    else:
        logs['DEV'].add('WARNING', f'result of numbers is : {result}')
        logs['USR'].add('INFO', f'debug line only : {result}')
        logs['DEV'].add('WARNING', f'hello i am a bad warning: {result}')
        logs['OPS'].add('ERROR', f'you should better use me in a try catch')
        logs['USR'].add('CRITICAL', f'glad to be here, finally someone called me')


def test_init():
    logs = initiate_logs({'TST': LOG_CONFIG['TST']})
    logs['TST'].add('WARNING', f'Hello - i need 10 Bytes to create a new log file ')


def test_rotation():
    logs = Logs(LOG_CONFIG.get('ROT').get('ROLE'), LOG_CONFIG.get('ROT').get('FILE'), 1)
    for i in range(20):
        logs.add('WARNING', f'Hello - i need 100 Bytes to')


def test_exc():
    logs = initiate_logs({'TST': LOG_CONFIG['TST']})
    try:
        result = 100 / 0  # This will raise a ZeroDivisionError
    except Exception as err:
        logs['TST'].catch('An error occurred: ' + str(err))

if __name__ == '__main__':
    test_logs()
    test_init()
    test_rotation()
    test_exc()
