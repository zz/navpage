import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
  """Main Page for category"""
  def get(self):
    template_values = {
      'url': 'url',
    }
    path = os.path.join(os.path.dirname(__file__), 'tpl/t.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/t/.*', MainPage)],
                                    debug=True)                       
def main():
  run_wsgi_app(application)
  
if __name__ == "__main__":
  main()