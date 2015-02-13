import os
import time
import RPi.GPIO as GPIO
import prime


while True:
    log = open('/var/www/log.txt', 'a')
    os.system('cp /var/www/queue.txt /var/www/queued.txt')
    os.system('> /var/www/queue.txt')
    queue = [line.strip() for line in open('/var/www/queued.txt', 'r')]
    queue.reverse()
    if len(queue) != 0:
        for drink in queue:
            if drink == 'Lemonade':
                log.write("Making Lemonade\n")
                import Lemonade
                time.sleep(60)
            elif drink == 'Tea':
                log.write("Making Tea\n")
                import Tea
                time.sleep(60)
            elif drink == 'Palmer':
                log.write("Making Arnold Palmer\n")
                import Palmer
                time.sleep(60)
            else:
                log.write("Invalid drink input\n")
    else:
        log.write("restart\n")
        log.close()
        time.sleep(5)
