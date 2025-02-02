import math
import time
from os import listdir
from os.path import getmtime
from os.path import isfile
from os.path import join
from os.path import splitext

import magic

from alarms import generate_alarm
from file_open_checks import FILE_CHECK_FUNCTIONS
from file_open_checks import FILE_FORMAT_MAPPING


IMAGE_FORMATS = ["jpeg", "jpg", "png"]
DOCUMENT_FORMATS = ["docx", "doc", "pdf"]

EXEMPT_FILES = []


ALL_SECURED_FILE_TYPES = IMAGE_FORMATS + DOCUMENT_FORMATS
ENTROPY_THRESHOLD_VALUE = 6.5

SECURE_VAULT_PATHS = {
    "secure_vault": {
        "path": "/home/hassaan/ransomware_vault/secure_vault",
        "existing_files": set(),
    },
}


def create_file_path(vault_name, filename):
    return "{}/{}".format(SECURE_VAULT_PATHS[vault_name]["path"], filename)


def check_file_type(filename):
    filename, file_extension = splitext(filename)
    return file_extension[1:]


def verify_file_type_without_extension(filepath, file_extension, activate_alarm=True):
    result = magic.from_file(filepath)
    if FILE_FORMAT_MAPPING[file_extension.lower()] in result.lower():
        return True
    if activate_alarm:
        generate_alarm(filepath)
    return False


def perform_file_security_check(filepath, file_extension):
    if not verify_file_type_without_extension(filepath, file_extension):
        return False
    return FILE_CHECK_FUNCTIONS[file_extension](filepath)


def calculate_file_entropy(filepath):
    with open(filepath, 'rb') as f:
        byteArr = list(f.read())
    fileSize = len(byteArr)
    print('File size in bytes: {:,d}, with file name: {}'.format(fileSize, filepath))
    # calculate the frequency of each byte value in the file
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr) / fileSize)
    # Shannon entropy
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    print('Shannon entropy: {}'.format(ent))
    return ent


def file_entropy_check(filepath):
    entropy = calculate_file_entropy(filepath)
    if entropy < ENTROPY_THRESHOLD_VALUE:
        generate_alarm(filepath)


def run_monitoring():
    last_check_time = time.time()
    while (True):
        print("*********************")
        print("Current status: {}".format(SECURE_VAULT_PATHS))
        print("Check at: {}".format(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(last_check_time))))

        for secure_vault_name in SECURE_VAULT_PATHS:
            secure_vault_path = SECURE_VAULT_PATHS[secure_vault_name]["path"]
            onlyfiles = [f for f in listdir(secure_vault_path) if isfile(join(secure_vault_path, f))]
            for filename in onlyfiles:
                if filename in EXEMPT_FILES:
                    continue
                file_extension = check_file_type(filename)
                if file_extension in ALL_SECURED_FILE_TYPES:
                    if filename not in SECURE_VAULT_PATHS[secure_vault_name]["existing_files"]:
                        SECURE_VAULT_PATHS[secure_vault_name]["existing_files"].add(filename)
                        filepath = create_file_path(secure_vault_name, filename)
                        no_issue = perform_file_security_check(filepath, file_extension)
                        #if no_issue:
                        file_entropy_check(filepath)
                        print("----------------------------------------------------")
                        print("Following file has been added: {}".format(filename))
                    elif getmtime(secure_vault_path + "/" + filename) > last_check_time:
                        no_issue = perform_file_security_check(filepath, file_extension)
                        if no_issue:
                            file_entropy_check(filepath)
                        print ("----------------------------------------------------")
                        print ("Following file has been modified: {}".format(filename))

                # print("Filename: {}".format(filename))
                # print ("*-*-*-*-* {} */*--*-*-*".format(getmtime(secure_vault_path + "/" + filename)))
                # print (type(getmtime(secure_vault_path + "/" + filename)))
                # print("last modified: {}".format(time.ctime(getmtime(secure_vault_path + "/" + filename))))
                # print("created: {}".format(time.ctime(getctime(secure_vault_path + "/" + filename))))
                print ('\n\n\n')

        last_check_time = time.time()
        time.sleep(10)


if __name__ == "__main__":
    run_monitoring()
