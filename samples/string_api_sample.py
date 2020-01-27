import vortex.core.instance as vortex

vdb = vortex.Instance('string_sample')

while vdb:
    vdb.input_as_string(input('Input: '))
    print('Result of Operation')
    print(vdb.result_as_string())
