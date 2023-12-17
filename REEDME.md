# Перед тем как пользоваться проектом надо создать виртуальное окружение командой:
python3 -m venv venv
# После войти в виртуальное окружение командой:
. venv/bin/activate
# Теперь надо устновить все необходимые библиотеки написанные на req.txt командой:
pip install -r req.txt

# Не забываем создать базу данных под названием task15. Команды:
psql

create database task15;

\q

# Чтобы войти в python shell воспользуйтесь командой:
./manage.py shell




# Далее для проверки вы можете использовать команды приведенные ниже
# MantToManyApp create commands in python shell:
>>> from ManyToManyApp.models import Bus, Human

Buses:
>>> bus1 = Bus.objects.create(busnumber=204, busmodel='Sprinter')
>>> bus2 = Bus.objects.create(busnumber=355, busmodel='Razvaluha')
>>> bus3 = Bus.objects.create(busnumber=106, busmodel='Mercedes')

Humans:
>>> human1 = Human.objects.create(name='Bagyshan', sex='male')
>>> human2 = Human.objects.create(name='Ivan', sex='male')
>>> human3 = Human.objects.create(name='Ayperi', sex='female')
>>> human4 = Human.objects.create(name='Saikal', sex='female')
>>> human5 = Human.objects.create(name='Alihan', sex='male')
>>> human6 = Human.objects.create(name='Rysia', sex='male')
>>> human7 = Human.objects.create(name='Talgat', sex='male')
>>> human8 = Human.objects.create(name='Aidana', sex='female')
>>> human9 = Human.objects.create(name='Ayzirek', sex='female')

Sets:
>>> human1.bus.set([bus1, bus2])
>>> human2.bus.set([bus2])
>>> human3.bus.set([bus2, bus3])
>>> human4.bus.set([bus2, bus3, bus1])
>>> human5.bus.set([bus3, bus1])
>>> human6.bus.set([bus1])
>>> human7.bus.set([bus1, bus2])
>>> human8.bus.set([bus3])
>>> human9.bus.set([bus3, bus2])

>>> human1.bus.all()
>>> bus1.humans.all()




# OneToOneApp create commands in python shell:
>>> from OneToOneApp.models import Country, Flag

Country 1:
>>> country1 = Country.objects.create(name='Kyrgyzstan', geography='Mountains')
>>> flag1 = Flag.objects.create(color='red', form='squere', country=country1)

Country 2:
>>> country2 = Country.objects.create(name='Russia', geography='North')
>>> flag2 = Flag.objects.create(color='red, blue, white', form='squere', country=country2)



