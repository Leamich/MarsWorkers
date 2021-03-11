from flask import Flask, render_template
import datetime as dt

from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def create_user(**kwargs):
    user = User()
    for arg_name in kwargs.keys():
        user.__setattr__(arg_name, kwargs[arg_name])
    return user


def create_job(**kwargs):
    job = Jobs()
    for arg_name in kwargs.keys():
        job.__setattr__(arg_name, kwargs[arg_name])
    return job


def initiate_users(db_sess):
    db_sess.add(create_user(**{'surname': 'Scott',
                               'name': 'Ridley',
                               'age': 21,
                               'position': 'captain',
                               'speciality': 'research engineer',
                               'address': 'module_1',
                               'email': 'scott_chief@mars.org'
                               }))

    db_sess.add(create_user(**{'surname': 'Stiles',
                               'name': 'Richard',
                               'age': 22,
                               'position': 'helper',
                               'speciality': 'general',
                               'address': 'module_3',
                               'email': 'stile_r@mars.org'
                               }))

    db_sess.add(create_user(**{'surname': 'Crowds',
                               'name': 'Scott',
                               'age': 23,
                               'position': 'junior captain',
                               'speciality': 'math',
                               'address': 'module_2',
                               'email': 'scotty_cr1998@mars.org'
                               }))

    db_sess.add(create_user(**{'surname': 'Canon',
                               'name': 'Pictures',
                               'age': 24,
                               'position': 'operator',
                               'speciality': 'cinema',
                               'address': 'module_7',
                               'email': 'canon_pict@mars.org'
                               }))

    db_sess.add(create_user(**{'surname': 'Ronan',
                               'name': 'Warwar',
                               'age': 25,
                               'position': 'warior',
                               'speciality': 'alien killer',
                               'address': 'module_1',
                               'email': 'kill_mars@mars.org'
                               }))


def initiate_jobs(db_sess):
    db_sess.add(create_job(**{'team_leader': 1,
                              'job': 'deployment of residential modules 1 '
                                     'and 2',
                              'work_size': 15,
                              'collaborators': '2, 3',
                              'start_date': dt.date.today(),
                              'is_finished': False
                              }))


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(jobs)

    return render_template('works_journal.html', jobs=jobs)


def main():
    db_session.global_init('db/mars_explorer.db')

    db_sess = db_session.create_session()
    initiate_users(db_sess)
    initiate_jobs(db_sess)

    app.run()


if __name__ == '__main__':
    main()
