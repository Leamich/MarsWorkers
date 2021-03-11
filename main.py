from flask import Flask
import datetime as dt
import sys

from data.jobs import Jobs
from data.users import User
from data import db_session


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def initiate_users(db_sess):
    db_sess.add(User(surname='Scott', name='Ridley', age=21,
                     position='captain',
                     speciality='research engineer',
                     address='module_1',
                     email='scott_chief@mars.org'
                     ))

    db_sess.add(User(surname='Stiles', name='Richard', age=22,
                     position='helper',
                     speciality='general',
                     address='module_2',
                     email='stile_r@mars.org'
                     ))

    db_sess.add(User(surname='Crowds', name='Scott', age=23,
                     position='junior captain',
                     speciality='math',
                     address='module_2',
                     email='scotty_cr1998@mars.org'
                     ))

    db_sess.add(User(surname='Canon', name='Pictures', age=24,
                     position='operator',
                     speciality='cinema',
                     address='module_1',
                     email='canon_pict@mars.org'
                     ))

    db_sess.add(User(surname='Ronan', name='Warwar', age=25,
                     position='warior',
                     speciality='alien killer',
                     address='module_1',
                     email='kill_mars@mars.org'
                     ))


def initiate_jobs(db_sess):
    db_sess.add(Jobs(team_leader=1,
                     job='deployment of residential modules 1 and 2',
                     work_size=15,
                     collaborators='2, 3',
                     start_date=dt.date.today(),
                     is_finished=False
                     ))


def main():
    db_session.global_init('db/mars_explorer.db')

    db_sess = db_session.create_session()
    initiate_users(db_sess)

    db_sess.commit()
    # app.run()


def request_type1():
    db_file = ' '.join(sys.argv[1:])

    db_session.global_init(db_file)
    db_sess = db_session.create_session()

    for user in db_sess.query(User).filter(User.address == 'module_1'):
        print(user)


if __name__ == '__main__':
    request_type1()
    # main()
