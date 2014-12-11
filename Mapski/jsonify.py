import zipfile
from CleverLeaf.settings import BASE_DIR, MEDIA_URL, MEDIA_ROOT
import shapefile
import json
from models import Shapefiler, UserLeaf
import os
import glob
import json

def shapeprocess(request, shapepk):
    path = Shapefiler.objects.get(pk=shapepk)
    print(path.file.path)  # print 1/

    # unzip folders
    with zipfile.ZipFile(path.file.path) as zf:
        print(os.path.join(BASE_DIR, 'media'))
        zf.extractall(os.path.join(BASE_DIR, 'media',str(path.file)[2:-4]))
        print("Jo")

    """
    This is necessary if multiple uploads have the same name in which case django adds an underscroe and a random string to uniquely idenfiy it. Unfortunately this means
    the two nested folders no longer have the same name. This is only necessary if the same name is uploaded more than once, so I will write a try/catch later. The uncommented
    variable 'shapefolderpath' is for unique name uploads
    """

    shapefolderpath = os.path.join(str(path.file)[2:-4], str(path.file)[2:-4].split('_')[0])

    shpfile_found = "placeholder"
    dbffile_found = "placeholder"

    print(1, str(path.file)[2:-4])
    print(2,os.path.join(BASE_DIR, 'media', str(path.file)[2:-4]))
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, 'media', str(path.file)[2:-4])):
        for f in files:
            if f.endswith('.shp'):
                print(f)
                shpfile_found = os.path.join(root, f)

            if f.endswith('.dbf'):
                print("eh", dirs)
                print(f)
                dbffile_found = os.path.join(root, f)



    myshp = open(shpfile_found, "rb")
    mydbf = open(dbffile_found, "rb")

    sf = shapefile.Reader(shp=myshp, dbf=mydbf)

    # generates a lsit of fields, does not include the first field 'DeletionFlag', It only includes fields wtih numeric values
    fieldlist = [i[0] for i in sf.fields[1:]]
    print(fieldlist)
    fieldlist = json.dumps(fieldlist)
    print(fieldlist)

    print(json.dumps(sf.shapeRecords().__geo_interface__))
    jsonvar = json.dumps(sf.shapeRecords().__geo_interface__)
    data = UserLeaf(user=request.user, jsonstr=jsonvar, attributes=fieldlist)
    data.save()

