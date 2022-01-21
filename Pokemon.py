class Pokemon:
    def __init__(self, json, name):
        self.name = name
        self.weight = json['weight']
        self.height = json['height']
        self.base_exp = json['base_experience']

    def print(self):
        print(f'''name: {self.name}
height: {self.height}
weight: {self.weight}
base_experience: {self.base_exp}''')
