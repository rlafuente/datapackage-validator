import datapackage_validate


def main(datapackage):
    try:
        datapackage_validate.validate(datapackage)
        # datapackage_validate.validate(datapackage, schema)
    except datapackage_validate.exceptions.DataPackageValidateException as e:
        print "Errors found in datapackage.json:"
        for err in e.errors:
            # only get the actual error msg
            err_msg = err[0]
            print "  - %s" % err_msg

if __name__ == "__main__":
    import sys
    import os
    import codecs
    arg = sys.argv[1]
    if os.path.isdir(arg):
        json_path = os.path.join(arg, "datapackage.json")
    elif os.path.exists(arg):
        json_path = arg
    json_contents = codecs.open(json_path, 'r', 'utf-8').read()
    main(json_contents)
