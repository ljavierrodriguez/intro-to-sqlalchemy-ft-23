""" 

SELECT
------

SELECT * FROM usuarios;

"""
from models import Usuario, Perfil, session, Publicacion
usuarios = Usuario.query.all() # SELECT * FROM usuarios; [<Usuario 1>, <Usuario 2>, ...<Usuario N>]
perfiles = Perfil.query.all()


""" 
SELECT * FROM usuarios WHERE username='lrodriguez';
"""

usuario = Usuario.query.filter_by(username='lrodriguez')
usuario = Usuario.query.filter(Usuario.username.like('%rod%'))


""" 
INSERT 
------

INSERT INTO usuarios (username, password, active) VALUES ('lrodriguez', '123456', true);

"""

# usuario = Usuario(usename="lrodriguez", password="123456", active=True)

usuario = Usuario()
usuario.username = "lrodriguez"
usuario.password = "123456"
usuario.active = True

session.add(usuario) # ejecutamos el query (insert)
session.commit() # guarda de manera definitiva en la base de datos

""" 
UPDATE
------

UPDATE usuarios SET password='abc123*' WHERE username='lrodriguez';

"""

usuario = Usuario.query.filter_by(username='lrodriguez').first() # [<Usuario 1>] => <Usuario 1>
usuario.password = 'abc123*'
session.commit()


""" 

DELETE
------

DELETE FROM usuarios WHERE id = 1;

"""

usuario = Usuario.query.get(1) # SELECT * FROM usuarios WHERE id = 1;
session.delete(usuario)
session.commit()


""" 
SELECT 
------

SELECT * FROM publicaciones WHERE id = 1;

"""

publicacion = Publicacion.query.get(1)

print(publicacion.id) # 1
print(publicacion.titulo) # Como crear una api con flask
print(publicacion.usuarios_id) # 1

# acceder al nombre del usuario a traves del backref
print(publicacion.usuario.username) # lrodriguez

usuario = Usuario.query.get(publicacion.usuarios_id)
print(usuario.username)



""" 
SELECT
-------

SELECT count(1) AS total FROM usuario AS u
JOIN publicaciones AS p ON u.id = p.usuarios_id
WHERE u.id = 1; 

"""

usuario = Usuario.query.get(1)
print(len(usuario.publicaciones))

publicaciones = Publicacion.query.filter_by(usuarios_id=usuario.id)
print(len(publicaciones))


for publicacion in usuario.publicaciones:
    print(publicacion.titulo)
    
    
publicacion = Publicacion()
publicacion.titulo = "Lo que el viento se llevo"

del_publicacion = Publicacion.query.get(10)

usuario.publicaciones.append(publicacion)