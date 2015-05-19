from jinja2 import Template
template = Template('hello {{name}}')
print template.render(name='world')



