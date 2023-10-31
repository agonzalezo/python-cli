import click
import json_handler
import qr_handler

@click.group()
def cli():
    pass

## List json data
@cli.command()
def list():
    users = json_handler.read_json()
    print(f"\tID\t\tName\t\tLastName\n")
    for user in users:
        print(f"\t{user['id']}\t|\t{user['name']}\t|\t{user['lastname']}")

## Add new data to the json
@cli.command()
@click.option('--name',type= str,required=True, help='Name of the new user')
@click.option('--lastname',type= str,required=True, help='Last Name of the new user')
def new(name, lastname):
    print(f'Creating the user [{name}]...')
    users = json_handler.read_json()
    new_id = len(users) + 1
    new_user = {
        'id': new_id,
        'name': name,
        'lastname': lastname
    }
    users.append(new_user)
    json_handler.write_json(users)
    print(f"User {new_user['name']} has been added.")

@cli.command()
@click.argument('id', type=int)
def user(id):
    found = False
    users = json_handler.read_json()
    for user in users:
        if user['id'] == id:
            print(f"\tID\t\tName\t\tLastName")
            found=True
            print(f"\t{user['id']}\t|\t{user['name']}\t|\t{user['lastname']}")
            break
    if not found:
        print(f'User with id {id} not found..')
        exit(99)


@cli.command()
@click.argument('id', type=int)
def rm(id):
    found = False
    users = json_handler.read_json()
    for user in users:
        if user['id'] == id:
            found=True
            print(f"\t{user['id']}\t|\t{user['name']}\t|\t{user['lastname']}")
            users.remove(user)
            json_handler.write_json(users)
            print(f"User {user['name']} has been removed")
            break
    if not found:
        print(f'User with id {id} not found..')
        exit(99)
            

@cli.command()
@click.option('--name',type= str,required=False, help='Name of the user')
@click.option('--lastname',type= str,required=False, help='Last Name of the user')
@click.argument('id', type=int)
def update(id, name, lastname):
    found = False
    updated = False
    users = json_handler.read_json()
    for user in users:
        if user['id'] == id:
            found=True
            if not name is None:
                user['name']=name
                updated= True
            if not lastname is None:
                user['lastname']=lastname
                updated= True
            if updated:
                json_handler.write_json(users)
                print(f"User {user['name']} has been updated")
                print(f"\t{user['id']}\t|\t{user['name']}\t|\t{user['lastname']}")
            else:
                print(f"UserId {user['id']} not changed")

            break
    if not found:
        print(f'User with id {id} not found..')
        exit(99)

@cli.command()
@click.option('--data',prompt="Insert data",help='Data to be encoded in qr')
@click.option('--qrtype',type=click.Choice(['ascii', 'image'], case_sensitive=False), default=('ascii'), help='Type of the qr code')
def genqr(data, qrtype):
    print(f'Creating the qr code type: {qrtype}, data: {data}')
    if qrtype == 'ascii':
        qr_handler.gen_ascii(data)
    elif qrtype == 'image':
        qr_handler.gen_image(data)

if __name__ == '__main__':
    cli()