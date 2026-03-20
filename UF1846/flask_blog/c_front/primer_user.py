from werkzeug.security import generate_password_hash

email = 'mugi@wara.com'
password = '1234'
rol = 'admin'

hashed_pw = generate_password_hash(password)

print(f"insert into usuarios(nombre,email,pw_hash,rol) values('Mugi Wara','{email}','{hashed_pw}','{rol}')")
