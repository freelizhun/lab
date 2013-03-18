#from blozer import url_mapper
#url_mapper.connect('/hello', views='views.hello')
import routes

mapper = routes.Mapper()
#mapper.connect('hello', '/hello', controller='views.hello', action='list')
mapper.connect('/hello', application='views.hello')

