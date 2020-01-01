"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Cat_s_Data.views
