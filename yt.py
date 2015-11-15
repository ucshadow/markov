import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from bs4 import BeautifulSoup
from random import randint

class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()


url = 'https://www.youtube.com/all_comments?v=Y_QYIuQBhZU'
#This does the magic.Loads everything
r = Render(url)
result = r.frame.toHtml()
a = (result.encode("utf-8"))
soup = BeautifulSoup(a, 'html.parser')
result = soup.findAll('div', {'class': 'comment-text-content'})
print(result[randint(0, 10)].text)



#  "https://www.youtube.com/all_comments?v=A0MCtroaydA"