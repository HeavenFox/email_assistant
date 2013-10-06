import webapp2
import html_utils

class MainPage(webapp2.RequestHandler):
  def post(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(html_utils.clean_html(self.request.get('html')))

application = webapp2.WSGIApplication([
  ('/util/cleanhtml', MainPage),
], debug = True)