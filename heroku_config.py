import os


class Var(object):
    APP_ID = int(os.environ.get("7234849APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("7a460bee3ad526efa09041251c82da0aAPI_HASH", None)
    STRING_SESSION = os.environ.get("1BVtsOGYBu2f9MSealvEOWxUMDvG1kz5ZgH6NC9uxgMjgRIuQLOxG2hCrDbuPpO094Q9WFGwfbjFsSk9Hc7f3QAeJjggctT83tO-rbWT6DjVeAvOWEu9paDsfBFmS2btyJYdCS1yJPJRSlWbuQMQCpC0-EopBzDgS2GV1W4hckTwDv2XZQ80at2jMx8lJSUEhNcvF6DFhqyXSDv7P0SMvF7i5aAsAw1zS6BBan_yknALrfgtsVbzmEltLzkVUdymGasr_fXyKGuNXe60XUaiskYUoq0RRqboHySMkzf33swewWfgEpU4KB3y7mzwjPsuGWclVPy_R1x2q8BT5ueidg9vMH-gOmDY=STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purpose
    SUDO_USERS = set(int(x) for x in os.environ.get("1694265744SUDO_USERS", "").split())
    LYDIA_API_KEY = os.environ.get("Lc78307e9-0950-4468-8bba-5d85a04d1077YDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None), 
    HEROKU_API_KEY = os.environ.get("c78307e9-0950-4468-8bba-5d85a04d1077HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("Doaremon securityHEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    # Send .get_id in any channel to fill th1973642892:AAGX6kseihB0IHs48YfI4mFCIknbN8_9Jz4is value.
    COMBINED_GROUP_ID = int(os.environ.get("-484604917COMBINED_GROUP_ID", -100))
    PLUGIN_CHANNEL = os.environ.get("-484604917PLUGIN_CHANNEL", f"{COMBINED_GROUP_ID}")
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("-484604917PRIVATE_GROUP_BOT_API_ID", f"{COMBINED_GROUP_ID}")
    PM_PERMIT_GROUP_ID = os.environ.get("PM_PERMIT_GROUP_ID", f"{COMBINED_GROUP_ID}")
    TG_BOT_USER_NAME_BF_HER = os.environ.get("@Doaremon_security_botTG_BOT_USER_NAME_BF_HER", None)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    if AUTH_TOKEN_DATA is not None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("-484604917PRIVATE_GROUP_ID", f"{COMBINED_GROUP_ID}")
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID =-484604917 -int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", -100))
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    LIGHTNING_PRO = os.environ.get("LIGHTNING_PRO", "YES")
    WHITE_CHAT = set(int(x) for x in os.environ.get("WHITE_CHAT", "").split())


class Development(Var):
    LOGGER = True
