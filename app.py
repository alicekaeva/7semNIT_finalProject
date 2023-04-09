from flask import Flask, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.issues
import controllers.index
import controllers.edit_issue
import controllers.edit_work
import controllers.login
import controllers.logout
import controllers.index_worker
import controllers.index_responsible
import controllers.history