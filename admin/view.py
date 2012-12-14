from flask import session, redirect, url_for, render_template, request
from markupsafe._speedups import escape
from sqlalchemy import exceptions

from models import Category, Project, Info, Skill, Client
from config import SITE_URL, STATIC_URL
from db import db_session

default = dict()
default['STATIC_URL'] = STATIC_URL
default['SITE_URL'] = SITE_URL

def check_user(func):
    def decorated(*args, **kwargs):
        if not 'username' in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)

    return decorated


@check_user
def admin():
    """ Admin page
    """
    prop = default
    return render_template('admin/index.html', **prop)


@check_user
def edit_project(project_id):
    """ Edit project
    """
    # if errors detected
    errors = []

    # saved?
    saved = False

    # if form incoming
    if request.method == 'POST':
        if not request.form['title']:
            errors += ['Title required!']

        if not errors:
            project = Project.query.get(project_id)
            project.title = unicode(escape(request.form['title']))
            project.description = unicode(escape(request.form['description']))
            project.logo = unicode(escape(request.form['logo']))
            project.link = unicode(escape(request.form['link']))
            project.category_id = int(escape(request.form['category']))
            project.client_id = int(escape(request.form['client']))

            try:
                db_session.add(project)
                db_session.commit()
                saved = True

            except exceptions.SQLAlchemyError:
                errors += ["Error saving project!"]
                saved = False

        else:
            project = Project.query.get(project_id)
    else:
        project = Project.query.get(project_id)

    categories = Category.query.all()
    clients = Client.query.all()

    prop = dict()
    prop.update(default)
    prop['project'] = project
    prop['categories'] = categories
    prop['clients'] = clients
    prop['errors'] = errors
    prop['saved'] = saved

    return render_template('admin/edit_project.html', **prop)


@check_user
def new_project():
    """ New project
    """

    # if errors detected
    errors = []

    # if form incoming
    if request.method == 'POST':
        if not request.form['title']:
            errors += ['Title required!']
        if not errors:
            project = dict()
            project['title'] = unicode(escape(request.form['title']))
            project['description'] = unicode(escape(request.form['description']))
            project['logo'] = unicode(escape(request.form['logo']))
            project['link'] = unicode(escape(request.form['link']))
            project['category_id'] = int(escape(request.form['category']))
            project['client_id'] = int(escape(request.form['client']))

            project = Project(**project)

            try:
                db_session.add(project)
                db_session.commit()
            except exceptions.SQLAlchemyError:
                db_session.rollback()
                errors += ['Error creating project #{0}\n'.format(project.id)]

            return redirect(url_for('edit_project', project_id=project.id))

    categories = Category.query.all()
    clients = Client.query.all()

    prop = dict()
    prop.update(default)
    prop['categories'] = categories
    prop['clients'] = clients
    prop['errors'] = errors

    return render_template('admin/new_project.html', **prop)


@check_user
def projects_list():
    """ Projects list
    """

    project_to_delete = request.values.get('delete', False)
    if project_to_delete:
        project = Project.query.get(int(project_to_delete))
        db_session.delete(project)
        db_session.commit()

        return redirect(url_for('projects_list'))

    projects = Project.query.all()

    prop = dict()
    prop.update(default)
    prop['projects'] = projects

    return render_template('admin/projects_list.html', **prop)


@check_user
def edit_about():
    """ About block edit
    """
    # saved?
    saved = False

    if request.method == 'POST':
        about = Info.query.filter(Info.title == 'about').first()
        about.value = unicode(request.form['about'])

        try:
            db_session.add(about)
            db_session.commit()
            saved = True
        except exceptions.SQLAlchemyError:
            db_session.rollback()
            saved = False

    about = Info.query.filter(Info.title == 'about').first()

    prop = dict()
    prop.update(default)
    prop['about'] = about.value
    prop['saved'] = saved

    return render_template('admin/edit_about.html', **prop)


