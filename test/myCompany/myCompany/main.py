from datetime import datetime
import sys

from myCompany.datasource import db_connector
from myCompany.handlers.budget_notification import BudgetNotificationHandler


def main():
    ''' Python CLI app entrypoint '''

    batch_date = datetime.today()
    args = sys.argv[1:]

    if len(args) >= 3:
        if len(args) == 3:
            module, tooling, action = args
        elif len(args) == 4:
            module, tooling, action, date_str = args
            try:
                batch_date = datetime.strptime(date_str, '%Y%m%d').date()
            except Exception:
                return f'Could not parse the given date: {date_str}. \n \
                         Please provide a date in the format %Y%m%d e.g. 20200101'

        if (module == 'budget' and tooling == 'notification' and action == 'run'):
            notification_handler = BudgetNotificationHandler(db_connector, batch_date=batch_date)
            return notification_handler.send_notifications_to_unnotified_budgets()

    print('''
    How to use this CLI: myCompany [module] [tooling] [action] <date> optional in format %Y%m%d

    Example of usage:
    `sttylight budget notification run`

    or
    `sttylight budget notification run 20200919`
    ''')


if __name__ == '__main__':
    main()
