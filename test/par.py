s = [{u'encrypt': False, u'icon': u'page_white_acrobat', u'bytes': 5242880, u'compress': False, u'thumb_exists': False,
 u'rev': u'367411f35daaef994a1835181491b4df', u'modified': u'Tue, 09 Apr 2013 02:08:07 +0000', u'store_bytes': 5242880,
 u'path': u'/foldertestrevision0/vsize.txt0', u'is_dir': False, u'store_size': u'5.0 MB', u'root': u'File Cruiser', u'size': u'5.0 MB'},
     {u'encrypt': False, u'icon': u'page_white_acrobat', u'bytes': 2097152, u'compress': False, u'thumb_exists': False, 
u'rev': u'4d15323d20eb8cc3d466fe31e9e00944', u'modified': u'Tue, 09 Apr 2013 02:08:06 +0000', u'store_bytes': 2097152,
 u'path': u'/foldertestrevision0/vsize.txt0', u'is_dir': False, u'store_size': u'2.0 MB', u'root': u'File Cruiser', u'size': u'2.0 MB'},
     {u'encrypt': False, u'icon': u'page_white_acrobat', u'bytes': 1048576, u'compress': False, u'thumb_exists': False,
 u'rev': u'59427a3159a5f469eb7d9e8721f61d00', u'modified': u'Tue, 09 Apr 2013 02:08:05 +0000', u'store_bytes': 1048576,
 u'path': u'/foldertestrevision0/vsize.txt0', u'is_dir': False, u'store_size': u'1.0 MB', u'root': u'File Cruiser', u'size': u'1.0 MB'}]
print s
print 'get revision'
for i in s:
    print i.get('rev')