@check_user
def edit_skills():
    """ About block edit
    """

    #saved?
    saved = False

    if request.method == 'POST':
        for field in request.form:
            if field.startswith('skill'):
                skill, skill_id = field.split('_')
                skill = Skill.query.get(int(skill_id))
                skill.percent = int(escape(request.form[field]))

                db_session.add(skill)
                db_session.commit()

        saved = True

    skills = Skill.query.all()

    prop = dict()
    prop.update(default)
    prop['skills'] = skills
    prop['saved'] = saved

    return render_template('admin/edit_skills.html', **prop)


@check_user
def edit_client(client_id):
    """ About block edit
    """
    # if errors detected
    errors = []

    #saved?
    saved = False

    # if form incoming
    if request.method == 'POST':
        if not request.form['title']:
            errors += ['Title required!']

        if not errors:
            client = Client.query.get(client_id)

            client.title = unicode(escape(request.form['title']))
            client.description = unicode(escape(request.form['description']))
            client.logo = unicode(escape(request.form['logo']))
            client.link = unicode(escape(request.form['link']))

            try:
                db_session.add(client)
                db_session.commit()
                saved = True
            except exceptions.SQLAlchemyError:
                db_session.rollback()
                saved = False
                errors += ['Error saving client #{0}\n'.format(client.id)]

        else:
            client = Client.query.get(client_id)

    else:
        client = Client.query.get(client_id)

    prop = dict()
    prop.update(default)
    prop['client'] = client
    prop['errors'] = errors
    prop['saved'] = saved

    return render_template('admin/edit_client.html', **prop)


@check_user
def new_client():
    """ About block edit
    """
    # if errors detected
    errors = []

    # if form incoming
    if request.method == 'POST':
        if not request.form['title']:
            errors += ['Title required!']

        if not errors:
            client = dict()
            client['title'] = unicode(escape(request.form['title']))
            client['description'] = unicode(escape(request.form['description']))
            client['logo'] = unicode(escape(request.form['logo']))
            client['link'] = unicode(escape(request.form['link']))

            client = Client(**client)

            try:
                db_session.add(client)
                db_session.commit()
            except exceptions.SQLAlchemyError:
                db_session.rollback()
                errors += ['Error creating client #{0}\n'.format(client.id)]

            return redirect(url_for('edit_client', client_id=client.id))

    prop = dict()
    prop.update(default)
    prop['errors'] = errors

    return render_template('admin/new_client.html', **prop)


@check_user
def clients_list():
    clients = Client.query.all()

    client_to_delete = request.values.get('delete', False)
    if client_to_delete:
        client = Client.query.get(int(client_to_delete))

        db_session.delete(client)
        db_session.commit()

        return redirect(url_for('clients_list'))

    prop = dict()
    prop.update(default)
    prop['clients'] = clients

    return render_template('admin/clients_list.html', **prop)


@check_user
def categories_list():

    #if errors detected
    errors = []

    #saved?
    saved = False

    if request.method == 'POST':
        categories = []

        saved = True

        for field in request.form:
            if field.startswith('title'):
                not_needed, category_id = field.split('-')
                categories.append(category_id)

        for category_id in categories:
            category = Category.query.get(int(category_id))
            category.title = escape(request.form['title-' + category_id])
            category.description = escape(request.form['description-' + category_id])

            try:
                db_session.add(category)
                db_session.commit()
            except exceptions.SQLAlchemyError:
                db_session.rollback()
                errors += ['Error saving category #{0}\n'.format(category.id)]
                saved = False

        if request.form['new-title']:
            category = Category(escape(request.form['new-title']), escape(request.form['new-description']))
            try:
                db_session.add(category)
                db_session.commit()
            except exceptions.SQLAlchemyError:
                db_session.rollback()
                errors += ['Error with new category']
                saved = False

    category_to_delete = request.values.get('delete', False)
    if category_to_delete:
        category = Category.query.get(int(category_to_delete))

        db_session.delete(category)
        db_session.commit()

        return redirect(url_for('categories_list'))

    categories = Category.query.all()

    prop = dict()
    prop.update(default)
    prop['categories'] = categories
    prop['saved'] = saved
    prop['errors'] = errors

    return render_template('admin/categories_list.html', **prop)
