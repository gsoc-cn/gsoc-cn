import os
from string import Template


class Generator(object):
    def __init__(self):
        self.resource_path = "./resources"
        self.output = "./resources/README.md"
        self.template = Template('''
#### 社区介绍

$content
#### 添加指南

> 根据模版文件 [template.md](./template.md) 添加即可
''')

    def parse(self):
        result = []
        for filename in os.listdir(self.resource_path):
            if filename.endswith(".md"):
                continue
            else:
                result.append(filename)
        result.sort(key=lambda v: v.upper())
        return result

    def generate(self, parse_result):
        result = ""
        for dirname in parse_result:
            result += "- [{0}](./{1})\n".format(dirname, dirname)
        return self.template.substitute(content=result)

    def parse_and_generate(self):
        parse_result = self.parse()
        generate_result = self.generate(parse_result)
        return generate_result

    def compile_and_save(self):
        generate_result = self.parse_and_generate()
        with open(self.output, "w") as f:
            f.write(generate_result)


if __name__ == "__main__":
    g = Generator()
    g.compile_and_save()
