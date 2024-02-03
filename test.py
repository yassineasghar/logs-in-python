from Logs import Logs

LOG_CONFIG = {
    'DEV': {'ROLE': 'for DEV', 'FILE': 'logs/dev.log'},
    'OPS': {'ROLE': 'for OPS', 'FILE': 'logs/ops.log'},
    'USR': {'ROLE': 'for USER', 'FILE': 'logs/usr.log'},
    'TST': {'ROLE': 'for test', 'FILE': 'logs/test.log'},
    'ROT': {'ROLE': 'for rotation', 'FILE': 'logs/rotated/0.log'},
}


class Operations:
    @staticmethod
    def validate(num):
        return num


class Tests:
    def __init__(self, configs):
        self.logs = {role: Logs(config['ROLE'], config['FILE']) for role, config in configs.items()}

    def test_logs(self):
        first_num = Operations.validate(34)
        second_num = Operations.validate(43)

        self.logs['DEV'].add('ERROR', f'first number is : {first_num}')
        self.logs['OPS'].add('ERROR', f'second number is : {second_num}')

        result = first_num + second_num
        if first_num != second_num:
            self.logs['DEV'].add('WARNING', f'result of numbers is : {result}')
            self.logs['USR'].add('INFO', f'debug line only : {result}')
            self.logs['DEV'].add('WARNING', f'hello i am a bad warning: {result}')
            self.logs['OPS'].add('ERROR', f'you should better use me in a try catch')
            self.logs['USR'].add('CRITICAL', f'glad to be here, finally someone called me')

    def test_init(self):
        logs = Logs(LOG_CONFIG.get('TST').get('ROLE'), LOG_CONFIG.get('TST').get('FILE'))
        logs.add('WARNING', f'Init test')

    def test_rotation(self):
        logs = Logs(LOG_CONFIG.get('ROT').get('ROLE'), LOG_CONFIG.get('ROT').get('FILE'), 1)
        for _ in range(20):
            logs.add('WARNING', f'Testing rotation of logs')

    def test_exc(self):
        try:
            result = 100 / 0
        except Exception as e:
            self.logs['TST'].catch(f'An error occurred in test_exc: {str(e)}')


if __name__ == "__main__":
    tests = Tests(LOG_CONFIG)
    tests.test_logs()
    tests.test_init()
    tests.test_rotation()
    tests.test_exc()