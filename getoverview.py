from oidv6 import OIDv6

oid = OIDv6.OIDv6()

args = dict()
args['type_data'] = 'all'
args['classes'] = ['classes.txt']
args['limit'] = 0
args['multi_classes'] = True
args['dataset'] = 'OIDv6'
args['yes'] = True
args['no_labels'] = False
args['no_clear_shell'] = True
args['command'] = 'downloader'

oid = OIDv6.OIDv6()
oid.download(args)
