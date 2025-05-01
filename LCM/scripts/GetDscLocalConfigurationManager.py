#!/usr/bin/python
import fileinput
import sys
import subprocess
from security import safe_command

omi_bindir = "<CONFIG_BINDIR>"
omicli_path = omi_bindir + "/omicli"

parameters = []
parameters.append(omicli_path)
parameters.append("iv")
parameters.append("<DSC_NAMESPACE>")
parameters.append("{")
parameters.append("MSFT_DSCLocalConfigurationManager")
parameters.append("}")
parameters.append("GetMetaConfiguration")

#s = ""
#for param in parameters:
#    s += param + " "

p = safe_command.run(subprocess.Popen, parameters, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()

print(stdout)
print(stderr)


