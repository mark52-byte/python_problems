# Import pandas
import subprocess
import os
import uuid

# def document_to_html(file_path):
#     tmp = "/tmp"
#     guid = str(uuid.uuid1())f
#     # convert the file, using a temporary file w/ a random name
#     command = "abiword -t %(tmp)s/%(guid)s.html %(file_path)s; cat %(tmp)s/%(guid)s.html" % locals()
#     p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=os.path.join(settings.PROJECT_DIR, "website/templates"))
#     error = p.stderr.readlines()
#     if error:
#         raise Exception("".join(error))
#     html = p.stdout.readlines()
#     return "".join(html)

# document_to_html("StarHealth1.pdf")



import pdftotree

pdftotree.parse("StarHealth2.pdf", html_path="table3.html", model_type=None, model_path=None, visualize=True)

# from pypdf2xml  import Pdf2htmlex

# import subprocess
# subprocess.call("pdf2htmlEX StarHealth2.pdf", shell=True)