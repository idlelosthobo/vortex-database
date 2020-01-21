import vortex.core.instance as vortex

vdb = vortex.Instance('testing')

while vdb:
    vdb.input_as_str(input('Input: '))
    print(vdb.result_as_str())