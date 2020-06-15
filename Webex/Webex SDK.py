from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(
    access_token='ODEwZmVjZmYtYzEwYS00ZGM1LWI0YzYtOTYwYzZhMjU4ODlkYmUyZDIzYmMtNTZj_PF84_bdc9a8b4-40e0-44a7-96eb-5e6cea4788dd')

teams = api.teams.list()
for team in teams:
    print(team)
    if getattr(team, 'name') != 'Ibe Team':
        create_team = api.teams.create('Ibe Team')
        teamId = getattr(create_team, 'id')
    else:
        teamId = team.id

print(api.people.me())
print(api.people.list())
api.people.create(emails=['dumbo@gmail.com'], displayName='Dumbo Ele',
    firstName='Dumbo', lastName='Ele')

roles = api.roles.list()
for role in roles:
    print(role)

rooms = api.rooms.list()
evaluator = False
for room in rooms:
    if room.title == 'Ibe Room':
        evaluator = True
        roomId = room.id
if evaluator == False:
    new_room = api.rooms.create('Ibe Room', teamId=teamId)
    roomId = new_room.id

api.messages.create(roomId, text='Posted for the API')