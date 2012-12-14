from view import index, sendmail
from admin.view import admin, edit_project, new_project, projects_list, edit_about, edit_skills, edit_client, clients_list, new_client, categories_list
from admin.validate import login, logout

def provide_urls(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/send', 'send', sendmail, methods=['POST'])

    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])

    app.add_url_rule('/admin', 'admin', admin)
    app.add_url_rule('/admin/projects/edit/<int:project_id>/', 'edit_project', edit_project, methods=['GET', 'POST'])
    app.add_url_rule('/admin/projects/new', 'new_project', new_project, methods=['GET', 'POST'])
    app.add_url_rule('/admin/projects', 'projects_list', projects_list)
    app.add_url_rule('/admin/edit_about', 'edit_about', edit_about, methods=['GET', 'POST'])
    app.add_url_rule('/admin/edit_skills', 'edit_skills', edit_skills, methods=['GET', 'POST'])
    app.add_url_rule('/admin/clients/edit/<int:client_id>', 'edit_client', edit_client, methods=['GET', 'POST'])
    app.add_url_rule('/admin/clients/new', 'new_client', new_client, methods=['GET', 'POST'])
    app.add_url_rule('/admin/clients', 'clients_list', clients_list)
    app.add_url_rule('/admin/categories', 'categories_list', categories_list, methods=['GET', 'POST'])
