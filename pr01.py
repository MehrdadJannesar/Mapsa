def log_message(msg):
    with open("log.txt", "a") as log_file:
        log_file.write("{}.\n".format(msg))
