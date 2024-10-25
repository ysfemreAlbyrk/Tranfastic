import gui_new
import shortcut
# import app
import tray
from datetime import datetime
import logging as log
import logging.config as logconf
log = log.getLogger("Main")

logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '[%(name)s] %(message)s',
            },
            'default': {
                'format': '%(asctime)s %(levelname)-8s - [%(name)s] %(message)s',
            },
            'separator': {
                'format': '%(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'default',
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
        },
    }
logconf.dictConfig(logging_config)

with open('app.log', 'a') as log_file:
    log_file.write("="*50 +" "+ str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +" " + "="*50 + "\n\n")


def main():
    log.info("Application started")
    try:
        shortcut_handler = shortcut.ShortcutHandler()
        tray.run_tray(shortcut_handler)
    except Exception as e:
        log.error(f"{e}")  # Hata bilgilerini detaylı bir şekilde günlüğe kaydet

if __name__ == "__main__":
    main()  