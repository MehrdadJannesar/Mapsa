# critical
# error
# warning
# info
# debug

def critical(msg):
    with open("filename.txt", "a") as log_file:
        log_file.write("[CRITICAL] {}\n".format(msg))

def error(msg):
    with open("filename.txt", "a") as log_file:
        log_file.write("[ERROR] {}\n".format(msg))

def warning(msg):
    with open("filename.txt", "a") as log_file:
        log_file.write("[WARNING] {}\n".format(msg))

def info(msg):
    with open("filename.txt", "a") as log_file:
        log_file.write("[INFO] {}\n".format(msg))

def debug(msg):
    with open("filename.txt", "a") as log_file:
        log_file.write("[DEBUG] {}\n".format(msg))
