class HelloReader:
    def __init__(self, path: str) -> None:
        self.input_file = path

    def reading_hello(self) -> str:
        with open(self.input_file, 'r') as f:
            content = f.read()
            if content.strip() == 'HELLO':
                return 'HELLO'
            else:
                return 'SOMETHING ELSE'
