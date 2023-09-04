{
    'name': 'Personal',
    'summary': 'Módulo para ejemplificar filtros con un modelo de Personal.',
    'description': 'Este módulo será utilizado para poder visualizar los distintos tipos de filtros que pueden aplicarse a una vista',
    'version': '1.0.0',
    'category': 'Human Resources',
    'author': 'Christofer Borrayo',
    'data': [
        'data/categoria.csv',
        'data/personal.csv'

        'security/Groups.xml'
        'security/Administrador.xml'
        'security/Empleado.xml'
        'security/Visitante.xml'

        'views/Menu_principal.xml'

        'views/personal/Pesonal_view_tree.xml'
        'views/personal/Menu.xml'

        'views/user/Create_user.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}