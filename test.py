from bot.database.models.tags import all_tags
from bot.utils.bug_catcher import check_time_format


def main():

   print(check_time_format("10.11.24 11:11"))



if __name__ == "__main__":
    main()
