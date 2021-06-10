# -*- coding: utf-8 -*-
import os
import subprocess
import sys


class Configuration(object):
    def __init__(self, wkhtmltopdf='', meta_tag_prefix='pdfkit-', environ={}):
        self.meta_tag_prefix = meta_tag_prefix

        self.wkhtmltopdf = wkhtmltopdf

        if not self.wkhtmltopdf:
            if sys.platform == 'win32':
                self.wkhtmltopdf = subprocess.Popen(
                    ['where', 'wkhtmltopdf'], stdout=subprocess.PIPE).communicate()[0].strip()
            else:
                self.wkhtmltopdf = subprocess.Popen(
                    ['which', 'wkhtmltopdf'], stdout=subprocess.PIPE).communicate()[0].strip()

        try:
            with open(self.wkhtmltopdf) as f:
                pass
        except IOError:
            raise IOError('No wkhtmltopdf executable found: "%s"\n'
                          'If this file exists please check that this process can '
                          'read it. Otherwise please install wkhtmltopdf - '
                          'https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf' % self.wkhtmltopdf)

        self.environ = environ

        if not self.environ:
            env = os.environ

            for key in env.keys():
                if not isinstance(env[key], str):
                    self.environ[key] = str(env[key])
